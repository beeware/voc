from ..java import (
    Code as JavaCode, ExceptionInfo as JavaExceptionInfo, LineNumberTable,
    opcodes as JavaOpcodes, Classref
)
from .utils import (
    ArgType, OpcodePosition,
    TRY, CATCH, END_TRY,
    jump, resolve_jump,
    ICONST_val, LCONST_val, DCONST_val, ALOAD_name, ASTORE_name, free_name
)


class IgnoreBlock(Exception):
    """An escape hatch; enable a block to be flagged as ignorable"""
    pass


class Block:
    def __init__(self, parent=None, verbosity=0):
        self._parent = parent
        self.verbosity = verbosity

        self.has_self = False
        self.parameters = []
        self.local_vars = {}
        self.deleted_vars = set()
        self.symbols = {}

        self.generator = None
        self.yield_points = []

        self.opcodes = []
        self.try_catches = []
        self.blocks = []
        self.jumps = []
        self.loops = []
        self.unknown_jump_targets = {}
        self.returns = {
            'annotation': None
        }

        self.next_resolve_list = []
        self.next_opcode_starts_line = None

    @property
    def active_local_vars(self):
        return {
            name: index
            for name, index in self.local_vars.items()
            if index is not None
        }

    def store_name(self, name):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def store_dynamic(self):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def load_name(self, name):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def delete_name(self, name):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    @property
    def can_ignore_empty(self):
        return False

    def add_opcodes(self, *opcodes):
        # Add the opcodes to the code list and process them.
        for opcode in opcodes:
            if opcode.process(self):
                # self.opcodes.extend([
                #     JavaOpcodes.LDC_W(str(opcode)),
                #     JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V')
                # ])

                self.opcodes.append(opcode)

                # If we've flagged a code line change, attach that to the opcode
                if self.next_opcode_starts_line:
                    opcode.starts_line = self.next_opcode_starts_line
                    self.next_opcode_starts_line = None

                # Resolve any references to the "next" opcode.
                for (obj, attr) in self.next_resolve_list:
                    # print("        resolve %s reference on %s %s with %s %s" % (attr, obj, id(obj), opcode, id(opcode)))
                    setattr(obj, attr.value, opcode)

                self.next_resolve_list = []

    def add_str(self, value):
        self.add_opcodes(
            JavaOpcodes.NEW('org/python/types/Str'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(value),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),
        )

    def add_int(self, value):
        self.add_opcodes(
            JavaOpcodes.NEW('org/python/types/Int'),
            JavaOpcodes.DUP(),
            LCONST_val(value),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', '(J)V'),
        )

    def add_float(self, value):
        self.add_opcodes(
            JavaOpcodes.NEW('org/python/types/Float'),
            JavaOpcodes.DUP(),
            DCONST_val(value),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Float', '<init>', '(D)V'),
        )

    def add_complex(self, value):
        self.add_opcodes(
            JavaOpcodes.NEW('org/python/types/Complex'),
            JavaOpcodes.DUP(),
            DCONST_val(value.imag),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Complex', '<init>', '(D)V'),
        )

    def add_tuple(self, data):
        self.add_opcodes(
            JavaOpcodes.NEW('org/python/types/Tuple'),
            JavaOpcodes.DUP(),

            JavaOpcodes.NEW('java/util/ArrayList'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('java/util/ArrayList', '<init>', '()V'),
        )

        for value in data:
            self.add_opcodes(
                JavaOpcodes.DUP(),
            )

            if value is None:
                self.add_opcodes(
                    JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;')
                )
            else:
                if isinstance(value, bool):
                    self.add_opcodes(
                        JavaOpcodes.NEW('org/python/types/Bool'),
                        JavaOpcodes.DUP(),
                        ICONST_val(value),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', '(Z)V'),
                    )

                elif isinstance(value, int):
                    self.add_opcodes(
                        JavaOpcodes.NEW('org/python/types/Int'),
                        JavaOpcodes.DUP(),
                        LCONST_val(value),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', '(J)V'),
                    )

                elif isinstance(value, float):
                    self.add_opcodes(
                        JavaOpcodes.NEW('org/python/types/Float'),
                        JavaOpcodes.DUP(),
                        JavaOpcodes.LDC2_W(value),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Float', '<init>', '(D)V'),
                    )

                elif isinstance(value, str):
                    self.add_opcodes(
                        JavaOpcodes.NEW('org/python/types/Str'),
                        JavaOpcodes.DUP(),
                        JavaOpcodes.LDC_W(value),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),
                    )

                elif isinstance(value, bytes):
                    self.add_opcodes(
                        JavaOpcodes.NEW('org/python/types/Bytes'),
                        JavaOpcodes.DUP(),
                        JavaOpcodes.LDC_W(value),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Bytes', '<init>', '(Ljava/lang/String;)V'),
                    )

                elif isinstance(value, tuple):
                    self.add_tuple(value)

                else:
                    raise RuntimeError("Unknown constant type %s" % type(value))

            self.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE('java/util/List', 'add', '(Ljava/lang/Object;)Z'),
                JavaOpcodes.POP()
            )

        self.add_opcodes(
            JavaOpcodes.INVOKESPECIAL('org/python/types/Tuple', '<init>', '(Ljava/util/List;)V'),
        )

    def add_callable(self, function, closure=False):
        self.add_opcodes(
            TRY(),
                # Wrap that function into a Callable.
                JavaOpcodes.NEW('org/python/types/Function'),
                JavaOpcodes.DUP(),
        )

        self.add_str(function.name)

        # Add the code object
        self.add_opcodes(
                JavaOpcodes.NEW('org/python/types/Code'),
                JavaOpcodes.DUP(),
        )

        self.add_int(function.code.co_argcount)
        self.add_tuple(function.code.co_cellvars)

        self.add_opcodes(
                JavaOpcodes.ACONST_NULL(),  # co_code
        )

        # self.add_tuple(function.code.co_consts)
        self.add_opcodes(
                JavaOpcodes.ACONST_NULL(),  # co_consts
        )

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
                JavaOpcodes.INVOKESPECIAL('org/python/types/Code', '<init>', '(Lorg/python/types/Int;Lorg/python/types/Tuple;Lorg/python/types/Bytes;Lorg/python/types/Tuple;Lorg/python/types/Str;Lorg/python/types/Int;Lorg/python/types/Int;Lorg/python/types/Tuple;Lorg/python/types/Int;Lorg/python/types/Bytes;Lorg/python/types/Str;Lorg/python/types/Tuple;Lorg/python/types/Int;Lorg/python/types/Int;Lorg/python/types/Tuple;)V'),

                # Get a Java Method representing the new function
                JavaOpcodes.LDC_W(Classref(function.class_descriptor)),
                JavaOpcodes.LDC_W(function.java_name),

                ICONST_val(len(function.parameters)),
                JavaOpcodes.ANEWARRAY('java/lang/Class'),
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
                # JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),
                JavaOpcodes.ACONST_NULL(),  # globals

                # Default args
                JavaOpcodes.NEW('java/util/ArrayList'),
                JavaOpcodes.DUP(),
                JavaOpcodes.INVOKESPECIAL('java/util/ArrayList', '<init>', '()V'),
        )

        # Default arguments list
        for arg in function.parameters:
            if arg['kind'] == ArgType.POSITIONAL_OR_KEYWORD and arg['default']:
                self.add_opcodes(
                    JavaOpcodes.DUP(),
                    ALOAD_name(self, arg['default']),
                    JavaOpcodes.INVOKEINTERFACE('java/util/List', 'add', '(Ljava/lang/Object;)Z'),
                    JavaOpcodes.POP(),
                )

        # Default keyword arguments list
        self.add_opcodes(
                JavaOpcodes.NEW('java/util/HashMap'),
                JavaOpcodes.DUP(),
                JavaOpcodes.INVOKESPECIAL('java/util/HashMap', '<init>', '()V'),
        )

        for arg in function.parameters:
            if arg['kind'] == ArgType.POSITIONAL_OR_KEYWORD and arg['default']:
                self.add_opcodes(
                    JavaOpcodes.DUP(),
                    JavaOpcodes.LDC_W(arg['name']),
                    ALOAD_name(self, arg['default']),
                    JavaOpcodes.INVOKEVIRTUAL('java/util/HashMap', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
                    JavaOpcodes.POP(),
                )

        # Closure. This is created and assigned when the function is accessed.
        self.add_opcodes(
            JavaOpcodes.ACONST_NULL(),
        )

        self.add_opcodes(
                JavaOpcodes.INVOKESPECIAL('org/python/types/Function', '<init>', '(Lorg/python/types/Str;Lorg/python/types/Code;Ljava/lang/reflect/Method;Ljava/util/Map;Ljava/util/List;Ljava/util/Map;Lorg/python/types/Closure;)V'),

            CATCH('java/lang/NoSuchMethodError'),
                ASTORE_name(self, '#EXCEPTION#'),
                JavaOpcodes.NEW('org/python/exceptions/RuntimeError'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W('Unable to find MAKE_FUNCTION output %s.%s' % (function.class_descriptor, function.name)),
                JavaOpcodes.INVOKESPECIAL('org/python/exceptions/RuntimeError', '<init>', '(Ljava/lang/String;)V'),
                JavaOpcodes.ATHROW(),
            END_TRY()
        )
        free_name(self, '#EXCEPTION#')

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
        yield_jumps = []

        for i, yield_point in enumerate(self.yield_points):
            yield_jumps.extend([
                ALOAD_name(self, '<generator>'),
                JavaOpcodes.GETFIELD('org/python/types/Generator', 'yield_point', 'I'),
                ICONST_val(i + 1),
                jump(JavaOpcodes.IF_ICMPEQ(0), self, yield_point, OpcodePosition.YIELD)
            ])

        self.opcodes = yield_jumps + self.opcodes

        # Make sure every local variable slot has been initialized
        # as an object. This is needed because Python allows a variable
        # to be instantiated in a sub-block, and used outside that block.
        # The JVM doesn't, and raises a verify error if you try. By
        # initializing all variables, we can trick the verifier.
        # TODO: Ideally, we'd only initialize the variables that are ambiguous.
        init_vars = []
        for i in range(len(self.parameters) + (1 if self.has_self else 0), len(self.active_local_vars) + len(self.deleted_vars)):
            if i == 0:
                opcode = JavaOpcodes.ASTORE_0()
            elif i == 1:
                opcode = JavaOpcodes.ASTORE_1()
            elif i == 2:
                opcode = JavaOpcodes.ASTORE_2()
            elif i == 3:
                opcode = JavaOpcodes.ASTORE_3()
            else:
                opcode = JavaOpcodes.ASTORE(i)
            init_vars.extend([
                JavaOpcodes.ACONST_NULL(),
                opcode
            ])

        self.opcodes = init_vars + self.opcodes

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
                # print("  FINALLY", try_catch.finally_handler.start_op.java_offset, try_catch.finally_handler.end_op.java_offset)
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
            max_stack=self.stack_depth() + len(exceptions),
            max_locals=len(self.active_local_vars) + len(self.deleted_vars),
            code=self.opcodes,
            exceptions=exceptions,
            attributes=[
                line_number_table
            ]
        )

    def transpile(self):
        return self.transpile_code()
