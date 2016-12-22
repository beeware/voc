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
        # However, if the most recent operation is a RETURN,
        # this jump isn't needed; just resolve the start position.
        if not isinstance(context.opcodes[-1], (JavaOpcodes.RETURN, JavaOpcodes.ARETURN)):
            jump_op = JavaOpcodes.GOTO(0)
            context.add_opcodes(jump_op)

            if len(if_block.elifs) == 0:
                if_block.jump_op = jump_op
            else:
                # print("    already got an endif")
                if_block.elifs[-1].jump_op = jump_op

        if len(if_block.elifs) == 0:
            jump(if_block.if_op, context, self, OpcodePosition.START)
        else:
            jump(if_block.elifs[-1].if_op, context, self, OpcodePosition.START)

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
# Some opcodes need to reference other opcodes (e.g., GOTO)
#
# These helpers help define and resolve those references.
##########################################################################

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

    target is the Python AST node.
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


##########################################################################
# Not entirely common, but complex, calls.
##########################################################################

class AddToArgs:
    def process(self, context):
        context.add_opcodes(
            JavaOpcodes.INVOKESTATIC(
                'org/Python',
                'addToArgs',
                args=['[Lorg/python/Object;', 'Lorg/python/Object;'],
                returns='[Lorg/python/Object;'
            )
        )


class AddToKwargs:
    def __init__(self, kwarg):
        self.kwarg = kwarg

    def process(self, context):
        context.add_opcodes(
            JavaOpcodes.LDC_W(self.kwarg),
            JavaOpcodes.INVOKESTATIC(
                'org/Python',
                'addToKwargs',
                args=['Ljava/util/Map;', 'Lorg/python/Object;', 'Ljava/lang/String;'],
                returns='Ljava/util/Map;'
            ),
        )
