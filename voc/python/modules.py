import os

from ..java import (
    Class as JavaClass,
    Code as JavaCode,
    Method as JavaMethod,
    opcodes as JavaOpcodes,
    SourceFile,
)
from .blocks import Block, IgnoreBlock
from .methods import MainMethod, Method, extract_parameters
from .opcodes import ASTORE_name, ALOAD_name, free_name, TRY, CATCH, END_TRY


class StaticBlock(Block):

    @property
    def has_void_return(self):
        return True

    def transpile_setup(self):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('org/python/ImportLib', 'modules', 'Ljava/util/Map;'),
            JavaOpcodes.LDC_W(self.module.descriptor),

            JavaOpcodes.NEW('org/python/types/Module'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(self.module.descriptor.replace('/', '.')),
            JavaOpcodes.INVOKESTATIC('java/lang/Class', 'forName', '(Ljava/lang/String;)Ljava/lang/Class;'),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Module', '<init>', '(Ljava/lang/Class;)V'),

            JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
            JavaOpcodes.POP()
        )
        # If there are any commands in this main method,
        # add a TRY-CATCH for SystemExit
        if self.commands:
            self.add_opcodes(
                TRY()
            )

    def transpile_teardown(self):
        # If there are any commands in this main method,
        # finish the TRY-CATCH for SystemExit
        if self.commands:
            self.add_opcodes(
                CATCH('org/python/exceptions/SystemExit'),
                    JavaOpcodes.GETFIELD('org/python/exceptions/SystemExit', 'return_code', 'I'),
                    JavaOpcodes.INVOKESTATIC('java/lang/System', 'exit', '(I)V'),
                END_TRY()
            )

    @property
    def use_registers(self):
        return False

    def store_name(self, name, use_locals):
        self.add_opcodes(
            ASTORE_name(self, '#value'),
            JavaOpcodes.LDC_W(self.module.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/ImportLib', 'getModule', '(Ljava/lang/String;)Lorg/python/types/Module;'),

            JavaOpcodes.LDC_W(name),
            ALOAD_name(self, '#value'),

            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__setattr__', '(Ljava/lang/String;Lorg/python/Object;)V'),
        )
        free_name(self, '#value')

    def store_dynamic(self):
        self.add_opcodes(
            ASTORE_name(self, '#value'),
            JavaOpcodes.LDC_W(self.module.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),

            JavaOpcodes.GETFIELD('org/python/types/Type', 'attrs', 'Ljava/util/Map;'),

            ALOAD_name(self, '#value'),
            JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'putAll', '(Ljava/util/Map;)V'),
        )
        free_name(self, '#value')

    def load_name(self, name, use_locals):
        self.add_opcodes(
            JavaOpcodes.LDC_W(self.module.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/ImportLib', 'getModule', '(Ljava/lang/String;)Lorg/python/types/Module;'),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getattribute__', '(Ljava/lang/String;)Lorg/python/Object;'),
            # JavaOpcodes.INVOKEVIRTUAL('org/python/types/Module', '__getattribute__', '(Ljava/lang/String;)Lorg/python/Object;'),
        )

    def delete_name(self, name, use_locals):
        self.add_opcodes(
            JavaOpcodes.LDC_W(self.module.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/ImportLib', 'getModule', '(Ljava/lang/String;)Lorg/python/types/Module;'),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKEVIRTUAL('org/python/types/Module', '__delattr__', '(Ljava/lang/String;)Lorg/python/Object;'),
        )

    @property
    def descriptor(self):
        return self.parent.descriptor

    @property
    def module(self):
        return self.parent

    def add_method(self, method_name, code):
        method = Method(self.module, method_name, extract_parameters(code), static=True, code=code)
        method.extract(code)
        self.module.methods.append(method)
        return method


class Module(Block):
    def __init__(self, namespace, sourcefile):
        super().__init__()
        self.namespace = namespace
        self.sourcefile = sourcefile
        self.name = os.path.splitext(os.path.basename(sourcefile))[0]

        self.methods = []
        self.classes = []
        self.anonymous_inner_class_count = 0

    @property
    def descriptor(self):
        return '/'.join(self.namespace.split('.') + [self.name])

    def transpile(self):
        """Convert a Python code block into a list of Java Classfile definitions.

        Returns a list of triples:
            (namespace, class_name, javaclassfile)

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
                if cmd.is_main_end(main_end):
                    try:
                        main = MainMethod(self, main_commands, end_offset=main_end)
                    except IgnoreBlock:
                        pass
                    main_end = None
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
                #  POP_JUMP_IF_FALSE: <end of block target>
                #  ... <main code>
                #  <end of block target>
                if cmd.is_main_start():
                    if main is not None:
                        print("Found duplicate main block... replacing previous main")

                    main_end = cmd.operation.target

                # All other module-level cmds goes into the static block
                else:
                    body_commands.append(cmd)

        body = StaticBlock(self, body_commands).transpile()

        # If there is any static content, generate a classfile
        # for this module
        classfile = JavaClass(self.descriptor, supername='org/python/types/Module')
        classfile.attributes.append(SourceFile(os.path.basename(self.sourcefile)))

        # Add a static method to the module.
        static_init = JavaMethod('<clinit>', '()V', public=False, static=True)
        static_init.attributes.append(body)
        classfile.methods.append(static_init)

        if main is None:
            print("Adding default main method...")
            main = MainMethod(self, [])

        classfile.methods.append(main.transpile())

        # Add a dummy init method.
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
                            JavaOpcodes.INVOKESPECIAL('org/python/types/Module', '<init>', '()V'),
                            JavaOpcodes.RETURN(),
                        ],
                    ),
                ]
            )
        )

        # Add any static methods defined in the module
        for method in self.methods:
            classfile.methods.append(method.transpile())

        # The list of classfiles that will be returned will contain
        # at least one entry - the class for the module itself.
        classfiles = [(self.namespace, self.name, classfile)]
        # Also output any classes defined in this module.
        for klass in self.classes:
            classfiles.append(klass.transpile())

        return classfiles
