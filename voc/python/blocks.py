import dis

from ..java import (
    Code as JavaCode,
    opcodes as JavaOpcodes,
    ExceptionInfo as JavaExceptionInfo,
    LineNumberTable
)

from .utils import extract_command, find_blocks
from .opcodes import ASTORE_name, ALOAD_name, ADELETE_name, IF, END_IF, resolve_jump


class IgnoreBlock(Exception):
    """An escape hatch; enable a block to be flagged as ignorable"""
    pass


class Block:
    def __init__(self, parent=None, commands=None):
        self.parent = parent
        self.commands = commands if commands else []
        self.localvars = {}

        self.code = []
        self.try_catches = []
        self.blocks = []
        self.jumps = []
        self.jump_targets = {}
        self.unknown_jump_targets = {}

        self.next_resolve_list = []
        self.next_opcode_starts_line = None

    @property
    def module(self):
        return self.parent

    def store_name(self, name, arguments, allow_locals=True):
        if allow_locals:
            self.add_opcodes(
                ASTORE_name(self, name)
            )
        else:
            self.add_opcodes(
                ASTORE_name(self, '#TEMP#'),
                JavaOpcodes.GETSTATIC(self.klass.descriptor, 'attrs', 'Ljava/util/Hashtable;'),
                JavaOpcodes.LDC_W(name),
                ALOAD_name(self, '#TEMP#'),
                JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
                JavaOpcodes.POP(),
            )

    def load_name(self, name, allow_locals=True):
        try:
            # Look for a local first.
            if allow_locals:
                self.add_opcodes(
                    ALOAD_name(self, name)
                )
            else:
                raise KeyError('Not scanning locals')
        except KeyError:
            self.add_opcodes(
                # If there isn't a local, look for a global
                JavaOpcodes.GETSTATIC(self.module.descriptor, 'globals', 'Ljava/util/Hashtable;'),
                JavaOpcodes.LDC_W(name),
                JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),

                # If there's nothing in the globals, then look for a builtin.
                IF(
                    [JavaOpcodes.DUP()],
                    JavaOpcodes.IFNONNULL
                ),
                    JavaOpcodes.POP(),
                    JavaOpcodes.GETSTATIC('org/Python', 'builtins', 'Ljava/util/Hashtable;'),
                    JavaOpcodes.LDC_W(name),
                    JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),

                    # If we still don't have something, throw a NameError.
                    IF(
                        [JavaOpcodes.DUP()],
                        JavaOpcodes.IFNONNULL
                    ),
                        JavaOpcodes.POP(),
                        JavaOpcodes.NEW('org/python/exceptions/NameError'),
                        JavaOpcodes.DUP(),
                        JavaOpcodes.LDC_W(name),
                        JavaOpcodes.INVOKESPECIAL('org/python/exceptions/NameError', '<init>', '(Ljava/lang/String;)V'),
                        JavaOpcodes.ATHROW(),
                    END_IF(),

                END_IF(),
                # Make sure we actually have a Python object
                JavaOpcodes.CHECKCAST('org/python/types/Object')
            )

    def delete_name(self, name, allow_locals=True):
        try:
            # Look for a local first.
            if allow_locals:
                self.add_opcodes(
                    ADELETE_name(self, name)
                )
            else:
                raise KeyError('Not scanning locals')
        except KeyError:
            self.add_opcodes(
                # If there isn't a local, look for a global
                JavaOpcodes.GETSTATIC(self.module.descriptor, 'globals', 'Ljava/util/Hashtable;'),
                JavaOpcodes.LDC_W(name),
                JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'remove', '(Ljava/lang/Object;)Ljava/lang/Object;'),
            )

    def extract(self, code, debug=False):
        """Break a code object into the parts it defines, populating the
        provided block.

        """
        instructions = list(dis.Bytecode(code))

        blocks = find_blocks(instructions)

        i = len(instructions)
        commands = []
        while i > 0:
            i, command = extract_command(instructions, blocks, i)
            commands.append(command)

        commands.reverse()

        if False:
            print ('=====' * 10)
            print (code)
            print ('-----' * 10)
            for command in commands:
                command.dump()
            print ('=====' * 10)

        # Append the extracted commands to any pre-existing ones.
        self.commands.extend(commands)

    def tweak(self):
        """Tweak the bytecode generated for this block."""
        pass

    def add_opcodes(self, *opcodes):
        # Add the opcodes to the code list and process them.
        for opcode in opcodes:
            # print("ADD OPCODE", id(opcode), opcode)
            if opcode.process(self):
                self.code.append(opcode)

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

        for opcode in self.code:
            depth = depth + opcode.stack_effect
            # print("   ", opcode, depth)
            if depth > max_depth:
                max_depth = depth
        return max_depth

    def ignore_empty(self):
        if len(self.code) == 1 and isinstance(self.code[0], JavaOpcodes.RETURN):
            raise IgnoreBlock()
        elif len(self.code) == 2 and isinstance(self.code[1], JavaOpcodes.ARETURN):
            raise IgnoreBlock()

    def void_return(self):
        """Ensure that end of the code sequence is a Java-style return of void.

        Java has a separate opcode for VOID returns, which is different to
        RETURN NULL. Replace "SET NULL" "ARETURN" pair with "RETURN".
        """

        if len(self.code) >= 2 and isinstance(self.code[-2], JavaOpcodes.ACONST_NULL) and isinstance(self.code[-1], JavaOpcodes.ARETURN):
            return_opcode = JavaOpcodes.RETURN()

            # Update the jump operation to point at the new return opcode.
            for opcode in self.code[-1].references:
                opcode.jump_op = return_opcode
                return_opcode.references.append(opcode)

            for opcode in self.code[-2].references:
                opcode.jump_op = return_opcode
                return_opcode.references.append(opcode)

            # Then, check to see if either opcode had a line number association.
            # if so, preserve the first one.
            if self.code[-2].starts_line is not None:
                return_opcode.starts_line = self.code[-2].starts_line
            elif self.code[-1].starts_line is not None:
                return_opcode.starts_line = self.code[-1].starts_line

            self.code = self.code[:-2] + [return_opcode]

    def add_return(self):
        self.add_opcodes(JavaOpcodes.RETURN())

    def transpile(self):
        """Create a JavaCode object representing the commands stored in the block

        May raise ``IgnoreBlock`` if the block should be ignored.
        """
        # Convert the sequence of commands into instructions.
        # Most of the instructions will be opcodes. However, some will
        # be instructions to add exception blocks, line number references, etc
        for cmd in self.commands:
            cmd.transpile(self)

        # Java requires that every body of code finishes with a return.
        # Make sure there is one.
        if len(self.code) == 0 or not isinstance(self.code[-1], (JavaOpcodes.RETURN, JavaOpcodes.ARETURN)):
            self.add_return()

        # Since we've processed all the Python opcodes, we can now resolve
        # all the unknown jump targets.
        # print('>>>>> Resolve references')
        for target, references in self.unknown_jump_targets.items():
            # print("   resolving %s references to %s" % (len(references), target))
            for opcode, position in references:
                resolve_jump(opcode, self, target, position)

        # Provide any tweaks that are needed because of the context in which
        # the block is being used.
        # print('>>>>> Tweak opcodes')
        self.tweak()

        # Now that we have a complete opcode list, postprocess the list
        # with the known offsets.
        offset = 0
        # print('>>>>> set offsets')
        for index, instruction in enumerate(self.code):
            # print("%4d:%4d (%s) %s" % (index, offset, id(instruction), instruction))
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
        for jump in self.jumps:
            # print ("JUMP", id(jump), jump, jump.java_offset, jump.jump_op, id(jump.jump_op))

            try:
                jump.offset = jump.jump_op.java_offset - jump.java_offset
            except AttributeError:
                jump.offset = jump.jump_op.start_op.java_offset - jump.java_offset

        # Construct a line number table from
        # the source code reference data on opcodes.
        line_numbers = []
        for code in self.code:
            if code.starts_line is not None:
                line_numbers.append((code.java_offset, code.starts_line))
        line_number_table = LineNumberTable(line_numbers)

        return JavaCode(
            max_stack=self.stack_depth() + len(exceptions),
            max_locals=len(self.localvars),
            code=self.code,
            exceptions=exceptions,
            attributes=[
                line_number_table
            ]
        )
