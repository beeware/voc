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
        context.loops.append(self)

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
        for loop in context.loops[::-1]:
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
# If an attempt is used to use a name that has been deleted, an exception
# is raised.
#
# Once a name has been deleted, the index will be recycled for re-use
# as a different name.
##########################################################################

def ALOAD_name(context, name):
    """Generate the opcode to load an object variable with the given name onto the stack.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    index = context.local_vars[name]

    # print("LOAD AVAR NAME", context, name, index)
    # print("locals: ", context.local_vars)

    if index == 0:
        return JavaOpcodes.ALOAD_0()
    elif index == 1:
        return JavaOpcodes.ALOAD_1()
    elif index == 2:
        return JavaOpcodes.ALOAD_2()
    elif index == 3:
        return JavaOpcodes.ALOAD_3()
    else:
        return JavaOpcodes.ALOAD(index)


def ASTORE_name(context, name):
    """Generate the opcode to store an object variable with the given name.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    try:
        index = context.local_vars[name]
    except KeyError:
        try:
            index = context.deleted_vars.pop()
            # print ("REUSE index", index)
        except KeyError:
            index = len(context.local_vars)
            # print ("GET NEW index", index)
        context.local_vars[name] = index

    # print("STORE AVAR NAME", context, index, name)
    # print("locals: ", context.local_vars)

    if index == 0:
        return JavaOpcodes.ASTORE_0()
    elif index == 1:
        return JavaOpcodes.ASTORE_1()
    elif index == 2:
        return JavaOpcodes.ASTORE_2()
    elif index == 3:
        return JavaOpcodes.ASTORE_3()
    else:
        return JavaOpcodes.ASTORE(index)


def ILOAD_name(context, name):
    """Generate the opcode to load an integer variable with the given name onto the stack.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    index = context.local_vars[name]

    # print("LOAD IVAR NAME", context, name, index)
    # print("locals: ", context.local_vars)

    if index == 0:
        return JavaOpcodes.ILOAD_0()
    elif index == 1:
        return JavaOpcodes.ILOAD_1()
    elif index == 2:
        return JavaOpcodes.ILOAD_2()
    elif index == 3:
        return JavaOpcodes.ILOAD_3()
    else:
        return JavaOpcodes.ILOAD(index)


def ISTORE_name(context, name):
    """Generate the opcode to store a variable with the given name.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    try:
        index = context.local_vars[name]
    except KeyError:
        try:
            index = context.deleted_vars.pop()
            # print ("REUSE index", index)
        except KeyError:
            index = len(context.local_vars)
            # print ("GET NEW index", index)
        context.local_vars[name] = index

    # print("STORE IVAR NAME", context, index, name)
    # print("locals: ", context.local_vars)

    if index == 0:
        return JavaOpcodes.ISTORE_0()
    elif index == 1:
        return JavaOpcodes.ISTORE_1()
    elif index == 2:
        return JavaOpcodes.ISTORE_2()
    elif index == 3:
        return JavaOpcodes.ISTORE_3()
    else:
        return JavaOpcodes.ISTORE(index)


def IINC_name(context, name, value):
    """Generate the opcode to increment an integer variable with the given name
    by the provided value.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    index = context.local_vars[name]

    return JavaOpcodes.IINC(index, value)


def free_name(context, name):
    """Remove a name from the local variable pool
    """
    index = context.local_vars[name]
    context.deleted_vars.add(index)
    del context.local_vars[name]

    # print("FREE", context, name, index)

    # print("locals: ", context.local_vars)


##########################################################################
# Handle constant values.
#
# There are multiple opcodes to load and retrieve constants. Use the
# best option available at any given time.
##########################################################################

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
        elif -32768 <= value <= 32767:
            return JavaOpcodes.SIPUSH(value)
        elif -2147483648 <= value <= 2147483647:
            return JavaOpcodes.LDC(value)
        else:
            return JavaOpcodes.LDC_W(value)
    else:
        raise RuntimeError("%s is not an integer constant" % value)


##########################################################################
# Some opcodes need to reference other opcodes (e.g., GOTO)
#
# These helpers help define and resolve those references.
##########################################################################

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
    # print("    add jump to reference %s 0x%x %s %s..." % (opcode, id(opcode), target, position))
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
    # print("RESOLVE %s 0x%x to %s %s" % (opcode, id(opcode), target, position))
    if position == Opcode.START:
        opcode.jump_op = target.start_op
    elif position == Opcode.END:
        opcode.jump_op = target.end_op
    elif position == Opcode.NEXT:
        opcode.jump_op = target.next_op
    else:
        raise Exception("Unknown opcode position")
    # print("JUMP OP IS", opcode.jump_op)
    context.jumps.append(opcode)
    opcode.jump_op.references.append(opcode)


##########################################################################
# Base classes for defining opcodes.
##########################################################################

class Opcode:
    # A prefaced operation is one that has arguments, and
    # those arguments may be the target of a jump, but *this*
    # opcode needs to issue commands before the arguments
    # are processed - which means that if the argument is
    # a jump target, the Java target offset needs to be
    # adjusted. The value of prefaced is the argument index
    # that needs to be prefaced.
    prefaced = None

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

    def materialize(self, context, arguments):
        for argument in arguments:
            argument.operation.materialize(context, argument.arguments)

    def transpile(self, context, arguments):
        # print ("TRANSPILE", self.python_offset, self)
        # If the Python opcode marks the start of a line of code,
        # transfer that relationship to the first opcode in the
        # generated Java code.
        if self.starts_line:
            context.next_opcode_starts_line = self.starts_line

        n_ops = len(context.code)

        # Actually convert the opcode. This is recursive down the Command sequence.
        self.convert(context, arguments)

        if len(context.code) == n_ops:
            context.next_resolve_list.append((self, 'end_op'))
        else:
            self.end_op = context.code[-1]
        context.next_resolve_list.append((self, 'next_op'))

        context.jump_targets[self.jump_target(arguments)] = self

    def convert_args(self, context, arguments):
        for argument in arguments:
            argument.operation.transpile(context, argument.arguments)

    def convert(self, context, arguments):
        self.convert_args(context, arguments)
        context.next_resolve_list.append((self, 'start_op'))
        self.convert_opcode(context, arguments)

    def jump_target(self, arguments):
        # Get the code offset for the jump operation, taking
        # prefacing into account.
        try:
            arg = arguments[self.prefaced]
            target = arg.operation.jump_target(arg.arguments)
        except (TypeError, IndexError):
            target = self.python_offset
        return target


class UnaryOpcode(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 1

    def convert_opcode(self, context, arguments):
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

    def convert_opcode(self, context, arguments):
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

        context.next_resolve_list.append((self, 'start_op'))
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

    def convert_opcode(self, context, arguments):
        # Ignore the top of the stack.
        context.add_opcodes(JavaOpcodes.POP())


class ROT_TWO(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 2

    def convert_opcode(self, context, arguments):
        context.add_opcodes(JavaOpcodes.SWAP())


# class ROT_THREE(Opcode):


class DUP_TOP(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 2

    def convert_opcode(self, context, arguments):
        context.add_opcodes(JavaOpcodes.DUP())


class DUP_TOP_TWO(Opcode):
    @property
    def consume_count(self):
        return 2

    @property
    def product_count(self):
        return 4

    def convert_opcode(self, context, arguments):
        context.add_opcodes(JavaOpcodes.DUP2())


class NOP(Opcode):
    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0

    def convert_opcode(self, context, arguments):
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
    prefaced = 0

    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 1

    def convert(self, context, arguments):
        context.next_resolve_list.append((self, 'start_op'))
        # At the time STORE_SUBSCR is called, the top two elements
        # on the stack will be the value to store, and the subject
        # of the store operation.
        context.add_opcodes(
            ASTORE_name(context, '#value-%x' % id(self)),
            ASTORE_name(context, '#subject-%x' % id(self)),
        )

        # Compute the arguments of the store, giving the store index:
        arguments[0].operation.transpile(context, arguments[0].arguments)

        context.add_opcodes(
            ALOAD_name(context, '#subject-%x' % id(self)),
            JavaOpcodes.SWAP(),
            ALOAD_name(context, '#value-%x' % id(self)),
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__setitem__', '(Lorg/python/Object;Lorg/python/Object;)V'),

        )
        # Clean up
        free_name(context, '#subject-%x' % id(self))
        free_name(context, '#value-%x' % id(self))


class DELETE_SUBSCR(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 1

    def convert_opcode(self, context, arguments):
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

    def convert_opcode(self, context, arguments):
        context.add_opcodes(
            ASTORE_name(context, '#temp-%x' % id(self)),

            JavaOpcodes.ICONST_1(),
            JavaOpcodes.ANEWARRAY('org/python/Object'),
            JavaOpcodes.DUP(),
            JavaOpcodes.ICONST_0(),

            ALOAD_name(context, '#temp-%x' % id(self)),
            JavaOpcodes.AASTORE(),

            JavaOpcodes.NEW('java/util/HashMap'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('java/util/HashMap', '<init>', '()V'),

            JavaOpcodes.INVOKESTATIC(
                'org/Python',
                'iter',
                '([Lorg/python/Object;Ljava/util/Map;)Lorg/python/Iterable;'
            ),

            JavaOpcodes.CHECKCAST('org/python/Iterable'),
        )

        # Clean up temp variable
        free_name(context, '#temp-%x' % id(self)),


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


class BREAK_LOOP(Opcode):
    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0

    def convert_opcode(self, context, arguments):
        for loop in context.loops[::-1]:
            if loop.end_op is None:
                current_loop = loop
                break

        context.add_opcodes(
            jump(JavaOpcodes.GOTO(0), context, current_loop, Opcode.NEXT)
        )


# class WITH_CLEANUP(Opcode):

class RETURN_VALUE(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0

    def convert_opcode(self, context, arguments):
        context.add_opcodes(JavaOpcodes.ARETURN())


class IMPORT_STAR(Opcode):
    @property
    def consume_count(self):
        return 1

    @property
    def product_count(self):
        return 0

    def convert_opcode(self, context, arguments):
        context.add_opcodes(
            ASTORE_name(context, '##module##'),
        )

        # Find exported symbols (__all__, or everything but _)
        # Add each one to current context


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

    def convert_opcode(self, context, arguments):
        pass


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

    def convert_opcode(self, context, arguments):
        # Depending on context, this might mean writing to local
        # variables or an attributes dictionary.
        context.store_name(self.name, use_locals=True)


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

    def convert_opcode(self, context, arguments):
        # Depending on context, this might mean deleting from local
        # variables, class attributes, or the global context.
        context.delete_name(self.name, use_locals=True)


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

    def convert_opcode(self, context, arguments):
        context.add_opcodes(
            ASTORE_name(context, '#index-%x' % id(self))
        )

        for i in range(self.count, 0, -1):
            context.add_opcodes(
                ALOAD_name(context, '#index-%x' % id(self)),
                JavaOpcodes.NEW('org/python/types/Int'),
                JavaOpcodes.DUP(),
                ICONST_val(i - 1),
                JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', '(I)V'),
                JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getitem__', '(Lorg/python/Object;)Lorg/python/Object;'),
            )
        free_name(context, '#index-%x' % id(self))


# class FOR_ITER(Opcode):
#     def __init__(self, target, python_offset, starts_line, is_jump_target):
#         super().__init__(python_offset, starts_line, is_jump_target)
#         self.target = target

#     def __arg_repr__(self):
#         return str(self.target)

#     @property
#     def consume_count(self):
#         return 1

#     @property
#     def product_count(self):
#         return 2


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
        context.next_resolve_list.append((self, 'start_op'))
        arguments[1].operation.transpile(context, arguments[1].arguments)
        context.add_opcodes(
            ASTORE_name(context, '#object-%x' % id(self))
        )

        arguments[0].operation.transpile(context, arguments[0].arguments)
        context.add_opcodes(
            ASTORE_name(context, '#value-%x' % id(self)),
        )

        context.add_opcodes(
            ALOAD_name(context, '#object-%x' % id(self)),
            JavaOpcodes.LDC_W(self.name),
            ALOAD_name(context, '#value-%x' % id(self)),
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__setattr__', '(Ljava/lang/String;Lorg/python/Object;)V'),
        )
        free_name(context, '#object-%x' % id(self))
        free_name(context, '#value-%x' % id(self))


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

    def convert_opcode(self, context, arguments):
        context.store_name(self.name, use_locals=False)


class DELETE_GLOBAL(Opcode):
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

    def convert_opcode(self, context, arguments):
        context.delete_name(self.name, use_locals=False)


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
        if const is None:
            context.add_opcodes(
                JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;')
            )
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

    def convert_opcode(self, context, arguments):
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

    def convert_opcode(self, context, arguments):
        # Depending on context, this might mean loading from local
        # variables, class attributes, or the global context.
        context.load_name(self.name, use_locals=True)


class BUILD_TUPLE(Opcode):
    prefaced = 0

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
        context.next_resolve_list.append((self, 'start_op'))
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
    prefaced = 0

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
        context.next_resolve_list.append((self, 'start_op'))
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

    # def convert_opcode(self, context, arguments):
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

    # def convert_opcode(self, context, arguments):
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
        context.next_resolve_list.append((self, 'start_op'))
        arguments[0].operation.transpile(context, arguments[0].arguments)
        context.add_opcodes(JavaOpcodes.LDC_W(self.name))

        context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getattribute__', '(Ljava/lang/String;)Lorg/python/Object;'),
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
        context.next_resolve_list.append((self, 'start_op'))
        # Add the operand which will be the left side, and thus the
        # target of the comparator operator.
        const_comparison = False
        for argument in arguments:
            if argument.operation.opname == 'LOAD_CONST':
                if argument.operation.const is not None:
                    const_comparison = True
            argument.operation.transpile(context, argument.arguments)

        if self.comparison == 'is not' and not const_comparison:
            context.add_opcodes(
                IF([], JavaOpcodes.IF_ACMPEQ),
                    JavaOpcodes.NEW('org/python/types/Bool'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.ICONST_1(),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', '(Z)V'),
                ELSE(),
                    JavaOpcodes.NEW('org/python/types/Bool'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.ICONST_0(),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', '(Z)V'),
                END_IF(),
            )
        elif self.comparison == 'is' and not const_comparison:
            context.add_opcodes(
                IF([], JavaOpcodes.IF_ACMPNE),
                    JavaOpcodes.NEW('org/python/types/Bool'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.ICONST_1(),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', '(Z)V'),
                ELSE(),
                    JavaOpcodes.NEW('org/python/types/Bool'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.ICONST_0(),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', '(Z)V'),
                END_IF(),
            )
        else:
            comparator = {
                '<': '__lt__',
                '<=': '__le__',
                '>': '__gt__',
                '>=': '__ge__',
                '==': '__eq__',
                '!=': '__ne__',
                'is': '__eq__',
                'is not': '__ne__',
                'exception match': '__eq__',
            }[self.comparison]

            context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE('org/python/Object', comparator, '(Lorg/python/Object;)Lorg/python/Object;')
            )


class IMPORT_NAME(Opcode):
    prefaced = 0

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
        return 1

    def convert(self, context, arguments):
        # Arg 0 is the level
        # Arg 1 is the list of symbols to import.
        # Ignore Arg 1 for the moment...

        # The line of code for the import is recorded
        # against the first argument.
        context.next_opcode_starts_line = arguments[0].operation.starts_line
        context.next_resolve_list.append((self, 'start_op'))

        context.add_opcodes(
            JavaOpcodes.LDC_W(self.name),
            ICONST_val(arguments[0].operation.const),

            JavaOpcodes.INVOKESTATIC('org/python/ImportLib', '__import__', '(Ljava/lang/String;I)Lorg/python/types/Module;')
        )


class IMPORT_FROM(Opcode):
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
        return 2

    def convert_opcode(self, context, arguments):
        # Add the operand which will be the left side, and thus the
        # target of the comparator operator.
        context.add_opcodes(
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(self.name),
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getattribute__', '(Ljava/lang/String;)Lorg/python/Object;'),
        )


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

    def convert_opcode(self, context, arguments):
        context.add_opcodes(
            jump(JavaOpcodes.GOTO(0), context, Ref(context, self.target), Opcode.START)
        )


class JUMP_IF_FALSE_OR_POP(Opcode):
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

    def convert_opcode(self, context, arguments):
        context.add_opcodes(
            IF([
                    JavaOpcodes.DUP(),
                    JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__bool__', '()Lorg/python/types/Bool;'),
                    JavaOpcodes.GETFIELD('org/python/types/Bool', 'value', 'Z'),
                    ], JavaOpcodes.IFNE),
                jump(JavaOpcodes.GOTO(0), context, Ref(context, self.target), Opcode.START),
            ELSE(),
                JavaOpcodes.POP(),
            END_IF(),
        )


class JUMP_IF_TRUE_OR_POP(Opcode):
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

    def convert_opcode(self, context, arguments):
        context.add_opcodes(
            IF([
                    JavaOpcodes.DUP(),
                    JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__bool__', '()Lorg/python/types/Bool;'),
                    JavaOpcodes.GETFIELD('org/python/types/Bool', 'value', 'Z'),
                    ], JavaOpcodes.IFEQ),
                jump(JavaOpcodes.GOTO(0), context, Ref(context, self.target), Opcode.START),
            ELSE(),
                JavaOpcodes.POP(),
            END_IF(),
        )


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

    def convert_opcode(self, context, arguments):
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

    def convert_opcode(self, context, arguments):
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

    def convert_opcode(self, context, arguments):
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

    def convert_opcode(self, context, arguments):
        context.load_name(self.name, use_locals=False)


class CONTINUE_LOOP(Opcode):
    @property
    def consume_count(self):
        return 0

    @property
    def product_count(self):
        return 0

    def convert_opcode(self, context, arguments):
        for loop in context.loops[::-1]:
            if loop.end_op is None:
                current_loop = loop
                break

        context.add_opcodes(
            jump(JavaOpcodes.GOTO(0), context, Ref(context, current_loop), Opcode.START)
        )


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

    def convert_opcode(self, context, arguments):
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

    def convert_opcode(self, context, arguments):
        try:
            context.add_opcodes(ALOAD_name(context, self.name))
        except KeyError:
            context.add_opcodes(
                JavaOpcodes.NEW('org/python/exceptions/UnboundLocalError'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W(self.name),
                JavaOpcodes.INVOKESPECIAL('org/python/exceptions/UnboundLocalError', '<init>', '(Ljava/lang/String;)V'),
                JavaOpcodes.ATHROW()
            )


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

    def convert_opcode(self, context, arguments):
        context.add_opcodes(ASTORE_name(context, self.name))


class DELETE_FAST(Opcode):
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

    def convert_opcode(self, context, arguments):
        free_name(self.name)


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

    def materialize(self, context, arguments):
        if arguments[0].operation.opname == 'LOAD_BUILD_CLASS':
            # Construct a class.
            from .klass import Class
            code = arguments[1].arguments[0].operation.const
            class_name = arguments[1].arguments[1].operation.const
            if len(arguments) == 4:
                super_name = arguments[2].operation.const
            else:
                super_name = None

            self.klass = Class(context.parent, class_name, super_name=super_name)
            self.klass.extract(code)
            context.parent.classes.append(self.klass)
        else:
            if arguments[0].operation.opname == 'MAKE_FUNCTION':
                arguments[0].operation.materialize(context, arguments[0].arguments)

            for i, argument in enumerate(arguments[1:self.args+1]):
                argument.operation.materialize(context, argument.arguments)

            for i, (name, argument) in enumerate(zip(arguments[self.args+1::2], arguments[self.args+2::2])):
                argument.operation.materialize(context, argument.arguments)

    def convert(self, context, arguments):
        context.next_resolve_list.append((self, 'start_op'))
        if arguments[0].operation.opname == 'LOAD_BUILD_CLASS':
            # print("DESCRIPTOR", klass.descriptor)
            # Push a callable onto the stack so that it can be stored
            # in globals and subsequently retrieved and run.
            context.add_opcodes(
                # Get a Method representing the new function
                TRY(),
                    JavaOpcodes.LDC_W(Classref(self.klass.descriptor)),
                    JavaOpcodes.ICONST_2(),
                    JavaOpcodes.ANEWARRAY('java/lang/Class'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.ICONST_0(),
                    JavaOpcodes.LDC_W(Classref('[Lorg/python/Object;')),
                    JavaOpcodes.AASTORE(),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.ICONST_1(),
                    JavaOpcodes.LDC_W(Classref('java/util/Map')),
                    JavaOpcodes.AASTORE(),
                    JavaOpcodes.INVOKEVIRTUAL(
                        'java/lang/Class',
                        'getConstructor',
                        '([Ljava/lang/Class;)Ljava/lang/reflect/Constructor;'
                    ),
                    ASTORE_name(context, '#CONSTRUCTOR'),

                    # # Then wrap that Constructor into a Callable.
                    JavaOpcodes.NEW('org/python/types/Constructor'),
                    JavaOpcodes.DUP(),
                    ALOAD_name(context, '#CONSTRUCTOR'),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Constructor', '<init>', '(Ljava/lang/reflect/Constructor;)V'),

                CATCH('java/lang/NoSuchMethodError'),
                    ASTORE_name(context, '#EXCEPTION'),
                    JavaOpcodes.NEW('org/python/exceptions/RuntimeError'),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.LDC_W('Unable to find class %s' % (self.klass.descriptor)),
                    JavaOpcodes.INVOKESPECIAL('org/python/exceptions/RuntimeError', '<init>', '(Ljava/lang/String;)V'),
                    JavaOpcodes.ATHROW(),
                END_TRY()
            )
            free_name(context, '#CONSTRUCTOR')
            free_name(context, '#EXCEPTION')
        else:
            if arguments[0].operation.opname == 'MAKE_FUNCTION':
                # If this is an comprehension, the line of code
                # defining the inline function will be associated with the
                # class that is created; pull out that line of code and
                # associate it with the use of the function, too.
                context.next_opcode_starts_line = arguments[0].arguments[0].operation.starts_line

            # Retrive the function
            self.prefaced = 0
            arguments[0].operation.transpile(context, arguments[0].arguments)

            context.add_opcodes(
                JavaOpcodes.CHECKCAST('org/python/Callable'),
                ASTORE_name(context, '#function-%x' % id(self)),
            )

            # Evaluate all the arguments
            for i, argument in enumerate(arguments[1:self.args+1]):
                argument.operation.transpile(context, argument.arguments)
                context.add_opcodes(
                    ASTORE_name(context, '#arg-%d-%x' % (i, id(self)))
                )

            # Create and populate the array of arguments to pass to invoke()
            context.add_opcodes(
                ICONST_val(self.args),
                JavaOpcodes.ANEWARRAY('org/python/Object'),
            )
            for i, argument in enumerate(arguments[1:self.args+1]):
                context.add_opcodes(
                    JavaOpcodes.DUP(),
                    ICONST_val(i),

                    ALOAD_name(context, '#arg-%d-%x' % (i, id(self))),
                    JavaOpcodes.AASTORE(),

                )
                # Clean up temporary storage for arg.
                free_name(context, '#arg-%d-%x' % (i, id(self)))

            # Store the arguments for later.
            context.add_opcodes(
                ASTORE_name(context, '#args-%x' % id(self)),
            )

            # Evaluate all the keyword arguments
            for i, (name, argument) in enumerate(zip(arguments[self.args+1::2], arguments[self.args+2::2])):
                argument.operation.transpile(context, argument.arguments)
                context.add_opcodes(
                    ASTORE_name(context, '#kwarg-%d-%x' % (i, id(self)))
                )

            # Create and populate the map of kwargs to pass to invoke().
            context.add_opcodes(
                JavaOpcodes.NEW('java/util/HashMap'),
                JavaOpcodes.DUP(),
                JavaOpcodes.INVOKESPECIAL('java/util/HashMap', '<init>', '()V')
            )

            for i, (name, argument) in enumerate(zip(arguments[self.args+1::2], arguments[self.args+2::2])):
                context.add_opcodes(
                    JavaOpcodes.DUP(),
                    JavaOpcodes.LDC_W(name.operation.const),
                    ALOAD_name(context, '#kwarg-%d-%x' % (i, id(self))),
                    JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
                    JavaOpcodes.POP()
                )
                free_name(context, '#kwarg-%d-%x' % (i, id(self)))

            # Store the keyword arguments for later.
            context.add_opcodes(
                ASTORE_name(context, '#kwargs-%x' % id(self)),
            )

            # Set up the stack and invoke the callable
            context.add_opcodes(
                ALOAD_name(context, '#function-%x' % id(self)),
                ALOAD_name(context, '#args-%x' % id(self)),
                ALOAD_name(context, '#kwargs-%x' % id(self)),

                JavaOpcodes.INVOKEINTERFACE('org/python/Callable', 'invoke', '([Lorg/python/Object;Ljava/util/Map;)Lorg/python/Object;'),
            )

            # Clean up temporary storage.
            free_name(context, '#function-%x' % id(self))
            free_name(context, '#args-%x' % id(self))
            free_name(context, '#kwargs-%x' % id(self))


class MAKE_FUNCTION(Opcode):
    prefaced = 0

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

    def materialize(self, context, arguments):
        # Add a new method definition to the context class/module
        code = arguments[-2].operation.const
        full_method_name = arguments[-1].operation.const

        if full_method_name == '<listcomp>':
            full_method_name = 'listcomp_%x' % id(self)
        self.method = context.add_method(full_method_name, code)

    def convert(self, context, arguments):
        full_method_name = arguments[-1].operation.const
        context.next_resolve_list.append((self, 'start_op'))

        if self.method.is_constructor:
            pass
            # Nothing needed on stack; class construction is self contained.

        elif self.method.is_closuremethod:
            context.add_opcodes(
                JavaOpcodes.NEW(self.method.parent.descriptor),
                JavaOpcodes.DUP(),
                JavaOpcodes.ICONST_0(),
                JavaOpcodes.ANEWARRAY('org/python/Object'),
                JavaOpcodes.NEW('java/util/HashMap'),
                JavaOpcodes.DUP(),
                JavaOpcodes.INVOKESPECIAL('java/util/HashMap', '<init>', '()V'),
                JavaOpcodes.INVOKESPECIAL(self.method.parent.descriptor, '<init>', '([Lorg/python/Object;Ljava/util/Map;)V'),

                JavaOpcodes.LDC_W(self.method.name),
                JavaOpcodes.INVOKEVIRTUAL(self.method.parent.descriptor, '__getattribute__', '(Ljava/lang/String;)Lorg/python/Object;')
            )

            # context.add_opcodes(
            #     JavaOpcodes.NEW('java/util/HashMap'),
            #     JavaOpcodes.DUP(),
            #     JavaOpcodes.INVOKESPECIAL('java/util/Map', '<init>', '()V'),
            #     JavaOpcodes.INVOKESPECIAL('org/python/types/Function', '<init>', '([Lorg/python/Object;Ljava/util/Map;)V'),
            # )
        else:
            # Push a callable onto the stack so that it can be stored
            # in globals and subsequently retrieved and run.
            add_callable(context, self.method, full_method_name)


def add_callable(context, method, full_method_name):
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

            JavaOpcodes.LDC_W(Classref('Ljava/util/Map;')),
            JavaOpcodes.AASTORE(),
            JavaOpcodes.INVOKEVIRTUAL(
                'java/lang/Class',
                'getMethod',
                '(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;'
            ),
            ASTORE_name(context, '#method'),

            # Then wrap that Method into a Callable.
            JavaOpcodes.NEW('org/python/types/Function'),
            JavaOpcodes.DUP(),

            JavaOpcodes.NEW('org/python/types/Str'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(full_method_name),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),

            JavaOpcodes.NEW('org/python/types/Code'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Code', '<init>', '()V'),

            # org.python.types.Int co_argcount,
            # org.python.types.Tuple co_cellvars,
            # org.python.types.Bytes co_code,
            # org.python.types.Tuple co_consts,
            # org.python.types.Str co_filename,
            # org.python.types.Int co_firstlineno,
            # org.python.types.Int co_flags,
            # org.python.types.Tuple co_freevars,
            # org.python.types.Int co_kwonlyargcount,
            # org.python.types.Bytes co_lnotab,
            # org.python.types.Str co_name,
            # org.python.types.Tuple co_names,
            # org.python.types.Int co_nlocals,
            # org.python.types.Int co_stacksize,
            # org.python.types.Tuple co_varnames
            # JavaOpcodes.INVOKESPECIAL('Lorg.python.types.Code;', '<init>', '(Lorg/python/types/Int;Lorg/python/types/Tuple;Lorg/python/types/Bytes;Lorg/python/types/Tuple;Lorg/python/types/Str;Lorg/python/types/Int;Lorg/python/types/Int;Lorg/python/types/Tuple;Lorg/python/types/Int;Lorg/python/types/Bytes;Lorg/python/types/Str;Lorg/python/types/Tuple;Lorg/python/types/Int;Lorg/python/types/Int;Lorg/python/types/Tuple;)V'),

            ALOAD_name(context, '#method'),

            # globals
            # JavaOpcodes.GETSTATIC('org/python/ImportLib', 'modules', 'Ljava/util/Map;'),
            # JavaOpcodes.LDC_W(method.module.descriptor),
            # JavaOpcodes.GETSTATIC(method.module.descriptor, 'attrs', 'Ljava/util/Map;'),
            JavaOpcodes.ACONST_NULL(),  # globals

            JavaOpcodes.ACONST_NULL(),  # defaults

            JavaOpcodes.ACONST_NULL(),  # closure

            JavaOpcodes.INVOKESPECIAL('org/python/types/Function', '<init>', '(Lorg/python/types/Str;Lorg/python/types/Code;Ljava/lang/reflect/Method;Ljava/util/Map;Ljava/util/Map;Ljava/util/ArrayList;)V'),

        CATCH('java/lang/NoSuchMethodError'),
            ASTORE_name(context, '#EXCEPTION#'),
            JavaOpcodes.NEW('org/python/exceptions/RuntimeError'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W('Unable to find MAKE_FUNCTION output %s.%s' % (context.descriptor, full_method_name)),
            JavaOpcodes.INVOKESPECIAL('org/python/exceptions/RuntimeError', '<init>', '(Ljava/lang/String;)V'),
            JavaOpcodes.ATHROW(),
        END_TRY()
    )


class BUILD_SLICE(Opcode):
    prefaced = 0

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

    def convert_opcode(self, context, arguments):
        context.add_opcodes(
            JavaOpcodes.NEW('org/python/types/Slice'),
            JavaOpcodes.DUP(),
        )

        if self.argc == 1:
            method_signature = '(Lorg/python/Object;)V'
        elif self.argc == 2:
            method_signature = '(Lorg/python/Object;Lorg/python/Object;)V'
        elif self.argc == 3:
            method_signature = '(Lorg/python/Object;Lorg/python/Object;Lorg/python/Object;)V'
        else:
            raise Exception("Unknown number of slice arguments")

        context.add_opcodes(
            JavaOpcodes.INVOKESPECIAL('org/python/types/Slice', '<init>', method_signature),
        )


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

    # def convert_opcode(self, context, arguments):
    #     return []


class LOAD_DEREF(Opcode):
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

    def convert_opcode(self, context, arguments):
        pass


class STORE_DEREF(Opcode):
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

    def convert_opcode(self, context, arguments):
        pass


class DELETE_DEREF(Opcode):
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

    def convert_opcode(self, context, arguments):
        pass

# class CALL_FUNCTION_KW(Opcode):
# class CALL_FUNCTION_VAR_KW(Opcode):

# class SETUP_WITH(Opcode):


class LIST_APPEND(Opcode):
    prefaced = 0

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
        context.next_resolve_list.append((self, 'start_op'))

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

# class SET_ADD(Opcode):
# class MAP_ADD(Opcode):

# class LOAD_CLASSDEREF(Opcode):
