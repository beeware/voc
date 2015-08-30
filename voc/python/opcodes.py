from ..java import opcodes as JavaOpcodes, Classref


##########################################################################
# Pseudo instructions used to flag the offset position of other
# attributes of the code, especially those depened on opcode offset.
##########################################################################


class TRY:
    """Mark the start of a try-catch block.

    This forms the first of at least three pseudo-operations:
        TRY()
            ...
        CATCH('your/exception/descriptor')
            ...
        CATCH('your/other/exception')
            ...
        END_TRY()

    END_TRY come *after* the last operation in the relevant block;
    but TRY and CATCH come *before* the first instruction. A little
    special handling is required to account for this.

        1. When the TRY is created, it is empty, and has no start_op.
           The empty pseudo-instruction is added to the exception list.
        2. When the instruction *after* the TRY or CATCH is processed,
           it is post-processed to fill in the operation marking the
           start of the relevant section.
        3. When a CATCH is found, that marks the end of the TRY; a
           new handler is registered in the current exception.
           If it's the first CATCH, a GOTO is added, with no offset,
           and recorded as the jump_op. The offset will be updated
           when the END is found.
        4. When an END is found, that marks the end of the current
           exception. An end_op is recorded; that means this try block
           is no longer current.

    Exception blocks can be nested, so when a CATCH or END is found,
    it is recorded against the last exception in the exception list
    that has no end_op recorded.

    """
    def __init__(self):
        self.start_op = None
        self.end_op = None
        self.jump_op = None
        self.handlers = []

    def process(self, code, try_catches):
        try_catches.append(self)

    def post_process(self, code, try_catches):
        self.start_op = code[-1]


class END_TRY:
    def process(self, code, try_catches):
        # Find the most recent exception on the stack that hasn't been
        # ended. That's the block we're ending.
        for self.exception in try_catches[::-1]:
            if self.exception.end_op is None:
                break

        self.exception.handlers[-1].end_op = code[-1]

    def post_process(self, code, try_catches):
        self.exception.end_op = code[-1]


class CATCH:
    def __init__(self, descriptor):
        self.descriptor = descriptor

    # The CATCH needs to be able to pass as an opcode under initial
    # post processing
    def __len__(self):
        3

    def process(self, code, try_catches):
        # Find the most recent exception on the stack that hasn't been
        # ended. That's the block that the catch applies to.
        for self.exception in try_catches[::-1]:
            if self.exception.end_op is None:
                break

        # If this is the first catch, insert a GOTO operation.
        # The jump distance will be updated when all the CATCH blocks
        # have been processed and the exception is converted.
        # If it isn't the first catch, then this catch concludes the
        # previous one. Record the end of the block for framing purposes.
        if len(self.exception.handlers) == 0:
            self.exception.jump_op = JavaOpcodes.GOTO(0)
            code.append(self.exception.jump_op)
        else:
            self.exception.handlers[-1].end_op = code[-1]

    def post_process(self, code, try_catches):
        self.start_op = code[-1]
        self.exception.handlers.append(self)


##########################################################################
# Local variables are stored in a dictionary, keyed by name,
# and with the value of the local variable register they are stored in.
#
# When a variable is deleted, a value of None is put in as the
# value.
##########################################################################

def ALOAD_name(localvars, name):
    """Generate the opcode to load a variable with the given name onto the stack.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    i = localvars[name]
    if i is None:
        raise KeyError(name)

    if i == 0:
        return JavaOpcodes.ALOAD_0()
    elif i == 1:
        return JavaOpcodes.ALOAD_1()
    elif i == 2:
        return JavaOpcodes.ALOAD_2()
    elif i == 3:
        return JavaOpcodes.ALOAD_3()
    else:
        return JavaOpcodes.ALOAD(i)


def ASTORE_name(localvars, name):
    """Generate the opcode to store a variable with the given name.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    try:
        i = localvars[name]
        if i is None:
            localvars[name] = i
    except KeyError:
        i = len(localvars)
        localvars[name] = i

    if i == 0:
        return JavaOpcodes.ASTORE_0()
    elif i == 1:
        return JavaOpcodes.ASTORE_1()
    elif i == 2:
        return JavaOpcodes.ASTORE_2()
    elif i == 3:
        return JavaOpcodes.ASTORE_3()
    else:
        return JavaOpcodes.ASTORE(i)


def ICONST_val(value):
    """Write a constant onto the stack.

    There are a couple of opcodes that can be used to optimize the
    loading of small integers; use them if possible.
    """
    if value == 0:
        return JavaOpcodes.ICONST_0()
    elif value == 1:
        return JavaOpcodes.ICONST_1()
    elif value == 2:
        return JavaOpcodes.ICONST_2()
    elif value == 3:
        return JavaOpcodes.ICONST_3()
    elif value == 4:
        return JavaOpcodes.ICONST_4()
    elif value == 5:
        return JavaOpcodes.ICONST_5()
    elif value == -1:
        return JavaOpcodes.ICONST_M1()
    else:
        return JavaOpcodes.LDC(value)


##########################################################################
# Base classes for defining opcodes.
##########################################################################

class Opcode:
    start_block = False
    end_block = False

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
                'org/python/Object',
                self.__method__,
                '()Lorg/python/Object;'
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
                'org/python/Object',
                self.__method__,
                '(Lorg/python/Object;)Lorg/python/Object;'
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
                'org/python/Object',
                self.__method__,
                '(Lorg/python/Object;)V'
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
    end_block = True

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):
        code = []
        return code


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
            if context.is_module:
                # If this is a module-level context, also store the name
                # in the globals dictionary for the module.
                code.extend([
                    ASTORE_name(context.localvars, '#TEMP#'),
                    JavaOpcodes.GETSTATIC(context.descriptor, 'globals', 'Ljava/util/Hashtable;'),
                    JavaOpcodes.LDC(self.name),
                    ALOAD_name(context.localvars, '#TEMP#'),
                    JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
                    ALOAD_name(context.localvars, '#TEMP#'),
                ])

            code.append(ASTORE_name(context.localvars, self.name))

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

    def convert(self, context, arguments):
        code = []
        return code


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
            JavaOpcodes.INVOKESPECIAL('org/python/Object', '__setattr__', '(Ljava/lang/String;Lorg/python/Object;)V'),
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
            JavaOpcodes.NEW('org/python/Object'),
            JavaOpcodes.DUP(),
            load_op,
            JavaOpcodes.INVOKESPECIAL('org/python/Object', '<init>', prototype),
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
            code.append(ALOAD_name(context.localvars, self.name))
        except KeyError:
            # Look for global name (static variable in current class)
            # Then look for builtin.
            code.append(JavaOpcodes.GETSTATIC(context.class_descriptor, self.name, 'Lorg/python/Object;'))

        return code


class BUILD_TUPLE(Opcode):
    def __init__(self, count):
        self.count = count

    def __arg_repr__(self):
        return str(self.count)

    @property
    def consume_count(self):
        return self.count

    @property
    def product_count(self):
        return 1

    # def convert(self, context, arguments):
    #     code = []
    #     return code


class BUILD_LIST(Opcode):
    def __init__(self, count):
        self.count = count

    def __arg_repr__(self):
        return str(self.count)

    @property
    def consume_count(self):
        return self.count

    @property
    def product_count(self):
        return 1

    # def convert(self, context, arguments):
    #     code = []
    #     return code


class BUILD_SET(Opcode):
    def __init__(self, count):
        self.count = count

    def __arg_repr__(self):
        return str(self.count)

    @property
    def consume_count(self):
        return self.count

    @property
    def product_count(self):
        return 1

    # def convert(self, context, arguments):
    #     code = []
    #     return code


class BUILD_MAP(Opcode):
    def __init__(self, count):
        self.count = count

    def __arg_repr__(self):
        return str(self.count)

    @property
    def consume_count(self):
        return self.count

    @property
    def product_count(self):
        return 1

    # def convert(self, context, arguments):
    #     code = []
    #     return code


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
            JavaOpcodes.INVOKESPECIAL('org/python/Object', '__getattr__', '(Ljava/lang/String;)Lorg/python/Object;'),
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

    def convert(self, context, arguments):
        code = []
        return code


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

    def convert(self, context, arguments):
        code = []
        return code


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
    start_block = True

    def __init__(self, delta):
        self.delta = delta

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):
        code = []
        return code

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
        return [ALOAD_name(context.localvars, self.name)]


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

        code.append(ASTORE_name(context.localvars, self.name))

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
            code = [
                # Retrieve the callable from globals
                JavaOpcodes.GETSTATIC(context.descriptor, 'globals', 'Ljava/util/Hashtable;'),
                JavaOpcodes.LDC(method_name),
                JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),
                JavaOpcodes.CHECKCAST('org/python/Callable'),

                # Create an array to pass in arguments to invoke()
                ICONST_val(len(arguments) - 1),
                JavaOpcodes.ANEWARRAY('org/python/Object'),
            ]

            for i, argument in enumerate(arguments[1:]):
                code.extend([
                    JavaOpcodes.DUP(),
                    ICONST_val(i),
                ])
                code.extend(argument.operation.convert(context, argument.arguments))
                code.append(JavaOpcodes.AASTORE())

            code.extend([
                JavaOpcodes.INVOKEINTERFACE('org/python/Callable', 'invoke', '([Lorg/python/Object;)Lorg/python/Object;', 2),
            ])
        return code

        # if class:
        #     JavaOpcodes.NEW('java/lang/CLASSNAME'),
        #     JavaOpcodes.DUP(),
        #     JavaOpcodes.INVOKESPECIAL('java/lang/CLASSNAME', '<init>', '()V'),
        # elif method:
        #     JavaOpcodes.INVOKEVIRTUAL('java/lang/CLASSNAME', method_name, descriptor)
        # elif staticmethod:
        #     JavaOpcodes.INVOKESTATIC('java/lang/CLASSNAME', method_name, descriptor)


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

    def convert(self, context, arguments):
        # Add a new method definition to the context class/module
        from .method import Method, extract_parameters

        code = arguments[0].operation.const
        method_name = arguments[-1].operation.const
        method = Method(context, method_name, extract_parameters(code), static=context.is_module)
        method.extract(code)

        context.add_method(method.transpile())

        # Push a callable onto the stack so that it can be stored
        # in globals and subsequently retrieved and run.
        return [
            # Get a Method representing the new function
            TRY(),
                JavaOpcodes.LDC(Classref(context.descriptor)),
                JavaOpcodes.LDC(method_name),
                JavaOpcodes.ICONST_1(),
                JavaOpcodes.ANEWARRAY('java/lang/Class'),
                JavaOpcodes.DUP(),
                JavaOpcodes.ICONST_0(),
                JavaOpcodes.LDC(Classref('org/python/Object')),
                JavaOpcodes.AASTORE(),
                JavaOpcodes.INVOKEVIRTUAL(
                    'java/lang/Class',
                    'getMethod',
                    '(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;'
                ),
                ASTORE_name(context.localvars, '#METHOD#'),

                # Then wrap that Method into a Callable.
                JavaOpcodes.NEW('org/python/Function'),
                JavaOpcodes.DUP(),
                ALOAD_name(context.localvars, '#METHOD#'),
                JavaOpcodes.INVOKESPECIAL('org/python/Function', '<init>', '(Ljava/lang/reflect/Method;)V'),
            CATCH('java/lang/NoSuchMethodError'),
                ASTORE_name(context.localvars, '#EXCEPTION#'),
                JavaOpcodes.NEW('org/python/exceptions/RuntimeError'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC('Unable to find MAKE_FUNCTION output %s.%s' % (context.descriptor, method_name)),
                JavaOpcodes.INVOKESPECIAL('org/python/exceptions/RuntimeError', '<init>', '(Ljava/lang/String;)V'),
                JavaOpcodes.ATHROW(),
            END_TRY()
        ]


# class BUILD_SLICE(Opcode):

class MAKE_CLOSURE(Opcode):
    def __init__(self, argc):
        self.argc = argc

    def __arg_repr__(self):
        return '%s' % (self.argc)

    @property
    def consume_count(self):
        return 3 + self.argc

    @property
    def product_count(self):
        return 1


class LOAD_CLOSURE(Opcode):
    def __init__(self, i):
        self.i = i

    def __arg_repr__(self):
        return '%s' % (self.i)

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        return []

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
