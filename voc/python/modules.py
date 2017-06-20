import os
import sys

from ..java import (
    Class as JavaClass,
    Classref as JavaClassref,
    Code as JavaCode,
    Method as JavaMethod,
    SourceFile as JavaSourceFile,
    opcodes as JavaOpcodes
)
from .blocks import Block, Accumulator
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
            self.has_init_file = True
        else:
            self.has_init_file = False

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
        return '.'.join(self.namespace.split('.') + ([self.name, '__init__'] if self.has_init_file else [self.name]))

    @property
    def class_descriptor(self):
        return '/'.join(self.namespace.split('.') + ([self.name, '__init__'] if self.has_init_file else [self.name]))

    def build_child_class_descriptor(self, child_name):
        return '/'.join([self.descriptor, child_name])

    def store_name(self, name, declare=False):
        self.add_opcodes(
            ASTORE_name('#value'),

            JavaOpcodes.GETSTATIC('python/sys', 'modules', 'Lorg/python/types/Dict;'),
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
            JavaOpcodes.GETSTATIC('python/sys', 'modules', 'Lorg/python/types/Dict;'),
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
            JavaOpcodes.GETSTATIC('python/sys', 'modules', 'Lorg/python/types/Dict;'),
            python.Str(self.full_name),
            python.Object.get_item(),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            python.Object.get_attribute(name),
        )

    def load_globals(self):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('python/sys', 'modules', 'Lorg/python/types/Dict;'),
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
            JavaOpcodes.GETSTATIC('python/sys', 'modules', 'Lorg/python/types/Dict;'),
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

    def add_class(self, class_name, extends, implements):
        from .klass import Class

        klass = Class(
            self,
            name=class_name,
            extends=extends,
            implements=implements,
        )

        self.classes.append(klass)

        self.add_opcodes(
            # Stack contains the bases list
            ASTORE_name('#bases'),

            # DEBUG("FORCE LOAD OF CLASS %s AT DEFINITION" % klass.descriptor),
            # - class
            JavaOpcodes.LDC_W(JavaClassref(klass.descriptor)),

            # - name
            JavaOpcodes.LDC_W(klass.name),

            # - bases
            ALOAD_name('#bases'),

            # - dict
            JavaOpcodes.ACONST_NULL(),

            JavaOpcodes.INVOKESTATIC(
                'org/python/types/Type',
                'declarePythonType',
                args=[
                    'Ljava/lang/Class;',
                    'Ljava/lang/String;',
                    'Ljava/util/List;',
                    'Ljava/util/Map;'
                ],
                returns='Lorg/python/types/Type;'
            ),

            free_name('#bases')
        )

        self.store_name(klass.name)

        self.add_opcodes(
            JavaOpcodes.INVOKESTATIC(
                klass.descriptor,
                'class$init',
                args=[],
                returns='V'
            ),
        )

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
        classfile.attributes.append(JavaSourceFile(os.path.basename(self.sourcefile)))

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
        new_method = Accumulator({'self': 0, 'klass': 1})

        new_method.add_opcodes(
            # Call super.__new__()
            ALOAD_name('self'),
            ALOAD_name('klass'),
            JavaOpcodes.INVOKESPECIAL(
                'org/python/types/Module',
                '__new__',
                args=['Lorg/python/Object;'],
                returns='Lorg/python/Object;'
            ),

            ALOAD_name('self'),
            JavaOpcodes.GETFIELD(
                'org/python/types/Object',
                '__dict__',
                'Ljava/util/Map;'
            ),

            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W("__file__"),
            python.Str(self.sourcefile),
            java.Map.put(),

            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W("__package__"),
            python.Str(self.name),
            java.Map.put(),

            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W("__name__"),
            python.Str(self.full_name),
            java.Map.put(),

            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W("__builtins__"),
            python.NONE(),
            java.Map.put(),

            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W("__cached__"),
            python.NONE(),
            java.Map.put(),

            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W("__doc__"),
            python.NONE(),
            java.Map.put(),

            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W("__loader__"),
            python.Str(),
            java.Map.put(),
        )

        # Python 3.6 introduced __annotations__ at the module level.
        if sys.hexversion > 0x03060000:
            new_method.add_opcodes(
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W("__annotations__"),
                python.Dict(),
                java.Map.put(),
            )

        new_method.add_opcodes(
            # last entry doesn't need to be duped, because we don't need to
            # reuse the value on the stack.
            JavaOpcodes.LDC_W("__spec__"),
            python.Str(),
            java.Map.put(),

            JavaOpcodes.ARETURN()
        )

        classfile.methods.append(
            JavaMethod(
                '__new__',
                '(Lorg/python/Object;)Lorg/python/Object;',
                attributes=[
                    JavaCode(
                        max_stack=new_method.max_stack(),
                        max_locals=new_method.max_locals(),
                        code=new_method.opcodes,
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
            self.name + ('/__init__' if self.has_init_file else ''),
            classfile
        )]
        # Also output any classes defined in this module.
        for klass in self.classes:
            classfiles.append(klass.transpile())

        return classfiles
