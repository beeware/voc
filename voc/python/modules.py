import os

from ..java import (
    Class as JavaClass, Code as JavaCode, Method as JavaMethod, SourceFile,
    opcodes as JavaOpcodes
)
from .blocks import Block
from .methods import (
    CO_GENERATOR, GeneratorFunction, Function,
)
from .types import java, python
from .types.primitives import (
    ALOAD_name, ASTORE_name, free_name,
)
# from .debug import DEBUG


class Module(Block):
    def __init__(self, namespace, sourcefile, verbosity=0):
        super().__init__(verbosity=verbosity)
        self.sourcefile = sourcefile

        parts = os.path.splitext(sourcefile)[0].split(os.path.sep)
        if parts[-1] == '__init__':
            parts.pop()

        # If the sourcefile started with a /, the first part will
        # be an empty string; replace that with the namespace.
        # Otherwise, prepend the namespace to the parts.
        if parts[0] == '':
            parts[0] = namespace
        else:
            parts = [namespace] + parts
        self.namespace = '.'.join(parts[:-1])
        self.name = parts[-1]

        self.functions = []
        self.classes = []
        self.anonymous_inner_class_count = 0

        # Preallocate space for self when
        # the module static block is invoked
        self.parameters = [None]
        self.local_vars['self'] = 0

    @property
    def module(self):
        return self

    @property
    def full_name(self):
        return '.'.join(self.namespace.split('.')[1:] + [self.name])

    @property
    def descriptor(self):
        return '/'.join(self.namespace.split('.') + [self.name])

    @property
    def class_name(self):
        return '.'.join(self.namespace.split('.') + [self.name, '__init__'])

    @property
    def class_descriptor(self):
        return '/'.join(self.namespace.split('.') + [self.name, '__init__'])

    # def visitor_setup(self):
    #     self.add_opcodes(
    #         DEBUG("STATIC BLOCK OF " + self.class_name),
    #     )

    def store_name(self, name):
        self.add_opcodes(
            ASTORE_name('#value'),
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),
            python.Str(self.full_name),
            python.Object.get_item(),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            ALOAD_name('#value'),
            python.Object.set_attr(name),

            free_name('#value')
        )

    def store_dynamic(self):
        self.add_opcodes(
            ASTORE_name('#value'),
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),
            python.Str(self.full_name),
            python.Object.get_item(),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            JavaOpcodes.GETFIELD('org/python/types/Module', '__dict__', 'Ljava/util/Map;'),

            ALOAD_name('#value'),
            java.Map.putAll(),

            free_name('#value')
        )

    def store_local(self):
        self.store_global()

    def load_name(self, name):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),
            python.Str(self.full_name),
            python.Object.get_item(),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            python.Object.get_attribute(name),
        )

    def load_globals(self):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),
            python.Str(self.full_name),
            python.Object.get_item(),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            JavaOpcodes.GETFIELD('org/python/types/Module', '__dict__', 'Ljava/util/Map;'),
        )

    def load_locals(self):
        self.load_globals()

    def load_vars(self):
        self.load_globals()

    def delete_name(self, name):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),
            python.Str(self.full_name),
            python.Object.get_item(),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            python.Object.del_attr(name),
        )

    def add_function(self, name, code, parameter_signatures, return_signature):
        if code.co_flags & CO_GENERATOR:
            # Generator method.
            function = GeneratorFunction(
                self,
                name=name,
                code=code,
                generator=code.co_name,
                parameters=parameter_signatures,
                returns=return_signature,
                static=True
            )
        else:
            # Normal function.
            function = Function(
                self,
                name=name,
                code=code,
                parameters=parameter_signatures,
                returns=return_signature,
                static=True,
            )

        # Add the function to the list that need to be
        # transpiled into Java functions
        self.functions.append(function)

        # Add a definition of the callable object
        self.add_callable(function)

        return function

    def add_class(self, class_name, bases, extends, implements):
        from .klass import Class

        klass = Class(
            self,
            name=class_name,
            bases=[
                'org/python/Object' if b == 'object' else b
                for b in bases
            ],
            extends=extends,
            implements=implements,
        )

        self.classes.append(klass)

        self.add_opcodes(
            # DEBUG("FORCE LOAD OF CLASS %s AT DEFINITION" % self.klass.descriptor),

            java.Class.forName(klass.descriptor.replace('/', '.')),
            python.Type.for_class(),
        )

        self.store_name(klass.name)

        return klass

    def visitor_teardown(self):
        self.add_opcodes(
            JavaOpcodes.RETURN(),
        )

    def transpile(self):
        """Convert a materialized Python code definition into a list of Java
        Classfile definitions.

        Returns a list of triples:
            (namespace, class_name, javaclassfile)

        The list contains the classfile for the module, plus and classes
        defined in the module.
        """
        # If there is any static content, generate a classfile
        # for this module
        classfile = JavaClass(self.class_descriptor, extends='org/python/types/Module')
        classfile.attributes.append(SourceFile(os.path.basename(self.sourcefile)))

        # Add a static method to the module, populated with the
        # body content of the module.
        static_init = JavaMethod('module$import', '()V', public=False)
        static_init.attributes.append(self.transpile_code())
        classfile.methods.append(static_init)

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
                            JavaOpcodes.INVOKESPECIAL('org/python/types/Module', '<init>', args=[], returns='V'),
                            JavaOpcodes.RETURN(),
                        ],
                    ),
                ]
            ),
        )

        # Add a __new__ method to set the filename of the module.
        classfile.methods.append(
            JavaMethod(
                '__new__',
                '(Lorg/python/Object;)Lorg/python/Object;',
                attributes=[
                    JavaCode(
                        max_stack=6,
                        max_locals=2,
                        code=[
                            JavaOpcodes.ALOAD_0(),
                            JavaOpcodes.ALOAD_1(),
                            JavaOpcodes.INVOKESPECIAL(
                                'org/python/types/Module',
                                '__new__',
                                args=['Lorg/python/Object;'],
                                returns='Lorg/python/Object;'
                            ),

                            JavaOpcodes.ALOAD_0(),
                            JavaOpcodes.GETFIELD('org/python/types/Object', '__dict__', 'Ljava/util/Map;'),

                            JavaOpcodes.LDC_W('__file__'),

                            JavaOpcodes.NEW('org/python/types/Str'),
                            JavaOpcodes.DUP(),
                            JavaOpcodes.LDC_W(self.sourcefile),
                            JavaOpcodes.INVOKESPECIAL(
                                'org/python/types/Str',
                                '<init>',
                                args=['Ljava/lang/String;'],
                                returns='V'
                            ),

                            JavaOpcodes.INVOKEINTERFACE(
                                'java/util/Map',
                                'put',
                                args=[
                                    'Ljava/lang/Object;'
                                    'Ljava/lang/Object;'
                                ],
                                returns='Ljava/lang/Object;'
                            ),
                            JavaOpcodes.POP(),

                            JavaOpcodes.ARETURN(),
                        ],
                    ),
                ]
            )
        )

        # Add any static methods defined in the module
        for function in self.functions:
            classfile.methods.extend(function.transpile())

        # The list of classfiles that will be returned will contain
        # at least one entry - the class for the module itself.
        classfiles = [(
            self.namespace,
            '%s/__init__' % self.name,
            classfile
        )]
        # Also output any classes defined in this module.
        for klass in self.classes:
            classfiles.append(klass.transpile())

        return classfiles
