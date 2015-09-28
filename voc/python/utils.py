from . import opcodes
from ..java import opcodes as JavaOpcodes


class Command:
    """A command is a sequence of instructions producing a distinct result.

    The `operation` is the final instruction that yields a result.
    A series of other instructions, known as `arguments` will be used
    to execute `operation`.

    The command also tracks the line number and code offset that it
    represents, plus whether the command is a jump target.

    Each argument is itself a Command; leaf nodes are Commands with no
    arguments.

    A command knows how many items it will pop from the stack, and
    how many it will push onto the stack. The stack count on a Command
    reflects the effect of the operation itself, plus *all* the arguments.

    A command may also encompass an internal block - for example, a for
    or while loop. Those blocks
    """
    def __init__(self, instruction, arguments=None):
        self.operation = instruction
        if arguments:
            self.arguments = arguments
        else:
            self.arguments = []

    def __repr__(self):
        try:
            return '<Command %s (%s args)> %s' % (self.operation.opname, len(self.arguments), self.arguments[0].operation.name)
        except:
            return '<Command %s (%s args)>' % (self.operation.opname, len(self.arguments))

    @property
    def consume_count(self):
        return sum(c.consume_count for c in self.arguments) + self.operation.consume_count

    @property
    def product_count(self):
        return sum(c.product_count for c in self.arguments) + self.operation.product_count

    def is_main_start(self):
        return (
            self.operation.opname == 'POP_JUMP_IF_FALSE'
            and self.arguments[0].operation.opname == 'COMPARE_OP' and self.arguments[0].operation.comparison == '=='
            and self.arguments[0].arguments[0].operation.opname == 'LOAD_NAME' and self.arguments[0].arguments[0].operation.name == '__name__'
            and self.arguments[0].arguments[1].operation.opname == 'LOAD_CONST' and self.arguments[0].arguments[1].operation.const == '__main__'
        )

    def is_main_end(self, main_end):
        if main_end == self.operation.python_offset:
            return True
        elif self.arguments and main_end <= self.arguments[0].operation.python_offset:
            return True
        return False

    def dump(self, depth=0):
        for op in self.arguments:
            op.dump(depth=depth + 1)
        print ('%s%4s:%4d -%s +%s' % (
                '>' if self.operation.is_jump_target else ' ',
                self.operation.starts_line if self.operation.starts_line is not None else '    ',
                self.operation.python_offset,
                self.operation.consume_count,
                self.operation.product_count
            ) + '    ' * depth, self.operation)

    def transpile(self, context):
        self.operation.transpile(context, self.arguments)


class TryExcept:
    def __init__(self, start, end, start_offset, end_offset, starts_line):
        self.start = start
        self.end = end

        self.start_offset = start_offset
        self.end_offset = end_offset

        self.starts_line = starts_line
        self.commands = []

        self.exceptions = []

        self.else_block = None
        self.finally_block = None

    def __repr__(self):
        return '<Try %s-%s | %s%s%s>' % (
            self.start,
            self.end,
            ', '.join(str(handler) for handler in self.exceptions),
            ' %s' % self.else_block if self.else_block else '',
            ' %s' % self.finally_block if self.finally_block else ''
        )

    @property
    def resume_index(self):
        if self.finally_block and self.exceptions:
            return self.start - 2
        else:
            return self.start - 1

    @property
    def consume_count(self):
        return sum(c.consume_count for c in self.commands)

    @property
    def product_count(self):
        return sum(c.product_count for c in self.commands)

    def is_main_start(self):
        return False

    def is_main_end(self, main_end):
        return False

    def dump(self, depth=0):
        print (' %4s:%4d      ' % (
                self.starts_line if self.starts_line is not None else '    ',
                self.start_offset,
            ) + '    ' * depth,
            'TRY:'
        )

        for command in self.commands:
            command.dump(depth=depth + 1)

        for handler in self.exceptions:
            handler.dump(depth=depth)

        if self.else_block:
            self.else_block.dump(depth=depth)

        if self.finally_block:
            self.finally_block.dump(depth=depth)

        print ('     :%4d      ' % (
                self.end_offset,
            ) + '    ' * depth,
            'END TRY'
        )

    def extract(self, instructions, blocks):
        self.operation = instructions[self.start - 1]
        i = self.end
        self.commands = []
        while i > self.start:
            i, command = extract_command(instructions, blocks, i, self.start)
            self.commands.append(command)

        self.commands.reverse()

        for handler in self.exceptions:
            handler.extract(instructions, blocks)

        if self.else_block:
            self.else_block.extract(instructions, blocks)

        if self.finally_block:
            self.finally_block.extract(instructions, blocks)

    def transpile(self, context):
        context.add_opcodes(opcodes.TRY(
                self.else_block,
                self.finally_block
            ))
        for command in self.commands:
            command.transpile(context)

        for handler in self.exceptions:
            # Define the exception handler.
            # On entry to the exception, the stack will contain
            # a single value - the exception being thrown.
            # This exception must be wrapped into an org/python/types/Object
            # so it can be used as an argument elsewhere.
            if len(handler.exceptions) > 1:  # catch multiple - except (A, B) as v:
                context.add_opcodes(
                    opcodes.CATCH('org/python/exceptions/%s' % handler.exceptions[0]),
                )
                if handler.var_name:
                    context.add_opcodes(
                        opcodes.ASTORE_name(context, handler.var_name),
                    )
                else:
                    # No named exception, but there is still an exception
                    # on the stack. Pop it off.
                    context.add_opcodes(JavaOpcodes.POP())

                handler.transpile(context)
            elif len(handler.exceptions) == 1:  # catch single - except A as v:
                context.add_opcodes(
                    opcodes.CATCH('org/python/exceptions/%s' % handler.exceptions[0]),
                )
                if handler.var_name:
                    context.add_opcodes(
                        opcodes.ASTORE_name(context, handler.var_name),
                    )
                else:
                    # No named exception, but there is still an exception
                    # on the stack. Pop it off.
                    context.add_opcodes(JavaOpcodes.POP())

                handler.transpile(context)
            else:
                # The bucket case - except:
                # No named exception, but there is still an exception
                # on the stack. Pop it off.
                context.add_opcodes(
                    opcodes.CATCH(),
                    JavaOpcodes.POP(),
                )
                handler.transpile(context)

        if self.finally_block:
            context.add_opcodes(
                opcodes.FINALLY(),
                opcodes.ASTORE_name(context, '##exception-%d##' % id(self))
            )

            for command in self.finally_block.commands:
                command.transpile(context)

            context.add_opcodes(
                opcodes.ALOAD_name(context, '##exception-%d##' % id(self)),
                JavaOpcodes.ATHROW(),
            )

        context.add_opcodes(opcodes.END_TRY())


class ExceptionBlock:
    def __init__(self, exceptions, var_name, start, end, start_offset, end_offset, starts_line):
        self.exceptions = exceptions
        self.var_name = var_name

        self.start = start
        self.end = end

        self.start_offset = start_offset
        self.end_offset = end_offset

        self.starts_line = starts_line
        self.commands = []

    def __repr__(self):
        if self.exceptions:
            if self.var_name:
                return '%s (%s): %s-%s' % (','.join(self.exceptions), self.var_name, self.start, self.end)
            else:
                return '%s: %s-%s' % (','.join(self.exceptions), self.start, self.end)
        else:
            return 'Bucket: %s-%s' % (self.start, self.end)

    def dump(self, depth=0):
        print (' %4s:%4d      ' % (
                self.starts_line if self.starts_line is not None else '    ',
                self.start_offset,
            ) + '    ' * depth,
            'CATCH %s%s:' % (
                ', '.join(self.exceptions) if self.exceptions else '',
                ' as %s' % self.var_name if self.var_name else '',
            )
        )

        for command in self.commands:
            command.dump(depth=depth + 1)

    def extract(self, instructions, blocks):
        i = self.end
        self.commands = []
        while i > self.start:
            i, command = extract_command(instructions, blocks, i, self.start)
            self.commands.append(command)

        self.commands.reverse()

    def transpile(self, context):
        context.next_opcode_starts_line = self.starts_line
        for command in self.commands:
            command.transpile(context)


class FinallyBlock:
    def __init__(self, start, end, start_offset, end_offset, starts_line):
        self.start = start
        self.end = end

        self.start_offset = start_offset
        self.end_offset = end_offset

        self.starts_line = starts_line
        self.commands = []

    def __repr__(self):
        return 'Finally: %s-%s' % (self.start, self.end)

    def dump(self, depth=0):
        print (' %4s:%4d      ' % (
                self.starts_line if self.starts_line is not None else '    ',
                self.start_offset,
            ) + '    ' * depth,
            'FINALLY:'
        )

        for command in self.commands:
            command.dump(depth=depth + 1)

    def extract(self, instructions, blocks):
        i = self.end
        self.commands = []
        while i > self.start:
            i, command = extract_command(instructions, blocks, i, self.start)
            self.commands.append(command)

        self.commands.reverse()

    def transpile(self, context):
        context.next_opcode_starts_line = self.starts_line
        for command in self.commands:
            command.transpile(context)


class ElseBlock:
    def __init__(self, start, end, start_offset, end_offset, starts_line):
        self.start = start
        self.end = end

        self.start_offset = start_offset
        self.end_offset = end_offset

        self.starts_line = starts_line
        self.commands = []

    def __repr__(self):
        return 'Else: %s-%s' % (self.start, self.end)

    def dump(self, depth=0):
        print (' %4s:%4d      ' % (
                self.starts_line if self.starts_line is not None else '    ',
                self.start_offset,
            ) + '    ' * depth,
            'ELSE:'
        )

        for command in self.commands:
            command.dump(depth=depth + 1)

    def extract(self, instructions, blocks):
        i = self.end
        self.commands = []
        while i > self.start:
            i, command = extract_command(instructions, blocks, i, self.start, literal=(i == self.end))
            self.commands.append(command)

        self.commands.reverse()

    def transpile(self, context):
        context.next_opcode_starts_line = self.starts_line
        for command in self.commands:
            command.transpile(context)


class ForLoop:
    def __init__(self, start, loop, varname, end, start_offset, loop_offset, end_offset, starts_line):
        self.start = start
        self.loop = loop
        self.end = end

        self.varname = varname

        self.start_offset = start_offset
        self.loop_offset = loop_offset
        self.end_offset = end_offset

        self.starts_line = starts_line

        self.loop_commands = []
        self.commands = []

    def __repr__(self):
        return '<For %s: %s-%s>' % (
            self.start,
            self.loop,
            self.end,
        )

    @property
    def consume_count(self):
        return sum(c.consume_count for c in self.commands)

    @property
    def product_count(self):
        return sum(c.product_count for c in self.commands)

    @property
    def resume_index(self):
        return self.start - 1

    def is_main_start(self):
        return False

    def is_main_end(self, main_end):
        return False

    def dump(self, depth=0):
        print (' %4s:%4d      ' % (
                self.starts_line if self.starts_line is not None else '    ',
                self.start_offset,
            ) + '    ' * depth,
            'FOR:'
        )

        for command in self.loop_commands:
            command.dump(depth=depth + 1)

        print ('     :%4d      ' % (
                self.loop_offset,
            ) + '    ' * depth,
            'LOOP:'
        )

        for command in self.commands:
            command.dump(depth=depth + 1)

        print ('     :%4d      ' % (
                self.end_offset,
            ) + '    ' * depth,
            'END FOR'
        )

    def extract(self, instructions, blocks):
        # Collect the commands related to setting up the loop variable
        i = self.end
        while i > self.loop:
            i, command = extract_command(instructions, blocks, i, self.loop)
            self.commands.append(command)

        self.commands.reverse()

        # Collect the commands for the actual loop
        i = self.loop - 2
        while i > self.start:
            i, command = extract_command(instructions, blocks, i, self.start)
            self.loop_commands.append(command)

        self.loop_commands.reverse()

    def pre_loop(self, context):
        pass

    def pre_iteration(self, context):
        context.add_opcodes(
            JavaOpcodes.DUP(),
        )

    def post_loop(self, context):
        context.add_opcodes(
            JavaOpcodes.POP(),
        )

    def transpile(self, context):
        context.next_opcode_starts_line = self.starts_line

        self.pre_loop(context)

        for command in self.loop_commands:
            command.transpile(context)

        loop = opcodes.START_LOOP()

        context.add_opcodes(
            loop,
                opcodes.TRY(),
        )
        self.pre_iteration(context)
        context.add_opcodes(
                    JavaOpcodes.INVOKEINTERFACE('org/python/Iterable', '__next__', '()Lorg/python/Object;'),
                opcodes.CATCH('org/python/exceptions/StopIteration'),
        )
        self.post_loop(context)
        context.add_opcodes(
                    opcodes.jump(JavaOpcodes.GOTO(0), context, loop, opcodes.Opcode.NEXT),
                opcodes.END_TRY(),
                opcodes.ASTORE_name(context, self.varname),
        )

        for command in self.commands:
            command.transpile(context)

        context.add_opcodes(opcodes.END_LOOP())


class ComprehensionForLoop(ForLoop):
    def __init__(self, start, loop, varname, end, start_offset, loop_offset, end_offset, starts_line):
        super().__init__(start, loop, varname, end, start_offset, loop_offset, end_offset, starts_line)

    def pre_loop(self, context):
        context.add_opcodes(
            opcodes.ASTORE_name(context, '##FOR-%s' % id(self)),
            opcodes.ALOAD_name(context, '##FOR-%s' % id(self)),
        )

    def pre_iteration(self, context):
        context.add_opcodes(
            JavaOpcodes.DUP(),
            opcodes.ALOAD_name(context, '.0'),
        )

    def post_loop(self, context):
        context.add_opcodes(
            JavaOpcodes.POP(),
            opcodes.ALOAD_name(context, '##FOR-%s' % id(self)),
        )


class WhileLoop:
    def __init__(self, start, end, start_offset, end_offset, starts_line):
        self.start = start
        self.end = end

        self.start_offset = start_offset
        self.end_offset = end_offset

        self.starts_line = starts_line
        self.commands = []

    def __repr__(self):
        return '<For %s-%s>' % (
            self.start,
            self.end,
        )

    @property
    def consume_count(self):
        return sum(c.consume_count for c in self.commands)

    @property
    def product_count(self):
        return sum(c.product_count for c in self.commands)

    @property
    def resume_index(self):
        return self.start - 1

    def is_main_start(self):
        return False

    def is_main_end(self, main_end):
        return False

    def dump(self, depth=0):
        print (' %4s:%4d      ' % (
                self.starts_line if self.starts_line is not None else '    ',
                self.start_offset,
            ) + '    ' * depth,
            'WHILE:'
        )

        for command in self.commands:
            command.dump(depth=depth + 1)

        print ('     :%4d      ' % (
                self.end_offset,
            ) + '    ' * depth,
            'END WHILE'
        )

    def extract(self, instructions, blocks):
        self.operation = instructions[self.start]
        i = self.end
        self.commands = []
        while i > self.start:
            i, command = extract_command(instructions, blocks, i, self.start)
            self.commands.append(command)

        self.commands.reverse()

    def transpile(self, context):
        context.next_opcode_starts_line = self.starts_line
        context.add_opcodes(opcodes.START_LOOP())

        for command in self.commands:
            command.transpile(context)

        end_loop = opcodes.END_LOOP()
        context.add_opcodes(end_loop)

        context.jump_targets[self.end_offset] = end_loop


def find_try_except(offset_index, instructions, i):
    instruction = instructions[i]
    try_start_index = i + 1
    try_end_index = offset_index[instruction.argval] - 2

    # Find the end of the entire try block
    end_jump_index = offset_index[instruction.argval] - 1
    end_block_offset = instructions[end_jump_index].argval
    end_block_index = offset_index[end_block_offset]

    while instructions[end_block_index].opname != 'END_FINALLY':
        end_block_index -= 1

    # print("START INDEX", try_start_index)
    # print("START OFFSET", instructions[try_start_index].offset)
    # print("TRY END INDEX", try_end_index)
    # print("TRY END OFFSET", instructions[try_end_index].offset)
    # print("END INDEX", end_block_index)
    # print("END OFFSET", instructions[end_block_index].offset)

    block = TryExcept(
        start=try_start_index,
        end=try_end_index,
        start_offset=instructions[try_start_index].offset,
        end_offset=instructions[try_end_index].offset,
        starts_line=instruction.starts_line
    )

    # find all the except blocks
    i = offset_index[instruction.argval] + 1
    while i < end_block_index:
        exceptions = []
        starts_line = instructions[offset_index[instruction.argval]].starts_line
        while instructions[i].opname == 'LOAD_NAME':
            exceptions.append(instructions[i].argval)
            i = i + 1

        # If there's more than 1 exception named, there will be
        # a BUILD_TUPLE instruction that needs to be skipped.
        if len(exceptions) > 1:
            i = i + 1

        if instructions[i].opname == 'COMPARE_OP':
            # An exception has been explicitly named
            i = i + 3

            # print ("CHECK", i, instructions[i].opname)
            if instructions[i].opname == 'POP_TOP':
                # Exception is specified, but not a name.
                var_name = None

                except_start_index = i + 2
                # print("EXCEPT START", except_start_index)

            elif instructions[i].opname == 'STORE_NAME':
                var_name = instructions[i].argval

                except_start_index = i + 3
                # print("EXCEPT START e", except_start_index)

        else:
            i = i + 3

            # Exception is specified, but not a name.
            var_name = None

            except_start_index = i
            # print("EXCEPT START anon", except_start_index)

        while not (instructions[i].opname in ('JUMP_FORWARD', 'JUMP_ABSOLUTE') and instructions[i].argval >= end_block_offset):
            i = i + 1

        if var_name:
            except_end_index = i - 7
        else:
            except_end_index = i - 1

        jump_offset = instructions[i].argval

        # print("EXCEPT END", except_end_index)
        # Step forward to the start of the next except block
        # (or the end of the try/catch)
        i = i + 2

        block.exceptions.append(
            ExceptionBlock(
                exceptions=exceptions,
                var_name=var_name,
                start=except_start_index,
                end=except_end_index,
                start_offset=instructions[except_start_index].offset,
                end_offset=instructions[except_end_index].offset,
                starts_line=starts_line
            )
        )

    if jump_offset > end_block_offset:
        start_else_index = end_block_index + 1

        end_else_index = offset_index[jump_offset]
        if instructions[end_else_index-1].opname == 'JUMP_FORWARD':
            end_else_index -= 1

        block.else_block = ElseBlock(
            start=start_else_index,
            end=end_else_index,
            start_offset=instructions[start_else_index].offset,
            end_offset=jump_offset,
            starts_line=instructions[end_block_index].starts_line
        )

        i = end_else_index

    return i, block


def find_blocks(instructions):
    offset_index = {}
    # print(">>>>>" * 10)
    for i, instruction in enumerate(instructions):
        # print("%4d:%4d %s %s" % (i, instruction.offset, instruction.opname, instruction.argval if instruction.argval is not None else ''))
        offset_index[instruction.offset] = i
    # print(">>>>>" * 10)

    blocks = {}
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        if instruction.opname == 'SETUP_EXCEPT':
            i, block = find_try_except(offset_index, instructions, i)
            blocks[i - 1] = block

        elif instruction.opname == 'SETUP_FINALLY':
            start_index = offset_index[instruction.argval]

            # print("FINALLY START INDEX", start_index)
            # print("FINALLY START OFFSET", instructions[start_index].offset)

            i = i + 1
            if instructions[i].opname == 'SETUP_EXCEPT':
                i, block = find_try_except(offset_index, instructions, i)
            else:
                # print("START INDEX", i)
                # print("START OFFSET", instructions[i].offset)

                # print("END INDEX", start_index - 2)
                # print("END OFFSET", instructions[start_index - 2].offset)

                block = TryExcept(
                    start=i,
                    end=start_index - 2,
                    start_offset=instructions[i].offset,
                    end_offset=instructions[start_index - 2].offset,
                    starts_line=instruction.starts_line
                )

            i = i + 1
            while instructions[i].opname != 'END_FINALLY':
                i = i + 1

            # print("FINALLY END INDEX", i)
            # print("FINALLY END OFFSET", instructions[i].offset)

            block.finally_block = FinallyBlock(
                start=start_index,
                end=i,
                start_offset=instructions[start_index].offset,
                end_offset=instructions[i].offset,
                starts_line=instruction.starts_line
            )

            blocks[i] = block
            i = i + 1

        elif instruction.opname == 'SETUP_LOOP':
            i = i + 1
            start_index = i

            while instructions[i].opname not in ('FOR_ITER', 'POP_JUMP_IF_FALSE'):
                i = i + 1

            # Find the end of the entire loop block.
            # Ignore the final instruction to jump back to the start.
            end_offset = instructions[i].argval
            end_index = offset_index[end_offset] - 1

            # print("START INDEX", start_index)
            # print("START OFFSET", instructions[start_index].offset)

            # print("END INDEX", end_index)
            # print("END OFFSET", end_offset)

            if instructions[i].opname == 'FOR_ITER':
                loop_offset = instructions[i + 2].offset
                loop_index = offset_index[loop_offset]

                # print("LOOP INDEX", loop_index)
                # print("LOOP OFFSET", loop_offset)
                # print("LOOP VAR", instructions[loop_index - 1].argval)

                block = ForLoop(
                    start=start_index,
                    loop=loop_index,
                    varname=instructions[loop_index - 1].argval,
                    end=end_index,
                    start_offset=instructions[start_index].offset,
                    loop_offset=loop_offset,
                    end_offset=end_offset,
                    starts_line=instruction.starts_line
                )
            else:
                block = WhileLoop(
                    start=start_index,
                    end=end_index,
                    start_offset=instructions[start_index].offset,
                    end_offset=end_offset,
                    starts_line=instruction.starts_line,
                )

            blocks[end_index + 1] = block
            i = i + 1

        elif instruction.opname == 'FOR_ITER':
            i = i + 1
            start_index = i - 1

            # Find the end of the entire loop block.
            # Ignore the final instruction to jump back to the start.
            end_offset = instruction.argval
            end_index = offset_index[end_offset] - 1

            # print("START INDEX", start_index)
            # print("START OFFSET", instructions[start_index].offset)

            # print("END INDEX", end_index)
            # print("END OFFSET", end_offset)

            loop_offset = instructions[i+1].offset
            loop_index = offset_index[loop_offset]

            # print("LOOP INDEX", loop_index)
            # print("LOOP OFFSET", loop_offset)
            # print("LOOP VAR", instructions[loop_index].argval)

            block = ComprehensionForLoop(
                start=start_index,
                loop=loop_index,
                varname=instructions[loop_index - 1].argval,
                end=end_index,
                start_offset=instructions[start_index].offset,
                loop_offset=loop_offset,
                end_offset=end_offset,
                starts_line=instruction.starts_line
            )

            blocks[end_index + 1] = block
            i = i + 1

        else:
            i = i + 1

    return blocks


def extract_command(instructions, blocks, i, start_index=0, literal=False):
    """Extract a single command from the end of the instruction list.

    See the definition of Command for details on the recursive nature
    of commands. We start at the *end* of the instruction list and
    work backwards because each command is essentially working towards
    a final result; each Command can be thought of as a "result".
    """
    i = i - 1
    instruction = instructions[i]
    argval = instruction.argval

    OpType = getattr(opcodes, instruction.opname)

    # If this instruction is preceded by EXTENDED_ARG, then
    # there is more arugment information to come. Integrate it
    # into the instruction argument we've already read.
    if i > 0 and instructions[i - 1].opname == 'EXTENDED_ARG':
        i = i - 1
        extended = instructions[i]

        argval = argval | extended.argval

    try:
        if literal:
            raise KeyError()
        # If this is a known block, defer to the block for
        # extraction instructions.
        cmd = blocks[i]

        cmd.extract(instructions, blocks)

        i = cmd.resume_index

    except KeyError:
        if instruction.arg is None:
            opcode = OpType(instruction.offset, instruction.starts_line, instruction.is_jump_target)
        else:
            opcode = OpType(argval, instruction.offset, instruction.starts_line, instruction.is_jump_target)

        cmd = Command(opcode)

        # print('>', i, instruction.offset, cmd.operation.opname, cmd.operation.consume_count)

        required = cmd.operation.consume_count
        while required > 0 and i > start_index:
            i, arg = extract_command(instructions, blocks, i)
            cmd.arguments.append(arg)
            required = required - arg.product_count + arg.consume_count

        # print('<', i, instruction.offset, cmd.operation.opname)

        # Since we did everything backwards, reverse to get
        # arguments back in the right order.
        cmd.arguments.reverse()

    return i, cmd
