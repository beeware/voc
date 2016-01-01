from ..java import (
    Code as JavaCode,
    Method as JavaMethod,
    opcodes as JavaOpcodes,
    RuntimeVisibleAnnotations,
    Annotation,
    ConstantElementValue,
)

from .blocks import Block
from .opcodes import (
    ALOAD_name, ASTORE_name, free_name,
    ILOAD_name, FLOAD_name, DLOAD_name,
    ICONST_val,
    Opcode, TRY, CATCH, END_TRY,
)

POSITIONAL_OR_KEYWORD = 1
VAR_POSITIONAL = 2
KEYWORD_ONLY = 3
VAR_KEYWORD = 4

CO_VARARGS = 0x0004
CO_VARKEYWORDS = 0x0008


def descriptor(annotation):
    if annotation == 'bool':
        return 'Z'
    elif annotation == 'byte':
        return 'B'
    elif annotation == 'char':
        return 'C'
    elif annotation == 'short':
        return 'S'
    elif annotation == 'int':
        return 'I'
    elif annotation == 'long':
        return 'J'
    elif annotation == 'float':
        return 'F'
    elif annotation == 'double':
        return 'D'
    elif annotation is None or annotation == 'void':
        return 'V'
    else:
        return 'L%s;' % annotation.replace('.', '/')


class Method(Block):
    def __init__(self, parent, name, parameters, returns=None, static=False, commands=None):
        super().__init__(parent, commands=commands)
        self.name = name
        self.parameters = parameters

        if returns is None:
            self.returns = {
                'annotation': 'org/python/Object'
            }
        else:
            self.returns = returns

        # Reserve space for the register that will hold self (if required)
        self.add_self()

        # Reserve space for the registers that will hold arguments.
        for i, param in enumerate(self.parameters):
            self.local_vars[param['name']] = len(self.local_vars)

        self.static = static

    def __repr__(self):
        return '<Method %s (%s parameters)>' % (self.name, len(self.parameters))

    @property
    def is_constructor(self):
        return False

    @property
    def is_closuremethod(self):
        return False

    @property
    def globals_module(self):
        return self.module

    def add_self(self):
        pass

    def store_name(self, name, use_locals):
        if use_locals:
            self.add_opcodes(
                ASTORE_name(self, name)
            )
        else:
            self.add_opcodes(
                ASTORE_name(self, '#value'),

                JavaOpcodes.GETSTATIC('org/python/ImportLib', 'modules', 'Ljava/util/Map;'),

                JavaOpcodes.LDC_W(self.globals_module.descriptor),
                JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),
                JavaOpcodes.CHECKCAST('org/python/types/Module'),

                JavaOpcodes.LDC_W(name),
                ALOAD_name(self, '#value'),

                JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__setattr__', '(Ljava/lang/String;Lorg/python/Object;)V'),
            )
            free_name(self, '#value')

    def store_dynamic(self):
        raise NotImplementedError('Methods cannot dynamically store variables.')

    def load_name(self, name, use_locals):
        if use_locals:
            try:
                self.add_opcodes(
                    ALOAD_name(self, name)
                )
                return
            except KeyError:
                pass

        self.add_opcodes(
            JavaOpcodes.GETSTATIC('org/python/ImportLib', 'modules', 'Ljava/util/Map;'),
            JavaOpcodes.LDC_W(self.globals_module.descriptor),

            JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            JavaOpcodes.LDC_W(name),

            JavaOpcodes.INVOKEVIRTUAL('org/python/types/Module', '__getattribute__', '(Ljava/lang/String;)Lorg/python/Object;'),
        )

    def delete_name(self, name):
        try:
            free_name(name)
        except KeyError:
            self.add_opcodes(
                JavaOpcodes.GETSTATIC('org/python/ImportLib', 'modules', 'Ljava/util/Map;'),
                JavaOpcodes.LDC_W(self.globals_module.descriptor),
                JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),
                JavaOpcodes.CHECKCAST('org/python/types/Module'),

                JavaOpcodes.LDC_W(name),

                JavaOpcodes.INVOKEVIRTUAL('org/python/types/Module', '__delattr__', '(Ljava/lang/String;)Lorg/python/Object;'),
            )

    @property
    def can_ignore_empty(self):
        return False

    @property
    def signature(self):
        return_descriptor = 'Lorg/python/Object;'
        return '(%s)%s' % (
            ''.join('Lorg/python/Object;' for p in self.parameters),
            return_descriptor
        )

    @property
    def method_name(self):
        return self.name

    @property
    def module(self):
        return self.parent

    def add_method(self, method_name, code, annotations):
        # If a method is added to a method, it is added as an anonymous
        # inner class.
        from .klass import ClosureClass
        callable = ClosureClass(
            parent=self.parent,
            name='%s$%s' % (self.parent.name, method_name.replace('.<locals>.', '$')),
            closure_var_names=code.co_names,
            bases=['org/python/types/Closure'],
            implements=['org/python/Callable'],
            public=True,
            final=True,
        )

        method = ClosureMethod(
            callable,
            name='invoke',
            parameters=extract_parameters(code, annotations),
            returns={
                'annotation': annotations.get('return', 'org/python/Object').replace('.', '/')
            }
        )
        method.extract(code)
        callable.methods.append(method)

        callable.fields = dict(
            (name, 'Lorg/python/Object;')
            for name in code.co_names
        )

        self.parent.classes.append(callable)

        return method

    def transpile_teardown(self):
        if len(self.opcodes) == 0 or not isinstance(self.opcodes[-1], (JavaOpcodes.RETURN, JavaOpcodes.ARETURN)):
            self.add_opcodes(JavaOpcodes.ARETURN())

    def method_attributes(self):
        return [
            RuntimeVisibleAnnotations([
                Annotation(
                    'Lorg/python/Method;',
                    {
                        '__doc__': ConstantElementValue("Python method (insert docs here)")
                    }
                )
            ])
        ]

    def transpile_method(self):
        return [
            JavaMethod(
                self.method_name,
                self.signature,
                static=self.static,
                attributes=[super().transpile()] + self.method_attributes()
            )
        ]

    def transpile_wrapper(self):
        return []

    def transpile(self):
        return self.transpile_method() + self.transpile_wrapper()


class InitMethod(Method):
    def __init__(self, parent):
        super().__init__(
            parent, '<init>',
            parameters=[
                {
                    'name': 'self',
                    'kind': POSITIONAL_OR_KEYWORD,
                    'annotation': 'org/python/Object'
                },
                {
                    'name': 'args',
                    'kind': POSITIONAL_OR_KEYWORD,
                    'annotation': '[Lorg/python/Object;'
                },
                {
                    'name': 'kwargs',
                    'kind': POSITIONAL_OR_KEYWORD,
                    'annotation': 'java/util/Map'
                }
            ],
            returns={'annotation': None},
        )

    def __repr__(self):
        return '<Constructor %s (%s parameters)>' % (self.klass.name, len(self.parameters))

    @property
    def is_constructor(self):
        return True

    @property
    def klass(self):
        return self.parent

    @property
    def module(self):
        return self.klass.module

    @property
    def can_ignore_empty(self):
        return False

    @property
    def signature(self):
        return '([Lorg/python/Object;Ljava/util/Map;)V'

    def transpile_setup(self):
        if self.klass.extends:
            super_class = self.klass.extends

            self.add_opcodes(
                JavaOpcodes.ALOAD_0(),
                # TODO - this only allows using the default constructor
                # for extended Java classes.
                JavaOpcodes.INVOKESPECIAL(super_class, '<init>', '()V'),
            )

        else:
            super_class = 'org/python/types/Object'

            self.add_opcodes(
                JavaOpcodes.ALOAD_0(),
                JavaOpcodes.ALOAD_1(),
                JavaOpcodes.ALOAD_2(),
                JavaOpcodes.INVOKESPECIAL(super_class, '<init>', '([Lorg/python/Object;Ljava/util/Map;)V'),
            )

    def transpile_teardown(self):
        self.add_opcodes(
            JavaOpcodes.RETURN()
        )


class InstanceMethod(Method):
    def __init__(self, parent, name, parameters, returns=None, static=False, commands=None):
        super().__init__(
            parent, name,
            parameters=parameters,
            returns=returns,
            static=static,
            commands=commands,
        )

    def __repr__(self):
        return '<InstanceMethod %s.%s (%s parameters)>' % (self.klass.name, self.name, len(self.parameters))

    @property
    def klass(self):
        return self.parent

    @property
    def module(self):
        return self.klass.module

    @property
    def bound_signature(self):
        return_descriptor = descriptor(self.returns.get('annotation'))
        return '(%s)%s' % (
            ''.join(descriptor(p['annotation']) for p in self.parameters[1:]),
            return_descriptor
        )

    def transpile_wrapper(self):
        # The first register holds "self"; since the binding is only
        # invoked via a native call, wrap it in a Java Object - unless
        # the object is an extension type, in which case the wrapper
        # object should already exist.
        binding_opcodes = [
            # JavaOpcodes.LDC_W("BINDING FOR " + self.name + self.signature),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

            # JavaOpcodes.LDC_W("BOUND AS " + self.name + self.bound_signature),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

            # JavaOpcodes.LDC_W("BINDING SELF IN"),
            # JavaOpcodes.ALOAD_0(),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;Ljava/lang/Object;)V'),

            JavaOpcodes.ALOAD_0(),
            JavaOpcodes.INSTANCEOF('org/python/Object'),
            JavaOpcodes.IFNE(36),  # 3

            # JavaOpcodes.LDC_W("CHECK FOR __VOC__ FIELD"),  # 3
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),  # 3

                JavaOpcodes.ALOAD_0(),  # 1

                JavaOpcodes.INVOKEVIRTUAL('java/lang/Object', 'getClass', '()Ljava/lang/Class;'),  # 3
                JavaOpcodes.LDC_W("__VOC__"),  # 3
                JavaOpcodes.INVOKEVIRTUAL('java/lang/Class', 'getField', '(Ljava/lang/String;)Ljava/lang/reflect/Field;'),  # 3

                JavaOpcodes.DUP(),  # 1
                JavaOpcodes.IFNONNULL(10),  # 3

                    # JavaOpcodes.LDC_W("NON NULL FIELD VALUE"),  # 3
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),  # 3

                    JavaOpcodes.ALOAD_0(),  # 1
                    JavaOpcodes.INVOKEVIRTUAL('java/lang/reflect/Field', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),  # 3

                    JavaOpcodes.GOTO(16),  # 3

                # else

                    # JavaOpcodes.LDC_W("NULL FIELD VALUE"),  # 3
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),  # 3

                    JavaOpcodes.POP(),  # 1
                    JavaOpcodes.NEW('org/python/java/Object'),  # 3
                    JavaOpcodes.DUP(),  # 1
                    JavaOpcodes.ALOAD_0(),  # 1
                    JavaOpcodes.INVOKESPECIAL('org/python/java/Object', '<init>', '(Ljava/lang/Object;)V'),  # 3

                    JavaOpcodes.GOTO(4),  # 3

            # else
                JavaOpcodes.ALOAD_0(),  # 1

            # JavaOpcodes.DUP(),
            # JavaOpcodes.LDC_W("BINDING SELF OUT"),
            # JavaOpcodes.SWAP(),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;Ljava/lang/Object;)V'),
        ]

        # Then extract each argument, converting to Python types as required.
        for i, param in enumerate(self.parameters[1:]):
            annotation = param.get('annotation', 'org/python/Object')

            if annotation is None:
                raise Exception("Parameters can't be void")
            elif annotation == "bool":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

                    ILOAD_name(self, param['name']),
                    JavaOpcodes.IFNE(9),
                        JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;'),
                        JavaOpcodes.GOTO(11),
                    # else
                        JavaOpcodes.NEW('org/python/types/Bool'),
                        JavaOpcodes.DUP(),
                        ILOAD_name(self, param['name']),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', '(Z)V'),
                    # endif
                ])
            elif annotation == "byte":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

                    ILOAD_name(self, param['name']),
                    JavaOpcodes.IFNE(9),
                        JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;'),
                        JavaOpcodes.GOTO(11),
                    # else
                        JavaOpcodes.NEW('org/python/types/Int'),
                        JavaOpcodes.DUP(),
                        ILOAD_name(self, param['name']),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', '(B)V'),
                    # endif
                ])
            elif annotation == 'char':
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

                    ILOAD_name(self, param['name']),
                    JavaOpcodes.IFNE(9),
                        JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;'),
                        JavaOpcodes.GOTO(11),
                    # else
                        JavaOpcodes.NEW('org/python/types/Str'),
                        JavaOpcodes.DUP(),
                        ILOAD_name(self, param['name']),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(C)V'),
                    # endif
                    # ASTORE_name(self, param['name'])
                ])
            elif annotation == "short":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

                    ILOAD_name(self, param['name']),
                    JavaOpcodes.IFNE(9),
                        JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;'),
                        JavaOpcodes.GOTO(11),
                    # else
                        JavaOpcodes.NEW('org/python/types/Int'),
                        JavaOpcodes.DUP(),
                        ILOAD_name(self, param['name']),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', '(S)V'),
                    # endif
                ])
            elif annotation == "int":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

                    ILOAD_name(self, param['name']),
                    JavaOpcodes.IFNE(9),
                        JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;'),
                        JavaOpcodes.GOTO(11),
                    # else
                        JavaOpcodes.NEW('org/python/types/Int'),
                        JavaOpcodes.DUP(),
                        ILOAD_name(self, param['name']),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', '(I)V'),
                    # endif
                ])
            elif annotation == "long":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

                    ILOAD_name(self, param['name']),
                    JavaOpcodes.IFNE(9),
                        JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;'),
                        JavaOpcodes.GOTO(11),
                    # else
                        JavaOpcodes.NEW('org/python/types/Int'),
                        JavaOpcodes.DUP(),
                        ILOAD_name(self, param['name']),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', '(J)V'),
                    # endif
                ])
            elif annotation == "float":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

                    FLOAD_name(self, param['name']),
                    JavaOpcodes.IFNE(9),
                        JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;'),
                        JavaOpcodes.GOTO(11),
                    # else
                        JavaOpcodes.NEW('org/python/types/Float'),
                        JavaOpcodes.DUP(),
                        FLOAD_name(self, param['name']),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Float', '<init>', '(F)V'),
                    # endif
                ])
            elif annotation == "double":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

                    DLOAD_name(self, param['name']),
                    JavaOpcodes.IFNE(9),
                        JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;'),
                        JavaOpcodes.GOTO(11),
                    # else
                        JavaOpcodes.NEW('org/python/types/Float'),
                        JavaOpcodes.DUP(),
                        DLOAD_name(self, param['name']),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Float', '<init>', '(D)V'),
                    # endif
                ])
            elif annotation == "java/lang/String":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

                    ALOAD_name(self, param['name']),
                    JavaOpcodes.ACONST_NULL(),
                    JavaOpcodes.IF_ACMPNE(9),
                        JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;'),
                        JavaOpcodes.GOTO(11),
                    # else
                        JavaOpcodes.NEW('org/python/types/Str'),
                        JavaOpcodes.DUP(),
                        ALOAD_name(self, param['name']),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),
                    # endif
                ])
            elif annotation != 'org/python/Object':
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT generic %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),

                    ALOAD_name(self, param['name']),
                    JavaOpcodes.ACONST_NULL(),
                    JavaOpcodes.IF_ACMPNE(9),
                        JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;'),
                        JavaOpcodes.GOTO(11),
                    # else
                        JavaOpcodes.NEW('org/python/java/Object'),
                        JavaOpcodes.DUP(),
                        ALOAD_name(self, param['name']),
                        # JavaOpcodes.INVOKEINTERFACE('org/python/Object', 'toJava', '()Ljava/lang/Object;'),
                        JavaOpcodes.INVOKESPECIAL('org/python/java/Object', '<init>', '(Ljava/lang/Object;)V'),
                    # endif
                ])
            else:  # org/python/Object; no transformation required
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s - PASS AS IS" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),
                    ALOAD_name(self, param['name']),
                ])

            # self.add_opcodes(
            #     JavaOpcodes.LDC_W("INPUT %s TRANSFORMED" % (i)),
            #     JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),
            # )
        # self.add_opcodes(
        #     JavaOpcodes.LDC_W("INPUTS TRANSFORMED"),
        #     JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),
        # )

        # Then call the method, and process the return type.
        binding_opcodes.extend([
            JavaOpcodes.INVOKESTATIC(self.klass.descriptor, self.name, self.signature),
        ])

        # Now convert the return type to a native type.
        return_type = self.returns['annotation']

        if return_type == 'void':
            binding_opcodes.extend([
                JavaOpcodes.POP(),
                JavaOpcodes.RETURN()
            ])
        elif return_type == 'bool':
            binding_opcodes.extend([
                JavaOpcodes.CHECKCAST('org/python/types/Bool'),
                JavaOpcodes.GETFIELD('org/python/types/Bool', 'value', 'Z'),
                JavaOpcodes.IRETURN(),
            ])
        elif return_type == 'byte':
            binding_opcodes.extend([
                JavaOpcodes.CHECKCAST('org/python/types/Int'),
                JavaOpcodes.GETFIELD('org/python/types/Int', 'value', 'J'),
                JavaOpcodes.L2I(),
                JavaOpcodes.I2B(),
                JavaOpcodes.IRETURN(),
            ])
        elif return_type == 'char':
            binding_opcodes.extend([
                JavaOpcodes.INVOKEINTERFACE('org/python/Object', 'toJava', '()Ljava/lang/Object;'),
                JavaOpcodes.CHECKCAST('java/lang/String'),
                ICONST_val(0),
                JavaOpcodes.INVOKEVIRTUAL('java/lang/String', 'charAt', '(I)C'),
                JavaOpcodes.IRETURN(),
            ])
        elif return_type == 'short':
            binding_opcodes.extend([
                JavaOpcodes.CHECKCAST('org/python/types/Int'),
                JavaOpcodes.GETFIELD('org/python/types/Int', 'value', 'J'),
                JavaOpcodes.L2I(),
                JavaOpcodes.I2S(),
                JavaOpcodes.IRETURN(),
            ])
        elif return_type == 'int':
            binding_opcodes.extend([
                JavaOpcodes.CHECKCAST('org/python/types/Int'),
                JavaOpcodes.GETFIELD('org/python/types/Int', 'value', 'J'),
                JavaOpcodes.L2I(),
                JavaOpcodes.IRETURN(),
            ])
        elif return_type == 'long':
            binding_opcodes.extend([
                JavaOpcodes.CHECKCAST('org/python/types/Int'),
                JavaOpcodes.GETFIELD('org/python/types/Int', 'value', 'J'),
                JavaOpcodes.LRETURN(),
            ])
        elif return_type == 'float':
            binding_opcodes.extend([
                JavaOpcodes.CHECKCAST('org/python/types/Float'),
                JavaOpcodes.GETFIELD('org/python/types/Float', 'value', 'D'),
                JavaOpcodes.DTOF(),
                JavaOpcodes.FRETURN(),
            ])
        elif return_type == 'double':
            binding_opcodes.extend([
                JavaOpcodes.CHECKCAST('org/python/types/Float'),
                JavaOpcodes.GETFIELD('org/python/types/Float', 'value', 'D'),
                JavaOpcodes.DRETURN(),
            ])
        elif return_type != 'org/python/Object':
            binding_opcodes.extend([
                JavaOpcodes.INVOKEINTERFACE('org/python/Object', 'toJava', '()Ljava/lang/Object;'),
                JavaOpcodes.CHECKCAST(return_type.replace('.', '/')),
                JavaOpcodes.ARETURN(),
            ])
        else:
            binding_opcodes.extend([
                JavaOpcodes.ARETURN()
            ])

        # binding_opcodes.extend([
        #     JavaOpcodes.LDC_W("BINDING OUTPUT to type %s" % self.returns['annotation']),
        #     JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),
        # ])

        wrapper_methods = [
            JavaMethod(
                self.name,
                self.bound_signature,
                attributes=[
                    JavaCode(
                        max_stack=len(self.parameters) + 4,
                        max_locals=len(self.parameters),
                        code=binding_opcodes
                    )
                ]
            ),
        ]

        if self.klass.extends:
            # We also need to generate a manual call to the super
            super_opcodes = [
                JavaOpcodes.ALOAD_0(),
            ]

            # Then extract each argument:
            for i, param in enumerate(self.parameters[1:]):
                super_opcodes.append({
                        'bool': JavaOpcodes.ILOAD(i + 1),
                        'byte': JavaOpcodes.ILOAD(i + 1),
                        'char': JavaOpcodes.ILOAD(i + 1),
                        'short': JavaOpcodes.ILOAD(i + 1),
                        'int': JavaOpcodes.ILOAD(i + 1),
                        'long': JavaOpcodes.ILOAD(i + 1),
                        'float': JavaOpcodes.FLOAD(i + 1),
                        'double': JavaOpcodes.DLOAD(i + 1),
                    }.get(param['annotation'], JavaOpcodes.ALOAD(i + 1))
                )

                # super_opcodes.extend([
                #     JavaOpcodes.LDC_W("SUPER WRAPPER ARGUMENT %s to type %s" % (i, param['annotation'])),
                #     JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),
                # ])

            # Then call the method, and process the return type.
            super_opcodes.extend([
                JavaOpcodes.INVOKESPECIAL(self.klass.extends.replace('.', '/'), self.name, self.bound_signature),

                {
                    'void': JavaOpcodes.RETURN(),
                    'bool': JavaOpcodes.IRETURN(),
                    'byte': JavaOpcodes.IRETURN(),
                    'char': JavaOpcodes.IRETURN(),
                    'short': JavaOpcodes.IRETURN(),
                    'int': JavaOpcodes.IRETURN(),
                    'long': JavaOpcodes.IRETURN(),
                    'float': JavaOpcodes.FRETURN(),
                    'double': JavaOpcodes.DRETURN(),
                }.get(self.returns['annotation'], JavaOpcodes.ARETURN()),

                # JavaOpcodes.LDC_W("SUPER WRAPPER OUTPUT to type %s" % self.returns['annotation']),
                # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', '(Ljava/lang/String;)V'),
            ])

            wrapper_methods.append(
                JavaMethod(
                    self.name + "$super",
                    self.bound_signature,
                    attributes=[
                        JavaCode(
                            max_stack=len(self.parameters) + 2,
                            max_locals=len(self.parameters) + 2,
                            code=super_opcodes
                        )
                    ]
                )
            )

        return wrapper_methods


class MainMethod(Method):
    def __init__(self, parent, commands=None, end_offset=None):
        super().__init__(
            parent, '__main__',
            parameters=[{'name': 'args', 'annotation': 'argv'}],
            returns={'annotation': None},
            static=True,
            commands=commands,
        )
        self.end_offset = end_offset

    def __repr__(self):
        return '<MainMethod %s>' % self.module.name

    @property
    def method_name(self):
        return 'main'

    @property
    def module(self):
        return self.parent

    @property
    def signature(self):
        return '([Ljava/lang/String;)V'

    @property
    def can_ignore_empty(self):
        return True

    @property
    def globals_module(self):
        return self.module

    # def add_self(self):
    #     pass

    def store_name(self, name, use_locals):
        self.add_opcodes(
            ASTORE_name(self, '#value'),
            JavaOpcodes.GETSTATIC('org/python/ImportLib', 'modules', 'Ljava/util/Map;'),
            JavaOpcodes.LDC_W(self.module.descriptor),
            JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            JavaOpcodes.LDC_W(name),
            ALOAD_name(self, '#value'),

            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__setattr__', '(Ljava/lang/String;Lorg/python/Object;)V'),
        )
        free_name(self, '#value')

    def store_dynamic(self):
        self.add_opcodes(
            ASTORE_name(self, '#value'),
            JavaOpcodes.LDC_W(self.module.descriptor),
            JavaOpcodes.INVOKESTATIC('org/python/types/Type', 'pythonType', '(Ljava/lang/String;)Lorg/python/types/Type;'),

            JavaOpcodes.GETFIELD('org/python/types/Type', 'attrs', 'Ljava/util/Map;'),
            ALOAD_name(self, '#value'),

            JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'putAll', '(Ljava/util/Map;)V'),
        )
        free_name(self, '#value')

    def load_name(self, name, use_locals):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('org/python/ImportLib', 'modules', 'Ljava/util/Map;'),
            JavaOpcodes.LDC_W(self.module.descriptor),
            JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getattribute__', '(Ljava/lang/String;)Lorg/python/Object;'),
        )

    def delete_name(self, name, use_locals):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('org/python/ImportLib', 'modules', 'Ljava/util/Map;'),
            JavaOpcodes.LDC_W(self.module.descriptor),
            JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKEVIRTUAL('org/python/types/Module', '__delattr__', '(Ljava/lang/String;)Lorg/python/Object;'),
        )

    def transpile_setup(self):
        self.add_opcodes(
            # Register this module as being __main__
            JavaOpcodes.GETSTATIC('org/python/ImportLib', 'modules', 'Ljava/util/Map;'),
            JavaOpcodes.LDC_W('__main__'),

            JavaOpcodes.NEW('org/python/types/Module'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(self.module.class_name),
            JavaOpcodes.INVOKESTATIC('java/lang/Class', 'forName', '(Ljava/lang/String;)Ljava/lang/Class;'),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Module', '<init>', '(Ljava/lang/Class;)V'),

            JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
            JavaOpcodes.POP(),
        )

        # If there are any commands in this main method,
        # add a TRY-CATCH for SystemExit
        if self.commands:
            self.add_opcodes(
                TRY()
            )

    def transpile_teardown(self):
        # Main method is a special case - it always returns Null,
        # but the code doesn't contain this return, so the jump
        # target doesn't exist. Fake a jump target for the return
        java_op = JavaOpcodes.RETURN()

        if self.end_offset:
            python_op = Opcode(self.end_offset, None, True)
            python_op.start_op = java_op
            self.jump_targets[self.end_offset] = python_op

        self.add_opcodes(java_op)

        # If there are any commands in this main method,
        # finish the TRY-CATCH for SystemExit
        if self.commands:
            self.add_opcodes(
                CATCH('org/python/exceptions/SystemExit'),
                    JavaOpcodes.GETFIELD('org/python/exceptions/SystemExit', 'return_code', 'I'),
                    JavaOpcodes.INVOKESTATIC('java/lang/System', 'exit', '(I)V'),
                END_TRY(),
                JavaOpcodes.RETURN()
            )

    def method_attributes(self):
        return [
        ]


class ClosureMethod(Method):
    def __init__(self, parent, name, parameters, returns=None, static=False, commands=None):

        super().__init__(
            parent, name,
            parameters=parameters,
            returns=returns,
            static=static,
            commands=commands,
        )

    def __repr__(self):
        return '<ClosureMethod %s (%s parameters, %s closure vars)>' % (
            self.name, len(self.parameters), len(self.parent.closure_var_names)
        )

    @property
    def is_closuremethod(self):
        return True

    @property
    def globals_module(self):
        return self.module.parent

    def add_self(self):
        self.local_vars['self'] = len(self.local_vars)

    # def _insert_closure_vars(self):
    #     # Load all the arguments into locals
    #     setup = []
    #     for i, closure_var_name in enumerate(self.parent.closure_var_names):
    #         setup.extend([
    #             ALOAD_name(self, 'self'),
    #             JavaOpcodes.GETFIELD('org/python/types/Function', closure_var_name, 'Lorg/python/Object;'),
    #             ASTORE_name(self, closure_var_name),
    #         ])
    #     self.opcodes = setup + self.opcodes


def extract_parameters(code, annotations):
    pos_count = code.co_argcount
    arg_names = code.co_varnames
    keyword_only_count = code.co_kwonlyargcount

    parameters = []

    # Non-keyword-only parameters.
    for offset, name in enumerate(arg_names[0:pos_count]):
        parameters.append({
            'name': name,
            'annotation': annotations.get(name, 'org/python/Object'),
            'kind': POSITIONAL_OR_KEYWORD,
        })

    # *args
    if code.co_flags & CO_VARARGS:
        name = arg_names[pos_count + keyword_only_count]
        annotation = annotations.get(name, 'org/python/Object')
        parameters.append({
            'name': name,
            'annotation': annotation,
            'kind': VAR_POSITIONAL
        })

    # Keyword-only parameters.
    for name in arg_names[pos_count:pos_count + keyword_only_count]:
        parameters.append({
            'name': name,
            'annotation': annotations.get(name, 'org/python/Object'),
            'kind': KEYWORD_ONLY,
        })

    # **kwargs
    if code.co_flags & CO_VARKEYWORDS:
        index = pos_count + keyword_only_count
        if code.co_flags & CO_VARARGS:
            index += 1

        name = arg_names[index]
        parameters.append({
            'name': name,
            'annotation': annotations.get(name, 'org/python/Object'),
            'kind': VAR_KEYWORD
        })

    return parameters
