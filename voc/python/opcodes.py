from ..java import opcodes as JavaOpcodes


##########################################################################
# Local variables are stored in a dictionary, keyed by name,
# and with the value of the local variable register they are stored in.
#
# When a variable is deleted, a value of None is put in as the
# value.
##########################################################################

def get_local(localvars, name):
    i = localvars[name]
    if i is None:
        raise KeyError(name)
    return i


def create_local(localvars, name):
    try:
        i = localvars[name]
        if i is None:
            localvars[name] = i
    except KeyError:
        i = len(localvars)
        localvars[name] = i
    return i


##########################################################################
# Base classes for defining opcodes.
##########################################################################

class Opcode:
    @property
    def opname(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.opname + ': ' + self.__arg_repr__()

    def __arg_repr__(self):
        return ''


class UnaryOpcode(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        code = []

        for argument in arguments:
            code.extend(argument.operation.convert(context, argument.arguments))

        code.append(
            JavaOpcodes.INVOKEVIRTUAL(
                'org/python/PyObject',
                self.__method__,
                '()Lorg/python/PyObject;'
            )
        )
        return code


class BinaryOpcode(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        code = []

        for argument in arguments:
            code.extend(argument.operation.convert(context, argument.arguments))

        code.append(
            JavaOpcodes.INVOKEVIRTUAL(
                'org/python/PyObject',
                self.__method__,
                '(Lorg/python/PyObject;)Lorg/python/PyObject;'
            )
        )
        return code


class InplaceOpcode(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        code = []

        for argument in arguments:
            code.extend(argument.operation.convert(context, argument.arguments))

        code.append(
            JavaOpcodes.INVOKEVIRTUAL(
                'org/python/PyObject',
                self.__method__,
                '(Lorg/python/PyObject;)V'
            )
        )
        return code


##########################################################################
# The actual Python opcodes
##########################################################################

class POP_TOP(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):
        print ('-----')
        code = []
        for argument in arguments:
            print (argument)
            code.extend(argument.operation.convert(context, argument.arguments))

        print ('-----')
        # If the most recent command is stored as None, then this is
        # return value of a void function. We can avoid a POP operation
        # in this case.
        if code[-1] is None:
            code.pop()
        else:
            code.append(JavaOpcodes.POP())

        return code


class ROT_TWO(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 2

    def convert(self, context, arguments):
        code = []
        code.append(JavaOpcodes.SWAP())
        return code

# class ROT_THREE(Opcode):


class DUP_TOP(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 2

    def convert(self, context, arguments):
        code = []
        code.append(JavaOpcodes.DUP())
        return code


class DUP_TOP_TWO(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 4

    def convert(self, context, arguments):
        code = []
        code.append(JavaOpcodes.DUP2())
        return code


class NOP(Opcode):
    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):
        code = []
        code.append(JavaOpcodes.NOP())
        return code

class UNARY_POSITIVE(Opcode):
    __method__ = '__pos__'


class UNARY_NEGATIVE(Opcode):
    __method__ = '__neg__'


# FIXME - there shouldn't be a __not__...
class UNARY_NOT(Opcode):
    __method__ = '__not__'


class UNARY_INVERT(Opcode):
    __method__ = '__invert__'


class BINARY_POWER(BinaryOpcode):
    __method__ = '__pow__'


class BINARY_MULTIPLY(BinaryOpcode):
    __method__ = '__mul__'


class BINARY_MODULO(BinaryOpcode):
    __method__ = '__mod__'


class BINARY_ADD(BinaryOpcode):
    __method__ = '__add__'


class BINARY_SUBTRACT(BinaryOpcode):
    __method__ = '__sub__'


class BINARY_SUBSCR(BinaryOpcode):
    __method__ = '__subscr__'


class BINARY_FLOOR_DIVIDE(BinaryOpcode):
    __method__ = '__floordiv__'


class BINARY_TRUE_DIVIDE(BinaryOpcode):
    __method__ = '__truediv__'



class INPLACE_FLOOR_DIVIDE(InplaceOpcode):
    __method__ = '__ifloordiv__'


class INPLACE_TRUE_DIVIDE(InplaceOpcode):
    __method__ = '__itruediv__'


# class STORE_MAP(Opcode):

class INPLACE_ADD(InplaceOpcode):
    __method__ = '__iadd__'


class INPLACE_SUBTRACT(InplaceOpcode):
    __method__ = '__isub__'


class INPLACE_MULTIPLY(InplaceOpcode):
    __method__ = '__imul__'


class INPLACE_MODULO(InplaceOpcode):
    __method__ = '__imod__'


# class STORE_SUBSCR(Opcode):
# class DELETE_SUBSCR(Opcode):


class BINARY_LSHIFT(BinaryOpcode):
    __method__ = '__lshift__'


class BINARY_RSHIFT(BinaryOpcode):
    __method__ = '__rshift__'


class BINARY_AND(BinaryOpcode):
    __method__ = '__and__'


class BINARY_XOR(BinaryOpcode):
    __method__ = '__xor__'


class BINARY_OR(BinaryOpcode):
    __method__ = '__or__'


class INPLACE_POWER(InplaceOpcode):
    __method__ = '__ipow__'



class GET_ITER(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 1


class PRINT_EXPR(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0


class LOAD_BUILD_CLASS(Opcode):
    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 1


# class YIELD_FROM(Opcode):

class INPLACE_LSHIFT(InplaceOpcode):
    __method__ = '__ilshift__'


class INPLACE_RSHIFT(InplaceOpcode):
    __method__ = '__irshift__'


class INPLACE_AND(InplaceOpcode):
    __method__ = '__iand__'


class INPLACE_XOR(InplaceOpcode):
    __method__ = '__ixor__'


class INPLACE_OR(InplaceOpcode):
    __method__ = '__ior__'


# class BREAK_LOOP(Opcode):
# class WITH_CLEANUP(Opcode):


class RETURN_VALUE(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):
        code = arguments[0].operation.convert(context, arguments[0].arguments)
        code.append(JavaOpcodes.ARETURN())
        return code


# class IMPORT_STAR(Opcode):
# class YIELD_VALUE(Opcode):


class POP_BLOCK(Opcode):
    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0


# class END_FINALLY(Opcode):
# class POP_EXCEPT(Opcode):


class STORE_NAME(Opcode):
    def __init__(self, name):
        self.name = name

    def __arg_repr__(self):
        return str(self.name)

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):
        code = []

        for argument in arguments:
            code.extend(argument.operation.convert(context, argument.arguments))

        # If the most recent command is stored as None, then this is
        # return value of a void function. We can avoid a POP operation
        # in this case.
        if code[-1] is None:
            code.pop()
        else:
            i = create_local(context.localvars, self.name)

            if i == 0:
                code.append(JavaOpcodes.ASTORE_0())
            elif i == 1:
                code.append(JavaOpcodes.ASTORE_1())
            elif i == 2:
                code.append(JavaOpcodes.ASTORE_2())
            elif i == 3:
                code.append(JavaOpcodes.ASTORE_3())
            else:
                code.append(JavaOpcodes.ASTORE(i))

        return code


# class DELETE_NAME(Opcode):
# class UNPACK_SEQUENCE(Opcode):


class FOR_ITER(Opcode):
    def __init__(self, delta):
        self.delta = delta

    def __arg_repr__(self):
        return str(self.delta)

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 2


# class UNPACK_EX(Opcode):


class STORE_ATTR(Opcode):
    def __init__(self, name):
        self.name = name

    def __arg_repr__(self):
        return str(self.name)

    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):
        # FIXME
        code = []
        code.extend(arguments[0].operation.convert(context, arguments[0].arguments))
        code.append(JavaOpcodes.LDC(self.name))
        code.extend(arguments[1].operation.convert(context, arguments[1].arguments))

        code.extend([
            JavaOpcodes.INVOKESPECIAL('org/python/PyObject', '__setattr__', '(Ljava/lang/String;Lorg/python/PyObject;)V'),
            JavaOpcodes.POP(),
        ])
        return code


# class DELETE_ATTR(Opcode):

# class STORE_GLOBAL(Opcode):
# class DELETE_GLOBAL(Opcode):


class LOAD_CONST(Opcode):
    def __init__(self, const):
        self.const = const

    def __arg_repr__(self):
        return str(self.const)

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        # A None value has it's own opcode.
        # If the constant is a byte or a short, we can
        # cut a value out of the constant pool.
        # Otherwise, use LDC.
        if self.const is None:
            return [
                JavaOpcodes.ACONST_NULL()
            ]
        elif isinstance(self.const, int) and self.const < 128:
            prototype = '(I)V'
            load_op = JavaOpcodes.BIPUSH(self.const)
        elif isinstance(self.const, int) and self.const < 32768:
            prototype = '(I)V'
            load_op = JavaOpcodes.SIPUSH(self.const)
        else:
            prototype = {
                int: '(I)V',
                str: '(Ljava/lang/String;)V',
            }[type(self.const)]
            load_op = JavaOpcodes.LDC(self.const)

        return [
            JavaOpcodes.NEW('org/python/PyObject'),
            JavaOpcodes.DUP(),
            load_op,
            JavaOpcodes.INVOKESPECIAL('org/python/PyObject', '<init>', prototype),
        ]


class LOAD_NAME(Opcode):
    def __init__(self, name):
        self.name = name

    def __arg_repr__(self):
        return str(self.name)

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        code = []
        try:
            i = get_local(context.localvars, self.name)
            if i == 0:
                code.append(JavaOpcodes.ALOAD_0())
            elif i == 1:
                code.append(JavaOpcodes.ALOAD_1())
            elif i == 2:
                code.append(JavaOpcodes.ALOAD_2())
            elif i == 3:
                code.append(JavaOpcodes.ALOAD_3())
            else:
                code.append(JavaOpcodes.ALOAD(i))
        except KeyError:
            # TODO:
            # Look for global name (static variable in current class)
            # Then look for builtin.
            raise
        return code


# class BUILD_TUPLE(Opcode):
# class BUILD_LIST(Opcode):
# class BUILD_SET(Opcode):
# class BUILD_MAP(Opcode):


class LOAD_ATTR(Opcode):
    def __init__(self, name):
        self.name = name

    def __arg_repr__(self):
        return str(self.name)

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        code = []
        code.extend(arguments[0].operation.convert(context, arguments[0].arguments))
        code.append(JavaOpcodes.LDC(self.name))

        code.extend([
            JavaOpcodes.INVOKESPECIAL('org/python/PyObject', '__getattr__', '(java/lang/String;org/python/PyObject)V'),
        ])
        return code


class COMPARE_OP(Opcode):
    def __init__(self, comparison):
        self.comparison = comparison

    def __arg_repr__(self):
        return self.comparison

    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 1


class IMPORT_NAME(Opcode):
    def __init__(self, target):
        self.target = target

    def __arg_repr__(self):
        return str(self.target)

    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        return [None]

# class IMPORT_FROM(Opcode):


class JUMP_FORWARD(Opcode):
    def __init__(self, delta):
        self.delta = delta

    def __arg_repr__(self):
        return str(self.delta)

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0


# class JUMP_IF_FALSE_OR_POP(Opcode):
# class JUMP_IF_TRUE_OR_POP(Opcode):


class JUMP_ABSOLUTE(Opcode):
    def __init__(self, target):
        self.target = target

    def __arg_repr__(self):
        return str(self.target)

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0


class POP_JUMP_IF_FALSE(Opcode):
    def __init__(self, target):
        self.target = target

    def __arg_repr__(self):
        return str(self.target)

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0


class POP_JUMP_IF_TRUE(Opcode):
    def __init__(self, target):
        self.target = target

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0


class LOAD_GLOBAL(Opcode):
    def __init__(self, name):
        self.name = name

    def __arg_repr__(self):
        return str(self.name)

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 1


# class CONTINUE_LOOP(Opcode):


class SETUP_LOOP(Opcode):
    def __init__(self, delta):
        self.delta = delta

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0


# class SETUP_EXCEPT(Opcode):
# class SETUP_FINALLY(Opcode):


class LOAD_FAST(Opcode):
    def __init__(self, name):
        self.name = name

    def __arg_repr__(self):
        return str(self.name)

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        code = []

        i = get_local(context.localvars, self.name)

        if i == 0:
            code.append(JavaOpcodes.ALOAD_0())
        elif i == 1:
            code.append(JavaOpcodes.ALOAD_1())
        elif i == 2:
            code.append(JavaOpcodes.ALOAD_2())
        elif i == 3:
            code.append(JavaOpcodes.ALOAD_3())
        else:
            code.append(JavaOpcodes.ALOAD(i))

        return code


class STORE_FAST(Opcode):
    def __init__(self, name):
        self.name = name

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):
        code = []

        for argument in arguments:
            code.extend(argument.operation.convert(context, argument.arguments))

        i = create_local(context.localvars, self.name)

        if i == 0:
            code.append(JavaOpcodes.ASTORE_0())
        elif i == 1:
            code.append(JavaOpcodes.ASTORE_1())
        elif i == 2:
            code.append(JavaOpcodes.ASTORE_2())
        elif i == 3:
            code.append(JavaOpcodes.ASTORE_3())
        else:
            code.append(JavaOpcodes.ASTORE(i))

        return code

# class DELETE_FAST(Opcode):

# class RAISE_VARARGS(Opcode):


class CALL_FUNCTION(Opcode):
    def __init__(self, argc):
        self.args = argc & 0xff
        self.kwargs = ((argc >> 8) & 0xFF)

    def __arg_repr__(self):
        return '%s args, %s kwargs' % (
            self.args,
            self.kwargs,
        )

    @property
    def consume_count(self):
        return 1 + self.args + 2 * self.kwargs

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        code = []

        if arguments[0].operation.name == 'print':
            if len(arguments) == 2:
                # Just the one argument - no need to use a StringBuilder.
                code.append(JavaOpcodes.GETSTATIC('java/lang/System', 'out', 'Ljava/io/PrintStream;'))
                code.extend(arguments[1].operation.convert(context, arguments[1].arguments))
            else:
                # Multiple arguments; use a StringBuilder to concatenate, and put a space
                # between each argument.
                code.extend([
                    JavaOpcodes.GETSTATIC('java/lang/System', 'out', 'Ljava/io/PrintStream;'),
                    JavaOpcodes.NEW('java/lang/StringBuilder'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.INVOKESPECIAL('java/lang/StringBuilder', '<init>', '()V'),
                ])

                code.extend(arguments[1].operation.convert(context, arguments[1].arguments))
                code.extend([
                    JavaOpcodes.INVOKEVIRTUAL('java/lang/StringBuilder', 'append', '(Ljava/lang/Object;)Ljava/lang/StringBuilder;'),
                ])

                for argument in arguments[2:]:
                    code.extend([
                        JavaOpcodes.LDC(" "),
                        JavaOpcodes.INVOKEVIRTUAL('java/lang/StringBuilder', 'append', '(Ljava/lang/String;)Ljava/lang/StringBuilder;')
                    ])
                    code.extend(argument.operation.convert(context, argument.arguments))
                    code.extend([
                        JavaOpcodes.INVOKEVIRTUAL('java/lang/StringBuilder', 'append', '(Ljava/lang/Object;)Ljava/lang/StringBuilder;'),
                    ])

            # The None value in the code list is a special case;
            # Python explicitly returns None and then pops the empty
            # result; Java can just return. We put a marker here that
            # the POP/STORE_* result can use to identify the special case.
            code.extend([
                JavaOpcodes.INVOKEVIRTUAL('java/io/PrintStream', 'println', '(Ljava/lang/Object;)V'),
                None
            ])

        else:
            method_name = arguments[0].operation.name
            descriptor = '(%s)Lorg/python/PyObject;' % ('Lorg/python/PyObject;' * (len(arguments) - 1))

            for argument in arguments[1:]:
                code.extend(argument.operation.convert(context, argument.arguments))

            code.extend([
                JavaOpcodes.INVOKESTATIC('org/pybee/example', method_name, descriptor),
                None
            ])
        return code


class MAKE_FUNCTION(Opcode):
    def __init__(self, argc):
        self.default_args = argc & 0xff
        self.default_kwargs = ((argc >> 8) & 0xFF)
        self.annotations = (argc >> 16) & 0x7FFF

    def __arg_repr__(self):
        return '%s default args, %s default kwargs, %s annotations' % (
            self.default_args,
            self.default_kwargs,
            self.annotations,
        )

    @property
    def consume_count(self):
        if self.annotations:
            return 2 + self.annotations
        else:
            return 2 + self.default_args + (2 * self.default_kwargs)

    @property
    def product_count(self):
        return 1


# class BUILD_SLICE(Opcode):

# class MAKE_CLOSURE(Opcode):
# class LOAD_CLOSURE(Opcode):

# class LOAD_DEREF(Opcode):
# class STORE_DEREF(Opcode):
# class DELETE_DEREF(Opcode):

# class CALL_FUNCTION_VAR(Opcode):
# class CALL_FUNCTION_KW(Opcode):
# class CALL_FUNCTION_VAR_KW(Opcode):

# class SETUP_WITH(Opcode):
# class LIST_APPEND(Opcode):

# class SET_ADD(Opcode):
# class MAP_ADD(Opcode):

# class LOAD_CLASSDEREF(Opcode):
