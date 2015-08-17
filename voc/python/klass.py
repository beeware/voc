import dis
import os

from ..java import (
    Class as JavaClass,
    Method as JavaMethod,
    Code as JavaCode,
    opcodes as JavaOpcodes,
    SourceFile,
    # LineNumberTable
)
# from .klass import transpile as transpile_class
from .method import transpile as transpile_method
from .utils import split_bytecode


def transpile(namespace, sourcefile, classblock):
    modulename = os.path.splitext(os.path.basename(sourcefile))[0]
    classname = classblock[-1].argval
    classfile = JavaClass('/'.join(namespace.split('.') + [modulename, classname]))
    classfile.attributes.append(SourceFile(os.path.basename(sourcefile)))

    # Every bytecode can add to the stack, or remove from the stack.
    # The stack starts empty; when the stack goes back to being empty
    # again after one or more opcodes, that deliniates a self contained
    # block of code. That code can follow some identifiable patterns
    # that require different handling in the translation into Java.
    blocks = split_bytecode(dis.Bytecode(classblock[1].argval))

    # Ultimately, all blocks are going to end up either:
    #  * Defining a class
    #  * Defining a static method
    #  * Defining the static initializer block
    #  * Defining the mainline
    # classes = []
    static_methods = []
    static_block = []
    init_method = None
    instance_methods = []

    for block in blocks:
        for instruction in block:
            print ('  ', instruction.opname, instruction.argval if instruction.arg else '')

        # Equivalent of "import dom":
        #   LOAD_CONST 0
        #   LOAD CONST None
        #   IMPORT_NAME <name>
        #   STORE_NAME <name>
        if len(block) > 1 and block[-2].opname == 'IMPORT_NAME':
            print ("Handle import of", block[-2].argval)

        # Equivalent of "class <Name>:":
        #   LOAD_BUILD_CLASS
        #   LOAD_CONST <code>
        #   LOAD_CONST <Name>
        #   MAKE_FUNCTION 0
        #   LOAD_CONST <Name>
        #   CALL_FUNCTION 2
        #   STORE_NAME <Name>
        elif block[0].opname == 'LOAD_BUILD_CLASS':
            # print ("Found inner class", block[-1].argval)
            # classes.append(self.transpile_class(sourcefile, block))
            print ("WARNING: Inner class %s will be ignored!" % block[-1].argval)

        # Equivalent of "if __name__ == '__main__':":
        #   ... default args ---
        #   LOAD_CONST <code>
        #   LOAD_CONST <classname>.__init__
        #   MAKE_FUNCTION <n_defaults>
        #   STORE_NAME __init__
        elif (len(block) >= 4
                and block[-4].opname == 'LOAD_CONST'
                and block[-3].opname == 'LOAD_CONST'
                and block[-2].opname == 'MAKE_FUNCTION'
                and block[-1].opname == 'STORE_NAME'):

            if block[-1].argval == '__init__':
                print("Found __init__ block")
                init_method = transpile_method(block, methodname='<name>')
            else:
                print("Found instance method %s" % block[-1].argval)
                instance_methods.append(transpile_method(block, methodname=block[-1].argval.split('.')[-1]))

        # All other module-level content goes into the static block
        # for the class.
        else:
            static_block.extend(block)

        print()

    if static_block:
        # If we have static block content, add a static block to the class
        static_init = JavaMethod('<clinit>', '()V', public=False, static=True)

        code = JavaCode(
                max_stack=2,
                max_locals=1,
                code=[
                    JavaOpcodes.GETSTATIC('java/lang/System', 'out', 'Ljava/io/PrintStream;'),
                    JavaOpcodes.LDC('Hello, Static Point World'),
                    JavaOpcodes.INVOKEVIRTUAL('java/io/PrintStream', 'println', '(Ljava/lang/String;)V'),
                    JavaOpcodes.RETURN(),
                ],
            )

        static_init.attributes.append(code)
        classfile.methods.append(static_init)

    if init_method:
        classfile.methods.append(init_method)
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

    for method in static_methods:
        classfile.methods.append(method)

    for method in instance_methods:
        classfile.methods.append(method)

    return classname, classfile
