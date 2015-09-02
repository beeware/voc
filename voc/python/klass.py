import os

from ..java import (
    Class as JavaClass,
    Field as JavaField,
    Method as JavaMethod,
    opcodes as JavaOpcodes,
    SourceFile,
    # LineNumberTable
)

from .blocks import Block
from .methods import InitMethod, InstanceMethod, extract_parameters
from .opcodes import ASTORE_name, ALOAD_name, IF, END_IF


class ClassBlock(Block):
    def tweak(self, code):
        code = [
            # Set up the class attributes dictionary for the class
            JavaOpcodes.NEW('java/util/Hashtable'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('java/util/Hashtable', '<init>', '()V'),
            JavaOpcodes.PUTSTATIC(self.klass.descriptor, 'attrs', 'Ljava/util/Hashtable;'),

            # # Set the __name__ atribute to the name of the parent module.
            JavaOpcodes.GETSTATIC(self.klass.descriptor, 'attrs', 'Ljava/util/Hashtable;'),
            JavaOpcodes.LDC('__name__'),
            JavaOpcodes.NEW('org/python/Object'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC(self.module.descriptor.replace('/', '.')),
            JavaOpcodes.INVOKESPECIAL('org/python/Object', '<init>', '(Ljava/lang/String;)V'),
            JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
            JavaOpcodes.POP()
        ] + code
        return self.void_return(code)

    def store_name(self, name, arguments, allow_locals=True):
        # Ignore a request to store __init__ - replace with the constructor
        if name == '__init__':
            return []

        return [
            ASTORE_name(self.localvars, '#TEMP#'),
            JavaOpcodes.GETSTATIC(self.klass.descriptor, 'attrs', 'Ljava/util/Hashtable;'),
            JavaOpcodes.LDC(name),
            ALOAD_name(self.localvars, '#TEMP#'),
            JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
            JavaOpcodes.POP(),
        ]

    def load_name(self, name, allow_locals=True):
        if allow_locals:
            code = [
                # look for a class attribute.
                JavaOpcodes.GETSTATIC(self.klass.descriptor, 'attrs', 'Ljava/util/Hashtable;'),
                JavaOpcodes.LDC(name),
                JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),
            ]
        else:
            code = []
        return code + [
            # Look for a global var.
            IF(
                [JavaOpcodes.DUP()],
                JavaOpcodes.IFNONNULL
            ),
                JavaOpcodes.POP(),
                JavaOpcodes.GETSTATIC(self.module.descriptor, 'globals', 'Ljava/util/Hashtable;'),
                JavaOpcodes.LDC(name),
                JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),

                # If there's nothing in the globals, then look for a builtin.
                IF(
                    [JavaOpcodes.DUP()],
                    JavaOpcodes.IFNONNULL
                ),
                    JavaOpcodes.POP(),
                    JavaOpcodes.GETSTATIC('org/Python', 'builtins', 'Ljava/util/Hashtable;'),
                    JavaOpcodes.LDC(name),
                    JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),
                END_IF(),
            END_IF()
        ]

    @property
    def descriptor(self):
        return self.parent.descriptor

    @property
    def klass(self):
        return self.parent

    @property
    def module(self):
        return self.parent.parent

    def add_method(self, full_method_name, code):
        class_name, method_name = full_method_name.split('.')
        if class_name != self.klass.name:
            raise Exception("Method %s being added to %s!" % (full_method_name, self.klass.name))
        if method_name == '__init__':
            method = InitMethod(self.klass, extract_parameters(code))
        else:
            method = InstanceMethod(self.klass, method_name, extract_parameters(code))

        method.extract(code)
        self.klass.methods.append(method.transpile())

        return method


class Class(Block):
    def __init__(self, module, name, super_name=None, methods=None, init=None):
        super().__init__(module)
        self.name = name
        self.super_name = super_name if super_name else 'org/python/Object'
        self.methods = methods if methods else []
        self.init = init

    @property
    def descriptor(self):
        return '/'.join([self.parent.descriptor, self.name])

    @property
    def module(self):
        return self.parent

    def add_method(self, method):
        self.methods.append(method)

    def transpile(self):
        classfile = JavaClass(self.descriptor, supername=self.super_name)
        classfile.attributes.append(SourceFile(os.path.basename(self.parent.sourcefile)))

        body = ClassBlock(self, self.commands).transpile()

        # Add a attrs dictionary to the class.
        classfile.fields.append(
            JavaField('attrs', 'Ljava/util/Hashtable;', public=True, static=True)
        )

        if body:
            # If we have block content, add a static block to the class
            static_init = JavaMethod('<clinit>', '()V', public=False, static=True)
            static_init.attributes.append(body)
            classfile.methods.append(static_init)

        # if self.init:
        #     classfile.methods.append(self.init)
        # else:
        #     # Add default constructor
        #     classfile.methods.append(
        #         JavaMethod(
        #             '<init>',
        #             '()V',
        #             attributes=[
        #                 JavaCode(
        #                     max_stack=1,
        #                     max_locals=1,
        #                     code=[
        #                         JavaOpcodes.ALOAD_0(),
        #                         JavaOpcodes.INVOKESPECIAL('org/python/Object', '<init>', '()V'),
        #                         JavaOpcodes.RETURN(),
        #                     ],
        #                 )
        #             ]
        #         )
        #     )

        for method in self.methods:
            classfile.methods.append(method)

        return self.name, classfile
