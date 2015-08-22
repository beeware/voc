import os

from ..java import (
    Class as JavaClass,
    Method as JavaMethod,
    Code as JavaCode,
    opcodes as JavaOpcodes,
    SourceFile,
    # LineNumberTable
)


def transpile(namespace, sourcefile, moduleparts):
    classfiles = []
    modulename = os.path.splitext(os.path.basename(sourcefile))[0]

    # If there is any static content, generate a classfile
    # for this module

    classfile = JavaClass('/'.join(namespace.split('.') + [modulename]))
    classfile.attributes.append(SourceFile(os.path.basename(sourcefile)))

    if moduleparts.block:
        static_init = JavaMethod('<clinit>', '()V', public=False, static=True)

        static_init.attributes.append(moduleparts.block)

        classfile.methods.append(static_init)

    main_method = JavaMethod('main', '([Ljava/lang/String;)V', public=True, static=True)
    if moduleparts.main is None:
        print("Adding default main method...")
        main_code = JavaCode(max_stack=0, max_locals=1, code=[JavaOpcodes.RETURN()])
    else:
        main_code = moduleparts.main

    main_method.attributes.append(main_code)
    classfile.methods.append(main_method)

    for method in moduleparts.methods:
        classfile.methods.append(method)

    if moduleparts.init:
        print("Unexpected __init__ method in static context... ignoring")

    classfiles.append((modulename, None, classfile))

    # Also output any subclasses.
    for classname, classfile in moduleparts.classes:
        classfiles.append((classname, modulename, classfile))

    return classfiles
