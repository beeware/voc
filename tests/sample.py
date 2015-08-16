from voc.java import Class, Method, SourceFile, Code, LineNumberTable, opcodes


print("Creating class 'sample'...")

classfile = Class('sample')

classfile.methods.append(
    Method(
        '<init>',
        '()V',
        attributes=[
            Code(
                max_stack=1,
                max_locals=1,
                code=[
                    opcodes.ALOAD_0(),
                    opcodes.INVOKESPECIAL('java/lang/Object', '<init>', '()V'),
                    opcodes.RETURN(),
                ],
                attributes=[
                    LineNumberTable({
                        0: 3
                    })
                ]
            )
        ]
    )
)

classfile.methods.append(
    Method(
        'main',
        '([Ljava/lang/String;)V',
        static=True,
        attributes=[
            Code(
                max_stack=0,
                max_locals=1,
                code=[
                    opcodes.RETURN(),
                ],
                attributes=[
                    LineNumberTable({
                        0: 8,
                    })
                ]
            )
        ]
    )
)

classfile.methods.append(
    Method(
        '<clinit>',
        '()V',
        public=False,
        static=True,
        attributes=[
            Code(
                max_stack=2,
                max_locals=1,
                code=[
                    opcodes.GETSTATIC('java/lang/System', 'out', 'Ljava/io/PrintStream;'),
                    opcodes.LDC('Hello, World'),
                    opcodes.INVOKEVIRTUAL('java/io/PrintStream', 'println', '(Ljava/lang/String;)V'),
                    opcodes.RETURN(),
                ],
                attributes=[
                    LineNumberTable({
                        0: 5,
                        8: 6
                    })
                ]
            )
        ]
    )
)

classfile.attributes.append(SourceFile('PyObject.java'))

print("Writing sample.class...")
with open('sample.class', 'wb') as out:
    classfile.write(out)
print("Done.")
