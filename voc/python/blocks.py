import ast
import dis

from ..java import (
    Code as JavaCode, ExceptionInfo as JavaExceptionInfo, LineNumberTable,
    opcodes as JavaOpcodes, Classref
)
from .utils import (
    TRY, CATCH, END_TRY,
    jump, resolve_jump, Ref,
    ICONST_val, ALOAD_name, ASTORE_name,
)


class IgnoreBlock(Exception):
    """An escape hatch; enable a block to be flagged as ignorable"""
    pass


class Block:
    def __init__(self, parent=None, commands=None, verbosity=0):
        self.parent = parent
        self.commands = commands if commands else []
        self.verbosity = verbosity

        self.local_vars = {}
        self.deleted_vars = set()

        self.generator = None
        self.yield_points = []

        self.opcodes = []
        self.try_catches = []
        self.blocks = []
        self.jumps = []
        self.loops = []
        self.jump_targets = {}
        self.unknown_jump_targets = {}
        self.returns = {
            'annotation': None
        }

        self.next_resolve_list = []
        self.next_opcode_starts_line = None

    @property
    def module(self):
        return self.parent

    def store_name(self, name, use_locals):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def store_dynamic(self):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def load_name(self, name, use_locals):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    def delete_name(self, name, use_locals):
        raise NotImplementedError('Abstract class `block` cannot be used directly.')

    @property
    def can_ignore_empty(self):
        return False

    def add_opcodes(self, *opcodes):
        # Add the opcodes to the code list and process them.
        for opcode in opcodes:
            # print("ADD OPCODE", id(opcode), opcode)
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
            ICONST_val(value),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', '(I)V'),
        )

    def add_float(self, value):
        self.add_opcodes(
            JavaOpcodes.NEW('org/python/types/Float'),
            JavaOpcodes.DUP(),
            ICONST_val(value),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Float', '<init>', '(D)V'),
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
                        ICONST_val(value),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', '(I)V'),
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

                # elif isinstance(value, bytes):
                #     self.add_opcodes(
                #         JavaOpcodes.NEW('org/python/types/Bytes'),
                #         JavaOpcodes.DUP(),
                #         JavaOpcodes.LDC_W(value),
                #         JavaOpcodes.INVOKESPECIAL('org/python/types/Bytes', '<init>', '(Ljava/lang/String;)V'),
                #     )

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

    def add_callable(self, function_def, method, closure=False):

        # We need the code object for the AST function definition.
        # Create and compile a module that only contains the function def;
        # the sixth last instruction will be a LOAD_CONST of the code
        # object for the function being defined.
        #   ...
        #   LOAD_CONST     (<code object>)
        #   LOAD_CONST     'function_name'
        #   MAKE_FUNCTION
        #   STORE_NAME     function_name
        #   LOAD_CONST     None
        #   RETURN_VALUE
        compiled = compile(
            ast.Module(body=[function_def]),
            filename=self.module.sourcefile,
            mode='exec'
        )
        code = list(dis.get_instructions(compiled))[-6].argval

        # Evaluate the full method name
        full_method_name = function_def.name.replace('.<locals>.', '$')
        if full_method_name.endswith('<listcomp>'):
            full_method_name = full_method_name.replace('<listcomp>', 'listcomp_%x' % id(self))
        elif full_method_name.endswith('<dictcomp>'):
            full_method_name = full_method_name.replace('<dictcomp>', 'dictcomp_%x' % id(self))
        elif full_method_name.endswith('<setcomp>'):
            full_method_name = full_method_name.replace('<setcomp>', 'setcomp_%x' % id(self))
        elif full_method_name.endswith('<genexpr>'):
            full_method_name = full_method_name.replace('<genexpr>', 'genexpr_%x' % id(self))

        self.add_opcodes(
            TRY(),
                # Wrap that Method into a Callable.
                JavaOpcodes.NEW('org/python/types/Function'),
                JavaOpcodes.DUP(),
        )

        self.add_str(full_method_name)

        # Add the code object
        self.add_opcodes(
                JavaOpcodes.NEW('org/python/types/Code'),
                JavaOpcodes.DUP(),
        )

        self.add_int(code.co_argcount)
        self.add_tuple(code.co_cellvars)

        self.add_opcodes(
                JavaOpcodes.ACONST_NULL(),  # co_code
        )

        # self.add_tuple(code.co_consts)
        self.add_opcodes(
                JavaOpcodes.ACONST_NULL(),  # co_consts
        )

        self.add_str(code.co_filename)
        self.add_int(code.co_firstlineno)
        self.add_int(code.co_flags)
        self.add_tuple(code.co_freevars)
        self.add_int(code.co_kwonlyargcount)

        self.add_opcodes(
                JavaOpcodes.ACONST_NULL(),  # co_lnotab
        )

        self.add_str(code.co_name)
        self.add_tuple(code.co_names)
        self.add_int(code.co_nlocals)
        self.add_int(code.co_stacksize)
        self.add_tuple(code.co_varnames)

        self.add_opcodes(
                JavaOpcodes.INVOKESPECIAL('org/python/types/Code', '<init>', '(Lorg/python/types/Int;Lorg/python/types/Tuple;Lorg/python/types/Bytes;Lorg/python/types/Tuple;Lorg/python/types/Str;Lorg/python/types/Int;Lorg/python/types/Int;Lorg/python/types/Tuple;Lorg/python/types/Int;Lorg/python/types/Bytes;Lorg/python/types/Str;Lorg/python/types/Tuple;Lorg/python/types/Int;Lorg/python/types/Int;Lorg/python/types/Tuple;)V'),

                # Get a Method representing the new function
                JavaOpcodes.LDC_W(Classref(method.parent.class_descriptor)),
                JavaOpcodes.LDC_W(method.name),

                ICONST_val(len(method.parameters)),
                JavaOpcodes.ANEWARRAY('java/lang/Class'),
        )

        for i, param in enumerate(method.parameters):
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

        # # Default arguments list
        # for argument in arguments[:opcode.default_args]:
        #     self.add_opcodes(
        #         JavaOpcodes.DUP(),
        #     )

        #     argument.operation.transpile(self, argument.arguments)

        #     self.add_opcodes(
        #         JavaOpcodes.INVOKEINTERFACE('java/util/List', 'add', '(Ljava/lang/Object;)Z'),
        #         JavaOpcodes.POP(),
        #     )

        # Default keyword arguments list
        self.add_opcodes(
                JavaOpcodes.NEW('java/util/HashMap'),
                JavaOpcodes.DUP(),
                JavaOpcodes.INVOKESPECIAL('java/util/HashMap', '<init>', '()V'),
        )

        # for name, argument in zip(
        #                 arguments[opcode.default_args:opcode.default_args + opcode.default_kwargs * 2:2],
        #                 arguments[opcode.default_args + 1:opcode.default_args + opcode.default_kwargs * 2 + 1:2]):
        #     self.add_opcodes(
        #         JavaOpcodes.DUP(),
        #         JavaOpcodes.LDC_W(name.operation.const),
        #     )

        #     argument.operation.transpile(self, argument.arguments)

        #     self.add_opcodes(
        #         JavaOpcodes.INVOKEVIRTUAL('java/util/HashMap', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
        #         JavaOpcodes.POP(),
        #     )

        # Closure
        if closure:
            closure_arg = arguments[-3]
            closure_arg.operation.transpile(self, closure_arg.arguments)
        else:
            self.add_opcodes(
                JavaOpcodes.ACONST_NULL(),
            )

        self.add_opcodes(
                JavaOpcodes.INVOKESPECIAL('org/python/types/Function', '<init>', '(Lorg/python/types/Str;Lorg/python/types/Code;Ljava/lang/reflect/Method;Ljava/util/Map;Ljava/util/List;Ljava/util/Map;Ljava/util/List;)V'),

            CATCH('java/lang/NoSuchMethodError'),
                ASTORE_name(self, '#EXCEPTION#'),
                JavaOpcodes.NEW('org/python/exceptions/RuntimeError'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W('Unable to find MAKE_FUNCTION output %s.%s' % (method.parent.descriptor, full_method_name)),
                JavaOpcodes.INVOKESPECIAL('org/python/exceptions/RuntimeError', '<init>', '(Ljava/lang/String;)V'),
                JavaOpcodes.ATHROW(),
            END_TRY()
        )

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

    def materialize(self):
        for cmd in self.commands:
            cmd.materialize(self)

    def transpile_setup(self):
        """Tweak the bytecode generated for this block."""
        pass

    def transpile_teardown(self):
        """Tweak the bytecode generated for this block."""
        pass

    def transpile_commands(self):
        """Create a JavaCode object representing the commands stored in the block

        May raise ``IgnoreBlock`` if the block should be ignored.
        """
        argument_vars = len(self.local_vars)

        # Insert content that needs to occur before the main block commands
        self.transpile_setup()

        # Convert the sequence of commands into instructions.
        # Most of the instructions will be opcodes. However, some will
        # be instructions to add exception blocks, line number references, etc
        for cmd in self.commands:
            cmd.transpile(self)

        # Insert content that needs to occur after the main block commands
        self.transpile_teardown()

        # Install the shortcut jump points for yield statements.
        yield_jumps = []

        for i, yield_point in enumerate(self.yield_points):
            yield_jumps.extend([
                ALOAD_name(self, '<generator>'),
                JavaOpcodes.GETFIELD('org/python/types/Generator', 'yield_point', 'I'),
                ICONST_val(i + 1),
                jump(JavaOpcodes.IF_ICMPEQ(0), self, Ref(self, yield_point), Opcode.YIELD)
            ])

        self.opcodes = yield_jumps + self.opcodes

        # Make sure every local variable slot has been initialized
        # as an object. This is needed because Python allows a variable
        # to be instantiated in a sub-block, and used outside that block.
        # The JVM doesn't, and raises a verify error if you try. By
        # initializing all variables, we can trick the verifier.
        # TODO: Ideally, we'd only initialize the variables that are ambiguous.
        init_vars = []
        for i in range(argument_vars, len(self.local_vars) + len(self.deleted_vars)):
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
                        handler.catch_end_op.java_offset,
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
            max_locals=len(self.local_vars) + len(self.deleted_vars),
            code=self.opcodes,
            exceptions=exceptions,
            attributes=[
                line_number_table
            ]
        )

    def transpile(self):
        return self.transpile_commands()
