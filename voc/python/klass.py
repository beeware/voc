import os

from ..java import (
    Class as JavaClass,
    Method as JavaMethod,
    Code as JavaCode,
    opcodes as JavaOpcodes,
    SourceFile,
    # LineNumberTable
)

from .utils import extract
from .block import Block


class Class(Block):
    def __init__(self, module, name, methods=None, init=None):
        super().__init__(module)
        self.name = name
        self.methods = methods if methods else []
        self.init = init

    @property
    def descriptor(self):
        return '/'.join([self.parent.descriptor, self.name])

    def add_method(self, method):
        self.methods.append(method)

    def transpile(self, code):
        extract(self, code)

        classfile = JavaClass(self.descriptor, supername='org/python/PyObject')
        classfile.attributes.append(SourceFile(os.path.basename(self.sourcefile)))

        if self.block:
            # If we have block content, add a static block to the class
            static_init = JavaMethod('<clinit>', '()V', public=False, static=True)
            static_init.attributes.append(self.block)
            classfile.methods.append(static_init)

        if self.init:
            classfile.methods.append(self.init)
        else:
            # Add default constructor
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
                                JavaOpcodes.INVOKESPECIAL('org/python/PyObject', '<init>', '()V'),
                                JavaOpcodes.RETURN(),
                            ],
                        )
                    ]
                )
            )

        for method in self.methods:
            classfile.methods.append(method)

        return self.name, classfile
