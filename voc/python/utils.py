import ast
from enum import Enum
from ..java import opcodes as JavaOpcodes


class ArgType(Enum):
    POSITIONAL_OR_KEYWORD = 1
    VAR_POSITIONAL = 2
    KEYWORD_ONLY = 3
    VAR_KEYWORD = 4


class OpcodePosition(Enum):
    START = 'start_op'
    END = 'end_op'
    NEXT = 'next_op'
    YIELD = 'yield_op'


def dump(node, annotate_fields=True, include_attributes=True, indent='  '):
    """
    Return a formatted dump of the tree in *node*.  This is mainly useful for
    debugging purposes.  The returned string will show the names and the values
    for fields.  This makes the code impossible to evaluate, so if evaluation is
    wanted *annotate_fields* must be set to False.  Attributes such as line
    numbers and column offsets are not dumped by default.  If this is wanted,
    *include_attributes* can be set to True.
    """
    def _format(node, level=0):
        if isinstance(node, ast.AST):
            fields = [(a, _format(b, level)) for a, b in ast.iter_fields(node)]
            if include_attributes and node._attributes:
                fields.extend([(a, _format(getattr(node, a), level))
                               for a in node._attributes])
            return ''.join([
                node.__class__.__name__,
                '(',
                ', '.join(
                    ('%s=%s' % field for field in fields)
                    if annotate_fields else (b for a, b in fields)),
                ')'])
        elif isinstance(node, list):
            lines = ['[']
            lines.extend((indent * (level + 2) + _format(x, level + 2) + ','
                         for x in node))
            if len(lines) > 1:
                lines.append(indent * (level + 1) + ']')
            else:
                lines[-1] += ']'
            return '\n'.join(lines)
        return repr(node)

    if not isinstance(node, ast.AST):
        raise TypeError('expected AST, got %r' % node.__class__.__name__)

    return _format(node)

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
        context.next_resolve_list.append((self, OpcodePosition.START))

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
        context.add_opcodes(jump(JavaOpcodes.GOTO(0), context, loop, OpcodePosition.START))

        # The next opcode is outside the LOOP block.
        context.next_resolve_list.append((loop, OpcodePosition.NEXT))
        context.next_resolve_list.append((loop, OpcodePosition.END))

        # The end operation is virtual, so all markers point
        # to the next operation
        context.next_resolve_list.append((self, OpcodePosition.START))
        context.next_resolve_list.append((self, OpcodePosition.END))
        context.next_resolve_list.append((self, OpcodePosition.NEXT))

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
        context.next_resolve_list.append((self, OpcodePosition.START))

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

            jump(if_block.if_op, context, self, OpcodePosition.START)
        else:
            # print("    already got an endif")
            if_block.handlers[-1].jump_op = jump_op

            jump(if_block.handlers[-1].if_op, context, self, OpcodePosition.START)

        # Record the start of the elif block
        context.next_resolve_list.append((self, OpcodePosition.START))

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
            jump(if_block.if_op, context, if_block, OpcodePosition.NEXT)

        # Each of the 'end of block' jumps go to the end as well.
        if if_block.jump_op:
            jump(if_block.jump_op, context, if_block, OpcodePosition.NEXT)

        for block in if_block.elifs:
            if block.jump_op:
                jump(block.jump_op, context, if_block, OpcodePosition.NEXT)

        # The next opcode is outside the IF/ELIF/ELSE block.
        context.next_resolve_list.append((if_block, OpcodePosition.NEXT))

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
        FINALLY()
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
        # If this TRY can be identified as the start of a new
        # line of source code, track that line.
        self.starts_line = None

        # The first command covered by the try block
        self.start_op = None

        # The last command in the try block. This may be a
        # jump to the else or finally block, or past the
        # other handlers.
        self.try_end_op = None

        # The jump to the else/finally block.
        self.jump_op = None

        # The last command in the try/catch/else/finally sequence
        self.end_op = None

        # The catch handlers
        self.handlers = []

        # A handler for the finally block
        self.finally_handler = None

    def process(self, context):
        context.try_catches.append(self)
        # print("    try-catches", [(id(t), t.end_op) for t in context.try_catches])

        # The next opcode is the start of the TRY block.
        context.next_resolve_list.append((self, OpcodePosition.START))

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

        # The first command covered by the catch block
        self.start_op = None

        # The end of the catch block.
        self.end_op = None

    # def __len__(self):
    #     # The CATCH needs to be able to pass as an opcode under initial
    #     # post processing
    #     return 3

    def process(self, context):
        # Find the most recent exception on the stack that hasn't been
        # ended. That's the block that the catch applies to.
        for try_catch in context.try_catches[::-1]:
            if try_catch.end_op is None:
                break

        # print("    current try_catch", try_catch)
        # print("    try-catches", [(id(t), t.end_op) for t in context.try_catches])

        # If this is the first catch, insert a GOTO operation to
        # the ELSE block. If it's the second or later catch, GOTO
        # the FINALLY block.
        # The jump distance will be updated when all the CATCH blocks
        # have been processed and the try_catch is converted.
        end_jump = JavaOpcodes.GOTO(0)
        if len(try_catch.handlers) == 0:
            try_catch.try_end_op = end_jump
            try_catch.jump_op = end_jump
        else:
            try_catch.handlers[-1].end_op = end_jump
            try_catch.handlers[-1].jump_op = end_jump
        context.add_opcodes(
            jump(end_jump, context, try_catch, OpcodePosition.NEXT)
        )

        # Add this catch block as a handler
        try_catch.handlers.append(self)

        # The next opcode is the start of the catch block.
        context.next_resolve_list.append((self, OpcodePosition.START))

        # This opcode isn't for the final output.
        return False


class FINALLY:
    def __init__(self):
        # If this FINALLY can be identified as the start of a new
        # line of source code, track that line.
        self.starts_line = None

        # The first command covered by the finally block
        self.start_op = None

        # The last command covered by the finally
        self.end_op = None

    def process(self, context):
        # Find the most recent exception on the stack that hasn't been
        # ended. That's the block that the catch applies to.
        for try_catch in context.try_catches[::-1]:
            if try_catch.end_op is None:
                break

        # print("    current try_catch", try_catch)
        # print("    try-catches", [(id(t), t.end_op) for t in context.try_catches])

        # If there are no catches, insert a GOTO operation.
        # The jump distance will be updated when all the CATCH blocks
        # have been processed and the try_catch is converted.
        # If it isn't the first catch, then this catch concludes the
        # previous one. Add a goto to the end of the block, and
        # record the end of the block for framing purposes.
        end_jump = JavaOpcodes.GOTO(0)
        if len(try_catch.handlers) == 0:
            try_catch.try_end_op = context.opcodes[-1]
        else:
            try_catch.handlers[-1].end_op = context.opcodes[-1]

        context.add_opcodes(jump(end_jump, context, try_catch, OpcodePosition.NEXT))

        # Add this block as the finally handler
        try_catch.finally_handler = self

        # The next opcode is the start of the finally block.
        context.next_resolve_list.append((self, OpcodePosition.START))

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
            try_catch.finally_handler.end_op = context.opcodes[-1]
        elif len(try_catch.handlers) > 0:
            try_catch.handlers[-1].end_op = context.opcodes[-1]

        try_catch.end_op = context.opcodes[-1]

        # The next opcode is the end of the try-catch block.
        context.next_resolve_list.append((try_catch, OpcodePosition.NEXT))

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


def LLOAD_name(context, name):
    """Generate the opcode to load a long variable with the given name onto the stack.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    index = context.local_vars[name]

    # print("LOAD LVAR NAME", context, name, index)
    # print("locals: ", context.local_vars)

    if index == 0:
        return JavaOpcodes.LLOAD_0()
    elif index == 1:
        return JavaOpcodes.LLOAD_1()
    elif index == 2:
        return JavaOpcodes.LLOAD_2()
    elif index == 3:
        return JavaOpcodes.LLOAD_3()
    else:
        return JavaOpcodes.LLOAD(index)


def FLOAD_name(context, name):
    """Generate the opcode to load a float variable with the given name onto the stack.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    index = context.local_vars[name]

    # print("LOAD FVAR NAME", context, name, index)
    # print("locals: ", context.local_vars)

    if index == 0:
        return JavaOpcodes.FLOAD_0()
    elif index == 1:
        return JavaOpcodes.FLOAD_1()
    elif index == 2:
        return JavaOpcodes.FLOAD_2()
    elif index == 3:
        return JavaOpcodes.FLOAD_3()
    else:
        return JavaOpcodes.FLOAD(index)


def DLOAD_name(context, name):
    """Generate the opcode to load a double variable with the given name onto the stack.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    index = context.local_vars[name]

    # print("LOAD LVAR NAME", context, name, index)
    # print("locals: ", context.local_vars)

    if index == 0:
        return JavaOpcodes.DLOAD_0()
    elif index == 1:
        return JavaOpcodes.DLOAD_1()
    elif index == 2:
        return JavaOpcodes.DLOAD_2()
    elif index == 3:
        return JavaOpcodes.DLOAD_3()
    else:
        return JavaOpcodes.DLOAD(index)


def free_name(context, name, must_exist=True):
    """Remove a name from the local variable pool

    By default the variable must exist. However, if you pass
    in must_exist, the non-existence of the variable will not
    be treated as an error. This is to allow for variables that
    are created as part of looping constructs, and may not be
    created in the case of an empty loop.
    """
    try:
        index = context.local_vars[name]
        context.deleted_vars.add(index)
        del context.local_vars[name]

        # print("FREE", context, name, index)
        # print("locals: ", context.local_vars)
    except KeyError:
        if must_exist:
            raise

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
            raise RuntimeError("%s is out of integer range" % value)
    else:
        raise RuntimeError("%s is not an integer constant" % value)


def LCONST_val(value):
    """Write an long integer constant onto the stack.

    There are a couple of opcodes that can be used to optimize the
    loading of small longs; use them if possible.
    """
    if isinstance(value, int):
        if value == 0:
            return JavaOpcodes.LCONST_0()
        elif value == 1:
            return JavaOpcodes.LCONST_1()
        else:
            return JavaOpcodes.LDC2_W(value)
    else:
        raise RuntimeError("%s is not a long integer constant" % value)


def FCONST_val(value):
    """Write a float constant onto the stack.

    There are a couple of opcodes that can be used to optimize the
    loading of some floats; use them if possible.
    """
    if isinstance(value, float):
        if value == 0.0:
            return JavaOpcodes.FCONST_0()
        elif value == 1.0:
            return JavaOpcodes.FCONST_1()
        elif value == 2.0:
            return JavaOpcodes.FCONST_2()
        else:
            return JavaOpcodes.LDC_W(value)
    else:
        raise RuntimeError("%s is not a float constant" % value)


def DCONST_val(value):
    """Write an double constant onto the stack.

    There are a couple of opcodes that can be used to optimize the
    loading of some doubles; use them if possible.
    """
    if isinstance(value, float):
        if value == 0.0:
            return JavaOpcodes.DCONST_0()
        elif value == 1.0:
            return JavaOpcodes.DCONST_1()
        else:
            return JavaOpcodes.LDC2_W(value)
    else:
        raise RuntimeError("%s is not a double constant" % value)


def extract_parameters(function_def):
    parameters = []
    for arg in function_def.args.args:
        parameters.append({
            'name': arg.arg,
            'annotation': arg.annotation if arg.annotation else 'org/python/Object',
            'kind': ArgType.POSITIONAL_OR_KEYWORD,
        })
    if function_def.args.vararg:
        parameters.append({
            'name': function_def.args.vararg,
            'annotation': arg.annotation if arg.annotation else 'org/python/Object',
            'kind': ArgType.VAR_POSITIONAL,
        })
    for arg in function_def.args.kwonlyargs:
        parameters.append({
            'name': arg.arg,
            'annotation': arg.annotation if arg.annotation else 'org/python/Object',
            'kind': ArgType.KEYWORD_ONLY,
        })
    if function_def.args.kwarg:
        parameters.append({
            'name': function_def.args.kwarg,
            'annotation': arg.annotation if arg.annotation else 'org/python/Object',
            'kind': ArgType.VAR_KEYWORD,
        })

    return parameters


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

    @property
    def yield_op(self):
        return self.context.jump_targets[self.target].yield_op


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
    if position == OpcodePosition.START:
        opcode.jump_op = target.start_op
    elif position == OpcodePosition.END:
        opcode.jump_op = target.end_op
    elif position == OpcodePosition.NEXT:
        opcode.jump_op = target.next_op
    elif position == OpcodePosition.YIELD:
        opcode.jump_op = target.yield_op
    else:
        raise Exception("Unknown opcode position")
    # print("JUMP OP IS", opcode.jump_op)
    context.jumps.append(opcode)
    opcode.jump_op.references.append(opcode)
