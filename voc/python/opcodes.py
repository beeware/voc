from ..java import opcodes as JavaOpcodes


class Opcode:
    @property
    def opname(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.opname + ': ' + self.__arg_repr__()

    def __arg_repr__(self):
        return ''


class POP_TOP(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0

    def convert(self, arguments):
        code = []
        for argument in arguments:
            code.extend(argument.operation.convert(argument.arguments))

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

    def convert(self, arguments):
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

    def convert(self, arguments):
        code.append(JavaOpcodes.DUP())
        return code


class DUP_TOP_TWO(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 4

    def convert(self, arguments):
        code.append(JavaOpcodes.DUP2())
        return code


class NOP(Opcode):
    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0

    def convert(self, arguments):
        code.append(JavaOpcodes.NOP())
        return code

# class UNARY_POSITIVE(Opcode):
# class UNARY_NEGATIVE(Opcode):
# class UNARY_NOT(Opcode):
# class UNARY_INVERT(Opcode):

class BINARY_POWER(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 1


class BINARY_MULTIPLY(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 1


class BINARY_MODULO(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 1


class BINARY_ADD(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 1

# class BINARY_SUBTRACT(Opcode):

class BINARY_SUBSCR(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 1

# class BINARY_FLOOR_DIVIDE(Opcode):
# class BINARY_TRUE_DIVIDE(Opcode):

# class INPLACE_FLOOR_DIVIDE(Opcode):
# class INPLACE_TRUE_DIVIDE(Opcode):

# class STORE_MAP(Opcode):

# class INPLACE_ADD(Opcode):
# class INPLACE_SUBTRACT(Opcode):
# class INPLACE_MULTIPLY(Opcode):
# class INPLACE_MODULO(Opcode):

# class STORE_SUBSCR(Opcode):
# class DELETE_SUBSCR(Opcode):

# class BINARY_LSHIFT(Opcode):
# class BINARY_RSHIFT(Opcode):
# class BINARY_AND(Opcode):
# class BINARY_XOR(Opcode):
# class BINARY_OR(Opcode):
# class INPLACE_POWER(Opcode):

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

# class INPLACE_LSHIFT(Opcode):
# class INPLACE_RSHIFT(Opcode):
# class INPLACE_AND(Opcode):
# class INPLACE_XOR(Opcode):
# class INPLACE_OR(Opcode):

# class BREAK_LOOP(Opcode):
# class WITH_CLEANUP(Opcode):


class RETURN_VALUE(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0

    def convert(self, arguments):
        code = []
        if arguments[0].operation.opname == 'LOAD_CONST' and arguments[0].operation.const is None:
            # Simple case - no return value.
            code.append(JavaOpcodes.RETURN())
        else:
            code.extend(arguments[0].operation.convert(arguments[0].arguments))
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
    def __init__(self, namei):
        self.namei = namei

    def __arg_repr__(self):
        return str(self.namei)

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0

    def convert(self, arguments):
        code = []

        # If the most recent command is stored as None, then this is
        # return value of a void function. We can avoid a POP operation
        # in this case.
        if code[-1] is None:
            code.pop()
        else:
            # FIXME - use namei
            code.append(JavaOpcodes.ASTORE_0())

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
    def __init__(self, namei):
        self.namei = namei

    def __arg_repr__(self):
        return str(self.namei)

    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 0

    def convert(self, arguments):
        # FIXME
        code = []
        code.extend(arguments[0].operation.convert(arguments[0].arguments))
        code.append(JavaOpcodes.LDC(self.namei))
        code.extend(arguments[1].operation.convert(arguments[1].arguments))

        code.extend([
            JavaOpcodes.INVOKESPECIAL('org/python/PyObject', '__setattr__', '(java/lang/String;org/python/PyObject)V'),
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

    def convert(self, arguments):
        return [
            JavaOpcodes.LDC(self.const)
        ]


class LOAD_NAME(Opcode):
    def __init__(self, namei):
        self.namei = namei

    def __arg_repr__(self):
        return str(self.namei)

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 1


# class BUILD_TUPLE(Opcode):
# class BUILD_LIST(Opcode):
# class BUILD_SET(Opcode):
# class BUILD_MAP(Opcode):

class LOAD_ATTR(Opcode):
    def __init__(self, namei):
        self.namei = namei

    def __arg_repr__(self):
        return str(self.namei)

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 1


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
    def __init__(self, namei):
        self.namei = namei

    def __arg_repr__(self):
        return str(self.namei)

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
    def __init__(self, varnum):
        self.varnum = varnum

    def __arg_repr__(self):
        return str(self.varnum)

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 1


class STORE_FAST(Opcode):
    def __init__(self, varnum):
        self.varnum = varnum

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0

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

    def convert(self, arguments):
        code = []

        if arguments[0].operation.namei == 'print':
            code.append(
                JavaOpcodes.GETSTATIC('java/lang/System', 'out', 'Ljava/io/PrintStream;'),
            )

            for argument in arguments[1:]:
                code.extend(argument.operation.convert(argument.arguments))

            code.extend([
                JavaOpcodes.INVOKEVIRTUAL('java/io/PrintStream', 'println', '(Ljava/lang/String;)V'),
                None
            ])
            # The None value in the code list is a special case;
            # Python explicitly returns None and then pops the empty
            # result; Java can just return. We put a marker here that
            # the POP/STORE_* result can use to identify the case.
        else:
            # FIXME
            # get method name from arguments[0].operation.namei
            for argument in arguments[1:]:
                code.extend(argument.operation.convert(argument.arguments))

            code.extend([
                # JavaOpcodes.INVOKEVIRTUAL('java/io/PrintStream', 'println', '(Ljava/lang/String;)V'),
            ])
        return code


class MAKE_FUNCTION(Opcode):
    def __init__(self, argc):
        self.args = argc & 0xff
        self.kwargs = ((argc >> 8) & 0xFF)
        self.annotations = (argc >> 16) & 0x7FFF
        self.annotation_names = 1 if self.annotations else 0

    def __arg_repr__(self):
        return '%s args, %s kwargs, %s annotations' % (
            self.args,
            self.kwargs,
            self.annotations,
        )

    @property
    def consume_count(self):
        return self.args + 2 * self.kwargs + self.annotations + self.annotation_names + 2

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
# class EXTENDED_ARG(Opcode):
