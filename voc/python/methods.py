from ..java import (
    Annotation, Code as JavaCode, ConstantElementValue, Method as JavaMethod,
    RuntimeVisibleAnnotations, opcodes as JavaOpcodes, Classref
)
from .blocks import Block
from .utils import (
    TRY, CATCH, END_TRY,
    ALOAD_name, ASTORE_name, free_name,
    DLOAD_name, FLOAD_name,
    ICONST_val, ILOAD_name,
    ArgType,
)

CO_VARARGS = 0x0004
CO_VARKEYWORDS = 0x0008
CO_GENERATOR = 0x0020


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


class Function(Block):
    def __init__(self, module, name, code, parameters, returns, static=False):
        super().__init__(parent=module)
        self.name = name

        # Python can redefine function symbols. Keep a track of any
        # function that is defined; if the symbol has already been
        # defined in this context, then append $n to the symbol in
        # the Java classfile.
        duplicates = self._parent.symbols.setdefault(self.name, [])
        duplicates.append(self.method_name)
        if len(duplicates) > 1:
            self._java_suffix = '$%d' % (len(duplicates) - 1)
        else:
            self._java_suffix = ''

        self.code = code
        self.parameters = parameters
        self.returns = returns

        # Reserve space for the register that will hold self (if required)
        self.add_self()

        # Reserve space for the registers that will hold arguments.
        for i, param in enumerate(self.parameters):
            self.local_vars[param['name']] = len(self.local_vars)

        self.static = static

    def __repr__(self):
        return '<Function %s (%s parameters)>' % (self.name, len(self.parameters))

    @property
    def is_constructor(self):
        return False

    def add_self(self):
        pass

    def store_name(self, name):
        if name in self.local_vars:
            self.add_opcodes(
                ASTORE_name(self, name)
            )
        else:
            self.add_opcodes(
                ASTORE_name(self, '#value'),

                JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

                JavaOpcodes.NEW('org/python/types/Str'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W(self.module.full_name),
                JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', args=['Ljava/lang/String;'], returns='V'),

                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__getitem__',
                    args=['Lorg/python/Object;'],
                    returns='Lorg/python/Object;'
                ),
                JavaOpcodes.CHECKCAST('org/python/types/Module'),

                JavaOpcodes.LDC_W(name),
                ALOAD_name(self, '#value'),

                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__setattr__',
                    args=['Ljava/lang/String;', 'Lorg/python/Object;'],
                    returns='V'
                ),
            )
            free_name(self, '#value')

    def store_dynamic(self):
        raise NotImplementedError('Functions cannot dynamically store variables.')

    def load_name(self, name):
        if name in self.local_vars:
            self.add_opcodes(
                ALOAD_name(self, name)
            )
        else:
            self.add_opcodes(
                JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

                JavaOpcodes.NEW('org/python/types/Str'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W(self.module.full_name),
                JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', args=['Ljava/lang/String;'], returns='V'),

                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__getitem__',
                    args=['Lorg/python/Object;'],
                    returns='Lorg/python/Object;'
                ),
                JavaOpcodes.CHECKCAST('org/python/types/Module'),

                JavaOpcodes.LDC_W(name),

                JavaOpcodes.INVOKEVIRTUAL(
                    'org/python/types/Module',
                    '__getattribute__',
                    args=['Ljava/lang/String;'],
                    returns='Lorg/python/Object;'
                ),
            )

    def load_globals(self):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

            JavaOpcodes.NEW('org/python/types/Str'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(self.module.full_name),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),

            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                '__getitem__',
                args=['Lorg/python/Object;'],
                returns='Lorg/python/Object;'
            ),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            JavaOpcodes.GETFIELD('org/python/types/Module', '__dict__', 'Ljava/util/Map;'),
        )

    def load_locals(self):
        self.add_opcodes(
            JavaOpcodes.NEW('java/util/HashMap'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('java/util/HashMap', '<init>', '()V')
        )
        for var_name, index in self.local_vars.items():
            if index is not None and not var_name.startswith('#'):
                self.add_opcodes(
                    JavaOpcodes.DUP(),

                    # JavaOpcodes.NEW('org/python/types/Str'),
                    # JavaOpcodes.DUP(),
                    JavaOpcodes.LDC_W(var_name),
                    # JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),

                    ALOAD_name(self, var_name),

                    JavaOpcodes.INVOKEINTERFACE(
                        'java/util/Map',
                        'put',
                        args=['Ljava/lang/Object;', 'Ljava/lang/Object;'],
                        returns='Ljava/lang/Object;'
                    ),
                    JavaOpcodes.POP()
                )

    def load_vars(self):
        self.load_locals()

    def delete_name(self, name):
        try:
            free_name(self, name)
        except KeyError:
            self.add_opcodes(
                JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

                JavaOpcodes.NEW('org/python/types/Str'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W(self.module.full_name),
                JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', args=['Ljava/lang/String;'], returns='V'),

                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__getitem__',
                    args=['Lorg/python/Object;'],
                    returns='Lorg/python/Object;'
                ),
                JavaOpcodes.CHECKCAST('org/python/types/Module'),

                JavaOpcodes.LDC_W(name),

                JavaOpcodes.INVOKEVIRTUAL(
                    'org/python/types/Module',
                    '__delattr__',
                    args=['Ljava/lang/String;'],
                    returns='V'
                ),
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
    def java_name(self):
        return self.name + self._java_suffix

    @property
    def module(self):
        return self._parent

    @property
    def class_descriptor(self):
        return self.module.class_descriptor

    def add_class(self, class_name, bases, extends, implements):
        from .klass import Class

        klass = Class(
            self.module,
            name=class_name,
            bases=bases,
            extends=extends,
            implements=implements,
        )

        self.module.classes.append(klass)

        self.add_opcodes(
            # JavaOpcodes.LDC_W("FORCE LOAD OF CLASS %s AT DEFINITION" % self.klass.descriptor),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),

            JavaOpcodes.LDC_W(klass.descriptor.replace('/', '.')),
            JavaOpcodes.INVOKESTATIC(
                'java/lang/Class',
                'forName',
                args=['Ljava/lang/String;'],
                returns='Ljava/lang/Class;'
            ),

            JavaOpcodes.INVOKESTATIC(
                'org/python/types/Type',
                'pythonType',
                args=['Ljava/lang/Class;'],
                returns='Lorg/python/types/Type;'
            ),
        )

        self.store_name(klass.name)

        return klass

    def add_function(self, name, code, parameter_signatures, return_signature):
        # If a function is added to a function, it is added as an anonymous
        # inner class.
        from .klass import ClosureClass
        klass = ClosureClass(
            module=self.module,
            name='%s$%s$%s' % (self.module.name, self.name, name),
            closure_var_names=code.co_freevars,
        )
        self.module.classes.append(klass)

        klass.visitor_setup()
        if code.co_flags & CO_GENERATOR:
            closure = GeneratorClosure(
                klass,
                code=code,
                generator=code.co_name,
                parameters=parameter_signatures,
                returns=return_signature,
            )
        else:
            closure = Closure(
                klass,
                code=code,
                parameters=parameter_signatures,
                returns=return_signature,
            )

        klass.methods.append(closure)

        for field in code.co_names:
            klass.fields[field] = 'Lorg/python/Object;'

        klass.visitor_teardown()

        self.add_opcodes(
            JavaOpcodes.NEW(klass.descriptor),
            JavaOpcodes.DUP(),

            # Define the closure vars
            JavaOpcodes.NEW('java/util/HashMap'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('java/util/HashMap', '<init>', args=[], returns='V')
        )

        for var_name in code.co_freevars:
            self.add_opcodes(
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W(var_name),
            )

            self.load_name(var_name)

            self.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE(
                    'java/util/Map',
                    'put',
                    args=['Ljava/lang/Object;', 'Ljava/lang/Object;'],
                    returns='Ljava/lang/Object;'
                ),
                JavaOpcodes.POP(),
            )

        self.add_opcodes(
            JavaOpcodes.INVOKESPECIAL(klass.descriptor, '<init>', args=['Ljava/util/Map;'], returns='V'),

            JavaOpcodes.LDC_W(Classref(klass.descriptor)),
            JavaOpcodes.INVOKESTATIC(
                'org/python/types/Type',
                'pythonType',
                args=['Ljava/lang/Class;'],
                returns='Lorg/python/types/Type;'
            ),

            JavaOpcodes.LDC_W('invoke'),
        )

        # Store the closure instance as an accessible symbol.
        self.add_callable(closure)

        self.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                '__setattr__',
                args=['Ljava/lang/String;', 'Lorg/python/Object;'],
                returns='V'
            ),
            JavaOpcodes.LDC_W('invoke'),
            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                '__getattribute__',
                args=['Ljava/lang/String;'],
                returns='Lorg/python/Object;'
            ),
        )

        return closure

    def visitor_teardown(self):
        if len(self.opcodes) == 0:
            # If there is no content in this method, add a RETURN.
            return_required = True
        elif isinstance(self.opcodes[-1], (JavaOpcodes.RETURN, JavaOpcodes.ARETURN)):
            # If the last opcode in the method is a RETURN, but that
            # return was not added at the root level (i.e., it's not a return
            # as the last statement of an IF statement), add one.
            try:
                return_required = self.opcodes[-1].depth > 0
            except AttributeError:
                return_required = True
        else:
            # If the last statement in the block isn't a RETURN, add one.
            return_required = True

        if return_required:
            self.add_opcodes(
                JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;'),
                JavaOpcodes.ARETURN()
            )

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
                self.java_name,
                self.signature,
                static=self.static,
                attributes=[self.transpile_code()] + self.method_attributes()
            )
        ]

    def transpile_wrapper(self):
        return []

    def transpile(self):
        return self.transpile_method() + self.transpile_wrapper()


class InitMethod(Function):
    def __init__(self, klass, parameters=None):
        super().__init__(
            klass,
            name='<init>',
            code=None,
            parameters=parameters if parameters else [
                {
                    'name': 'self',
                    'kind': ArgType.POSITIONAL_OR_KEYWORD,
                    'annotation': 'org/python/Object'
                },
                {
                    'name': 'args',
                    'kind': ArgType.VAR_POSITIONAL,
                    'annotation': '[Lorg/python/Object;'
                },
                {
                    'name': 'kwargs',
                    'kind': ArgType.VAR_KEYWORD,
                    'annotation': 'java/util/Map'
                }
            ],
            returns={'annotation': None},
        )
        self.build()

    def __repr__(self):
        return '<Constructor %s (%s parameters)>' % (self.klass.name, len(self.parameters))

    @property
    def is_constructor(self):
        return True

    @property
    def klass(self):
        return self._parent

    @property
    def module(self):
        return self.klass.module

    @property
    def class_descriptor(self):
        return self.klass.descriptor

    @property
    def can_ignore_empty(self):
        return False

    @property
    def signature(self):
        return '([Lorg/python/Object;Ljava/util/Map;)V'

    def build(self):
        # Construct the contents of the constructor method...
        self.add_opcodes(
            # Create the instance
            JavaOpcodes.ALOAD_0(),
            JavaOpcodes.DUP(),
            # TODO - this only allows using the default constructor
            # for extended Java classes.
            JavaOpcodes.INVOKESPECIAL(self.klass.extends_descriptor, '<init>', args=[], returns='V'),

            JavaOpcodes.INVOKESTATIC(
                'org/python/types/Type',
                'toPython',
                args=['Ljava/lang/Object;'],
                returns='Lorg/python/Object;'
            ),

            JavaOpcodes.LDC_W('__init__'),
            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                '__getattribute_null',
                args=['Ljava/lang/String;'],
                returns='Lorg/python/Object;'
            ),

            # If no __init__ exists, just return.
            JavaOpcodes.DUP(),
            JavaOpcodes.IFNULL(13),  # 3

            # Check that it is a callable
            JavaOpcodes.CHECKCAST('org/python/Callable'),  # 3

            # ...and invoke it
            JavaOpcodes.ALOAD_1(),  # 1
            JavaOpcodes.ALOAD_2(),  # 1
            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Callable',
                'invoke',
                args=['[Lorg/python/Object;', 'Ljava/util/Map;'],
                returns='Lorg/python/Object;'
            ),  # 5

            JavaOpcodes.POP(),  # 1

            JavaOpcodes.RETURN()
        )


class Method(Function):
    def __init__(self, klass, name, code, parameters, returns=None, static=False):
        super().__init__(
            klass,
            name=name,
            code=code,
            parameters=parameters,
            returns=returns,
            static=static,
        )

    def __repr__(self):
        return '<InstanceMethod %s.%s (%s parameters)>' % (self.klass.name, self.name, len(self.parameters))

    @property
    def klass(self):
        return self._parent

    @property
    def module(self):
        return self.klass.module

    @property
    def class_descriptor(self):
        return self.klass.descriptor

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
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),

            # JavaOpcodes.LDC_W("BOUND AS " + self.name + self.bound_signature),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),

            # JavaOpcodes.LDC_W("BINDING SELF IN"),
            # JavaOpcodes.ALOAD_0(),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug',
            #     args=['Ljava/lang/String;', 'Ljava/lang/Object;'], returns='V'),

            JavaOpcodes.ALOAD_0(),
            JavaOpcodes.INVOKESTATIC(
                'org/python/types/Type',
                'toPython',
                args=['Ljava/lang/Object;'],
                returns='Lorg/python/Object;'
            ),  # 3

            # JavaOpcodes.DUP(),
            # JavaOpcodes.LDC_W("BINDING SELF OUT"),
            # JavaOpcodes.SWAP(),
            # JavaOpcodes.INVOKESTATIC('org/Python', 'debug',
            #     args=['Ljava/lang/String;', 'Ljava/lang/Object;'], returns='V'),
        ]

        # Then extract each argument, converting to Python types as required.
        for i, param in enumerate(self.parameters[1:]):
            annotation = param['annotation']

            if annotation is None:
                raise Exception("Parameters can't be void")
            elif annotation == "bool":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),

                    JavaOpcodes.NEW('org/python/types/Bool'),
                    JavaOpcodes.DUP(),
                    ILOAD_name(self, param['name']),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', args=['Z'], returns='V'),
                ])
            elif annotation == "byte":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),

                    JavaOpcodes.NEW('org/python/types/Int'),
                    JavaOpcodes.DUP(),
                    ILOAD_name(self, param['name']),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', args=['B'], returns='V'),
                ])
            elif annotation == 'char':
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),

                    JavaOpcodes.NEW('org/python/types/Str'),
                    JavaOpcodes.DUP(),
                    ILOAD_name(self, param['name']),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', args=['C'], returns='V'),
                ])
            elif annotation == "short":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),

                    JavaOpcodes.NEW('org/python/types/Int'),
                    JavaOpcodes.DUP(),
                    ILOAD_name(self, param['name']),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', args=['S'], returns='V'),
                ])
            elif annotation == "int":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),

                    JavaOpcodes.NEW('org/python/types/Int'),
                    JavaOpcodes.DUP(),
                    ILOAD_name(self, param['name']),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', args=['I'], returns='V'),
                ])
            elif annotation == "long":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),

                    JavaOpcodes.NEW('org/python/types/Int'),
                    JavaOpcodes.DUP(),
                    ILOAD_name(self, param['name']),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Int', '<init>', args=['J'], returns='V'),
                ])
            elif annotation == "float":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),

                    JavaOpcodes.NEW('org/python/types/Float'),
                    JavaOpcodes.DUP(),
                    FLOAD_name(self, param['name']),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Float', '<init>', args=['F'], returns='V'),
                ])
            elif annotation == "double":
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),

                    JavaOpcodes.NEW('org/python/types/Float'),
                    JavaOpcodes.DUP(),
                    DLOAD_name(self, param['name']),
                    JavaOpcodes.INVOKESPECIAL('org/python/types/Float', '<init>', args=['D'], returns='V'),
                ])
            else:
                binding_opcodes.extend([
                    # JavaOpcodes.LDC_W("INPUT %s TRANSFORM %s" % (i, annotation)),
                    # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),
                    ALOAD_name(self, param['name']),
                    JavaOpcodes.INVOKESTATIC(
                        'org/python/types/Type',
                        'toPython',
                        args=['Ljava/lang/Object;'],
                        returns='Lorg/python/Object;'
                    ),
                ])

            # self.add_opcodes(
            #     JavaOpcodes.LDC_W("INPUT %s TRANSFORMED" % (i)),
            #     JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),
            # )
        # self.add_opcodes(
        #     JavaOpcodes.LDC_W("INPUTS TRANSFORMED"),
        #     JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),
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
                JavaOpcodes.INVOKEINTERFACE('org/python/Object', 'toJava', args=[], returns='Ljava/lang/Object;'),
                JavaOpcodes.CHECKCAST('java/lang/String'),
                ICONST_val(0),
                JavaOpcodes.INVOKEVIRTUAL('java/lang/String', 'charAt', args=['I'], returns='C'),
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
                JavaOpcodes.INVOKEINTERFACE('org/python/Object', 'toJava', args=[], returns='Ljava/lang/Object;'),
                JavaOpcodes.CHECKCAST(return_type.replace('.', '/')),
                JavaOpcodes.ARETURN(),
            ])
        else:
            binding_opcodes.extend([
                JavaOpcodes.ARETURN()
            ])

        # binding_opcodes.extend([
        #     JavaOpcodes.LDC_W("BINDING OUTPUT to type %s" % self.returns['annotation']),
        #     JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),
        # ])

        wrapper_methods = [
            JavaMethod(
                self.java_name,
                self.bound_signature,
                attributes=[
                    JavaCode(
                        max_stack=len(self.parameters) + 5,
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
                    'long': JavaOpcodes.LRETURN(),
                    'float': JavaOpcodes.FRETURN(),
                    'double': JavaOpcodes.DRETURN(),
                }.get(self.returns['annotation'], JavaOpcodes.ARETURN()),

                # JavaOpcodes.LDC_W("SUPER WRAPPER OUTPUT to type %s" % self.returns['annotation']),
                # JavaOpcodes.INVOKESTATIC('org/Python', 'debug', args=['Ljava/lang/String;'], returns='V'),
            ])

            wrapper_methods.append(
                JavaMethod(
                    self.java_name + "$super",
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


class MainFunction(Function):
    def __init__(self, module):
        super().__init__(
            module,
            name='__main__',
            code=None,
            parameters=[{'name': 'args', 'annotation': 'argv'}],
            returns={'annotation': None},
            static=True,
        )

    def __repr__(self):
        return '<MainFunction %s>' % self.module.name

    @property
    def java_name(self):
        return 'main'

    @property
    def module(self):
        return self._parent

    @property
    def signature(self):
        return '([Ljava/lang/String;)V'

    @property
    def can_ignore_empty(self):
        return True

    def store_name(self, name):
        self.add_opcodes(
            ASTORE_name(self, '#value'),
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

            JavaOpcodes.NEW('org/python/types/Str'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(self.module.full_name),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', args=['Ljava/lang/String;'], returns='V'),

            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                '__getitem__',
                args=['Lorg/python/Object;'],
                returns='Lorg/python/Object;'
            ),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            JavaOpcodes.LDC_W(name),
            ALOAD_name(self, '#value'),

            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                '__setattr__',
                args=['Ljava/lang/String;', 'Lorg/python/Object;'],
                returns='V'
            ),
        )
        free_name(self, '#value')

    def store_dynamic(self):
        self.add_opcodes(
            ASTORE_name(self, '#value'),
            JavaOpcodes.LDC_W(self.module.class_name),
            JavaOpcodes.INVOKESTATIC(
                'org/python/types/Type',
                'pythonType',
                args=['Ljava/lang/String;'],
                returns='Lorg/python/types/Type;'
            ),

            JavaOpcodes.GETFIELD('org/python/types/Type', '__dict__', 'Ljava/util/Map;'),
            ALOAD_name(self, '#value'),

            JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'putAll', args=['Ljava/util/Map;'], returns='V'),
        )
        free_name(self, '#value')

    def load_name(self, name):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

            JavaOpcodes.NEW('org/python/types/Str'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(self.module.full_name),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', args=['Ljava/lang/String;'], returns='V'),

            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                '__getitem__',
                args=['Lorg/python/Object;'],
                returns='Lorg/python/Object;'
            ),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                '__getattribute__',
                args=['Ljava/lang/String;'],
                returns='Lorg/python/Object;'
            ),
        )

    def delete_name(self, name):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

            JavaOpcodes.NEW('org/python/types/Str'),
            JavaOpcodes.DUP(),
            JavaOpcodes.LDC_W(self.module.full_name),
            JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', args=['Ljava/lang/String;'], returns='V'),

            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                '__getitem__',
                args=['Lorg/python/Object;'],
                returns='Lorg/python/Object;'
            ),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKEVIRTUAL(
                'org/python/types/Module',
                '__delattr__',
                args=['Ljava/lang/String;'],
                returns='V'
            ),
        )

    def visitor_setup(self):
        self.add_opcodes(
            # Add a TRY-CATCH for SystemExit
            TRY(),
        )
        self.add_opcodes(
                # Initialize and register this module
                JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),
                JavaOpcodes.DUP(),

                JavaOpcodes.NEW('org/python/types/Str'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W(self.module.full_name),
                JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', args=['Ljava/lang/String;'], returns='V'),

                JavaOpcodes.NEW(self.module.class_descriptor),
                JavaOpcodes.DUP(),
                JavaOpcodes.DUP(),
                JavaOpcodes.INVOKESPECIAL(self.module.class_descriptor, '<init>', args=[], returns='V'),
                ASTORE_name(self, '#module'),

                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__setitem__',
                    args=['Lorg/python/Object;', 'Lorg/python/Object;'],
                    returns='V'
                ),

                # Register the same instances as __main__
                JavaOpcodes.NEW('org/python/types/Str'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W('__main__'),
                JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', args=['Ljava/lang/String;'], returns='V'),

                ALOAD_name(self, '#module'),
                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__setitem__',
                    args=['Lorg/python/Object;', 'Lorg/python/Object;'],
                    returns='V'
                ),

                # Set the module's __name__ and __package__
                ALOAD_name(self, '#module'),
                JavaOpcodes.LDC_W("__name__"),

                JavaOpcodes.NEW('org/python/types/Str'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W("__main__"),
                JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', '(Ljava/lang/String;)V'),

                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__setattr__',
                    args=['Ljava/lang/String;', 'Lorg/python/Object;'],
                    returns='V'
                ),

                ALOAD_name(self, '#module'),
                JavaOpcodes.LDC_W("__package__"),
                JavaOpcodes.GETSTATIC("org/python/types/NoneType", "NONE", "Lorg/python/Object;"),
                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__setattr__',
                    args=['Ljava/lang/String;', 'Lorg/python/Object;'],
                    returns='V'
                ),

                # Run the module block.
                ALOAD_name(self, '#module'),
                JavaOpcodes.INVOKEVIRTUAL(self.module.class_descriptor, 'module$import', args=[], returns='V'),
        )

    def visitor_teardown(self):
        # Close out the TRY-CATCH for SystemExit
        self.add_opcodes(
            CATCH('org/python/exceptions/SystemExit'),
        )
        self.add_opcodes(
                JavaOpcodes.GETFIELD('org/python/exceptions/SystemExit', 'return_code', 'I'),
                JavaOpcodes.INVOKESTATIC('java/lang/System', 'exit', args=['I'], returns='V'),
        )
        self.add_opcodes(
            END_TRY(),
            JavaOpcodes.RETURN()
        )

    def method_attributes(self):
        return []


class Closure(Function):
    def __init__(self, klass, code, parameters, returns=None, static=False):
        super().__init__(
            klass,
            name='invoke',
            code=code,
            parameters=parameters,
            returns=returns,
            static=static,
        )

    def __repr__(self):
        return '<Closure %s (%s parameters, %s closure variables)>' % (
            self.name, len(self.parameters), len(self.klass.closure_var_names)
        )

    @property
    def klass(self):
        return self._parent

    @property
    def module(self):
        return self.klass.module

    @property
    def class_descriptor(self):
        return self.klass.descriptor

    def add_self(self):
        # In a closure method, the first argument is the closure,
        # not self. self *might* be the first argument -- but in
        # that case, it's just the first argument in an unbound
        # method.
        self.local_vars['<closure>'] = len(self.local_vars)
        self.has_self = True

    def load_name(self, name):
        if name in self.local_vars:
            self.add_opcodes(
                ALOAD_name(self, name)
            )
        elif name in self.klass.closure_var_names:
            self.add_opcodes(
                ALOAD_name(self, '<closure>'),
                JavaOpcodes.CHECKCAST('org/python/types/Closure'),
                JavaOpcodes.GETFIELD('org/python/types/Closure', 'closure_vars', 'Ljava/util/Map;'),
                JavaOpcodes.LDC_W(name),
                JavaOpcodes.INVOKEINTERFACE(
                    'java/util/Map',
                    'get',
                    args=['Ljava/lang/Object;'],
                    returns='Ljava/lang/Object;'
                ),
            )
        else:
            self.add_opcodes(
                JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

                JavaOpcodes.NEW('org/python/types/Str'),
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W(self.module.full_name),
                JavaOpcodes.INVOKESPECIAL('org/python/types/Str', '<init>', args=['Ljava/lang/String;'], returns='V'),

                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__getitem__',
                    args=['Lorg/python/Object;'],
                    returns='Lorg/python/Object;'
                ),
                JavaOpcodes.CHECKCAST('org/python/types/Module'),

                JavaOpcodes.LDC_W(name),

                JavaOpcodes.INVOKEVIRTUAL(
                    'org/python/types/Module',
                    '__getattribute__',
                    args=['Ljava/lang/String;'],
                    returns='Lorg/python/Object;'
                ),
            )


class ClosureInitMethod(InitMethod):
    def __init__(self, klass):
        super().__init__(
            klass,
            parameters=[
                {
                    'name': 'self',
                    'kind': ArgType.POSITIONAL_OR_KEYWORD,
                    'annotation': 'org/python/Object'
                },
                {
                    'name': 'kwargs',
                    'kind': ArgType.VAR_KEYWORD,
                    'annotation': 'java/util/Map'
                }
            ],
        )

    def __repr__(self):
        return '<Closure constructor %s (%s parameters)>' % (self.klass.name, len(self.parameters))

    @property
    def signature(self):
        return '(Ljava/util/Map;)V'

    def build(self):
        # Get the __init__ method for the class...
        self.add_opcodes(
            # Create the instance
            JavaOpcodes.ALOAD_0(),
            JavaOpcodes.DUP(),
            # TODO - this only allows using the default constructor
            # for extended Java classes.
            JavaOpcodes.ALOAD_1(),
            JavaOpcodes.INVOKESPECIAL(self.klass.extends_descriptor, '<init>', args=['Ljava/util/Map;'], returns='V'),

            JavaOpcodes.RETURN()
        )


class GeneratorFunction(Function):
    def __init__(self, module, name, code, generator, parameters, returns=None, static=False):
        super().__init__(
            module,
            name=name,
            code=code,
            parameters=parameters,
            returns=returns,
            static=static,
        )
        self.generator = generator

    @property
    def klass(self):
        return self.module

    def add_self(self):
        self.local_vars['<generator>'] = len(self.local_vars)
        self.has_self = True

    def visitor_setup(self):
        # Restore the variables needed for the entry of the generator.
        self.add_opcodes(
            ALOAD_name(self, '<generator>'),
            JavaOpcodes.GETFIELD('org/python/types/Generator', 'stack', '[Lorg/python/Object;'),
        )

        for i, param in enumerate(self.parameters):
            self.add_opcodes(
                JavaOpcodes.DUP(),
                ICONST_val(i),
                JavaOpcodes.AALOAD(),
                JavaOpcodes.ASTORE(i + 1),
            )
        self.add_opcodes(
            JavaOpcodes.POP(),
        )

    def visitor_teardown(self):
        if len(self.opcodes) == 0 or not isinstance(self.opcodes[-1], JavaOpcodes.ATHROW):
            self.add_opcodes(
                JavaOpcodes.NEW('org/python/exceptions/StopIteration'),
                JavaOpcodes.DUP(),
                JavaOpcodes.INVOKESPECIAL('org/python/exceptions/StopIteration', '<init>', args=[], returns='V'),
                JavaOpcodes.ATHROW(),
            )

    def transpile_method(self):
        return [
            JavaMethod(
                self.method_name + "$generator",
                '(Lorg/python/types/Generator;)Lorg/python/Object;',
                static=True,
                attributes=[self.transpile_code()] + self.method_attributes()
            )
        ]

    def transpile_wrapper(self):
        wrapper_opcodes = [
            # Construct a generator instance
            JavaOpcodes.NEW('org/python/types/Generator'),
            JavaOpcodes.DUP(),

            # p1: The name of the generator
            JavaOpcodes.LDC_W(self.generator),

            # p2: The actual generator method
            JavaOpcodes.LDC_W(self.klass.class_name),
            JavaOpcodes.INVOKESTATIC(
                'java/lang/Class',
                'forName',
                args=['Ljava/lang/String;'],
                returns='Ljava/lang/Class;'
            ),

            JavaOpcodes.LDC_W(self.method_name + "$generator"),
            ICONST_val(1),
            JavaOpcodes.ANEWARRAY('java/lang/Class'),
            JavaOpcodes.DUP(),

            ICONST_val(0),
            JavaOpcodes.LDC_W('org.python.types.Generator'),
            JavaOpcodes.INVOKESTATIC(
                'java/lang/Class',
                'forName',
                args=['Ljava/lang/String;'],
                returns='Ljava/lang/Class;'
            ),
            JavaOpcodes.AASTORE(),

            JavaOpcodes.INVOKEVIRTUAL(
                'java/lang/Class',
                'getMethod',
                args=['Ljava/lang/String;', '[Ljava/lang/Class;'],
                returns='Ljava/lang/reflect/Method;'
            ),

            # p3: The arguments passed to the generator method. These will be
            # restored on the first call to the generator.
            ICONST_val(len(self.parameters)),
            JavaOpcodes.ANEWARRAY('org/python/Object'),
        ]

        for i, param in enumerate(self.parameters):
            wrapper_opcodes.extend([
                JavaOpcodes.DUP(),
                ICONST_val(i),
                JavaOpcodes.ALOAD(i + (0 if self.static else 1)),
                JavaOpcodes.AASTORE(),
            ])

        # Construct and return the generator object.
        wrapper_opcodes.extend([
            JavaOpcodes.INVOKESPECIAL(
                'org/python/types/Generator',
                '<init>',
                args=['Ljava/lang/String;', 'Ljava/lang/reflect/Method;', '[Lorg/python/Object;'],
                returns='V'
            ),
            JavaOpcodes.ARETURN(),
        ])

        return [
            JavaMethod(
                self.method_name,
                self.signature,
                static=self.static,
                attributes=[
                    JavaCode(
                        max_stack=len(self.parameters) + 8,
                        max_locals=len(self.parameters) + 8,
                        code=wrapper_opcodes
                    )
                ]
            )
        ]


class GeneratorClosure(GeneratorFunction):
    def __init__(self, module, code, generator, parameters, returns=None, static=False):
        super().__init__(
            module,
            name='invoke',
            code=code,
            generator=generator,
            parameters=parameters,
            returns=returns,
            static=static,
        )

    def __repr__(self):
        return '<GeneratorClosure %s (%s parameters)>' % (
            self.name, len(self.parameters)
        )

    @property
    def klass(self):
        return self._parent

    @property
    def module(self):
        return self.klass.module

    @property
    def class_descriptor(self):
        return self.klass.descriptor
