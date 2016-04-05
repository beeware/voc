import dis

from ..java import (
    Code as JavaCode,
    opcodes as JavaOpcodes,
    ExceptionInfo as JavaExceptionInfo,
    LineNumberTable
)

from .utils import extract_command, find_blocks
from .opcodes import Ref, resolve_jump, jump, Opcode, ALOAD_name, ICONST_val


class IgnoreBlock(Exception):
    """An escape hatch; enable a block to be flagged as ignorable"""
    pass


class Block:
    def __init__(self, parent=None, commands=None, verbosity=0):
        self.parent = parent
        self.commands = commands if commands else []
        self.verbosity = verbosity

        self.local_vars = {}
        self.deleted_vars = set()

        self.generator = None
        self.yield_points = []

        self.opcodes = []
        self.try_catches = []
        self.blocks = []
        self.jumps = []
        self.loops = []
        self.jump_targets = {}
        self.unknown_jump_targets = {}
        self.returns = {
            'annotation': None
        }

        self.next_resolve_list = []
        self.next_opcode_starts_line = None

    @property
    def module(self):
        return self.parent

    def store_name(self, name, use_locals):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def store_dynamic(self):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def load_name(self, name, use_locals):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def delete_name(self, name, use_locals):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def extract(self, code):
        """Break a code object into the parts it defines, populating the
        provided block.

        """
        self.code = code
        instructions = list(dis.Bytecode(code))

        if self.verbosity > 1:
            print ('=' * len(str(code)))
            print (code)
            print ('-' * len(str(code)))

        # for i, inst in enumerate(instructions):
        #     print (i, inst.offset, inst.opname, inst.argval)

        blocks = find_blocks(instructions)

        i = len(instructions)
        commands = []
        while i > 0:
            i, command = extract_command(instructions, blocks, i)
            commands.append(command)

        commands.reverse()

        if self.verbosity > 1:
            for command in commands:
                command.dump()

        # Append the extracted commands to any pre-existing ones.
        self.commands.extend(commands)

    @property
    def can_ignore_empty(self):
        return False

    def add_opcodes(self, *opcodes):
        # Add the opcodes to the code list and process them.
        for opcode in opcodes:
            # print("ADD OPCODE", id(opcode), opcode)
            if opcode.process(self):
                # self.opcodes.extend([
                #     JavaOpcodes.LDC_W(str(opcode)),
                #     JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V')
                # ])

                self.opcodes.append(opcode)

                # If we've flagged a code line change, attach that to the opcode
                if self.next_opcode_starts_line:
                    opcode.starts_line = self.next_opcode_starts_line
                    self.next_opcode_starts_line = None

                # Resolve any references to the "next" opcode.
                for (obj, attr) in self.next_resolve_list:
                    # print("        resolve %s reference on %s %s with %s %s" % (attr, obj, id(obj), opcode, id(opcode)))
                    setattr(obj, attr, opcode)

                self.next_resolve_list = []

    def stack_depth(self):
        "Evaluate the maximum stack depth required by a sequence of Java opcodes"
        depth = 0
        max_depth = 0

        for opcode in self.opcodes:
            depth = depth + opcode.stack_effect
            # print("   ", opcode, depth)
            if depth > max_depth:
                max_depth = depth
        return max_depth

    def materialize(self):
        for cmd in self.commands:
            cmd.materialize(self)

    def transpile_setup(self):
        """Tweak the bytecode generated for this block."""
        pass

    def transpile_teardown(self):
        """Tweak the bytecode generated for this block."""
        pass

    def transpile_commands(self):
        """Create a JavaCode object representing the commands stored in the block

        May raise ``IgnoreBlock`` if the block should be ignored.
        """
        argument_vars = len(self.local_vars)

        # Insert content that needs to occur before the main block commands
        self.transpile_setup()

        # Convert the sequence of commands into instructions.
        # Most of the instructions will be opcodes. However, some will
        # be instructions to add exception blocks, line number references, etc
        for cmd in self.commands:
            cmd.transpile(self)

        # Insert content that needs to occur after the main block commands
        self.transpile_teardown()

        # Install the shortcut jump points for yield statements.
        yield_jumps = []

        for i, yield_point in enumerate(self.yield_points):
            yield_jumps.extend([
                ALOAD_name(self, '<generator>'),
                JavaOpcodes.GETFIELD('org/python/types/Generator', 'yield_point', 'I'),
                ICONST_val(i + 1),
                jump(JavaOpcodes.IF_ICMPEQ(0), self, Ref(self, yield_point), Opcode.YIELD)
            ])

        self.opcodes = yield_jumps + self.opcodes

        # Make sure every local variable slot has been initialized
        # as an object. This is needed because Python allows a variable
        # to be instantiated in a sub-block, and used outside that block.
        # The JVM doesn't, and raises a verify error if you try. By
        # initializing all variables, we can trick the verifier.
        # TODO: Ideally, we'd only initialize the variables that are ambiguous.
        init_vars = []
        for i in range(argument_vars, len(self.local_vars) + len(self.deleted_vars)):
            if i == 0:
                opcode = JavaOpcodes.ASTORE_0()
            elif i == 1:
                opcode = JavaOpcodes.ASTORE_1()
            elif i == 2:
                opcode = JavaOpcodes.ASTORE_2()
            elif i == 3:
                opcode = JavaOpcodes.ASTORE_3()
            else:
                opcode = JavaOpcodes.ASTORE(i)
            init_vars.extend([
                JavaOpcodes.ACONST_NULL(),
                opcode
            ])

        self.opcodes = init_vars + self.opcodes

        # Since we've processed all the Python opcodes, we can now resolve
        # all the unknown jump targets.
        # print('>>>>> Resolve references')
        for target, references in self.unknown_jump_targets.items():
            # print("   resolving %s references to %s" % (len(references), target))
            for opcode, position in references:
                resolve_jump(opcode, self, target, position)

        # If the block has no content in it, and the block allows,
        # ignore this block.
        if self.can_ignore_empty:
            if len(self.opcodes) == 1 and isinstance(self.opcodes[0], JavaOpcodes.RETURN):
                raise IgnoreBlock()
            elif len(self.opcodes) == 2 and isinstance(self.opcodes[1], JavaOpcodes.ARETURN):
                raise IgnoreBlock()

        # Now that we have a complete opcode list, postprocess the list
        # with the known offsets.
        offset = 0
        # print('>>>>> set offsets', self)
        for index, instruction in enumerate(self.opcodes):
            # print("%4d:%4d (0x%x) %s" % (index, offset, id(instruction), instruction))
            instruction.java_index = index
            instruction.java_offset = offset
            offset += len(instruction)
        # print('>>>>> end set offsets')

        # Construct the exception table, updating any
        # end-of-exception GOTO operations with the right opcode.
        # Record a frame range for each one.
        exceptions = []
        for try_catch in self.try_catches:
            # print("TRY CATCH START", id(try_catch), try_catch.start_op, try_catch.start_op.java_offset)
            # print("        TRY END", try_catch.try_end_op, try_catch.try_end_op.java_offset)
            # print("            END", try_catch.end_op, try_catch.end_op.java_offset)
            for handler in try_catch.handlers:
                # print("  HANDLER", handler.start_op, handler.end_op, handler.descriptors)
                if handler.descriptors:
                    for descriptor in handler.descriptors:
                        exceptions.append(JavaExceptionInfo(
                            try_catch.start_op.java_offset,
                            try_catch.try_end_op.java_offset,
                            handler.start_op.java_offset,
                            descriptor
                        ))
                else:
                    exceptions.append(JavaExceptionInfo(
                        try_catch.start_op.java_offset,
                        try_catch.try_end_op.java_offset,
                        handler.start_op.java_offset,
                        'org/python/exceptions/BaseException'
                    ))

            # Add definitions for the finally block
            if try_catch.finally_handler:
                # print("  FINALLY", try_catch.finally_handler.start_op.java_offset, try_catch.finally_handler.end_op.java_offset)
                exceptions.append(JavaExceptionInfo(
                    try_catch.start_op.java_offset,
                    try_catch.try_end_op.java_offset,
                    try_catch.finally_handler.start_op.java_offset,
                    None
                ))
                for handler in try_catch.handlers:
                    # print("   h", handler.descriptors)
                    exceptions.append(JavaExceptionInfo(
                        handler.start_op.java_offset,
                        handler.catch_end_op.java_offset,
                        try_catch.finally_handler.start_op.java_offset,
                        None
                    ))

        # Update any jump instructions
        # print ("There are %s jumps" % len(self.jumps))
        for jmp in self.jumps:
            # print ("JUMP", hex(id(jmp)), jmp, jmp.java_offset, jmp.jump_op, hex(id(jmp.jump_op)))

            try:
                jmp.offset = jmp.jump_op.java_offset - jmp.java_offset
            except AttributeError:
                jmp.offset = jmp.jump_op.start_op.java_offset - jmp.java_offset

        # Construct a line number table from
        # the source code reference data on opcodes.
        line_numbers = []
        for opcode in self.opcodes:
            if opcode.starts_line is not None:
                line_numbers.append((opcode.java_offset, opcode.starts_line))
        line_number_table = LineNumberTable(line_numbers)

        return JavaCode(
            max_stack=self.stack_depth() + len(exceptions),
            max_locals=len(self.local_vars) + len(self.deleted_vars),
            code=self.opcodes,
            exceptions=exceptions,
            attributes=[
                line_number_table
            ]
        )

    def transpile(self):
        return self.transpile_commands()
