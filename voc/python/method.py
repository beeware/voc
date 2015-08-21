from ..java import Method as JavaMethod


def transpile(methodname, parts):
    method = JavaMethod(
        methodname,
        '()V',
        attributes=[
            parts.block
        ]
    )
    return method
