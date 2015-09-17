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
    def __init__(self, instruction, arguments=None):
        self.operation = instruction
        if arguments:
            self.arguments = arguments
        else:
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
        for op in self.arguments:
            op.dump(depth=depth + 1)
        print ('%s%s%4s:%4d -%s +%s' % (
                '{' if self.operation.start_block else
                    '}' if self.operation.end_block else ' ',
                '>' if self.operation.is_jump_target else ' ',
                self.operation.starts_line if self.operation.starts_line is not None else '    ',
                self.operation.python_offset,
                self.operation.consume_count,
                self.operation.product_count
            ) + '    ' * depth, self.operation)


class Frame:
    """A representation of a stack frame.
    """
    def __init__(self, frame_type=None):
        self.frame_type = frame_type
        self.depth = 0
        self.available = 0

    def __repr__(self):
        return u'<Frame %s: %s>' % (id(self), self.frame_type)


def extract_command(instructions, i, frame_stack=None):
    """Extract a single command from the end of the instruction list.

    See the definition of Command for details on the recursive nature
    of commands. We start at the *end* of the instruction list and
    work backwards because each command is essentially working towards
    a final result; each Command can be thought of as a "result".
    """
    if frame_stack is None:
        frame_stack = [Frame()]
    current_frame = frame_stack[-1]
    current_frame.depth += 1

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

    # print('>', instruction.offset, cmd.operation.opname, current_frame)

    ended_blocks = 0
    # If we find the end of a code block, create a command
    # that contains everything from the start of the block
    if opcode.end_block:
        # print ("END BLOCK", opcode, opcode.end_block)
        if opcode.end_block == 'finally' and current_frame.frame_type != 'except':
            opcode.end_block = 'except'
        elif isinstance(opcode.end_block, bool) and current_frame.frame_type == 'except':
            opcode.end_block = 'finally'

        # print ("Add %s frame" % opcode.end_block)
        frame_stack.append(Frame(opcode.end_block))
        current_frame = frame_stack[-1]

        while ended_blocks == 0:
            i, arg, ended_blocks = extract_command(instructions, i, frame_stack=frame_stack)
            cmd.arguments.append(arg)

        # frame_types = [f.frame_type for f in frame_stack[1:]]
        # print ("END %s BLOCK(s) %s on %s" % (ended_blocks, opcode.start_block, frame_types), repr(current_frame.frame_type))

        ended_blocks -= 1
        frame_stack.pop()
        current_frame = frame_stack[-1]

    # If we find the start of a code block, that closes out
    # a command, so just return.
    elif opcode.start_block:
        # Safety check - make sure we're found the
        # type of block we were expecting
        # frame_types = [f.frame_type for f in frame_stack[1:]]
        # print ("START BLOCK %s on %s" % (opcode.start_block, frame_types), repr(current_frame.frame_type))
        if opcode.start_block == 'except':
            return i, cmd, 2
        else:
            return i, cmd, 1

    # Otherwise; look for a group of commands that will
    # bring the stack back to an empty state, indicating
    # an endpoint in a command chain.
    else:
        required = cmd.operation.consume_count

        # print("   top level frame", current_frame.frame_type, current_frame.depth)
        if current_frame.frame_type == 'except':
            if cmd.operation.opname == 'DUP_TOP' and instruction.is_jump_target:
                current_frame.available = 3
                pool_consume = min(current_frame.available, required)
                current_frame.available -= pool_consume
                required -= pool_consume

        # print("   %s has %s required inputs (initial)" % (current_frame, required))
        while required > 0 and ended_blocks == 0:
            i, arg, ended_blocks = extract_command(instructions, i, frame_stack=frame_stack)
            cmd.arguments.append(arg)
            # print ('   ', arg.operation.opname, 'produces', arg.operation.product_count)
            required = required - arg.operation.product_count

            # print("   still requires %s (%s in pool); adjust" % (required, current_frame.available))
            if required < 0:
                # print("   Produced more than needed")
                current_frame.available -= required

            if required > 0 and current_frame.available:
                # print("   Use stored stash")
                pool_consume = min(current_frame.available, required)
                current_frame.available -= pool_consume
                required -= pool_consume

            # print("   %s has %s required inputs (%s in pool)" % (current_frame, required, current_frame.available))

    # print('<', instruction.offset, cmd.operation.opname, current_frame)

    current_frame.depth -= 1

    # Since we did everything backwards, reverse to get
    # arguments back in the right order.
    cmd.arguments.reverse()
    return i, cmd, ended_blocks
