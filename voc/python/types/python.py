from ...java import opcodes as JavaOpcodes, Classref as JavaClassref

from . import java as Java


##########################################################################
# Python types and their operations
##########################################################################

class Callable:
    class invoke:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Callable',
                    'invoke',
                    args=['[Lorg/python/Object;', 'Ljava/util/Map;'],
                    returns='Lorg/python/Object;'
                ),
            )


class Iterable:
    class next:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__next__',
                    args=[],
                    returns='Lorg/python/Object;'
                )
            )


class Type:
    class for_class:
        def __init__(self, name):
            self.name = name

        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.LDC_W(JavaClassref(self.name)),
                JavaOpcodes.INVOKESTATIC(
                    'org/python/types/Type',
                    'pythonType',
                    args=['Ljava/lang/Class;'],
                    returns='Lorg/python/types/Type;'
                )
            )

    class for_name:
        def __init__(self, name):
            self.name = name

        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.LDC_W(self.name),
                JavaOpcodes.INVOKESTATIC(
                    'org/python/types/Type',
                    'pythonType',
                    args=['Ljava/lang/String;'],
                    returns='Lorg/python/types/Type;'
                )
            )

    class to_python:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKESTATIC(
                    'org/python/types/Type',
                    'toPython',
                    args=['Ljava/lang/Object;'],
                    returns='Lorg/python/Object;'
                )
            )


class Object:
    class get_attribute:
        def __init__(self, attr, use_null=False):
            self.attr = attr
            self.use_null = use_null

        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.LDC_W(self.attr),
            )
            if self.use_null:
                context.add_opcodes(
                    JavaOpcodes.INVOKEINTERFACE(
                        'org/python/Object',
                        '__getattribute_null',
                        args=['Ljava/lang/String;'],
                        returns='Lorg/python/Object;'
                    ),
                )
            else:
                context.add_opcodes(
                    JavaOpcodes.INVOKEINTERFACE(
                        'org/python/Object',
                        '__getattribute__',
                        args=['Ljava/lang/String;'],
                        returns='Lorg/python/Object;'
                    ),
                )

    class set_attr:
        def __init__(self, attr):
            self.attr = attr

        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.LDC_W(self.attr),
                JavaOpcodes.SWAP(),
                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__setattr__',
                    args=['Ljava/lang/String;', 'Lorg/python/Object;'],
                    returns='V'
                ),
            )

    class del_attr:
        def __init__(self, attr=None):
            self.attr = attr

        def process(self, context):
            if self.attr:
                context.add_opcodes(
                    JavaOpcodes.LDC_W(self.attr),
                )
            context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__delattr__',
                    args=['Ljava/lang/String;'],
                    returns='V'
                ),
            )

    class get_item:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__getitem__',
                    args=['Lorg/python/Object;'],
                    returns='Lorg/python/Object;'
                ),
            )

    class set_item:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__setitem__',
                    args=['Lorg/python/Object;', 'Lorg/python/Object;'],
                    returns='V'
                ),
            )

    class del_item:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__delitem__',
                    args=['Lorg/python/Object;'],
                    returns='V'
                ),
            )

    class iter:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__iter__',
                    args=[],
                    returns='Lorg/python/Object;'
                )
            )

    class as_boolean:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    'toBoolean',
                    args=[],
                    returns='Z'
                ),
            )


class NONE:
    def process(self, context):
        context.add_opcodes(
            JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;')
        )


class Dict:
    def process(self, context):
        context.add_opcodes(
            Java.New('org/python/types/Dict'),
            Java.Init('org/python/types/Dict')
        )

    class set_item:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKEVIRTUAL(
                    'org/python/types/Dict',
                    '__setitem__',
                    args=['Lorg/python/Object;', 'Lorg/python/Object;'],
                    returns='V'
                )
            )


class Set:
    def process(self, context):
        context.add_opcodes(
            Java.New('org/python/types/Set'),
            Java.Init('org/python/types/Set')
        )

    class add:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKEVIRTUAL(
                    'org/python/types/Set',
                    'add',
                    args=['Lorg/python/Object;'],
                    returns='Lorg/python/Object;'
                ),
                JavaOpcodes.POP()
            )


class List:
    def process(self, context):
        context.add_opcodes(
            Java.New('org/python/types/List'),
            Java.Init('org/python/types/List')
        )

    class append:
        def process(self, context):
            context.add_opcodes(
                JavaOpcodes.INVOKEVIRTUAL(
                    'org/python/types/List',
                    'append',
                    args=['Lorg/python/Object;'],
                    returns='Lorg/python/Object;'
                ),
                JavaOpcodes.POP()
            )


class Str:
    def __init__(self, value=None):
        self.value = value

    def process(self, context):
        if self.value:
            context.add_opcodes(
                Java.New('org/python/types/Str'),
                JavaOpcodes.LDC_W(self.value),
                Java.Init('org/python/types/Str', 'Ljava/lang/String;')
            )
        else:
            context.add_opcodes(
                Java.New('org/python/types/Str'),
                Java.Init('org/python/types/Str')
            )
