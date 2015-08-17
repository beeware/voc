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
from .klass import transpile as transpile_class
from .method import transpile as transpile_method
from .utils import split_bytecode, max_stack_required


def transpile(namespace, sourcefile, code):
    classfiles = []
    modulename = os.path.splitext(os.path.basename(sourcefile))[0]

    # Every bytecode can add to the stack, or remove from the stack.
    # The stack starts empty; when the stack goes back to being empty
    # again after one or more opcodes, that deliniates a self contained
    # block of code. That code can follow some identifiable patterns
    # that require different handling in the translation into Java.
    blocks = split_bytecode(dis.Bytecode(code))

    # Ultimately, all blocks are going to end up either:
    #  * Defining a class
    #  * Defining a static method
    #  * Defining the static initializer block
    #  * Defining the mainline
    classes = []
    static_methods = []
    static_block = []
    main_block = []

    main_end = None
    for block in blocks:
        if main_end is not None:
            # Marker for the end of the main block:
            #   JUMP_FORWARD <target>
            if len(block) == 1 and block[0].opname == 'JUMP_FORWARD' and block[0].argval == main_end:
                main_end = None
            else:
                main_block.extend(block)
        else:
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
                print ("Found class", block[-1].argval)
                classes.append(transpile_class(namespace, sourcefile, block))

            # Equivalent of "def <name>(...):":
            #   ... load arg defaults ...
            #   LOAD_CONST <code>
            #   LOAD_CONST <name>
            #   MAKE_FUNCTION <n_defaults>
            #   STORE_NAME <name>
            elif len(block) > 1 and block[-2].opname == 'MAKE_FUNCTION':
                print ("Found static method", block[-1].argval)
                static_methods.append(transpile_method(block))

            # Equivalent of "if __name__ == '__main__':":
            #   LOAD_NAME __name__
            #   LOAD_CONST __main__
            #   COMPARE_OP ==
            #   POP_JUMP_IF_FALSE <target>
            elif (len(block) == 4
                    and block[0].opname == 'LOAD_NAME' and block[0].argval == '__name__'
                    and block[1].opname == 'LOAD_CONST' and block[1].argval == '__main__'
                    and block[2].opname == 'COMPARE_OP' and block[2].argval == '=='
                    and block[3].opname == 'POP_JUMP_IF_FALSE'):
                print("Found main block")
                main_end = block[3].argval

            # All other module-level content goes into the static block
            # for the class.
            else:
                static_block.extend(block)

    # If there is any static content, generate a classfile
    # for this module
    if static_block or main_block:
        classfile = JavaClass('/'.join(namespace.split('.') + [modulename]))
        classfile.attributes.append(SourceFile(os.path.basename(sourcefile)))

        if static_block:
            max_stack = max_stack_required(static_block)

            static_init = JavaMethod('<clinit>', '()V', public=False, static=True)
            code = JavaCode(
                    max_stack=2,
                    max_locals=1,
                    code=[
                        JavaOpcodes.GETSTATIC('java/lang/System', 'out', 'Ljava/io/PrintStream;'),
                        JavaOpcodes.LDC('Hello, Static World'),
                        JavaOpcodes.INVOKEVIRTUAL('java/io/PrintStream', 'println', '(Ljava/lang/String;)V'),
                        JavaOpcodes.RETURN(),
                    ],
                )

            static_init.attributes.append(code)
            classfile.methods.append(static_init)

        main = JavaMethod('main', '([Ljava/lang/String;)V', public=True, static=True)
        if main_block:
            code = JavaCode(
                    max_stack=2,
                    max_locals=1,
                    code=[
                        JavaOpcodes.GETSTATIC('java/lang/System', 'out', 'Ljava/io/PrintStream;'),
                        JavaOpcodes.LDC('Hello, World'),
                        JavaOpcodes.INVOKEVIRTUAL('java/io/PrintStream', 'println', '(Ljava/lang/String;)V'),
                        JavaOpcodes.RETURN(),
                    ],
                )
        else:
            print("Adding default main method...")
            code = JavaCode(max_stack=0, max_locals=1, code=[JavaOpcodes.RETURN()])

        main.attributes.append(code)
        classfile.methods.append(main)

        for method in static_methods:
            classfile.methods.append(method)

        classfiles.append((modulename, None, classfile))

    # Also output any subclasses.
    for klass, classfile in classes:
        classfiles.append((klass, modulename, classfile))

    return classfiles
