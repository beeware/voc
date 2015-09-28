from ..java import opcodes as JavaOpcodes, Classref


##########################################################################
# Pseudo instructions used to flag the offset position of other
# attributes of the code, especially those depened on opcode offset.
##########################################################################

# A sentinel value to mark jumps that need to be resolved.
# This is used to differntiate from the "none" value indicating
# a currently open IF/TRY block.
RESOLVE = object()


class START_LOOP:
    """A pseudo instruction that can be used to mark the
    start of a loop (either a FOR or a WHILE)
    """
    def __init__(self):
        # The opcode that is the first in the formal LOOP block
        self.start_op = None

        # The last operation in the LOOP block
        self.end_op = None

        # If this IF can be identified as the start of a new
        # line of source code, track that line.
        self.starts_line = None

    def process(self, context):
        # Record the start of the if block
        context.next_resolve_list.append((self, 'start_op'))

        # Record this loop.
        context.blocks.append(self)

        # This opcode isn't for the final output.
        return False


class END_LOOP:
    """A no-op pseudo instruction that can be used to mark the
    end of a loop
    """
    def __init__(self):
        # The opcode that is the first in the formal IF block
        self.start_op = None

        # The last operation in the IF-ELSE block - the target for
        # all if-exiting jumps.
        self.end_op = None

        # If this IF can be identified as the start of a new
        # line of source code, track that line.
        self.starts_line = None

    def process(self, context):
        # Find the most recent if block on the stack that hasn't been
        # ended. That's the block that the elif applies to.
        for loop in context.blocks[::-1]:
            if loop.end_op is None:
                loop.end_op = RESOLVE
                break

        # A jump back to the start of the loop for another iteration
        context.add_opcodes(jump(JavaOpcodes.GOTO(0), context, loop, Opcode.START))

        # The next opcode is outside the LOOP block.
        context.next_resolve_list.append((loop, 'next_op'))
        context.next_resolve_list.append((loop, 'end_op'))

        # The end operation is virtual, so all markers point
        # to the next operation
        context.next_resolve_list.append((self, 'start_op'))
        context.next_resolve_list.append((self, 'end_op'))
        context.next_resolve_list.append((self, 'next_op'))

        # This opcode isn't for the final output.
        return False


class IF:
    """Mark the start of an if-endif block.

    This forms the first of at least two pseudo-operations. It might be
    as simple as:
        IF([], IFOPCODE)
            ...
        END_IF()

    or as complex as

        IF([
                ... # commands to prepare stack for IF opcode
            ],
            IFOPCODE
        )
            ...
        ELIF([
                ... # commands to prepare stack for next IF opcode
            ],
            IFOPCODE
        )
            ...
        ELIF([
                ... # commands to prepare stack for next IF opcode
            ],
            IFOPCODE
        )
            ...
        ELSE()
            ...
        END_IF()

    END_IF comes *after* the last operation in the relevant block;
    but IF, ELIF and ELSE come *before* the first instruction. A little
    special handling is required to account for this.

        1. When the IF is created, it is empty, and has no start_op.
           The empty pseudo-instruction is added to the blocks list.
        2. When the instruction *after* the IF, ELIF or ELSE is processed,
           it is post-processed to fill in the operation marking the
           start of the relevant section.
        3. When the first ELIF/ELSE is found, that marks the end of the IF; a
           new elif block is registered. A GOTO is added, with no offset,
           to the end of the IF block. The offset will be updated
           when the END_IF is found.
        3. When the 2+ ELIF/ELSE is found, that marks the end of the previous
           ELIF; a new elif block is registered. A GOTO is added, with no offset,
           to the end of the previous block. The offset will be updated
           when the END_IF is found.
        4. When an END_IF is found, that marks the end of the current
           IF-ELIF-ELSE block. An end_op is recorded; that means this if block
           is no longer current.

    IF-ELSE blocks can be nested, so when an ELIF, ELSE or END_IF is found,
    it is recorded against the last IF in the blocks list
    that has no end_op recorded.

    """
    def __init__(self, commands, opcode):
        # The commands to prepare the stack for the IF comparison
        self.commands = commands if commands is not None else []
        # print("CREATE IF", id(self), opcode)

        # The opcode class to instantiate
        self.opcode = opcode

        # The opcode that is the first in the formal IF block
        self.start_op = None

        # The instantiated opcode for the comparison
        self.if_op = None

        # The list of all ELSE blocks associated with this IF
        self.elifs = []

        # The jump operation at the end of the IF, jumping to the
        # end of the IF-ELSE block.
        self.jump_op = None

        # The last operation in the IF-ELSE block - the target for
        # all if-exiting jumps.
        self.end_op = None

        # If this IF can be identified as the start of a new
        # line of source code, track that line.
        self.starts_line = None

    def process(self, context):
        # Record the start of the if block
        context.next_resolve_list.append((self, 'start_op'))

        # Add the stack prepration commands to the code list
        context.add_opcodes(*self.commands)

        # Create an instance of the opcode and put it on the code list
        self.if_op = self.opcode(0)
        context.add_opcodes(self.if_op)

        # Record this IF.
        context.blocks.append(self)

        # This opcode isn't for the final output.
        return False


class ELIF:
    def __init__(self, commands, opcode):
        # The master IF block
        self.if_block = None

        # The commands to prepare the stack for the IF comparison
        self.commands = commands if commands is not None else []

        # The opcode class to instantiate
        self.opcode = opcode

        # The instantiated opcode for the comparison
        self.elif_op = None

        # The jump operation at the end of the ELIF, jumping to the
        # end of the IF-ELSE block.
        self.jump_op = None

        # If this ELIF can be identified as the start of a new
        # line of source code, track that line.
        self.starts_line = None

    def process(self, context):
        # Find the most recent if block on the stack that hasn't been
        # ended. That's the block that the elif applies to.
        for if_block in context.blocks[::-1]:
            if if_block.end_op is None:
                if_block.end_op = RESOLVE
                break

        # If this is the first elif, add a GOTO and use it as the
        # jump operation at the end of the IF block. If there are
        # ELIFs, add the GOTO as the jump operation on the most
        # recent ELIF.
        jump_op = JavaOpcodes.GOTO(0)
        context.add_opcodes(jump_op)

        if len(if_block.elifs) == 0:
            if_block.jump_op = jump_op

            jump(if_block.if_op, context, self, Opcode.START)
        else:
            # print("    already got an endif")
            if_block.handlers[-1].jump_op = jump_op

            jump(if_block.handlers[-1].if_op, context, self, Opcode.START)

        # Record the start of the elif block
        context.next_resolve_list.append((self, 'start_op'))

        if self.opcode:
            # print("    this is an elif")
            # Add the stack prepration commands to the code list
            context.add_opcodes(*self.commands)

            # Create an instance of the opcode and put it on the code list
            self.if_op = self.opcode(0)
            context.add_opcodes(self.if_op)

        # else:
            # print("    this is an else")

        if_block.elifs.append(self)
        # print("IF BLOCKS: ", [(id(b), b.end_op) for b in context.blocks])

        # This opcode isn't for the final output.
        return False


class ELSE(ELIF):
    def __init__(self):
        # ELSE if an ELIF with no preparation and no comparison opcode
        super().__init__(None, None)


class END_IF:
    def __init__(self):
        # If this IF can be identified as the start of a new
        # line of source code, track that line.
        self.starts_line = None

    def process(self, context):
        # Find the most recent if block on the stack that hasn't been
        # ended. That's the block that the elif applies to.
        for if_block in context.blocks[::-1]:
            if if_block.end_op is None:
                if_block.end_op = RESOLVE
                break

        # If there aren't any ELIF/ELSE definitions, then the
        # main if block jumps straight to the end.
        if len(if_block.elifs) == 0:
            jump(if_block.if_op, context, if_block, Opcode.NEXT)

        # Each of the 'end of block' jumps go to the end as well.
        if if_block.jump_op:
            jump(if_block.jump_op, context, if_block, Opcode.NEXT)

        for block in if_block.elifs:
            if block.jump_op:
                jump(block.jump_op, context, if_block, Opcode.NEXT)

        # The next opcode is outside the IF/ELIF/ELSE block.
        context.next_resolve_list.append((if_block, 'next_op'))

        # This opcode isn't for the final output.
        return False


class TRY:
    """Mark the start of a try-catch block.

    This forms the first of at least three pseudo-operations:
        TRY()
            ...
        CATCH(['your/exception/descriptor1', 'your/exception/descriptor2'])
            ...
        CATCH('your/other/exception')
            ...
        CATCH()
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
    def __init__(self, else_block=None, finally_block=None):
        # The first command covered by the try block
        self.start_op = None

        # The last command covered by the try
        self.try_end_op = None

        # The jump at the end of the try block, after any
        # else and finally processing
        self.jump_op = None

        # The last command in the try/catch/else sequence
        self.end_op = None
        self.handlers = []

        # The commands for the "else" block
        self.else_block = else_block

        # The commands for the "finally" block
        self.finally_block = finally_block

        # A handler for the finally block
        self.finally_handler = None

        # If this TRY can be identified as the start of a new
        # line of source code, track that line.
        self.starts_line = None

    def process(self, context):
        context.try_catches.append(self)
        # print("    try-catches", [(id(t), t.end_op) for t in context.try_catches])

        # The next opcode is the start of the TRY block.
        context.next_resolve_list.append((self, 'start_op'))

        # This opcode isn't for the final output.
        return False


class CATCH:
    def __init__(self, descriptors=None):
        if descriptors is None:
            self.descriptors = []
        elif isinstance(descriptors, str):
            self.descriptors = [descriptors]
        else:
            self.descriptors = descriptors

        # If this CATCH can be identified as the start of a new
        # line of source code, track that line.
        self.starts_line = None

        # The last command covered by the catch
        self.catch_end_op = None

        # The jump at the end of the catch block, after any
        # finally processing
        self.jump_op = None

    def __len__(self):
        # The CATCH needs to be able to pass as an opcode under initial
        # post processing
        return 3

    def process(self, context):
        # Find the most recent exception on the stack that hasn't been
        # ended. That's the block that the catch applies to.
        for try_catch in context.try_catches[::-1]:
            if try_catch.end_op is None:
                break

        # print("    current try_catch", try_catch)
        # print("    try-catches", [(id(t), t.end_op) for t in context.try_catches])

        # If this is the first catch, insert a GOTO operation.
        # The jump distance will be updated when all the CATCH blocks
        # have been processed and the try_catch is converted.
        # If it isn't the first catch, then this catch concludes the
        # previous one. Add a goto to the end of the block, and
        # record the end of the block for framing purposes.
        end_jump = JavaOpcodes.GOTO(0)
        if len(try_catch.handlers) == 0:
            if try_catch.else_block or try_catch.finally_block:
                context.next_resolve_list.append((try_catch, 'try_end_op'))
            else:
                try_catch.try_end_op = end_jump

            if try_catch.else_block:
                for command in try_catch.else_block.commands:
                    command.transpile(context)

            if try_catch.finally_block:
                for command in try_catch.finally_block.commands:
                    command.transpile(context)

            try_catch.jump_op = end_jump
        else:
            if try_catch.else_block or try_catch.finally_block:
                context.next_resolve_list.append((try_catch.handlers[-1], 'catch_end_op'))
            else:
                try_catch.handlers[-1].catch_end_op = end_jump

            if try_catch.finally_block:
                for command in try_catch.finally_block.commands:
                    command.transpile(context)

            try_catch.handlers[-1].jump_op = end_jump
            try_catch.handlers[-1].end_op = context.code[-1]

        context.add_opcodes(end_jump)
        jump(end_jump, context, try_catch, Opcode.NEXT)

        # Add this catch block as a handler
        try_catch.handlers.append(self)

        # The next opcode is the start of the catch block.
        context.next_resolve_list.append((self, 'start_op'))

        # This opcode isn't for the final output.
        return False


class FINALLY:
    def __init__(self):
        # If this FINALLY can be identified as the start of a new
        # line of source code, track that line.
        self.starts_line = None

        # The last command covered by the finally
        self.end_op = None

    def __len__(self):
        # The FINALLY needs to be able to pass as an opcode under initial
        # post processing
        return 3

    def process(self, context):
        # Find the most recent exception on the stack that hasn't been
        # ended. That's the block that the catch applies to.
        for try_catch in context.try_catches[::-1]:
            if try_catch.end_op is None:
                break

        # print("    current try_catch", try_catch)
        # print("    try-catches", [(id(t), t.end_op) for t in context.try_catches])

        # If this is the first catch, insert a GOTO operation.
        # The jump distance will be updated when all the CATCH blocks
        # have been processed and the try_catch is converted.
        # If it isn't the first catch, then this catch concludes the
        # previous one. Add a goto to the end of the block, and
        # record the end of the block for framing purposes.
        end_jump = JavaOpcodes.GOTO(0)
        if len(try_catch.handlers) == 0:
            if try_catch.else_block or try_catch.finally_block:
                context.next_resolve_list.append((try_catch, 'try_end_op'))
            else:
                try_catch.try_end_op = end_jump

            if try_catch.else_block:
                for command in try_catch.else_block.commands:
                    command.transpile(context)

            if try_catch.finally_block:
                for command in try_catch.finally_block.commands:
                    command.transpile(context)

            try_catch.jump_op = end_jump
        else:
            if try_catch.else_block or try_catch.finally_block:
                context.next_resolve_list.append((try_catch.handlers[-1], 'catch_end_op'))
            else:
                try_catch.handlers[-1].catch_end_op = end_jump

            if try_catch.finally_block:
                for command in try_catch.finally_block.commands:
                    command.transpile(context)

            try_catch.handlers[-1].jump_op = end_jump
            try_catch.handlers[-1].end_op = context.code[-1]

        context.add_opcodes(end_jump)
        jump(end_jump, context, try_catch, Opcode.NEXT)

        # Add this catch block as a handler
        try_catch.finally_handler = self

        # The next opcode is the start of the finally block.
        context.next_resolve_list.append((self, 'start_op'))

        # This opcode isn't for the final output.
        return False


class END_TRY:
    def __init__(self):
        # If this END TRY can be identified as the start of a new
        # line of source code, track that line.
        self.starts_line = None

    def process(self, context):
        # Find the most recent exception on the stack that hasn't been
        # ended. That's the block we're ending.
        for try_catch in context.try_catches[::-1]:
            if try_catch.end_op is None:
                try_catch.end_op = RESOLVE
                break

        # print("    current try_catch", try_catch)
        # print("    try-catches", [(id(t), t.end_op) for t in context.try_catches])

        if try_catch.finally_handler:
            try_catch.finally_handler.end_op = context.code[-1]
        elif len(try_catch.handlers) > 0:
            try_catch.handlers[-1].end_op = context.code[-1]

        try_catch.end_op = context.code[-1]

        # The next opcode is the end of the try-catch block.
        context.next_resolve_list.append((try_catch, 'next_op'))

        # This opcode isn't for the final output.
        return False


##########################################################################
# Local variables are stored in a dictionary, keyed by name,
# and with the value of the local variable register they are stored in.
#
# When a variable is deleted, a value of None is put in as the
# value.
##########################################################################

# A marker for deleted variable names.
DELETED = object()


def ALOAD_name(context, name):
    """Generate the opcode to load a variable with the given name onto the stack.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    i = context.localvars[name]
    if i == DELETED:
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


def ASTORE_name(context, name):
    """Generate the opcode to store a variable with the given name.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    try:
        i = context.localvars[name]
        if i == DELETED:
            context.localvars[name] = i
    except KeyError:
        i = len(context.localvars)
        context.localvars[name] = i

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


def ADELETE_name(context, name):
    """Remove a name from the localvar pool
    """
    try:
        value = context.localvars[name]
        if value == DELETED:
            raise KeyError("Local variable '%s' already deleted" % name)
        context.localvars[name] = DELETED
    except KeyError:
        raise


def ICONST_val(value):
    """Write an integer constant onto the stack.

    There are a couple of opcodes that can be used to optimize the
    loading of small integers; use them if possible.
    """
    if isinstance(value, bool):
        if value:
            return JavaOpcodes.ICONST_1()
        else:
            return JavaOpcodes.ICONST_0()
    elif isinstance(value, int):
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
            return JavaOpcodes.SIPUSH(value)
    else:
        raise RuntimeError("%s is not an integer constant" % value)


class Ref:
    """A reference to an opcode by target offset"""
    def __init__(self, context, target):
        self.context = context
        self.target = target

    def __repr__(self):
        try:
            return repr(self.context.jump_targets[self.target])
        except KeyError:
            return '<Ref: offset %s>' % self.target

    @property
    def start_op(self):
        return self.context.jump_targets[self.target].start_op

    @property
    def end_op(self):
        return self.context.jump_targets[self.target].end_op

    @property
    def next_op(self):
        return self.context.jump_targets[self.target].next_op


def jump(opcode, context, target, position):
    """Define a jump operation.

    The specific offset will be resolved once all the
    Java opcodes have been instantiated
    """
    # print("    add jump to reference %s %s %s %s..." % (opcode, id(opcode), target, position))
    context.unknown_jump_targets.setdefault(target, []).append((opcode, position))
    return opcode


def resolve_jump(opcode, context, target, position):
    """Resolve a jump target in an opcode.

    target is the Python opcode (or a Ref instance).
    When Python code is converted to Java, it will turn into
    0-N opcodes. We need to specify which one will be used
    as the Java offset:
     * START - the first Java opcode generated from this Python opcode
     * END - the last Java opcode generated from the Python opcode
     * NEXT - the next Java opcode added after this block.
    """
    # print("RESOLVE %s %s to %s %s" % (opcode, id(opcode), target, position))
    if position == Opcode.START:
        opcode.jump_op = target.start_op
    elif position == Opcode.END:
        opcode.jump_op = target.end_op
    elif position == Opcode.NEXT:
        opcode.jump_op = target.next_op
    else:
        raise Exception("Unknown opcode position")

    context.jumps.append(opcode)
    opcode.jump_op.references.append(opcode)


##########################################################################
# Base classes for defining opcodes.
##########################################################################

class Opcode:
    START = 10
    END = 20
    NEXT = 30

    def __init__(self, python_offset, starts_line, is_jump_target):
        self.python_offset = python_offset
        self.starts_line = starts_line
        self.is_jump_target = is_jump_target

    @property
    def opname(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.opname + ': ' + self.__arg_repr__()

    def __arg_repr__(self):
        return ''

    def transpile(self, context, arguments):
        # If the Python opcode marks the start of a line of code,
        # transfer that relationship to the first opcode in the
        # generated Java code.
        if self.starts_line:
            context.next_opcode_starts_line = self.starts_line

        context.next_resolve_list.append((self, 'start_op'))
        n_ops = len(context.code)

        # Actually convert the opcode. This is recursive down the Command sequence.
        self.convert(context, arguments)

        if len(context.code) == n_ops:
            context.next_resolve_list.append((self, 'end_op'))
        else:
            self.end_op = context.code[-1]
        context.next_resolve_list.append((self, 'next_op'))

        # Save the code offset for the jump operation.
        context.jump_targets[self.python_offset] = self


class UnaryOpcode(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

        context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                self.__method__,
                '()Lorg/python/Object;'
            )
        )


class BinaryOpcode(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

        context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                self.__method__,
                '(Lorg/python/Object;)Lorg/python/Object;'
            )
        )


class InplaceOpcode(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        arguments[0].operation.transpile(context, arguments[0].arguments)
        context.add_opcodes(JavaOpcodes.DUP())

        for argument in arguments[1:]:
            argument.operation.transpile(context, argument.arguments)

        context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                self.__method__,
                '(Lorg/python/Object;)V'
            )
        )


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
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

        # Ignore the top of the stack.
        context.add_opcodes(JavaOpcodes.POP())


class ROT_TWO(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 2

    def convert(self, context, arguments):
        context.add_opcodes(JavaOpcodes.SWAP())


# class ROT_THREE(Opcode):


class DUP_TOP(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 2

    def convert(self, context, arguments):
        context.add_opcodes(JavaOpcodes.DUP())


class DUP_TOP_TWO(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 4

    def convert(self, context, arguments):
        context.add_opcodes(JavaOpcodes.DUP2())


class NOP(Opcode):
    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):
        context.add_opcodes(JavaOpcodes.NOP())


class UNARY_POSITIVE(UnaryOpcode):
    __method__ = '__pos__'


class UNARY_NEGATIVE(UnaryOpcode):
    __method__ = '__neg__'


class UNARY_NOT(UnaryOpcode):
    __method__ = '__not__'


class UNARY_INVERT(UnaryOpcode):
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
    __method__ = '__getitem__'


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


class STORE_SUBSCR(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        # At the time STORE_SUBSCR is called, the top two elements
        # on the stack will be the number to store, and the subject of the store.
        # We need the subject to be first.
        context.add_opcodes(
            JavaOpcodes.SWAP(),
        )
        # The stack is now subject, value.
        # Compute the arguments of the store, giving the store index:
        arguments[0].operation.transpile(context, arguments[0].arguments)
        # And again, we need the order tweaked; the store index should be last.
        context.add_opcodes(
            JavaOpcodes.SWAP(),
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__setitem__', '(Lorg/python/Object;Lorg/python/Object;)V'),
        )


class DELETE_SUBSCR(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        arguments[0].operation.transpile(context, arguments[0].arguments)
        context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__delitem__', '(Lorg/python/Object;)V'),
        )


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

    def convert(self, context, arguments):

        context.add_opcodes(
            JavaOpcodes.ICONST_1(),
            JavaOpcodes.ANEWARRAY('org/python/Object'),
            JavaOpcodes.DUP(),
            JavaOpcodes.ICONST_0(),
        )

        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

        context.add_opcodes(
            JavaOpcodes.AASTORE(),

            JavaOpcodes.NEW('java/util/Hashtable'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('java/util/Hashtable', '<init>', '()V'),

            JavaOpcodes.INVOKESTATIC(
                'org/Python',
                'iter',
                '([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Iterable;'
            ),

            JavaOpcodes.CHECKCAST('org/python/Iterable'),
        )


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
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

        context.add_opcodes(JavaOpcodes.ARETURN())


# class IMPORT_STAR(Opcode):
# class YIELD_VALUE(Opcode):


class POP_BLOCK(Opcode):
    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0


class END_FINALLY(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 0


class POP_EXCEPT(Opcode):
    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):
        # print("convert POP_EXCEPT", len(arguments))
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)


class STORE_NAME(Opcode):
    def __init__(self, name, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

        # Depending on context, this might mean writing to local
        # variables, class attributes, or to the global context.
        context.store_name(self.name, arguments)


class DELETE_NAME(Opcode):
    def __init__(self, name, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.name = name

    def __arg_repr__(self):
        return str(self.name)

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

        # Depending on context, this might mean deleting from local
        # variables, class attributes, or to the global context.
        context.delete_name(self.name, arguments)


class UNPACK_SEQUENCE(Opcode):
    def __init__(self, count, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.count = count

    def __arg_repr__(self):
        return str(self.count)

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return self.count

    def convert(self, context, arguments):
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

        context.add_opcodes(
            ASTORE_name(context, '##TEMP_%d##' % id(self))
        )

        for i in range(self.count, 0, -1):
            context.add_opcodes(
                ALOAD_name(context, '##TEMP_%d##' % id(self)),
                ICONST_val(i - 1),
                JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getitem__', '(I)Lorg/python/Object;'),
            )


class FOR_ITER(Opcode):
    def __init__(self, target, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.target = target

    def __arg_repr__(self):
        return str(self.target)

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 2


# class UNPACK_EX(Opcode):


class STORE_ATTR(Opcode):
    def __init__(self, name, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
        arguments[1].operation.transpile(context, arguments[1].arguments)
        context.add_opcodes(JavaOpcodes.LDC_W(self.name))
        arguments[0].operation.transpile(context, arguments[0].arguments)

        context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__setattr__', '(Ljava/lang/String;Lorg/python/Object;)V'),
        )


# class DELETE_ATTR(Opcode):

class STORE_GLOBAL(Opcode):
    def __init__(self, name, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

        # Depending on context, this might mean writing to local
        # variables, class attributes, or to the global context.
        context.store_name(self.name, arguments, allow_locals=False)


# class DELETE_GLOBAL(Opcode):


class LOAD_CONST(Opcode):
    def __init__(self, const, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.const = const

    def __arg_repr__(self):
        return str(self.const)

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 1

    def _convert(self, context, arguments, const):
        # A None value has it's own opcode.
        # If the constant is a byte or a short, we can
        # cut a value out of the constant pool.
        if const is None:
            context.add_opcodes(JavaOpcodes.ACONST_NULL())
            return
        else:
            if isinstance(const, bool):
                context.add_opcodes(
                    JavaOpcodes.NEW('org/python/types/Bool'),
                    JavaOpcodes.DUP(),
                    ICONST_val(const),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', '(Z)V'),
                )

            elif isinstance(const, int):
                context.add_opcodes(
                    JavaOpcodes.NEW('org/python/types/Int'),
                    JavaOpcodes.DUP(),
                    ICONST_val(const),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', '(I)V'),
                )

            elif isinstance(const, float):
                context.add_opcodes(
                    JavaOpcodes.NEW('org/python/types/Float'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.LDC2_W(const),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Float', '<init>', '(D)V'),
                )

            elif isinstance(const, str):
                context.add_opcodes(
                    JavaOpcodes.NEW('org/python/types/Str'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.LDC_W(const),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),
                )

            # elif isinstance(const, bytes):
            #     context.add_opcodes(
            #         JavaOpcodes.NEW('org/python/types/Bytes'),
            #         JavaOpcodes.DUP(),
            #         JavaOpcodes.LDC_W(const),
            #         JavaOpcodes.INVOKESPECIAL('org/python/types/Bytes', '<init>', '(Ljava/lang/String;)V'),
            #     )

            elif isinstance(const, tuple):
                context.add_opcodes(
                    JavaOpcodes.NEW('org/python/types/Tuple'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.NEW('java/util/ArrayList'),
                    JavaOpcodes.DUP(),
                    ICONST_val(len(const)),
                    JavaOpcodes.INVOKESPECIAL('java/util/ArrayList', '<init>', '(I)V')
                )

                for val in const:
                    context.add_opcodes(
                        JavaOpcodes.DUP(),
                    )
                    self._convert(context, arguments, val)
                    context.add_opcodes(
                        JavaOpcodes.INVOKEVIRTUAL('java/util/ArrayList', 'add', '(Ljava/lang/Object;)Z'),
                        JavaOpcodes.POP()
                    )

                context.add_opcodes(
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Tuple', '<init>', '(Ljava/util/ArrayList;)V'),
                )

            else:
                raise RuntimeError("Unknown constant type %s" % type(const))

    def convert(self, context, arguments):
        self._convert(context, arguments, self.const)


class LOAD_NAME(Opcode):
    def __init__(self, name, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
        context.load_name(self.name)


class BUILD_TUPLE(Opcode):
    def __init__(self, count, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.count = count

    def __arg_repr__(self):
        return str(self.count)

    @property
    def consume_count(self):
        return self.count

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        context.add_opcodes(
            JavaOpcodes.NEW('org/python/types/Tuple'),
            JavaOpcodes.DUP(),

            JavaOpcodes.NEW('java/util/ArrayList'),
            JavaOpcodes.DUP(),
            ICONST_val(self.count),
            JavaOpcodes.INVOKESPECIAL('java/util/ArrayList', '<init>', '(I)V')
        )

        for argument in arguments:
            context.add_opcodes(
                JavaOpcodes.DUP(),
            )

            argument.operation.transpile(context, argument.arguments)

            context.add_opcodes(
                JavaOpcodes.INVOKEVIRTUAL('java/util/ArrayList', 'add', '(Ljava/lang/Object;)Z'),
                JavaOpcodes.POP(),
            )

        context.add_opcodes(
            JavaOpcodes.INVOKESPECIAL('org/python/types/Tuple', '<init>', '(Ljava/util/ArrayList;)V')
        )


class BUILD_LIST(Opcode):
    def __init__(self, count, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.count = count

    def __arg_repr__(self):
        return str(self.count)

    @property
    def consume_count(self):
        return self.count

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        context.add_opcodes(
            JavaOpcodes.NEW('org/python/types/List'),
            JavaOpcodes.DUP(),

            JavaOpcodes.NEW('java/util/ArrayList'),
            JavaOpcodes.DUP(),
            ICONST_val(self.count),
            JavaOpcodes.INVOKESPECIAL('java/util/ArrayList', '<init>', '(I)V')
        )

        for argument in arguments:
            context.add_opcodes(
                JavaOpcodes.DUP(),
            )

            argument.operation.transpile(context, argument.arguments)

            context.add_opcodes(
                JavaOpcodes.INVOKEVIRTUAL('java/util/ArrayList', 'add', '(Ljava/lang/Object;)Z'),
                JavaOpcodes.POP(),
            )

        context.add_opcodes(
            JavaOpcodes.INVOKESPECIAL('org/python/types/List', '<init>', '(Ljava/util/ArrayList;)V')
        )


class BUILD_SET(Opcode):
    def __init__(self, count, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
    def __init__(self, count, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
    def __init__(self, name, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
        # print("LOAD_ATTR", context, arguments)
        arguments[0].operation.transpile(context, arguments[0].arguments)
        context.add_opcodes(JavaOpcodes.LDC_W(self.name))

        context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getattr__', '(Ljava/lang/String;)Lorg/python/Object;'),
        )


class COMPARE_OP(Opcode):
    def __init__(self, comparison, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.comparison = comparison

    def __arg_repr__(self):
        return self.comparison

    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        # Add the operand which will be the left side, and thus the
        # target of the comparator operator.
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

        comparator = {
            '<': '__lt__',
            '<=': '__lte__',
            '>': '__gt__',
            '>=': '__gte__',
            '==': '__eq__',
            'exception match': '__eq__',
        }[self.comparison]

        context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', comparator, '(Lorg/python/Object;)Lorg/python/Object;')
        )


class IMPORT_NAME(Opcode):
    def __init__(self, target, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
        pass  # FIXME


class IMPORT_FROM(Opcode):
    def __init__(self, target, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.target = target

    def __arg_repr__(self):
        return str(self.target)

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        pass


class JUMP_FORWARD(Opcode):
    def __init__(self, target, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
        context.add_opcodes(
            jump(JavaOpcodes.GOTO(0), context, Ref(context, self.target), Opcode.START)
        )


# class JUMP_IF_FALSE_OR_POP(Opcode):
# class JUMP_IF_TRUE_OR_POP(Opcode):


class JUMP_ABSOLUTE(Opcode):
    def __init__(self, target, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
        context.add_opcodes(
            jump(JavaOpcodes.GOTO(0), context, Ref(context, self.target), Opcode.START)
        )


class POP_JUMP_IF_FALSE(Opcode):
    def __init__(self, target, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

        context.add_opcodes(
            # (bool) TOS.value
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__bool__', '()Lorg/python/types/Bool;'),
            JavaOpcodes.GETFIELD('org/python/types/Bool', 'value', 'Z'),

            # Jump if false
            jump(JavaOpcodes.IFEQ(0), context, Ref(context, self.target), Opcode.START)
        )


class POP_JUMP_IF_TRUE(Opcode):
    def __init__(self, target, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.target = target

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

        context.add_opcodes(
            # (bool) TOS.value
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__bool__', '()Lorg/python/types/Bool;'),
            JavaOpcodes.GETFIELD('org/python/types/Bool', 'value', 'Z'),

            # Jump if not false
            jump(JavaOpcodes.IFNE(0), context, Ref(context, self.target), Opcode.START)
        )


class LOAD_GLOBAL(Opcode):
    def __init__(self, name, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
        context.load_name(self.name, allow_locals=False)


# class CONTINUE_LOOP(Opcode):


class SETUP_LOOP(Opcode):
    def __init__(self, delta, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.delta = delta

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):
        pass


class SETUP_EXCEPT(Opcode):
    def __init__(self, delta, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.delta = delta

    def __arg_repr__(self):
        return ' %s' % self.delta

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0


class SETUP_FINALLY(Opcode):
    def __init__(self, delta, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.delta = delta

    def __arg_repr__(self):
        return ' %s' % self.delta

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0


class LOAD_FAST(Opcode):
    def __init__(self, name, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
        context.add_opcodes(ALOAD_name(context, self.name))


class STORE_FAST(Opcode):
    def __init__(self, name, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

        context.add_opcodes(ASTORE_name(context, self.name))


# class DELETE_FAST(Opcode):


# class RAISE_VARARGS(Opcode):


class CALL_FUNCTION(Opcode):
    def __init__(self, argc, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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

        if arguments[0].operation.opname == 'LOAD_BUILD_CLASS':
            # Construct a class.
            from .klass import Class

            code = arguments[1].arguments[0].operation.const
            class_name = arguments[1].arguments[1].operation.const
            if len(arguments) == 4:
                super_name = arguments[2].operation.const
            else:
                super_name = None

            klass = Class(context.parent, class_name, super_name=super_name)
            klass.extract(code)
            context.parent.classes.append(klass.transpile())
            # print("DESCRIPTOR", klass.descriptor)
            # Push a callable onto the stack so that it can be stored
            # in globals and subsequently retrieved and run.
            context.add_opcodes(
                # Get a Method representing the new function
                TRY(),
                    JavaOpcodes.LDC_W(Classref(klass.descriptor)),
                    JavaOpcodes.ICONST_2(),
                    JavaOpcodes.ANEWARRAY('java/lang/Class'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.ICONST_0(),
                    JavaOpcodes.LDC_W(Classref('[Lorg/python/Object;')),
                    JavaOpcodes.AASTORE(),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.ICONST_1(),
                    JavaOpcodes.LDC_W(Classref('java/util/Hashtable')),
                    JavaOpcodes.AASTORE(),
                    JavaOpcodes.INVOKEVIRTUAL(
                        'java/lang/Class',
                        'getConstructor',
                        '([Ljava/lang/Class;)Ljava/lang/reflect/Constructor;'
                    ),
                    ASTORE_name(context, '#CONSTRUCTOR#'),

                    # # Then wrap that Constructor into a Callable.
                    JavaOpcodes.NEW('org/python/types/Constructor'),
                    JavaOpcodes.DUP(),
                    ALOAD_name(context, '#CONSTRUCTOR#'),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Constructor', '<init>', '(Ljava/lang/reflect/Constructor;)V'),

                CATCH('java/lang/NoSuchMethodError'),
                    ASTORE_name(context, '#EXCEPTION#'),
                    JavaOpcodes.NEW('org/python/exceptions/RuntimeError'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.LDC_W('Unable to find class %s' % (klass.descriptor)),
                    JavaOpcodes.INVOKESPECIAL('org/python/exceptions/RuntimeError', '<init>', '(Ljava/lang/String;)V'),
                    JavaOpcodes.ATHROW(),
                END_TRY()
            )

        else:
            if arguments[0].operation.opname == 'MAKE_FUNCTION':
                # If this is an comprehension, the line of code
                # defining the inline function will be associated with the
                # class that is created; pull out that line of code and
                # associate it with the use of the function, too.
                context.next_opcode_starts_line = arguments[0].arguments[0].operation.starts_line

            # Retrive the function
            arguments[0].operation.transpile(context, arguments[0].arguments)

            context.add_opcodes(
                JavaOpcodes.CHECKCAST('org/python/Callable'),
            )

            final_args = self.args
            first_arg = 0

            # If the function has been retrived using LOAD_ATTR, that means
            # it's an instance method. We need to pass the instance itself
            # as the first argument, so make space for that.
            # If MAKE_FUNCTION was used, that means it's an inline function
            # definition - the result of a comprehension.
            if arguments[0].operation.opname == 'LOAD_ATTR':
                final_args += 1
                first_arg = 1
            elif arguments[0].operation.opname == 'MAKE_FUNCTION':
                final_args += 1
                first_arg = 1
                context.add_opcodes(
                    ASTORE_name(context, '##comprehension##'),
                    ALOAD_name(context, '##comprehension##')
                )

            context.add_opcodes(
                # Create an array to pass in arguments to invoke()
                ICONST_val(final_args),
                JavaOpcodes.ANEWARRAY('org/python/Object'),
            )

            # If it's an instance method, put the instance at the start of
            # the argument list.
            if arguments[0].operation.opname == 'LOAD_ATTR':
                context.add_opcodes(
                    JavaOpcodes.DUP(),
                    ICONST_val(0),
                )
                arguments[0].arguments[0].operation.transpile(context, arguments[0].arguments[0].arguments)
                context.add_opcodes(JavaOpcodes.AASTORE())
            elif arguments[0].operation.opname == 'MAKE_FUNCTION':
                context.add_opcodes(
                    JavaOpcodes.DUP(),
                    ICONST_val(0),
                )

                context.add_opcodes(
                    ALOAD_name(context, '##comprehension##'),
                    JavaOpcodes.AASTORE()
                )

            # Push all the arguments into an array
            for i, argument in enumerate(arguments[1:self.args+1]):
                context.add_opcodes(
                    JavaOpcodes.DUP(),
                    ICONST_val(first_arg + i),
                )
                argument.operation.transpile(context, argument.arguments)
                context.add_opcodes(JavaOpcodes.AASTORE())

            # Create a Hashtable, and push all the kwargs into it.
            context.add_opcodes(
                JavaOpcodes.NEW('java/util/Hashtable'),
                JavaOpcodes.DUP(),
                JavaOpcodes.INVOKESPECIAL('java/util/Hashtable', '<init>', '()V')
            )

            for name, argument in zip(arguments[self.args+1::2], arguments[self.args+2::2]):
                context.add_opcodes(
                    JavaOpcodes.DUP(),
                    JavaOpcodes.LDC_W(name),
                )
                argument.operation.transpile(context, argument.arguments)
                context.add_opcodes(
                    JavaOpcodes.INVOKEVIRTUAL('java/util/Hashtable', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
                    JavaOpcodes.POP()
                )

            context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE('org/python/Callable', 'invoke', '([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;'),
            )
        return code


class MAKE_FUNCTION(Opcode):
    def __init__(self, argc, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.argc = argc
        self.default_args = argc & 0xff
        self.default_kwargs = ((argc >> 8) & 0xFF)
        self.annotations = (argc >> 16) & 0x7FFF

    def __arg_repr__(self):
        return '%d %s default args, %s default kwargs, %s annotations' % (
            self.argc,
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
        code = arguments[-2].operation.const
        full_method_name = arguments[-1].operation.const

        method = context.add_method(full_method_name, code)

        if method.is_constructor:
            pass
            # Nothing needed on stack; class construction is self contained.
        elif method.is_closuremethod:
            context.add_opcodes(
                JavaOpcodes.NEW(method.callable),
                JavaOpcodes.DUP(),
                JavaOpcodes.INVOKESPECIAL(method.callable, '<init>', '()V'),
            )
        else:
            # Push a callable onto the stack so that it can be stored
            # in globals and subsequently retrieved and run.
            context.add_opcodes(
                # Get a Method representing the new function
                TRY(),
                    JavaOpcodes.LDC_W(Classref(context.descriptor)),
                    JavaOpcodes.LDC_W(method.name),
                    JavaOpcodes.ICONST_2(),
                    JavaOpcodes.ANEWARRAY('java/lang/Class'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.ICONST_0(),
                    JavaOpcodes.LDC_W(Classref('[Lorg/python/Object;')),
                    JavaOpcodes.AASTORE(),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.ICONST_1(),
                    JavaOpcodes.LDC_W(Classref('java/util/Hashtable')),
                    JavaOpcodes.AASTORE(),
                    JavaOpcodes.INVOKEVIRTUAL(
                        'java/lang/Class',
                        'getMethod',
                        '(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;'
                    ),
                    ASTORE_name(context, '#METHOD#'),

                    # Then wrap that Method into a Callable.
                    JavaOpcodes.NEW(method.callable),
                    JavaOpcodes.DUP(),
                    ALOAD_name(context, '#METHOD#'),
                    ICONST_val(method.static),
                    JavaOpcodes.INVOKESPECIAL(method.callable, '<init>', '(Ljava/lang/reflect/Method;Z)V'),
                CATCH('java/lang/NoSuchMethodError'),
                    ASTORE_name(context, '#EXCEPTION#'),
                    JavaOpcodes.NEW('org/python/exceptions/RuntimeError'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.LDC_W('Unable to find MAKE_FUNCTION output %s.%s' % (context.module.descriptor, full_method_name)),
                    JavaOpcodes.INVOKESPECIAL('org/python/exceptions/RuntimeError', '<init>', '(Ljava/lang/String;)V'),
                    JavaOpcodes.ATHROW(),
                END_TRY()
            )


class BUILD_SLICE(Opcode):
    def __init__(self, argc, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.argc = argc

    def __arg_repr__(self):
        return '%s' % (self.argc)

    @property
    def consume_count(self):
        return self.argc

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)


class MAKE_CLOSURE(Opcode):
    def __init__(self, argc, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
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
    def __init__(self, i, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.i = i

    def __arg_repr__(self):
        return '%s' % (self.i)

    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 1

    # def convert(self, context, arguments):
    #     return []

# class LOAD_DEREF(Opcode):
# class STORE_DEREF(Opcode):
# class DELETE_DEREF(Opcode):

# class CALL_FUNCTION_KW(Opcode):
# class CALL_FUNCTION_VAR_KW(Opcode):

# class SETUP_WITH(Opcode):


class LIST_APPEND(Opcode):
    def __init__(self, index, python_offset, starts_line, is_jump_target):
        super().__init__(python_offset, starts_line, is_jump_target)
        self.index = index

    def __arg_repr__(self):
        return str(self.index)

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0

    def convert(self, context, arguments):

        if self.index == 2:
            context.add_opcodes(
                JavaOpcodes.GETFIELD('org/python/types/List', 'value', 'Ljava/util/ArrayList;'),
            )

            for argument in arguments:
                argument.operation.transpile(context, argument.arguments)

            context.add_opcodes(
                JavaOpcodes.INVOKEVIRTUAL('java/util/ArrayList', 'add', '(Ljava/lang/Object;)Z'),
                JavaOpcodes.POP(),
            )
        else:
            raise RuntimeError("Don't know how to handle LIST_APPEND at index %d" % self.index)

        # for i in range(1, self.index):
        #     context.add_opcodes(
        #         ASTORE_name(context, '##temp-%s-%s##' % (id(self), i))
        #     )

        # context.add_opcodes(
        #     JavaOpcodes.DUP(),
        # )

        # for argument in arguments:
        #     argument.operation.transpile(context, argument.arguments)

        # context.add_opcodes(
        #     JavaOpcodes.INVOKEVIRTUAL('java/util/ArrayList', 'add', '(Ljava/util/ArrayList;)Z'),
        #     JavaOpcodes.POP(),
        # )

        # for i in range(self.index, 1, -1):
        #     context.add_opcodes(
        #         ALOAD_name(context, '##temp-%s-%s##' % (id(self), i - 1))
        #     )

# class SET_ADD(Opcode):
# class MAP_ADD(Opcode):

# class LOAD_CLASSDEREF(Opcode):
