import os

from ..java import (
    Annotation,
    Class as JavaClass,
    Classref as JavaClassref,
    Code as JavaCode,
    ConstantElementValue,
    Field as JavaField,
    Method as JavaMethod, RuntimeVisibleAnnotations,
    SourceFile,
    opcodes as JavaOpcodes,
)
from .blocks import Block, IgnoreBlock
from .methods import (
    InitMethod, ClosureInitMethod, GeneratorMethod, Method, CO_GENERATOR
)
from .types import java, python
from .types.primitives import (
    ALOAD_name, ASTORE_name, free_name,
)
# from .debug import DEBUG, DEBUG_value


class Class(Block):
    CONSTRUCTOR = InitMethod

    def __init__(
            self, parent, name,
            namespace=None, extends=None, implements=None,
            public=True, final=False, methods=None, fields=None, init=None,
            verbosity=0, include_default_constructor=True):
        super().__init__(parent=parent, verbosity=verbosity)
        self.name = name
        if namespace is None:
            self.namespace = '.'.join([self.module.namespace, self.module.name])
        else:
            self.namespace = namespace

        self._extends = extends

        self.implements = implements if implements else []
        self.public = public
        self.final = final
        self.methods = methods if methods else []
        self.fields = fields if fields else {}
        self.init = init

        self.include_default_constructor = include_default_constructor

        # Track constructors when they are added
        self.init_method = None

        # Mark this class as being a VOC generated class.
        self.fields["__VOC__"] = "Lorg/python/Object;"

        self._constructor = None

    @property
    def descriptor(self):
        return self._parent.build_child_class_descriptor(self.name)

    @property
    def class_name(self):
        return '.'.join([self._parent.class_name, self.name])

    @property
    def module(self):
        return self._parent.module

    def build_child_class_descriptor(self, child_name):
        return '$'.join([self.descriptor, child_name])

    def add_class(self, class_name, extends, implements):
        klass = Class(
            self,
            name=class_name,
            extends=extends,
            implements=implements,
        )

        self.module.classes.append(klass)

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

    def visitor_setup(self):
        self.add_opcodes(
            # DEBUG("DEFINITION BLOCK OF " + self.descriptor),
            # Force the loading and instantiation of the python module
            # that defines the class.
            # This may already be imported, but just in case
            JavaOpcodes.LDC_W(self.module.full_name),
            JavaOpcodes.ACONST_NULL(),
            JavaOpcodes.ACONST_NULL(),
            JavaOpcodes.ACONST_NULL(),
            JavaOpcodes.ICONST_0(),
            JavaOpcodes.INVOKESTATIC(
                'org/python/ImportLib',
                '__import__',
                args=[
                    'Ljava/lang/String;',
                    'Ljava/util/Map;',
                    'Ljava/util/Map;',
                    '[Ljava/lang/String;',
                    'I',
                ],
                returns='Lorg/python/types/Module;'
            ),
            JavaOpcodes.POP(),

            # Set the module name
            python.Str(self.module.full_name),
        )

        self.store_name('__module__')

        self.add_opcodes(
            python.Str(self.name),
        )
        self.store_name('__qualname__')

        # self.add_opcodes(
        #     DEBUG("DEFINITION BLOCK OF " + self.descriptor + " DONE"),
        # )

    def store_name(self, name, declare=False):
        self.add_opcodes(
            ASTORE_name('#value'),
            python.Type.for_class(self.descriptor),

            ALOAD_name('#value'),
            python.Object.set_attr(name),

            free_name('#value')
        )

    def store_dynamic(self):
        self.add_opcodes(
            ASTORE_name('#value'),
            python.Type.for_class(self.descriptor),

            JavaOpcodes.GETFIELD('org/python/types/Type', '__dict__', 'Ljava/util/Map;'),
            ALOAD_name('#value'),

            java.Map.putAll(),
            free_name('#value')
        )

    def load_name(self, name):
        self.add_opcodes(
            python.Type.for_class(self.descriptor),
            python.Object.get_attribute(name),
        )

    def load_globals(self):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('python/sys', 'modules', 'Lorg/python/types/Dict;'),

            python.Str(self.module.full_name),

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
            python.Type.for_name(self.descriptor),
            python.Object.del_attr(name),
        )

    @property
    def constructor(self):
        # Make sure there is a Java constructor
        if self._constructor is None:
            init = self.CONSTRUCTOR(self)
            init.visitor_setup()
            init.visitor_teardown()
            return init
        return self._constructor

    @constructor.setter
    def constructor(self, value):
        self._constructor = value

    def add_function(self, name, code, parameter_signatures, return_signature):
        if code.co_flags & CO_GENERATOR:
            method = GeneratorMethod(
                self,
                name=name,
                code=code,
                generator=code.co_name,
                parameters=parameter_signatures,
                returns=return_signature,
                static=True,
            )

        else:
            method = Method(
                self,
                name=name,
                code=code,
                parameters=parameter_signatures,
                returns=return_signature,
                static=True,
            )

        # Add the method to the list that need to be
        # transpiled into Java methods
        self.methods.append(method)

        # Add a definition of the callable object
        self.add_callable(method)

        if method.name == '__init__':
            self.init_method = method

        return method

    def visitor_teardown(self):
        self.add_opcodes(
            JavaOpcodes.RETURN()
        )

    @property
    def extends(self):
        if self._extends:
            return self._extends
        else:
            return 'org.python.types.Object'

    @property
    def extends_descriptor(self):
        return self.extends.replace('.', '/')

    def transpile(self):
        classfile = JavaClass(
            self.descriptor,
            extends=self.extends_descriptor,
            implements=self.implements,
            public=self.public,
            final=self.final
        )

        classfile.attributes.append(
            SourceFile(os.path.basename(self.module.sourcefile))
        )

        classfile.attributes.append(
            RuntimeVisibleAnnotations([
                Annotation(
                    'Lorg/python/Method;',
                    {
                        '__doc__': ConstantElementValue("Python Class (insert docs here)")
                    }
                )
            ])
        )

        try:
            # If we have block content, add a static block to the class
            static_init = JavaMethod('class$init', '()V', public=False, static=True)
            static_init.attributes.append(super().transpile())
            classfile.methods.append(static_init)
        except IgnoreBlock:
            pass

        # Add any manually defined fields
        classfile.fields.extend([
            JavaField(name, descriptor)
            for name, descriptor in self.fields.items()
        ])

        # Add any methods
        for method in self.methods:
            classfile.methods.extend(method.transpile())

        # Add the constructor
        classfile.methods.extend(self.constructor.transpile())

        # Ensure the class has a class protected, no-args init() so that
        # instances can be instantiated.
        if self.include_default_constructor:
            classfile.methods.append(
                JavaMethod(
                    '<init>',
                    '()V',
                    public=False,
                    static=False,
                    attributes=[
                        JavaCode(
                            max_stack=1,
                            max_locals=1,
                            code=[
                                JavaOpcodes.ALOAD_0(),
                                JavaOpcodes.INVOKESPECIAL(self.extends_descriptor, '<init>', args=[], returns='V'),
                                JavaOpcodes.RETURN(),
                            ]
                        )
                    ]
                )
            )

        return self.namespace, self.descriptor.split('/')[-1], classfile


class ClosureClass(Class):
    CONSTRUCTOR = ClosureInitMethod

    def __init__(self, parent, name, closure_var_names, verbosity=0):
        super().__init__(
            parent=parent,
            name=name,
            extends='org/python/types/Closure',
            implements=['org/python/Callable'],
            verbosity=verbosity,
            include_default_constructor=False,
        )
        self.closure_var_names = closure_var_names
