import os

from ..java import (
    Class as JavaClass,
    Field as JavaField,
    Method as JavaMethod,
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
    def has_void_return(self):
        return True

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

            JavaOpcodes.NEW('org/python/types/Str'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),
            ALOAD_name(self, '#value'),

            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__setattr__', '(Lorg/python/Object;Lorg/python/Object;)V'),
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
            JavaOpcodes.NEW('org/python/types/Str'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),
            JavaOpcodes.INVOKEVIRTUAL('org/python/types/Type', '__getattribute__', '(Lorg/python/Object;)Lorg/python/Object;'),
        )

    def delete_name(self, name, use_locals):
        self.add_opcodes(
            JavaOpcodes.LDC_W(self.klass.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),
            JavaOpcodes.NEW('org/python/types/Str'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),
            JavaOpcodes.INVOKEVIRTUAL('org/python/types/Type', '__delattr__', '(Lorg/python/Object;)Lorg/python/Object;'),
        )

    def add_method(self, full_method_name, code):
        class_name, method_name = full_method_name.split('.')
        if class_name != self.klass.name:
            raise Exception("Method %s being added to %s!" % (full_method_name, self.klass.name))

        method = InstanceMethod(self.klass, method_name, extract_parameters(code), code=code)
        method.extract(code)
        self.klass.add_method(method)

        return method


class Class(Block):
    def __init__(self, module, name, namespace=None, super_name=None, interfaces=None, public=True, final=False, methods=None, fields=None, init=None):
        super().__init__(module)
        self.name = name
        self.super_name = super_name if super_name else 'org/python/types/Object'
        self.interfaces = interfaces
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
    def module(self):
        return self.parent

    def add_method(self, method):
        self.methods.append(method)
        if method.name == '__init__':
            if self.init_method is not None:
                raise Exception("Multiple __init__ methods defined")
            self.init_method = method

    def materialize(self):
        # Create the body of the class
        self.body = ClassBlock(self, self.commands)

        # Materialize the body of the class
        self.body.materialize()

        # Materialize any methods in the class
        for method in self.methods:
            method.materialize()

    def transpile(self):
        classfile = JavaClass(
            self.descriptor,
            supername=self.super_name,
            interfaces=self.interfaces,
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
            classfile.methods.append(method.transpile())

        return self.namespace, self.name, classfile


class InnerClass(Class):
    def __init__(self, parent, name, super_name=None, interfaces=None, public=True, final=False, methods=None, init=None):
        if isinstance(parent, Class):
            module = parent.module
        else:
            module = parent
        super().__init__(
            module=module,
            name=name,
            namespace=parent.namespace,
            super_name=super_name,
            interfaces=interfaces,
            public=public,
            final=final,
            methods=methods,
            init=init
        )


class ClosureClass(Class):
    def __init__(self, parent, closure_var_names, name=None, super_name=None, interfaces=None, public=True, final=False, methods=None, init=None):
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
            super_name=super_name,
            interfaces=interfaces,
            public=public,
            final=final,
            methods=methods,
            init=init
        )
