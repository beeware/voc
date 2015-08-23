from collections import namedtuple
import dis
import os

from . import opcodes

from .klass import transpile as transpile_class
from .method import transpile as transpile_method, signature as method_signature
from .block import transpile as transpile_block


Parts = namedtuple('Parts', ['classes', 'methods', 'block', 'main', 'init'])


class Command:
    """A command is a sequence of instructions producing a distinct result.

    The `operation` is the final instruction that yields a result.
    A series of other instructions, known as `arguments` will be used
    to execute `operation`.

    Each argument is itself a Command; leaf nodes are Commands with no
    arguments.

    A command knows how many items it will pop from the stack, and
    how many it will push onto the stack. The stack count on a Command
    reflects the effect of the operation itself, plus *all* the arguments.
    """
    def __init__(self, instruction):
        self.operation = instruction
        self.arguments = []

    def __repr__(self):
        return '<Command %s (%s args)>' % (self.operation.opname, len(self.arguments))

    @property
    def consume_count(self):
        return sum(c.consume_count for c in self.arguments) + self.operation.consume_count

    @property
    def product_count(self):
        return sum(c.product_count for c in self.arguments) + self.operation.product_count

    def dump(self, depth=0):
        for op in self.arguments:
            op.dump(depth=depth+1)
        print ('    ' * depth, self.operation)


class Context:
    """An object describing the context in which a given code block will execute.

    Constructor takes the following arguments:
     * sourcefile - The source file providing the code definition
     * namespace - The namespace for the object being constructed.
     * name - The object currently being constructed.
     * localvars - The local context dictionary in which the method operates.
            If no localvars are provided, the method signature will be used
            to construct one, reflecting the state of the stack at entry to
            a new context.
     * is_class - boolean, indicating if the current context is a class
     * is_static - boolean, indicating if the current context is static
     * signature - A list of dictionaries, each dictionary providing details
            about an argument to the method.
     * return_signature - A single dictionary, providing details about the
            return type of the object.
     * ignore_empty - If True, a block that contains only a "return" statement
            will be flagged, and not turned into a full method. This is to
            avoid defining do-nothing <init> and <clinit> methods on classes.
    """
    def __init__(
            self, sourcefile, namespace, name,
            localvars=None,
            is_class=False, is_static=False,
            signature=None, return_signature=None,
            ignore_empty=False):
        self.sourcefile = sourcefile
        self.namespace = namespace
        self.name = name

        if signature is None:
            self.signature = []
        else:
            self.signature = signature

        if localvars is None:
            self.localvars = dict((p['name'], i) for i, p in enumerate(self.signature))
        else:
            self.localvars = localvars

        if return_signature is None:
            self.return_signature = {}
        else:
            self.return_signature = return_signature

        self.is_class = is_class
        self.is_static = is_static
        self.ignore_empty = ignore_empty

    @property
    def modulename(self):
        return os.path.splitext(os.path.basename(self.sourcefile))[0]

    @property
    def class_descriptor(self):
        if self.is_class:
            return '/'.join(self.namespace.split('.') + [self.modulename, self.name])
        else:
            return '/'.join(self.namespace.split('.') + [self.modulename])

    @property
    def void_return(self):
        return self.return_signature.get('annotation') is None

    @property
    def descriptor(self):
        return_descriptor = 'V' if self.return_signature.get('annotation') is None else 'Lorg/python/PyObject;'

        # Special case for the main method; otherwise, every argument is a PyObject.
        if self.signature == [{'annotation': 'argv'}]:
            param_descriptor = '[Ljava/lang/String;'
        else:
            param_descriptor = 'Lorg/python/PyObject;' * len(self.signature)

        return '(%s)%s' % (param_descriptor, return_descriptor)


def extract(context, code):
    """Break a code object into the parts it defines.

    Returns a Parts object describing the components of
    the code object, fully decomposed into
    """
    instructions = list(dis.Bytecode(code))
    commands = []
    i = len(instructions)

    while i > 0:
        i, command = extract_command(instructions, i, depth=1)
        commands.append(command)

    commands.reverse()

    print ('=====' * 10)
    print (code)
    print ('-----' * 10)
    for command in commands:
        command.dump()
    print ('=====' * 10)

    # Ultimately, all commands are going to end up either:
    #  * Defining a class
    #  * Defining a method
    #  * Defining an block of executable code
    # There are a couple of special-case initializer blocks (main entry
    # points, __init__, etc), so we track those separately.
    classes = []
    methods = []
    block = None
    main = None
    init = None

    main_commands = []
    block_commands = []

    main_end = None
    for cmd in commands:
        if main_end is not None:
            # Marker for the end of the main block:
            #   JUMP_FORWARD <main_end>
            if len(cmd.arguments) == 0 and cmd.operation.opname == 'JUMP_FORWARD' and cmd.operation.delta == main_end:
                main_end = None
                main_context = Context(
                    name='__main__',
                    namespace=context.namespace,
                    sourcefile=context.sourcefile,
                    is_static=True,
                    signature=[{'name': 'args', 'annotation': 'argv'}],
                    ignore_empty=True,
                )
                main = transpile_block(main_context, main_commands)
            else:
                main_commands.append(cmd)
        else:
            # Variable storage of some kind - including storing in the bit bucket.
            if cmd.operation.opname in ('POP_TOP', 'STORE_NAME'):
                # Equivalent of "import dom":
                #           LOAD_CONST 0
                #           LOAD CONST None
                #       IMPORT_NAME <name>
                #   STORE_NAME <name>
                if cmd.arguments[0].operation.opname == 'IMPORT_NAME':
                    # print ("Handle import of", cmd.arguments[0].operation.target)
                    pass

                #           ... load arg defaults ...
                #           LOAD_CONST <code>
                #           LOAD_CONST <name>
                #       MAKE_FUNCTION <n_defaults>
                #   STORE_NAME <name>
                elif cmd.arguments[0].operation.opname == 'MAKE_FUNCTION':
                    # print ("Found method", cmd.operation.name)
                    code = cmd.arguments[0].arguments[-2].operation.const
                    print ("MAKE FUNCTION", cmd.operation.name)
                    method_context = Context(
                        sourcefile=context.sourcefile,
                        namespace=context.namespace,
                        name=cmd.operation.name,
                        is_static=context.is_static,
                        signature=method_signature(code),
                        return_signature={'annotation': object}
                    )
                    parts = extract(method_context, code)
                    if parts.classes:
                        print("Ignoring inner class definition.")
                    if parts.methods:
                        print("Ignoring inner method definition.")
                    if parts.main:
                        print("Ignoring inner __main__ definition.")
                    if parts.init:
                        print("Ignoring inner __init__ definition.")
                    method = transpile_method(method_context, parts)
                    if cmd.operation.name == '__init__':
                        # print (" - adding as special case: __init__")
                        if init is not None:
                            print("Found duplicate constructor... replacing previous constructor")

                        init = method
                    else:
                        methods.append(method)

                elif cmd.arguments[0].operation.opname == 'CALL_FUNCTION':
                    # Equivalent of "class <Name>:":
                    #           LOAD_BUILD_CLASS
                    #               LOAD_CONST <code>
                    #               LOAD_CONST <Name>
                    #           MAKE_FUNCTION 0
                    #           LOAD_CONST <Name>
                    #       CALL_FUNCTION 2
                    #   STORE_NAME <Name>
                    if cmd.arguments[0].arguments[0].operation.opname == 'LOAD_BUILD_CLASS':
                        # print ("Found class", cmd.operation.name)
                        code = cmd.arguments[0].arguments[1].arguments[0].operation.const
                        class_context = Context(
                            sourcefile=context.sourcefile,
                            namespace=context.namespace,
                            name=context.name,
                            is_class=True,
                            ignore_empty=True,
                        )
                        parts = extract(class_context, code)
                        if parts.classes:
                            print("Ignoring inner class definition.")
                        if parts.main:
                            print("Ignoring inner __main__ definition.")
                        classes.append(transpile_class(class_context, parts))

                    # Equivalent of "name = method_name(...)"
                    #           LOAD_NAME <method_name>
                    #           ... load arg ...
                    #       CALL_FUNCTION <n_args>
                    #   STORE_NAME <name>
                    else:
                        # print ("Static block invocation of", cmd.arguments[-1].arguments[0].operation.name)
                        block_commands.append(cmd)

                # Equivalent of "name = method_name(...)"
                #       ... load arg ...
                #   STORE_NAME <name>
                else:
                    block_commands.append(cmd)

            # This is looking for a very specific pattern:
            #   if __name__ == '__main__':
            #       ...
            # which is represented as:
            #         LOAD_NAME: __name__
            #         LOAD_CONST: __main__
            #     COMPARE_OP: ==
            #  POP_JUMP_IF_FALSE: <end of block>
            #  ... <main code>
            #  JUMP_FORWARD <end of block>
            elif (cmd.operation.opname == 'POP_JUMP_IF_FALSE'
                    and cmd.arguments[0].operation.opname == 'COMPARE_OP' and cmd.arguments[0].operation.comparison == '=='
                    and cmd.arguments[0].arguments[0].operation.opname == 'LOAD_NAME' and cmd.arguments[0].arguments[0].operation.name == '__name__'
                    and cmd.arguments[0].arguments[1].operation.opname == 'LOAD_CONST' and cmd.arguments[0].arguments[1].operation.const == '__main__'):
                # print("Found main block")
                if main is not None:
                    print("Found duplicate main block... replacing previous main")

                main_end = cmd.operation.target

            # All other module-level cmds goes into the static block
            else:
                block_commands.append(cmd)

    block = transpile_block(context, block_commands)

    return Parts(classes=classes, methods=methods, block=block, main=main, init=init)


def extract_command(instructions, i, depth):
    i = i - 1
    instruction = instructions[i]
    argval = instruction.argval

    OpType = getattr(opcodes, instruction.opname)
    # print ('    ' * depth, "Extract; i=", i, instruction)
    # If this instruction is preceded by EXTENDED_ARG, then
    # there is more arugment information to come. Integrate it
    # into the instruction argument we've already read.
    if i > 0 and instructions[i - 1].opname == 'EXTENDED_ARG':
        i = i - 1
        extended = instructions[i]

        argval = argval | extended.argval

    if instruction.arg is None:
        opcode = OpType()
    else:
        opcode = OpType(argval)

    cmd = Command(opcode)

    stack = cmd.operation.consume_count

    while stack > 0:
        i, arg = extract_command(instructions, i, depth + 1)
        cmd.arguments.append(arg)
        # print('    ' * depth, '+', arg.consume_count, arg.product_count)
        stack = stack + arg.consume_count - arg.product_count
        # print('    ' * depth, 'stack is now', stack)

    # print('    ' * depth, 'cmd complete')
    cmd.arguments.reverse()
    return i, cmd
