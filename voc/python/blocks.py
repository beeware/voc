import dis

from ..java import (
    Code as JavaCode,
    opcodes as JavaOpcodes,
    ExceptionInfo as JavaExceptionInfo,
)

from .utils import extract_command
from .opcodes import ASTORE_name, ALOAD_name


class IgnoreBlock(Exception):
    """An escape hatch; enable a block to be flagged as ignorable"""
    pass


class CodeParts:
    def __init__(self, context):
        self.context = context
        self.code = []
        self.try_catches = []
        self.if_blocks = []

    def tweak(self):
        self.code = self.context.tweak(self.code)

    def stack_depth(self):
        "Evaluate the maximum stack depth required by a sequence of Java opcodes"
        depth = 0
        max_depth = 0
        for opcode in self.code:
            # print("   ", opcode)
            depth = depth + opcode.stack_effect
            if depth > max_depth:
                max_depth = depth
        return max_depth


class Block:
    def __init__(self, parent=None, commands=None):
        self.parent = parent
        self.commands = commands if commands else []
        self.localvars = {}

    def store_name(self, name, arguments):
        return [
            ASTORE_name(self.localvars, self.name)
        ]

    def load_name(self, name, arguments):
        return [
            ALOAD_name(self.localvars, self.name)
        ]

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

        parts = CodeParts(self)
        prev = None
        for cmd in self.commands:
            for instruction in cmd.operation.convert(self, cmd.arguments):
                instruction.process(parts)
                if prev is not None:
                    prev.post_process(parts)
                prev = instruction
        if prev is not None:
            prev.post_process(parts)

        # Java requires that every body of code finishes with a return.
        # Make sure there is one.
        if not isinstance(parts.code[-1], (JavaOpcodes.RETURN, JavaOpcodes.ARETURN)):
            parts.code.append(JavaOpcodes.RETURN())

        # Provide any tweaks that are needed because of the context in which
        # the block is being used.
        parts.tweak()

        # Now that we have a complete opcode list, postprocess the list
        # with the known offsets.
        offset = 0
        for index, instruction in enumerate(parts.code):
            instruction.code_index = index
            instruction.code_offset = offset
            offset += len(instruction)

        # Then construct the exception table, updating any
        # end-of-exception GOTO operations with the right opcode.
        # Record a frame range for each one.
        exceptions = []
        for try_catch in parts.try_catches:
            for handler in try_catch.handlers:
                exceptions.append(JavaExceptionInfo(
                    try_catch.start_op.code_offset,
                    try_catch.jump_op.code_offset,
                    handler.start_op.code_offset,
                    handler.descriptor
                ))

            try_catch.jump_op.offset = try_catch.end_op.code_offset - try_catch.jump_op.code_offset

        # Lastly, update any IF-related offsets
        for if_block in parts.if_blocks:
            if_block.if_op.offset = if_block.end_op.code_offset - if_block.if_op.code_offset

        return JavaCode(
            max_stack=parts.stack_depth(),
            max_locals=len(self.localvars),
            code=parts.code,
            exceptions=exceptions,
        )
