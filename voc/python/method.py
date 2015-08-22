from ..java import Method as JavaMethod


def transpile(methodname, parts, static=False):
    method = JavaMethod(
        methodname,
        '()V',
        static=static,
        attributes=[
            parts.block
        ]
    )
    return method
