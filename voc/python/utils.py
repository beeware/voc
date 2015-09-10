from . import opcodes


class Command:
    """A command is a sequence of instructions producing a distinct result.

    The `operation` is the final instruction that yields a result.
    A series of other instructions, known as `arguments` will be used
    to execute `operation`.

    The command also tracks the line number and code offset that it
    represents, plus whether the command is a jump target.

    Each argument is itself a Command; leaf nodes are Commands with no
    arguments.

    A command knows how many items it will pop from the stack, and
    how many it will push onto the stack. The stack count on a Command
    reflects the effect of the operation itself, plus *all* the arguments.

    A command may also encompass an internal block - for example, a for
    or while loop. Those blocks
    """
    def __init__(self, instruction):
        self.operation = instruction
        self.arguments = []

    def __repr__(self):
        try:
            return '<Command %s (%s args)> %s' % (self.operation.opname, len(self.arguments), self.arguments[0].operation.name)
        except:
            return '<Command %s (%s args)>' % (self.operation.opname, len(self.arguments))

    @property
    def consume_count(self):
        return sum(c.consume_count for c in self.arguments) + self.operation.consume_count

    @property
    def product_count(self):
        return sum(c.product_count for c in self.arguments) + self.operation.product_count

    def dump(self, depth=0):
        if self.operation.end_block:
            child_depth = 0
            depth = 0
        else:
            child_depth = depth + 1
        for op in self.arguments:
            op.dump(depth=child_depth)
        print ('%s%s%s:%s ' % (
                '{' if self.operation.start_block else
                    '}' if self.operation.end_block else ' ',
                '>' if self.operation.is_jump_target else ' ',
                "%4s" % self.operation.starts_line if self.operation.starts_line is not None else '    ',
                self.operation.code_offset
            ) + '    ' * depth, self.operation)


class Frame:
    """A representation of a stack frame.
    """
    def __init__(self, frame_type=None):
        self.frame_type = frame_type
        self.stack_depth = 0


def extract_command(instructions, i, frame_stack=None):
    """Extract a single command from the end of the instruction list.

    See the definition of Command for details on the recursive nature
    of commands. We start at the *end* of the instruction list and
    work backwards because each command is essentially working towards
    a final result; each Command can be thought of as a "result".
    """
    global overall_depth
    if frame_stack is None:
        frame_stack = [Frame()]
    current_frame = frame_stack[-1]

    i = i - 1
    instruction = instructions[i]
    argval = instruction.argval

    OpType = getattr(opcodes, instruction.opname)

    # If this instruction is preceded by EXTENDED_ARG, then
    # there is more arugment information to come. Integrate it
    # into the instruction argument we've already read.
    if i > 0 and instructions[i - 1].opname == 'EXTENDED_ARG':
        i = i - 1
        extended = instructions[i]

        argval = argval | extended.argval

    if instruction.arg is None:
        opcode = OpType(instruction.offset, instruction.starts_line, instruction.is_jump_target)
    else:
        opcode = OpType(argval, instruction.offset, instruction.starts_line, instruction.is_jump_target)

    cmd = Command(opcode)

    # If we find the end of a code block, create a command
    # that contains everything from the start of the block
    if opcode.end_block:
        frame_stack.append(Frame(opcode.end_block))
        while True:
            i, arg = extract_command(instructions, i, frame_stack=frame_stack)
            cmd.arguments.append(arg)
            if arg.operation.start_block:
                break

    # If we find the start of a code block, that closes out
    # a command, so just return.
    elif opcode.start_block:
        frame = frame_stack.pop()
        # Safety check - make sure we're found the
        # type of block we were expecting

        assert isinstance(frame.frame_type, bool) or frame.frame_type == opcode.start_block
        return i, cmd

    # Otherwise; look for a group of commands that will
    # bring the stack back to an empty state, indicating
    # an endpoint in a command chain.
    else:
        stack = cmd.operation.consume_count

        while stack > 0 and i > 0:
            i, arg = extract_command(instructions, i, frame_stack=frame_stack)
            cmd.arguments.append(arg)

            stack = stack + arg.consume_count - arg.product_count

    # Since we did everything backwards, reverse to get
    # arguments back in the right order.
    cmd.arguments.reverse()
    return i, cmd
