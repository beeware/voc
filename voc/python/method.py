from ..java import (
    Method as JavaMethod,
    Code as JavaCode,
)


def transpile(methodname, parts):

    method = JavaMethod(
        methodname,
        '()V',
        attributes=parts.block
    )
    return method
