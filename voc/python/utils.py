import dis


def split_bytecode(instructions):
    """Split a list of bytecodes into it's functional blocks.

    Uses dis.stack_effect() to work out the net effect of a body of code.

    Also returns the maximum stack depth required by the bytecode.
    """
    blocks = []
    cmd = []
    stack = 0
    for instruction in instructions:
        print (">>", stack, instruction.opname, instruction.argval if instruction.arg else '')
        cmd.append(instruction)
        stack = stack + dis.stack_effect(instruction.opcode, instruction.arg)

        if stack == 0:
            blocks.append(cmd)
            cmd = []
    return blocks


def max_stack_required(instructions):
    stack = 0
    max_stack = 0
    for instruction in instructions:
        stack = stack + dis.stack_effect(instruction.opcode, instruction.arg)

        if stack > max_stack:
            max_stack = stack

    return max_stack
