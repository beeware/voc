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
from .methods import InitMethod, Method, extract_parameters
from .opcodes import ASTORE_name, ALOAD_name


class ClassBlock(Block):
    def tweak(self, code):
        code = [
            # Set up the class attributes dictionary for the class
            JavaOpcodes.NEW('java/util/Hashtable'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('java/util/Hashtable', '<init>', '()V'),
            JavaOpcodes.PUTSTATIC(self.klass.descriptor, 'attrs', 'Ljava/util/Hashtable;'),

            # Set the __module__ atribute to the name of the parent module.
            JavaOpcodes.GETSTATIC(self.klass.descriptor, 'attrs', 'Ljava/util/Hashtable;'),
            JavaOpcodes.LDC('__module__'),
            JavaOpcodes.NEW('org/python/Object'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC(self.module.descriptor.replace('/', '.')),
            JavaOpcodes.INVOKESPECIAL('org/python/Object', '<init>', '(Ljava/lang/String;)V'),
            JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
            JavaOpcodes.POP()
        ] + code
        return self.void_return(code)

    def store_name(self, name, arguments):
        return [
            ASTORE_name(self.localvars, '#TEMP#'),
            JavaOpcodes.GETSTATIC(self.klass.descriptor, 'attrs', 'Ljava/util/Hashtable;'),
            JavaOpcodes.LDC(name),
            ALOAD_name(self.localvars, '#TEMP#'),
            JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
            ALOAD_name(self.localvars, '#TEMP#'),
        ]

    @property
    def klass(self):
        return self.parent

    @property
    def module(self):
        return self.parent.parent

    def add_method(self, method_name, code):
        if method_name == '%s.__init__' % self.klass.name:
            method = InitMethod(self.klass, extract_parameters(code))
        else:
            method = Method(self.klass, method_name, extract_parameters(code))

        method.extract(code)
        self.klass.methods.append(method.transpile())


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
