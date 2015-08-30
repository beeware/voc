import os

from ..java import (
    Class as JavaClass,
    Field as JavaField,
    Method as JavaMethod,
    Code as JavaCode,
    opcodes as JavaOpcodes,
    SourceFile,
    # LineNumberTable
)
from .block import Block, IgnoreBlock
from .method import MainMethod


class StaticBlock(Block):
    def tweak(self, code):
        # If the block is the module-level definition start the code by setting the
        # globals to be the locals for this class
        code = [
            JavaOpcodes.NEW('java/util/Hashtable'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('java/util/Hashtable', '<init>', '()V'),
            JavaOpcodes.PUTSTATIC(self.parent.descriptor, 'globals', 'Ljava/util/Hashtable;'),
        ] + code
        return self.void_return(code)

    @property
    def is_module(self):
        return True

    @property
    def descriptor(self):
        return self.parent.descriptor

    def add_method(self, method):
        self.parent.methods.append(method)


class Module(Block):
    def __init__(self, namespace, sourcefile):
        super().__init__()
        self.namespace = namespace
        self.sourcefile = sourcefile
        self.name = os.path.splitext(os.path.basename(sourcefile))[0]

        self.methods = []
        self.classes = []

    @property
    def is_module(self):
        return True

    @property
    def descriptor(self):
        return '/'.join(self.namespace.split('.') + [self.name])

    def transpile(self):
        """Convert a Python code block into a list of Java Classfile definitions.

        Returns a list of triples:
            (namespace, classname, javaclassfile)

        The list contains the classfile for the module, plus and classes
        defined in the module.
        """
        main_commands = []
        body_commands = []
        main_end = None

        main = None

        for cmd in self.commands:
            if main_end is not None:
                # Marker for the end of the main block:
                #   JUMP_FORWARD <main_end>
                if len(cmd.arguments) == 0 and cmd.operation.opname == 'JUMP_FORWARD' and cmd.operation.delta == main_end:
                    main_end = None

                    try:
                        main = MainMethod(self, main_commands).transpile()
                    except IgnoreBlock:
                        pass
                else:
                    main_commands.append(cmd)
            else:
                # Look for a very specific pattern, flagging the "main" method:
                #   if __name__ == '__main__':
                #       ...
                # which is represented as:
                #         LOAD_NAME: __name__
                #         LOAD_CONST: __main__
                #     COMPARE_OP: ==
                #  POP_JUMP_IF_FALSE: <end of block>
                #  ... <main code>
                #  JUMP_FORWARD <end of block>
                if (cmd.operation.opname == 'POP_JUMP_IF_FALSE'
                        and cmd.arguments[0].operation.opname == 'COMPARE_OP' and cmd.arguments[0].operation.comparison == '=='
                        and cmd.arguments[0].arguments[0].operation.opname == 'LOAD_NAME' and cmd.arguments[0].arguments[0].operation.name == '__name__'
                        and cmd.arguments[0].arguments[1].operation.opname == 'LOAD_CONST' and cmd.arguments[0].arguments[1].operation.const == '__main__'):
                    # print("Found main block")
                    if main is not None:
                        print("Found duplicate main block... replacing previous main")

                    main_end = cmd.operation.target

                # All other module-level cmds goes into the static block
                else:
                    body_commands.append(cmd)

        body = StaticBlock(self, body_commands).transpile()

        # If there is any static content, generate a classfile
        # for this module
        classfile = JavaClass(self.descriptor, supername='org/python/PyObject')
        classfile.attributes.append(SourceFile(os.path.basename(self.sourcefile)))

        # Add a globals dictionary to the module.
        classfile.fields.append(
            JavaField('globals', 'Ljava/util/Hashtable;', public=True, static=True)
        )

        # Add a static method to the module.
        static_init = JavaMethod('<clinit>', '()V', public=False, static=True)
        static_init.attributes.append(body)
        classfile.methods.append(static_init)

        if main is None:
            print("Adding default main method...")
            main = JavaMethod(
                'main',
                '([Ljava/lang/String;)V',
                public=True,
                static=True,
                attributes=[
                    JavaCode(
                        max_stack=0,
                        max_locals=1,
                        code=[JavaOpcodes.RETURN()]
                    )
                ]
            )

        classfile.methods.append(main)

        # Add any static methods defined in the module
        for method in self.methods:
            classfile.methods.append(method)

        # The list of classfiles that will be returned will contain
        # at least one entry - the class for the module itself.
        classfiles = [(self.namespace, self.name, classfile)]

        # Also output any classes defined in this module.
        for classname, classfile in self.classes:
            classfiles.append(('%s.%s' % (self.namespace, self.name), classname, classfile))

        return classfiles
