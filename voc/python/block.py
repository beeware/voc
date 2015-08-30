import dis

from ..java import (
    Code as JavaCode,
    opcodes as JavaOpcodes,
    ExceptionInfo as JavaExceptionInfo,
    StackMapTable as JavaStackMapTable,
    SameLocals1StackItemFrame,
    # SameFrame,
    ObjectVariableInfo
)

from .utils import extract_command, stack_depth


class IgnoreBlock(Exception):
    """An escape hatch; enable a block to be flagged as ignorable"""
    pass


class Block:
    def __init__(self, parent=None, commands=None):
        self.parent = parent
        self.commands = commands if commands else []
        self.localvars = {}

    @property
    def is_module(self):
        return False

    def extract(self, code):
        """Break a code object into the parts it defines, populating the
        provided block.

        """
        instructions = list(dis.Bytecode(code))
        i = len(instructions)
        commands = []
        while i > 0:
            i, command = extract_command(instructions, i)
            commands.append(command)

        commands.reverse()

        print ('=====' * 10)
        print (code)
        print ('-----' * 10)
        for command in commands:
            command.dump()
        print ('=====' * 10)

        # Append the extracted commands to any pre-existing ones.
        self.commands.extend(commands)

    def tweak(self, code):
        """Tweak the bytecode generated for this block."""
        return code

    def ignore_empty(self, code):
        if len(code) == 1 and isinstance(code[0], JavaOpcodes.RETURN):
            raise IgnoreBlock()
        elif len(code) == 2 and isinstance(code[1], JavaOpcodes.ARETURN):
            raise IgnoreBlock()
        return code

    def void_return(self, code):
        if len(code) >= 2 and isinstance(code[-2], JavaOpcodes.ACONST_NULL) and isinstance(code[-1], JavaOpcodes.ARETURN):
            code = code[:-2] + [JavaOpcodes.RETURN()]
        return code

    def transpile(self):
        """Create a JavaCode object representing the commands stored in the block

        May raise ``IgnoreBlock`` if the block should be ignored.
        """
        # Convert the sequence of commands into instructions.
        # Most of the instructions will be opcodes. However, some will
        # be instructions to add exception blocks, line number references,
        # or other
        code = []
        try_catches = []
        prev = None
        for cmd in self.commands:
            for instruction in cmd.operation.convert(self, cmd.arguments):
                if prev is not None:
                    prev.post_process(instruction)
                instruction.process(code, try_catches)
                prev = instruction

        # Java requires that every body of code finishes with a return.
        # Make sure there is one.
        if not isinstance(code[-1], (JavaOpcodes.RETURN, JavaOpcodes.ARETURN)):
            code.append(JavaOpcodes.RETURN())

        # Provide any tweaks that are needed because of the context in which
        # the block is being used.
        code = self.tweak(code)

        # Now that we have a complete opcode list, postprocess the list
        # with the known offsets...
        offset = 0
        for instruction in code:
            instruction.code_offset = offset
            offset += len(instruction)

        # ... then construct the exception table and stack map table, updating
        # any end-of-exception GOTO operations with the right opcode.
        stack_map_table = JavaStackMapTable()
        exceptions = []
        for try_catch in try_catches:
            for descriptor, catch_op in try_catch.handlers:
                exceptions.append(JavaExceptionInfo(
                    try_catch.start_op.code_offset,
                    try_catch.jump_op.code_offset,
                    catch_op.code_offset,
                    descriptor
                ))

                # Stack map frame for the catch block.
                stack_map_table.entries.append(
                    SameLocals1StackItemFrame(
                        catch_op.code_offset,
                        ObjectVariableInfo(descriptor)
                    )
                )

                # Stack map frame for the return to normal code.
                stack_map_table.entries.append(
                    SameLocals1StackItemFrame(
                        try_catch.end_op.code_offset - catch_op.code_offset - 1,
                        ObjectVariableInfo('org/python/Function')  # FIXME
                    )
                )

            try_catch.jump_op.offset = try_catch.end_op.code_offset - try_catch.jump_op.code_offset

        return JavaCode(
            max_stack=stack_depth(code),
            max_locals=len(self.localvars),
            code=code,
            exceptions=exceptions,
            attributes=[
                stack_map_table,
            ]
        )
