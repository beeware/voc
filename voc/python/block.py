from ..java import Code as JavaCode, opcodes as JavaOpcodes


def transpile(context, commands):
    code = []
    for cmd in commands:
        code.extend(cmd.operation.convert(context.localvars, cmd.arguments))

    # Make sure there is a return at the end.
    if not isinstance(code[-1], (JavaOpcodes.RETURN, JavaOpcodes.ARETURN)):
        code.append(JavaOpcodes.RETURN())

    # Check for an empty block (i.e., a block that only has a return in it,
    # or a return of a null)
    if context.ignore_empty:
        if len(code) == 1 and isinstance(code[0], JavaOpcodes.RETURN):
            return None
        elif len(code) == 2 and isinstance(code[1], JavaOpcodes.ARETURN):
            return None

    # If we require a void return, convert any "return None" into a straight return.
    if context.void_return:
        if len(code) > 2 and isinstance(code[-1], JavaOpcodes.ARETURN) and isinstance(code[-2], JavaOpcodes.ACONST_NULL):
            code = code[:-2] + [JavaOpcodes.RETURN()]

    return JavaCode(
        max_stack=20,
        max_locals=len(context.localvars) + 1,
        code=code
    )
