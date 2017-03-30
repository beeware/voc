from ...java import opcodes as JavaOpcodes

from .primitives import ICONST_val


##########################################################################
# Common Java operations
##########################################################################

class New:
    def __init__(self, classname):
        self.classname = classname

    def process(self, context):
        context.add_opcodes(
            JavaOpcodes.NEW(self.classname),
            JavaOpcodes.DUP()
        )


class Init:
    def __init__(self, classname, *args):
        self.classname = classname
        self.args = args

    def process(self, context):
        context.add_opcodes(
            JavaOpcodes.INVOKESPECIAL(
                self.classname,
                '<init>',
                args=self.args,
                returns='V'
            ),
        )


class Yield:
    def __init__(self, yield_point):
        self.yield_point = yield_point

    def process(self, context):
        context.add_opcodes(
            ICONST_val(self.yield_point),
            JavaOpcodes.INVOKEVIRTUAL(
                'org/python/types/Generator',
                'yield',
                args=['Ljava/util/Map;', 'I'],
                returns='V'
            ),
            # "yield" by returning from the generator method.
            JavaOpcodes.ARETURN()
        )


##########################################################################
# Java types and their operations
##########################################################################

class Array:
    def __init__(self, size, classname='org/python/Object', fill=None):
        self.size = size
        self.classname = classname
        self.fill = fill

    def process(self, context):
        context.add_opcodes(
            ICONST_val(self.size),
            JavaOpcodes.ANEWARRAY(self.classname),
        )
        if self.fill:
            for i in range(self.size):
                context.add_opcodes(
                    JavaOpcodes.DUP(),
                    ICONST_val(i),
                    self.fill,
                    JavaOpcodes.AASTORE(),
                )

    class get:
        def __init__(self, index):
            self.index = index

        def process(self, context):
            context.add_opcodes(
                ICONST_val(self.index),
                JavaOpcodes.AALOAD(),
            )


class List:
    def __init__(self, size=None):
        self.size = size

    def process(self, context):
        context.add_opcodes(
            JavaOpcodes.NEW('java/util/ArrayList'),
            JavaOpcodes.DUP(),
        )

        if self.size:
            context.add_opcodes(
                ICONST_val(self.size),
                Init('java/util/ArrayList', 'I')
            )
        else:
            context.add_opcodes(
                Init('java/util/ArrayList')
            )

    class add:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE(
                    'java/util/List',
                    'add',
                    args=['Ljava/lang/Object;'],
                    returns='Z'
                ),
                JavaOpcodes.POP(),
            )


class Map:
    def process(self, context):
        context.add_opcodes(
            JavaOpcodes.NEW('java/util/HashMap'),
            JavaOpcodes.DUP(),
            Init('java/util/HashMap')
        )

    class get:
        def __init__(self, key):
            self.key = key

        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.LDC_W(self.key),
                JavaOpcodes.INVOKEINTERFACE(
                    'java/util/Map',
                    'get',
                    args=['Ljava/lang/Object;'],
                    returns='Ljava/lang/Object;'
                )
            )

    class put:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE(
                    'java/util/Map',
                    'put',
                    args=['Ljava/lang/Object;', 'Ljava/lang/Object;'],
                    returns='Ljava/lang/Object;'
                ),
                JavaOpcodes.POP()
            )

    class putAll:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE(
                    'java/util/Map',
                    'putAll',
                    args=['Ljava/util/Map;'],
                    returns='V'
                ),
            )


class Class:
    class forName:
        def __init__(self, classname):
            self.classname = classname

        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.LDC_W(self.classname),
                JavaOpcodes.INVOKESTATIC(
                    'java/lang/Class',
                    'forName',
                    args=['Ljava/lang/String;'],
                    returns='Ljava/lang/Class;'
                ),
            )


class THROW:
    # Raise an exception of given type with given arguments
    # Example:
    #    THROW(
    #        'org/python/exceptions/AttributeError',
    #        ['Ljava/lang/String;', JavaOpcodes.LDC_W("Invalid attribute")],
    #    )
    def __init__(self, exception_class, *exception_args):
        self.exception_class = exception_class
        self.exc_arg_types = [e[0] for e in exception_args]
        self.exc_arg_values = [e[1] for e in exception_args]

    def process(self, context):
        context.add_opcodes(
            New(self.exception_class),
            *self.exc_arg_values
        )
        context.add_opcodes(
            Init(self.exception_class, *self.exc_arg_types),
            JavaOpcodes.ATHROW(),
        )
