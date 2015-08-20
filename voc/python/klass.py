import os

from ..java import (
    Class as JavaClass,
    Method as JavaMethod,
    Code as JavaCode,
    opcodes as JavaOpcodes,
    SourceFile,
    # LineNumberTable
)


def transpile(namespace, sourcefile, classname, parts):
    modulename = os.path.splitext(os.path.basename(sourcefile))[0]
    classfile = JavaClass('/'.join(namespace.split('.') + [modulename, classname]))
    classfile.attributes.append(SourceFile(os.path.basename(sourcefile)))

    if parts.block:
        # If we have block content, add a static block to the class
        static_init = JavaMethod('<clinit>', '()V', public=False, static=True)
        static_init.attributes.append(parts.block)
        classfile.methods.append(static_init)

    if parts.init:
        classfile.methods.append(parts.init)
    else:
        # Add default constructor
        classfile.methods.append(
            JavaMethod(
                '<init>',
                '()V',
                attributes=[
                    JavaCode(
                        max_stack=1,
                        max_locals=1,
                        code=[
                            JavaOpcodes.ALOAD_0(),
                            JavaOpcodes.INVOKESPECIAL('org/python/PyObject', '<init>', '()V'),
                            JavaOpcodes.RETURN(),
                        ],
                    )
                ]
            )
        )

    for method in parts.methods:
        classfile.methods.append(method)

    return classname, classfile
