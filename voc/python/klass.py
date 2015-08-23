import os

from ..java import (
    Class as JavaClass,
    Method as JavaMethod,
    Code as JavaCode,
    opcodes as JavaOpcodes,
    SourceFile,
    # LineNumberTable
)


def transpile(context, parts):
    classfile = JavaClass(context.class_descriptor)
    classfile.attributes.append(SourceFile(os.path.basename(context.sourcefile)))

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

    return context.classname, classfile
