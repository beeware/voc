import os

from ..java import (
    Annotation, Class as JavaClass, Code as JavaCode, ConstantElementValue,
    Field as JavaField, Method as JavaMethod, RuntimeVisibleAnnotations,
    SourceFile, opcodes as JavaOpcodes,
)
from .blocks import Block, IgnoreBlock
from .methods import (
    CO_GENERATOR, InitMethod, ClosureInitMethod, Function, Method
)
from .utils import (
    ALOAD_name, ASTORE_name, free_name
)


class Class(Block):
    def __init__(self, module, name, namespace=None, bases=None, extends=None, implements=None, public=True, final=False, methods=None, fields=None, init=None, verbosity=0, include_default_constructor=True):
        super().__init__(parent=module, verbosity=verbosity)
        self.name = name
        if namespace is None:
            self.namespace = '%s.%s' % (module.namespace, module.name)
        else:
            self.namespace = namespace

        self.bases = bases if bases else []
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

        self.methods.append(self.constructor())

    @property
    def descriptor(self):
        return '/'.join([self.namespace.replace('.', '/'), self.name])

    @property
    def class_name(self):
        return '.'.join(self.namespace.split('.') + [self.name])

    @property
    def module(self):
        return self._parent

    def visitor_setup(self):
        self.add_opcodes(
            # JavaOpcodes.LDC_W("STATIC BLOCK OF " + self.klass.descriptor),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

            # Force the loading and instantiation of the module
            # that contains the class.
            JavaOpcodes.LDC_W(self.module.full_name),
            JavaOpcodes.ACONST_NULL(),
            JavaOpcodes.ICONST_0(),
            JavaOpcodes.INVOKESTATIC('org/python/ImportLib', '__import__', '(Ljava/lang/String;[Ljava/lang/String;I)Lorg/python/types/Module;'),
            JavaOpcodes.POP(),

            # Set __base__ on the type
            JavaOpcodes.LDC_W(self.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),

            JavaOpcodes.LDC_W(self.extends_descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),

            # JavaOpcodes.DUP(),
            # JavaOpcodes.LDC_W("__base__ for %s should be %s; is" % (self.klass, self.extends_descriptor)),
            # JavaOpcodes.SWAP(),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;Ljava/lang/Object;)V'),

            JavaOpcodes.PUTFIELD('org/python/types/Type', '__base__', 'Lorg/python/types/Type;'),

            # Set __bases__ on the type
            JavaOpcodes.LDC_W(self.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),

            JavaOpcodes.NEW('org/python/types/Tuple'),
            JavaOpcodes.DUP(),

            JavaOpcodes.NEW('java/util/ArrayList'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('java/util/ArrayList', '<init>', '()V'),
        )

        if self.extends:
            self.add_opcodes(
                JavaOpcodes.DUP(),

                JavaOpcodes.NEW('org/python/types/Str'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W(self.extends.replace('.', '/')),
                JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),

                JavaOpcodes.INVOKEVIRTUAL('java/util/ArrayList', 'add', '(Ljava/lang/Object;)Z'),
                JavaOpcodes.POP()
            )

        for base in self.bases:
            base_namespace = self.namespace.replace('.', '/') + '/'
            self.add_opcodes(
                JavaOpcodes.DUP(),

                JavaOpcodes.NEW('org/python/types/Str'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W(base if base.startswith('org/python/') else base_namespace + base),
                JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),

                JavaOpcodes.INVOKEVIRTUAL('java/util/ArrayList', 'add', '(Ljava/lang/Object;)Z'),
                JavaOpcodes.POP()
            )

        self.add_opcodes(
            JavaOpcodes.INVOKESPECIAL('org/python/types/Tuple', '<init>', '(Ljava/util/List;)V'),

            JavaOpcodes.PUTFIELD('org/python/types/Type', '__bases__', 'Lorg/python/types/Tuple;'),

            # Load the globals module
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

            JavaOpcodes.NEW('org/python/types/Str'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(self.module.full_name),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),

            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getitem__', '(Lorg/python/Object;)Lorg/python/Object;'),
        )

        self.store_name('__module__')

        self.add_opcodes(
            JavaOpcodes.NEW('org/python/types/Str'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(self.name),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V')
        )
        self.store_name('__qualname__')

        # self.add_opcodes(
        #     JavaOpcodes.LDC_W("STATIC BLOCK OF " + self.klass.descriptor + " DONE"),
        #     JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),
        # )

    def store_name(self, name):
        self.add_opcodes(
            ASTORE_name(self, '#value'),
            JavaOpcodes.LDC_W(self.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),

            JavaOpcodes.LDC_W(name),
            ALOAD_name(self, '#value'),

            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__setattr__', '(Ljava/lang/String;Lorg/python/Object;)V'),
        )
        free_name(self, '#value')

    def store_dynamic(self):
        self.add_opcodes(
            ASTORE_name(self, '#value'),
            JavaOpcodes.LDC_W(self.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),

            JavaOpcodes.GETFIELD('org/python/types/Type', '__dict__', 'Ljava/util/Map;'),
            ALOAD_name(self, '#value'),

            JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'putAll', '(Ljava/util/Map;)V'),
        )
        free_name(self, '#value')

    def store_global(self):
        self.add_opcodes(
            ASTORE_name(self, '#varname'),
            ASTORE_name(self, '#value'),

            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

            JavaOpcodes.NEW('org/python/types/Str'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(self.module.full_name),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),

            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getitem__', '(Lorg/python/Object;)Lorg/python/Object;'),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            ALOAD_name(self, '#varname'),
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', 'toJava', '()Ljava/lang/Object;'),
            JavaOpcodes.CHECKCAST('java/lang/String'),

            ALOAD_name(self, '#value'),

            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__setattr__', '(Ljava/lang/String;Lorg/python/Object;)V'),
        )
        free_name(self, '#value')

    def store_local(self):
        self.add_opcodes(
            ASTORE_name(self),
        )

    def load_name(self, name):
        self.add_opcodes(
            JavaOpcodes.LDC_W(self.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKEVIRTUAL('org/python/types/Type', '__getattribute__', '(Ljava/lang/String;)Lorg/python/Object;'),
        )

    def load_globals(self):
        self.add_opcodes(
            JavaOpcodes.DUP(),
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

            JavaOpcodes.NEW('org/python/types/Str'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(self.full_name),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),

            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getitem__', '(Lorg/python/Object;)Lorg/python/Object;'),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            JavaOpcodes.GETFIELD('org/python/types/Module', '__dict__', 'Ljava/util/Map;'),

            JavaOpcodes.INVOKEVIRTUAL('org/python/types/Dict', 'addMap', '(Ljava/util/Map;)V'),
        )

    def load_locals(self):
        self.load_globals()

    def delete_name(self, name):
        self.add_opcodes(
            JavaOpcodes.LDC_W(self.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKEVIRTUAL('org/python/types/Type', '__delattr__', '(Ljava/lang/String;)V'),
        )

    def constructor(self):
        # Make sure there is a Java constructor
        return InitMethod(self)

    def add_function(self, name, code, parameter_signatures, return_signature):
        if False:  # FIXME code.co_flags & CO_GENERATOR:
            raise Exception("Can't handle Generator instance methods (yet)")
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
            if 'Exception' in self.bases:
                return 'org.python.exceptions.Exception'
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
            static_init = JavaMethod('<clinit>', '()V', public=False, static=True)
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
                                JavaOpcodes.INVOKESPECIAL(self.extends_descriptor, '<init>', '()V'),
                                JavaOpcodes.RETURN(),
                            ]
                        )
                    ]
                )
            )

        return self.namespace, self.name, classfile


class ClosureClass(Class):
    def __init__(self, module, name, closure_var_names, verbosity=0):
        super().__init__(
            module=module,
            name=name,
            extends='org/python/types/Closure',
            implements=['org/python/Callable'],
            verbosity=verbosity,
            include_default_constructor=False,
        )
        self.closure_var_names = closure_var_names

    def constructor(self):
        # Make sure there is a default constructor
        return ClosureInitMethod(self)
