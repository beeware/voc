from ..java import Code as JavaCode, opcodes as JavaOpcodes


def transpile(commands, ignore_empty=False):
    localvars = {}
    code = []
    for cmd in commands:
        code.extend(cmd.operation.convert(localvars, cmd.arguments))

    # Make sure there is a return at the end.
    if not isinstance(code[-1], (
                            JavaOpcodes.RETURN,
                            JavaOpcodes.ARETURN,
                            JavaOpcodes.DRETURN,
                            JavaOpcodes.FRETURN,
                            JavaOpcodes.IRETURN,
                            JavaOpcodes.LRETURN
                        )):
        code.append(JavaOpcodes.RETURN())

    # Check for an empty block (i.e., a block that only has a return in it)
    if ignore_empty:
        if len(code) == 1 and isinstance(code[0], JavaOpcodes.RETURN):
            return None

    return JavaCode(
        max_stack=20,
        max_locals=len(localvars) + 1,
        code=code
    )
