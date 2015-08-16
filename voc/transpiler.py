import dis
import importlib
import marshal
import os
import py_compile

from voc.java import (
    Class as JavaClass,
    Method as JavaMethod,
    Code as JavaCode,
    opcodes as JavaOpcodes,
    SourceFile,
    # LineNumberTable
)


def transpile(sourcefile, namespace, outdir=None):
    print("Compiling %s..." % sourcefile)
    py_compile.compile(sourcefile)

    transpiler = Transpiler(namespace)

    transpiler.transpile_module(sourcefile)

    transpiler.write(outdir)


class Transpiler:
    def __init__(self, namespace):
        self.namespace = namespace
        self.classfiles = []

    def write(self, outdir):
        # Create directory tree to store classfile
        if outdir:
            dirparts = [outdir]
        else:
            dirparts = []
        dirparts = dirparts + self.namespace.split('.')
        dirname = os.path.join(*dirparts)

        try:
            os.makedirs(dirname)
        except FileExistsError:
            pass

        for classname, module, classfile in self.classfiles:

            if module:
                classfilename = os.path.join(dirname, module, '%s.class' % classname)
                try:
                    os.mkdir(os.path.join(dirname, module))
                except FileExistsError:
                    pass
            else:
                classfilename = os.path.join(dirname, '%s.class' % classname)

            print("Writing %s..." % classfilename)
            with open(classfilename, 'wb') as out:
                classfile.write(out)
        print("Done.")

    def split_bytecode(self, instructions):
        """Split a list of bytecodes into it's functional blocks.

        Uses dis.stack_effect() to work out the net effect of a body of code.

        Also returns the maximum stack depth required by the bytecode.
        """
        blocks = []
        cmd = []
        stack = 0
        for instruction in instructions:
            cmd.append(instruction)
            stack = stack + dis.stack_effect(instruction.opcode, instruction.arg)

            if stack == 0:
                blocks.append(cmd)
                cmd = []
        return blocks

    def max_stack_required(self, instructions):
        stack = 0
        max_stack = 0
        for instruction in instructions:
            stack = stack + dis.stack_effect(instruction.opcode, instruction.arg)

            if stack > max_stack:
                max_stack = stack

        return max_stack

    def transpile_module(self, sourcefile):
        classname = os.path.splitext(os.path.basename(sourcefile))[0]
        with open(importlib.util.cache_from_source(sourcefile), 'rb') as compiled:
            # Read off the magic from the start of the PYC file.
            compiled.read(12)

            # Decompile the code object.
            code = marshal.load(compiled)

        # Every bytecode can add to the stack, or remove from the stack.
        # The stack starts empty; when the stack goes back to being empty
        # again after one or more opcodes, that deliniates a self contained
        # block of code. That code can follow some identifiable patterns
        # that require different handling in the translation into Java.
        blocks = self.split_bytecode(dis.Bytecode(code))

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
                    classes.append(self.transpile_class(sourcefile, block))

                # Equivalent of "def <name>(...):":
                #   ... load arg defaults ...
                #   LOAD_CONST <code>
                #   LOAD_CONST <name>
                #   MAKE_FUNCTION <n_defaults>
                #   STORE_NAME <name>
                elif len(block) > 1 and block[-2].opname == 'MAKE_FUNCTION':
                    print ("Found static method", block[-1].argval)
                    static_methods.append(self.transpile_method(block))

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
            classfile = JavaClass('/'.join(self.namespace.split('.') + [classname]))
            classfile.attributes.append(SourceFile(os.path.basename(sourcefile)))

            if static_block:
                print (static_block)
                max_stack = self.max_stack_required(static_block)

                static_init = JavaMethod('<clinit>', '()V', public=False, static=True)
                code = JavaCode(
                        max_stack=max_stack,
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

            # Add default constructor
            # self.classfile.methods.append(
            #     JavaMethod(
            #         '<init>',
            #         '()V',
            #         attributes=[
            #             JavaCode(
            #                 max_stack=1,
            #                 max_locals=1,
            #                 code=[
            #                     JavaOpcodes.ALOAD_0(),
            #                     JavaOpcodes.INVOKESPECIAL('java/lang/Object', '<init>', '()V'),
            #                     JavaOpcodes.RETURN(),
            #                 ],
            #             )
            #         ]
            #     )
            # )

            for method in static_methods:
                classfile.methods.append(method)

            self.classfiles.append((classname, None, classfile))

        # Also output any subclasses.
        for klass, classfile in classes:
            self.classfiles.append((klass, classname, classfile))

    def transpile_method(self, block):
        name = block[-1].argval
        method = JavaMethod(
            name,
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

    def transpile_class(self, sourcefile, block):
        modulename = os.path.splitext(os.path.basename(sourcefile))[0]
        classname = block[-1].argval
        classfile = JavaClass('/'.join(self.namespace.split('.') + [modulename, classname]))
        classfile.attributes.append(SourceFile(os.path.basename(sourcefile)))

        # if static_block:
        #     # If we have static block content, then make sure the return content is included.
        #     if return_block:
        #         static_block.extend(return_block)

        #     static_init = JavaMethod('<clinit>', '()V', public=False, static=True)

        #     code = JavaCode(
        #             max_stack=2,
        #             max_locals=1,
        #             code=[
        #                 JavaOpcodes.GETSTATIC('java/lang/System', 'out', 'Ljava/io/PrintStream;'),
        #                 JavaOpcodes.LDC('Hello, Static World'),
        #                 JavaOpcodes.INVOKEVIRTUAL('java/io/PrintStream', 'println', '(Ljava/lang/String;)V'),
        #                 JavaOpcodes.RETURN(),
        #             ],
        #         )

        #     static_init.attributes.append(code)
        #     classfile.methods.append(static_init)

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
                            JavaOpcodes.INVOKESPECIAL('java/lang/Object', '<init>', '()V'),
                            JavaOpcodes.RETURN(),
                        ],
                    )
                ]
            )
        )

        # for method in static_methods:
        #     classfile.methods.append(method)

        return classname, classfile

    def _handle_LOAD_NAME(self, instruction, state):
        code = []
        if instruction.argval == 'print':
            code.append(JavaOpcodes.GETSTATIC('java/lang/System', 'out', 'Ljava/io/PrintStream;'))
        else:
            code.append(JavaOpcodes.GETSTATIC('java/lang/System', 'out', 'Ljava/io/PrintStream;'))
        return code

    def _handle_LOAD_CONST(self, instruction, state):
        code.append(JavaOpcodes.LDC('Hello, World'))
        return code

    def _handle_CALL_FUNCTION(self, instruction, state):
        print("**CALL FUNCTION**", [(instruction.opname, instruction.argval) for instruction in state['stack']])

    def _handle_RETURN_VALUE(self, instruction, state):
        print("**RETURN**", [(instruction.opname, instruction.argval) for instruction in state['stack']])
