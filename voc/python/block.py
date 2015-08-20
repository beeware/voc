from ..java import Code as JavaCode


def transpile(commands):
    code = []
    for cmd in commands:
        code.extend(cmd.operation.convert(cmd.arguments))

    return JavaCode(
        max_stack=20,
        max_locals=10,
        code=code
    )
