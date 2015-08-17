from ..java import (
    Method as JavaMethod,
    Code as JavaCode,
    opcodes as JavaOpcodes,
)


def transpile(block, methodname=None):
    if methodname is None:
        methodname = block[-1].argval
    method = JavaMethod(
        methodname,
        '()V',
        attributes=[
            JavaCode(
                max_stack=2,
                max_locals=1,
                code=[
                    JavaOpcodes.GETSTATIC('java/lang/System', 'out', 'Ljava/io/PrintStream;'),
                    JavaOpcodes.LDC('Hello, World'),
                    JavaOpcodes.INVOKEVIRTUAL('java/io/PrintStream', 'println', '(Ljava/lang/String;)V'),
                    JavaOpcodes.RETURN(),
                ],
            )
        ]
    )
    return method
