import os

from ..java import (
    Class as JavaClass,
    Field as JavaField,
    Method as JavaMethod,
    Code as JavaCode,
    opcodes as JavaOpcodes,
    SourceFile,
    RuntimeVisibleAnnotations,
    Annotation,
    ConstantElementValue,
)

from .blocks import Block, IgnoreBlock
from .methods import InitMethod, InstanceMethod, extract_parameters
from .opcodes import ASTORE_name, ALOAD_name, free_name


class ClassBlock(Block):
    @property
    def descriptor(self):
        return self.parent.descriptor

    @property
    def klass(self):
        return self.parent

    @property
    def module(self):
        return self.klass.module

    def store_name(self, name, use_locals):
        self.add_opcodes(
            ASTORE_name(self, '#value'),
            JavaOpcodes.LDC_W(self.klass.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),

            JavaOpcodes.LDC_W(name),
            ALOAD_name(self, '#value'),

            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__setattr__', '(Ljava/lang/String;Lorg/python/Object;)V'),
        )
        free_name(self, '#value')

    def store_dynamic(self):
        self.add_opcodes(
            ASTORE_name(self, '#value'),
            JavaOpcodes.LDC_W(self.klass.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),

            JavaOpcodes.GETFIELD('org/python/types/Type', 'attrs', 'Ljava/util/Map;'),
            ALOAD_name(self, '#value'),

            JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'putAll', '(Ljava/util/Map;)V'),
        )
        free_name(self, '#value')

    def load_name(self, name, use_locals):
        self.add_opcodes(
            JavaOpcodes.LDC_W(self.klass.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKEVIRTUAL('org/python/types/Type', '__getattribute__', '(Ljava/lang/String;)Lorg/python/Object;'),
        )

    def delete_name(self, name, use_locals):
        self.add_opcodes(
            JavaOpcodes.LDC_W(self.klass.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKEVIRTUAL('org/python/types/Type', '__delattr__', '(Ljava/lang/String;)Lorg/python/Object;'),
        )

    def add_method(self, full_method_name, code, annotations):
        parts = full_method_name.split('.')
        method_name = parts[-1]
        class_name = parts[-2]

        if class_name != self.klass.name:
            raise Exception("Method %s being added to %s!" % (full_method_name, self.klass.name))

        parameters = extract_parameters(code, annotations)

        method = InstanceMethod(
            self.klass,
            name=method_name,
            parameters=parameters,
            returns={
                'annotation': annotations.get('return', 'org.python.Object').replace('.', '/')
            },
            static=True,
            verbosity=self.klass.verbosity
        )
        method.extract(code)
        self.klass.add_method(method)

        return method

    def transpile_setup(self):
        base_namespace = self.parent.namespace.replace('.', '/') + '/'

        if self.klass.extends:
            base_descriptor = self.klass.extends.replace('.', '/')
        else:
            base_descriptor = self.klass.bases[0] if self.klass.bases[0].startswith('org/python/') else base_namespace + self.klass.bases[0]

        self.add_opcodes(
            # JavaOpcodes.LDC_W("STATIC BLOCK OF " + self.klass.descriptor),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

            # JavaOpcodes.LDC_W("FORCE LOAD OF " + self.module.class_name),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

            # Force the loading and instantiation of the module
            # that contains the class.
            JavaOpcodes.LDC_W(self.module.class_name),
            JavaOpcodes.INVOKESTATIC('java/lang/Class', 'forName', '(Ljava/lang/String;)Ljava/lang/Class;'),
            JavaOpcodes.POP(),

            # Set __base__ on the type
            JavaOpcodes.LDC_W(self.klass.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),

            JavaOpcodes.LDC_W(base_descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),

            # JavaOpcodes.DUP(),
            # JavaOpcodes.LDC_W("__base__ for %s should be %s; is" % (self.klass, base_descriptor)),
            # JavaOpcodes.SWAP(),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;Ljava/lang/Object;)V'),

            JavaOpcodes.PUTFIELD('org/python/types/Type', '__base__', 'Lorg/python/types/Type;'),

            # Set __bases__ on the type
            JavaOpcodes.LDC_W(self.klass.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),

            JavaOpcodes.NEW('org/python/types/Tuple'),
            JavaOpcodes.DUP(),

            JavaOpcodes.NEW('java/util/ArrayList'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('java/util/ArrayList', '<init>', '()V'),
        )

        if self.klass.extends:
            self.add_opcodes(
                JavaOpcodes.DUP(),

                JavaOpcodes.NEW('org/python/types/Str'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W(self.klass.extends.replace('.', '/')),
                JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),

                JavaOpcodes.INVOKEVIRTUAL('java/util/ArrayList', 'add', '(Ljava/lang/Object;)Z'),
                JavaOpcodes.POP()
            )

        for base in self.klass.bases:
            base_namespace = self.parent.namespace.replace('.', '/') + '/'
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

            # JavaOpcodes.LDC_W("STATIC BLOCK OF " + self.klass.descriptor + " DONE"),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),
        )

    def transpile_teardown(self):
        self.add_opcodes(
            JavaOpcodes.RETURN()
        )


class Class(Block):
    def __init__(self, module, name, namespace=None, bases=None, extends=None, implements=None, public=True, final=False, methods=None, fields=None, init=None, verbosity=0):
        super().__init__(module, verbosity=verbosity)
        self.name = name
        self.bases = bases if bases else ['org/python/types/Object']
        self.extends = extends
        self.implements = implements if implements else []
        self.public = public
        self.final = final
        self.methods = methods if methods else []
        self.fields = fields if fields else {}
        self.init = init
        if namespace is None:
            self.namespace = '%s.%s' % (self.parent.namespace, self.parent.name)
        else:
            self.namespace = namespace
        self.anonymous_inner_class_count = 0

        # Track constructors when they are added
        self.init_method = None

        # Make sure there is a default constructor
        self.add_method(InitMethod(self))

    @property
    def descriptor(self):
        return '/'.join([self.namespace.replace('.', '/'), self.name])

    @property
    def class_name(self):
        return '.'.join(self.namespace.split('.') + [self.name])

    @property
    def class_descriptor(self):
        return '/'.join(self.namespace.split('.') + [self.name])

    @property
    def module(self):
        return self.parent

    def add_method(self, method):
        self.methods.append(method)
        if method.name == '__init__':
            self.init_method = method

    def materialize(self):
        # Create the body of the class
        self.body = ClassBlock(self, self.commands)

        # Materialize the body of the class
        self.body.materialize()

        # Materialize any methods in the class
        for method in self.methods:
            method.materialize()

        # Add a field to indicate this was a VOC generated class.
        # The value of this field is the VOC wrapper instance in the
        # case of an extension type; it will be self in most other
        # cases.
        self.fields["__VOC__"] = "Lorg/python/Object;"

    def transpile(self):
        classfile = JavaClass(
            self.descriptor,
            extends=self.extends if self.extends else 'org/python/types/Object',
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
            static_init.attributes.append(self.body.transpile())
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

        if self.extends:
            classfile.methods.append(
                JavaMethod(
                    '<init>',
                    '()V',
                    static=False,
                    attributes=[
                        JavaCode(
                            max_stack=1,
                            max_locals=1,
                            code=[
                                JavaOpcodes.ALOAD_0(),
                                JavaOpcodes.INVOKESPECIAL(self.extends, '<init>', '()V'),
                                JavaOpcodes.RETURN(),
                            ]
                        )
                    ]
                )
            )

        return self.namespace, self.name, classfile


class InnerClass(Class):
    def __init__(self, parent, name, bases=None, extends=None, implements=None, public=True, final=False, methods=None, init=None):
        if isinstance(parent, Class):
            module = parent.module
        else:
            module = parent
        super().__init__(
            module=module,
            name=name,
            namespace=parent.namespace,
            bases=bases,
            extends=extends,
            implements=implements,
            public=public,
            final=final,
            methods=methods,
            init=init
        )


class ClosureClass(Class):
    def __init__(self, parent, closure_var_names, name=None, extends=None, bases=None, implements=None, public=True, final=False, methods=None, init=None):
        self.closure_var_names = closure_var_names
        if isinstance(parent, Class):
            module = parent.module
        else:
            module = parent
        if name is None:
            parent.anonymous_inner_class_count += 1
            name = "%s$%d" % (parent.name, parent.anonymous_inner_class_count)
        super().__init__(
            module=module,
            name=name,
            namespace=parent.namespace,
            bases=bases,
            extends=extends,
            implements=implements,
            public=public,
            final=final,
            methods=methods,
            init=init
        )
