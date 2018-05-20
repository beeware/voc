import types

from ..java import (
    Code as JavaCode, ExceptionInfo as JavaExceptionInfo, LineNumberTable,
    opcodes as JavaOpcodes, Classref
)
from .structures import (
    ArgType, OpcodePosition,
    TRY, CATCH, END_TRY,
    jump, resolve_jump,
)
from .types import java, python
from .types.primitives import (
    ICONST_val, LCONST_val, DCONST_val, ALOAD_index, ALOAD_name, ASTORE_index, ASTORE_name, free_name
)

# from .debug import DEBUG, DEBUG_value


class IgnoreBlock(Exception):
    """An escape hatch; enable a block to be flagged as ignorable"""
    pass


class BlockCodeTooLarge(Exception):
    """Enable a block to be flagged too large to transpile."""
    def __init__(self, code_length):
        self.code_length = code_length


class Accumulator:
    def __init__(self, local_vars=None):
        self.opcodes = []

        self.local_vars = local_vars if local_vars else {}
        self.deleted_vars = set()

        self.next_resolve_list = []
        self.next_opcode_starts_line = None

    def add_opcodes(self, *opcodes):
        # Add the opcodes to the code list and process them.
        for opcode in opcodes:
            if opcode.process(self):
                # self.opcodes.extend([
                #     DEBUG(str(opcode)),
                # ])

                self.opcodes.append(opcode)

                # If we've flagged a code line change, attach that to the opcode
                if self.next_opcode_starts_line:
                    opcode.starts_line = self.next_opcode_starts_line
                    self.next_opcode_starts_line = None

                # Resolve any references to the "next" opcode.
                for (obj, attr) in self.next_resolve_list:
                    # print("        resolve %s reference on %s %s with %s %s" % (
                    #     attr, obj, id(obj), opcode, id(opcode))
                    # )
                    setattr(obj, attr.value, opcode)

                self.next_resolve_list = []

    @property
    def active_local_vars(self):
        return {
            name: index
            for name, index in self.local_vars.items()
            if index is not None
        }

    def stack_depth(self):
        "Evaluate the maximum stack depth required by a sequence of Java opcodes"
        depth = 0
        max_depth = 0

        for opcode in self.opcodes:
            depth = depth + opcode.stack_effect
            # print("   ", opcode, depth)
            if depth > max_depth:
                max_depth = depth
        return max_depth

    def max_stack(self, exceptions=None):
        stack_depth = self.stack_depth()
        if exceptions:
            return stack_depth + len(exceptions)
        else:
            return stack_depth

    def max_locals(self):
        return len(self.active_local_vars) + len(self.deleted_vars)


class Block(Accumulator):
    def __init__(self, parent=None, verbosity=0):
        super().__init__()
        self._parent = parent
        self.verbosity = verbosity

        self.has_self = False
        self.parameters = []
        self.symbols = {}

        self.generator = None
        self.yield_points = []

        self.try_catches = []
        self.blocks = []
        self.jumps = []
        self.loops = []
        self.unknown_jump_targets = {}
        self.returns = {
            'annotation': None
        }

    def store_name(self, name, declare=False):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def store_dynamic(self):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def load_name(self, name):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def load_globals(self):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def load_locals(self):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def load_vars(self):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def delete_name(self, name):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    @property
    def can_ignore_empty(self):
        return False

    @property
    def has_nested_structure(self):
        """Whether the block has nested structures inside.
        """
        return any([self.blocks, self.loops, self.try_catches])

    def add_str(self, value):
        self.add_opcodes(
            python.Str(value),
        )

    def add_int(self, value):
        self.add_opcodes(
            java.New('org/python/types/Int'),
            LCONST_val(value),
            java.Init('org/python/types/Int', 'J'),
        )

    def add_float(self, value):
        self.add_opcodes(
            java.New('org/python/types/Float'),
            DCONST_val(value),
            java.Init('org/python/types/Float', 'D'),
        )

    def add_complex(self, value):
        self.add_opcodes(
            java.New('org/python/types/Complex'),
            DCONST_val(value.imag),
            java.Init('org/python/types/Complex', 'D'),
        )

    def add_tuple(self, data):
        self.add_opcodes(
            java.New('org/python/types/Tuple'),

            java.New('java/util/ArrayList'),
            java.Init('java/util/ArrayList'),
        )

        for value in data:
            self.add_opcodes(
                JavaOpcodes.DUP(),
            )

            if value is None:
                self.add_opcodes(
                    python.NONE()
                )
            else:
                if isinstance(value, bool):
                    self.add_opcodes(
                        java.New('org/python/types/Bool'),
                        ICONST_val(value),
                        java.Init('org/python/types/Bool', 'Z'),
                    )

                elif isinstance(value, int):
                    self.add_opcodes(
                        java.New('org/python/types/Int'),
                        LCONST_val(value),
                        java.Init('org/python/types/Int', 'J'),
                    )

                elif isinstance(value, float):
                    self.add_opcodes(
                        java.New('org/python/types/Float'),
                        JavaOpcodes.LDC2_W(value),
                        java.Init('org/python/types/Float', 'D'),
                    )

                elif isinstance(value, str):
                    self.add_opcodes(
                        python.Str(value),
                    )

                elif isinstance(value, bytes):
                    self.add_opcodes(
                        java.New('org/python/types/Bytes'),
                        JavaOpcodes.LDC_W(value.decode('ISO-8859-1')),
                        java.Init('org/python/types/Bytes', 'Ljava/lang/String;'),
                    )

                elif isinstance(value, tuple):
                    self.add_tuple(value)

                elif isinstance(value, complex):
                    self.add_opcodes(
                        java.New('org/python/types/Complex'),
                        DCONST_val(value.real),
                        DCONST_val(value.imag),
                        java.Init('org/python/types/Complex', 'D', 'D'),
                    )

                elif isinstance(value, types.CodeType):
                    self.add_opcodes(
                        JavaOpcodes.ACONST_NULL()
                    )

                else:
                    raise RuntimeError("Unknown constant type %s" % type(value))

            self.add_opcodes(
                java.List.add(),
            )

        self.add_opcodes(
            java.Init('org/python/types/Tuple', 'Ljava/util/List;'),
        )

    def add_callable(self, function, closure=False):
        self.add_opcodes(
            TRY(),
        )
        self.add_opcodes(
                # Wrap that function into a Callable.
                java.New('org/python/types/Function'),
        )

        self.add_str(function.code.co_name)

        # Add the code object
        self.add_opcodes(
                java.New('org/python/types/Code'),
        )

        self.add_int(function.code.co_argcount)
        self.add_tuple(function.code.co_cellvars)

        self.add_opcodes(
                JavaOpcodes.ACONST_NULL(),  # co_code
        )

        self.add_tuple(function.code.co_consts)
        self.add_str(function.code.co_filename)
        self.add_int(function.code.co_firstlineno)
        self.add_int(function.code.co_flags)
        self.add_tuple(function.code.co_freevars)
        self.add_int(function.code.co_kwonlyargcount)

        self.add_opcodes(
                JavaOpcodes.ACONST_NULL(),  # co_lnotab
        )

        self.add_str(function.code.co_name)
        self.add_tuple(function.code.co_names)
        self.add_int(function.code.co_nlocals)
        self.add_int(function.code.co_stacksize)
        self.add_tuple(function.code.co_varnames)

        self.add_opcodes(
                java.Init(
                    'org/python/types/Code',
                    'Lorg/python/types/Int;',
                    'Lorg/python/types/Tuple;',
                    'Lorg/python/types/Bytes;',
                    'Lorg/python/types/Tuple;',
                    'Lorg/python/types/Str;',
                    'Lorg/python/types/Int;',
                    'Lorg/python/types/Int;',
                    'Lorg/python/types/Tuple;',
                    'Lorg/python/types/Int;',
                    'Lorg/python/types/Bytes;',
                    'Lorg/python/types/Str;',
                    'Lorg/python/types/Tuple;',
                    'Lorg/python/types/Int;',
                    'Lorg/python/types/Int;',
                    'Lorg/python/types/Tuple;',
                ),

                # Get a Java Method representing the new function
                JavaOpcodes.LDC_W(Classref(function.class_descriptor)),
                JavaOpcodes.LDC_W(function.pyimpl_name),

                java.Array(len(function.parameters), classname='java/lang/Class'),
        )

        for i, param in enumerate(function.parameters):
            self.add_opcodes(
                JavaOpcodes.DUP(),
                ICONST_val(i),
                JavaOpcodes.LDC_W(Classref('org/python/Object')),
                JavaOpcodes.AASTORE(),
            )

        self.add_opcodes(
                JavaOpcodes.INVOKEVIRTUAL(
                    'java/lang/Class',
                    'getMethod',
                    '(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;'
                ),

                # globals
                # JavaOpcodes.GETSTATIC('python/sys', 'modules', 'Lorg/python/types/Dict;'),
                JavaOpcodes.ACONST_NULL(),  # globals

                # Default args
                java.List(),
        )

        # Default arguments list
        for arg in function.parameters:
            if arg['kind'] == ArgType.POSITIONAL_OR_KEYWORD and arg['default']:
                self.add_opcodes(
                    JavaOpcodes.DUP(),
                    ALOAD_name(arg['default']),
                    java.List.add(),
                )

        # Default keyword arguments list
        self.add_opcodes(
                java.Map(),
        )

        for arg in function.parameters:
            if arg['kind'] in (
                    ArgType.POSITIONAL_OR_KEYWORD,
                    ArgType.KEYWORD_ONLY) and arg['default']:
                self.add_opcodes(
                    JavaOpcodes.DUP(),
                    JavaOpcodes.LDC_W(arg['name']),
                    ALOAD_name(arg['default']),
                    java.Map.put(),
                )

        # Closure. This is created and assigned when the function is accessed.
        self.add_opcodes(
                JavaOpcodes.ACONST_NULL(),
        )

        self.add_opcodes(
                java.Init(
                    'org/python/types/Function',
                    'Lorg/python/types/Str;',
                    'Lorg/python/types/Code;',
                    'Ljava/lang/reflect/Method;',
                    'Ljava/util/Map;',
                    'Ljava/util/List;',
                    'Ljava/util/Map;',
                    'Lorg/python/types/Closure;',
                ),
        )
        self.add_opcodes(
            CATCH('java/lang/NoSuchMethodError')
        )
        self.add_opcodes(
                ASTORE_name('#EXCEPTION#'),
                java.New('org/python/exceptions/RuntimeError'),
                JavaOpcodes.LDC_W('Unable to find MAKE_FUNCTION output %s.%s' % (
                    function.class_descriptor, function.name)
                ),
                java.Init('org/python/exceptions/RuntimeError', 'Ljava/lang/String;'),
                JavaOpcodes.ATHROW(),
        )
        self.add_opcodes(
            END_TRY(),
            free_name('#EXCEPTION#')
        )

    def visitor_setup(self):
        """Tweak the bytecode generated for this block."""
        pass

    def visitor_teardown(self):
        """Tweak the bytecode generated for this block."""
        pass

    def transpile_code(self):
        """Create a JavaCode object representing the opcodes stored in the block

        May raise ``IgnoreBlock`` if the block should be ignored.
        """
        # Install the shortcut jump points for yield statements.
        yield_jumps = Accumulator()

        for i, yield_point in enumerate(self.yield_points):
            yield_jumps.add_opcodes(
                ALOAD_index(self.local_vars['<generator>']),
                JavaOpcodes.GETFIELD('org/python/types/Generator', 'yield_point', 'I'),
                ICONST_val(i + 1),
                jump(JavaOpcodes.IF_ICMPEQ(0), self, yield_point, OpcodePosition.YIELD)
            )

        self.opcodes = yield_jumps.opcodes + self.opcodes

        # Make sure every local variable slot has been initialized
        # as an object. This is needed because Python allows a variable
        # to be instantiated in a sub-block, and used outside that block.
        # The JVM doesn't, and raises a verify error if you try. By
        # initializing all variables, we can trick the verifier.
        # TODO: Ideally, we'd only initialize the variables that are ambiguous.
        init_vars = Accumulator()
        for i in range(
                    len(self.parameters) + (1 if self.has_self else 0),
                    len(self.active_local_vars) + len(self.deleted_vars)
                ):
            init_vars.add_opcodes(
                JavaOpcodes.ACONST_NULL(),
                ASTORE_index(i)
            )

        self.opcodes = init_vars.opcodes + self.opcodes

        # Since we've processed all the Python opcodes, we can now resolve
        # all the unknown jump targets.
        # print('>>>>> Resolve references')
        for target, references in self.unknown_jump_targets.items():
            # print("   resolving %s references to %s" % (len(references), target))
            for opcode, position in references:
                resolve_jump(opcode, self, target, position)

        # If the block has no content in it, and the block allows,
        # ignore this block.
        if self.can_ignore_empty:
            if len(self.opcodes) == 1 and isinstance(self.opcodes[0], JavaOpcodes.RETURN):
                raise IgnoreBlock()
            elif len(self.opcodes) == 2 and isinstance(self.opcodes[1], JavaOpcodes.ARETURN):
                raise IgnoreBlock()

        # Now that we have a complete opcode list, postprocess the list
        # with the known offsets.
        offset = 0
        # print('>>>>> set offsets', self)
        for index, instruction in enumerate(self.opcodes):
            # print("%4d:%4d (0x%x) %s" % (index, offset, id(instruction), instruction))
            instruction.java_index = index
            instruction.java_offset = offset
            offset += len(instruction)
        # print('>>>>> end set offsets')

        # The maximum length of a method in JVM is 65534 bytes. (See: Section 4.7.3, JVM 7 Specs)
        if offset > 65534:
            raise BlockCodeTooLarge(offset)

        # Construct the exception table, updating any
        # end-of-exception GOTO operations with the right opcode.
        # Record a frame range for each one.
        exceptions = []
        for try_catch in self.try_catches:
            # print("TRY CATCH START", id(try_catch), try_catch.start_op, try_catch.start_op.java_offset)
            # print("        TRY END", try_catch.try_end_op, try_catch.try_end_op.java_offset)
            # print("            END", try_catch.end_op, try_catch.end_op.java_offset)
            for handler in try_catch.handlers:
                # print("  HANDLER", handler.start_op, handler.end_op, handler.descriptors)
                if handler.descriptors:
                    for descriptor in handler.descriptors:
                        exceptions.append(JavaExceptionInfo(
                            try_catch.start_op.java_offset,
                            try_catch.try_end_op.java_offset,
                            handler.start_op.java_offset,
                            descriptor
                        ))
                else:
                    exceptions.append(JavaExceptionInfo(
                        try_catch.start_op.java_offset,
                        try_catch.try_end_op.java_offset,
                        handler.start_op.java_offset,
                        'org/python/exceptions/BaseException'
                    ))

            # Add definitions for the finally block
            if try_catch.finally_handler:
                # print(
                #     "  FINALLY",
                #     try_catch.finally_handler.start_op.java_offset,
                #     try_catch.finally_handler.end_op.java_offset
                # )
                exceptions.append(JavaExceptionInfo(
                    try_catch.start_op.java_offset,
                    try_catch.try_end_op.java_offset,
                    try_catch.finally_handler.start_op.java_offset,
                    None
                ))
                for handler in try_catch.handlers:
                    # print("   h", handler.descriptors)
                    exceptions.append(JavaExceptionInfo(
                        handler.start_op.java_offset,
                        handler.end_op.java_offset,
                        try_catch.finally_handler.start_op.java_offset,
                        None
                    ))

        # Update any jump instructions
        # print ("There are %s jumps" % len(self.jumps))
        for jmp in self.jumps:
            # print ("JUMP", hex(id(jmp)), jmp, jmp.java_offset, jmp.jump_op, hex(id(jmp.jump_op)))
            try:
                jmp.offset = jmp.jump_op.java_offset - jmp.java_offset
            except AttributeError:
                jmp.offset = jmp.jump_op.start_op.java_offset - jmp.java_offset

        # Construct a line number table from
        # the source code reference data on opcodes.
        line_numbers = []
        for opcode in self.opcodes:
            if opcode.starts_line is not None:
                line_numbers.append((opcode.java_offset, opcode.starts_line))
        line_number_table = LineNumberTable(line_numbers)

        return JavaCode(
            max_stack=self.max_stack(exceptions),
            max_locals=self.max_locals(),
            code=self.opcodes,
            exceptions=exceptions,
            attributes=[
                line_number_table
            ]
        )

    def transpile(self):
        return self.transpile_code()
