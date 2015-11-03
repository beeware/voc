import os

from ..java import (
    Class as JavaClass,
    Code as JavaCode,
    Field as JavaField,
    Method as JavaMethod,
    opcodes as JavaOpcodes,
    SourceFile,
    RuntimeVisibleAnnotations,
    Annotation,
    ConstantElementValue,
    # LineNumberTable
)

from .blocks import Block
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
        if name != '__init__':
            self.add_opcodes(
                ASTORE_name(self, '#value'),
                JavaOpcodes.LDC_W(self.klass.descriptor),
                JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),

                JavaOpcodes.LDC_W(name),
                ALOAD_name(self, '#value'),

                JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__setattr__', '(Ljava/lang/String;Lorg/python/Object;)V'),
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

    def add_method(self, full_method_name, code):
        class_name, method_name = full_method_name.split('.')
        if class_name != self.klass.name:
            raise Exception("Method %s being added to %s!" % (full_method_name, self.klass.name))
        if method_name == '__init__':
            method = InitMethod(self.klass, extract_parameters(code))
        else:
            method = InstanceMethod(self.klass, method_name, extract_parameters(code))

        method.extract(code)
        self.klass.methods.append(method)

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

    @property
    def descriptor(self):
        return '/'.join([self.namespace.replace('.', '/'), self.name])

    @property
    def module(self):
        return self.parent

    def add_method(self, method):
        self.methods.append(method)

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

        body = ClassBlock(self, self.commands).transpile()

        # Add any manually defined fields
        classfile.fields.extend([
            JavaField(name, descriptor)
            for name, descriptor in self.fields.items()
        ])

        if body:
            # If we have block content, add a static block to the class
            static_init = JavaMethod('<clinit>', '()V', public=False, static=True)
            static_init.attributes.append(body)
            classfile.methods.append(static_init)

        constructor_found = False
        for method in self.methods:
            classfile.methods.append(method.transpile())
            if method.name == '__init__':
                constructor_found = True

        # If there's no constructor explicitly defined, add a default one.
        if not constructor_found:
            classfile.methods.append(
                JavaMethod(
                    '<init>',
                    '([Lorg/python/Object;Ljava/util/Map;)V',
                    attributes=[
                        JavaCode(
                            max_stack=1,
                            max_locals=3,
                            code=[
                                JavaOpcodes.ALOAD_0(),
                                JavaOpcodes.INVOKESPECIAL('org/python/types/Object', '<init>', '()V'),
                                JavaOpcodes.RETURN(),
                            ],
                        ),
                    ]
                )
            )

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


class AnonymousInnerClass(Class):
    def __init__(self, parent, closure_var_names, super_name=None, interfaces=None, public=True, final=False, methods=None, init=None):
        # self.closure_var_names = closure_var_names
        if isinstance(parent, Class):
            module = parent.module
        else:
            module = parent
        parent.anonymous_inner_class_count += 1
        counter = parent.anonymous_inner_class_count
        super().__init__(
            module=module,
            name="%s$%d" % (parent.name, counter),
            namespace=parent.namespace,
            super_name=super_name,
            interfaces=interfaces,
            public=public,
            final=final,
            methods=methods,
            init=init
        )
