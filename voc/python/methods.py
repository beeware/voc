import sys
from ..java import (
    Annotation, Code as JavaCode, ConstantElementValue, Method as JavaMethod,
    RuntimeVisibleAnnotations, opcodes as JavaOpcodes
)
from .blocks import Block, Accumulator
from .structures import (
    TRY, CATCH, END_TRY,
    ArgType,
)
from .types import java, python
from .types.primitives import (
    ALOAD_name, ASTORE_name, free_name,
    DLOAD_name, FLOAD_name,
    ICONST_val, ILOAD_name,
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

        # Reserve space for the register that will hold locals
        self.local_vars['#locals'] = len(self.local_vars)

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
                # Store in a local variable
                ASTORE_name(name),

                # Also store in the locals variable
                ALOAD_name('#locals'),
                JavaOpcodes.LDC_W(name),
                ALOAD_name(name),
                java.Map.put(),
            )
        else:
            self.add_opcodes(
                ASTORE_name('#value'),

                JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

                python.Str(self.module.full_name),

                python.Object.get_item(),
                JavaOpcodes.CHECKCAST('org/python/types/Module'),

                ALOAD_name('#value'),

                python.Object.set_attr(name),
                free_name('#value')
            )

    def store_dynamic(self):
        raise NotImplementedError('Functions cannot dynamically store variables.')

    def load_name(self, name):
        if name in self.local_vars:
            self.add_opcodes(
                ALOAD_name(name)
            )
        else:
            self.add_opcodes(
                JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

                python.Str(self.module.full_name),

                python.Object.get_item(),
                JavaOpcodes.CHECKCAST('org/python/types/Module'),

                python.Object.get_attribute(name),
            )

    def load_globals(self):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

            python.Str(self.module.full_name),
            python.Object.get_item(),

            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            JavaOpcodes.GETFIELD('org/python/types/Module', '__dict__', 'Ljava/util/Map;'),
        )

    def load_locals(self):
        self.add_opcodes(
            ALOAD_name('#locals')
        )

    def load_vars(self):
        self.load_locals()

    def delete_name(self, name):
        try:
            self.add_opcodes(
                free_name(name)
            )
        except NameError:
            self.add_opcodes(
                JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),

                python.Str(self.module.full_name),

                python.Object.get_item(),
                JavaOpcodes.CHECKCAST('org/python/types/Module'),

                python.Object.del_attr(name),
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
            # DEBUG("FORCE LOAD OF CLASS %s AT DEFINITION" % self.klass.descriptor),

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
            java.New(klass.descriptor),
            # Define the closure vars
            java.Map(),
        )

        for var_name in code.co_freevars:
            self.add_opcodes(
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W(var_name),
            )
            self.load_name(var_name)
            self.add_opcodes(
                java.Map.put(),
            )

        self.add_opcodes(
            java.Init(klass.descriptor, 'Ljava/util/Map;'),
            python.Type.for_name(klass.descriptor),
        )

        # Store the closure instance as an accessible symbol.
        self.add_callable(closure)

        self.add_opcodes(
            python.Object.set_attr('invoke'),
            python.Object.get_attribute('invoke'),
        )

        return closure

    def visitor_setup(self):
        self.add_opcodes(
            java.Map(),
            ASTORE_name('#locals')
        )

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
                python.NONE(),
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
            java.Init(self.klass.extends_descriptor),
            python.Type.to_python(),

            python.Object.get_attribute('__init__', use_null=True),
            # If no __init__ exists, just return.
            JavaOpcodes.DUP(),
            JavaOpcodes.IFNULL(13),  # 3

            # Check that it is a callable
            JavaOpcodes.CHECKCAST('org/python/Callable'),  # 3

            # ...and invoke it
            JavaOpcodes.ALOAD_1(),  # 1
            JavaOpcodes.ALOAD_2(),  # 1
            python.Callable.invoke(),  # 5

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
        binding = Accumulator(self.local_vars)

        binding.add_opcodes(
            # DEBUG("BINDING FOR " + self.name + self.signature),
            # DEBUG("BOUND AS " + self.name + self.bound_signature),
            # JavaOpcodes.ALOAD_0(),
            # DEBUG_value("BINDING SELF IN"),

            JavaOpcodes.ALOAD_0(),
            python.Type.to_python(),  # 3

            # DEBUG_value("BINDING SELF OUT", dup=True),
        )

        # Then extract each argument, converting to Python types as required.
        for i, param in enumerate(self.parameters[1:]):
            annotation = param['annotation']

            if annotation is None:
                raise Exception("Parameters can't be void")
            elif annotation == "bool":
                binding.add_opcodes(
                    # DEBUG("INPUT %s TRANSFORM %s" % (i, annotation)),

                    java.New('org/python/types/Bool'),
                    ILOAD_name(param['name']),
                    java.Init('org/python/types/Bool', 'Z'),
                )
            elif annotation == "byte":
                binding.add_opcodes(
                    # DEBUG("INPUT %s TRANSFORM %s" % (i, annotation)),

                    java.New('org/python/types/Int'),
                    ILOAD_name(param['name']),
                    java.Init('org/python/types/Int', 'B'),
                )
            elif annotation == 'char':
                binding.add_opcodes(
                    # DEBUG("INPUT %s TRANSFORM %s" % (i, annotation)),

                    java.New('org/python/types/Str'),
                    ILOAD_name(param['name']),
                    java.Init('org/python/types/Str', 'C'),
                )
            elif annotation == "short":
                binding.add_opcodes(
                    # DEBUG("INPUT %s TRANSFORM %s" % (i, annotation)),

                    java.New('org/python/types/Int'),
                    ILOAD_name(param['name']),
                    java.Init('org/python/types/Int', 'S'),
                )
            elif annotation == "int":
                binding.add_opcodes(
                    # DEBUG("INPUT %s TRANSFORM %s" % (i, annotation)),

                    java.New('org/python/types/Int'),
                    ILOAD_name(param['name']),
                    java.Init('org/python/types/Int', 'I'),
                )
            elif annotation == "long":
                binding.add_opcodes(
                    # DEBUG("INPUT %s TRANSFORM %s" % (i, annotation)),

                    java.New('org/python/types/Int'),
                    ILOAD_name(param['name']),
                    java.Init('org/python/types/Int', 'J'),
                )
            elif annotation == "float":
                binding.add_opcodes(
                    # DEBUG("INPUT %s TRANSFORM %s" % (i, annotation)),

                    java.New('org/python/types/Float'),
                    FLOAD_name(param['name']),
                    java.Init('org/python/types/Float', 'F'),
                )
            elif annotation == "double":
                binding.add_opcodes(
                    # DEBUG("INPUT %s TRANSFORM %s" % (i, annotation)),

                    java.New('org/python/types/Float'),
                    DLOAD_name(param['name']),
                    java.Init('org/python/types/Float', 'D'),
                )
            else:
                binding.add_opcodes(
                    # DEBUG("INPUT %s TRANSFORM %s" % (i, annotation)),
                    ALOAD_name(param['name']),
                    python.Type.to_python(),
                )

            # binding.add_opcodes(
            #     DEBUG("INPUT %s TRANSFORMED" % (i)),
            # )
        # binding.add_opcodes(
        #     DEBUG("INPUTS TRANSFORMED"),
        # )

        # Then call the method, and process the return type.
        binding.add_opcodes(
            JavaOpcodes.INVOKESTATIC(self.klass.descriptor, self.name, self.signature),
        )

        # Now convert the return type to a native type.
        return_type = self.returns['annotation']

        if return_type == 'void':
            binding.add_opcodes(
                JavaOpcodes.POP(),
                JavaOpcodes.RETURN()
            )
        elif return_type == 'bool':
            binding.add_opcodes(
                JavaOpcodes.CHECKCAST('org/python/types/Bool'),
                JavaOpcodes.GETFIELD('org/python/types/Bool', 'value', 'Z'),
                JavaOpcodes.IRETURN(),
            )
        elif return_type == 'byte':
            binding.add_opcodes(
                JavaOpcodes.CHECKCAST('org/python/types/Int'),
                JavaOpcodes.GETFIELD('org/python/types/Int', 'value', 'J'),
                JavaOpcodes.L2I(),
                JavaOpcodes.I2B(),
                JavaOpcodes.IRETURN(),
            )
        elif return_type == 'char':
            binding.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE('org/python/Object', 'toJava', args=[], returns='Ljava/lang/Object;'),
                JavaOpcodes.CHECKCAST('java/lang/String'),
                ICONST_val(0),
                JavaOpcodes.INVOKEVIRTUAL('java/lang/String', 'charAt', args=['I'], returns='C'),
                JavaOpcodes.IRETURN(),
            )
        elif return_type == 'short':
            binding.add_opcodes(
                JavaOpcodes.CHECKCAST('org/python/types/Int'),
                JavaOpcodes.GETFIELD('org/python/types/Int', 'value', 'J'),
                JavaOpcodes.L2I(),
                JavaOpcodes.I2S(),
                JavaOpcodes.IRETURN(),
            )
        elif return_type == 'int':
            binding.add_opcodes(
                JavaOpcodes.CHECKCAST('org/python/types/Int'),
                JavaOpcodes.GETFIELD('org/python/types/Int', 'value', 'J'),
                JavaOpcodes.L2I(),
                JavaOpcodes.IRETURN(),
            )
        elif return_type == 'long':
            binding.add_opcodes(
                JavaOpcodes.CHECKCAST('org/python/types/Int'),
                JavaOpcodes.GETFIELD('org/python/types/Int', 'value', 'J'),
                JavaOpcodes.LRETURN(),
            )
        elif return_type == 'float':
            binding.add_opcodes(
                JavaOpcodes.CHECKCAST('org/python/types/Float'),
                JavaOpcodes.GETFIELD('org/python/types/Float', 'value', 'D'),
                JavaOpcodes.DTOF(),
                JavaOpcodes.FRETURN(),
            )
        elif return_type == 'double':
            binding.add_opcodes(
                JavaOpcodes.CHECKCAST('org/python/types/Float'),
                JavaOpcodes.GETFIELD('org/python/types/Float', 'value', 'D'),
                JavaOpcodes.DRETURN(),
            )
        elif return_type != 'org/python/Object':
            binding.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE('org/python/Object', 'toJava', args=[], returns='Ljava/lang/Object;'),
                JavaOpcodes.CHECKCAST(return_type.replace('.', '/')),
                JavaOpcodes.ARETURN(),
            )
        else:
            binding.add_opcodes(
                JavaOpcodes.ARETURN()
            )

        # binding.add_opcodes(
        #     DEBUG("BINDING OUTPUT to type %s" % self.returns['annotation']),
        # )

        wrapper_methods = [
            JavaMethod(
                self.java_name,
                self.bound_signature,
                attributes=[
                    JavaCode(
                        max_stack=len(self.parameters) + 5,
                        max_locals=len(self.parameters),
                        code=binding.opcodes
                    )
                ]
            ),
        ]

        if self.klass.extends:
            # We also need to generate a manual call to the super
            super_wrapper = Accumulator()
            super_wrapper.add_opcodes(
                JavaOpcodes.ALOAD_0(),
            )

            # Then extract each argument:
            for i, param in enumerate(self.parameters[1:]):
                super_wrapper.add_opcodes({
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
            super_wrapper.add_opcodes(
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

                # DEBUG("SUPER WRAPPER OUTPUT to type %s" % self.returns['annotation']),
            )

            wrapper_methods.append(
                JavaMethod(
                    self.java_name + "$super",
                    self.bound_signature,
                    attributes=[
                        JavaCode(
                            max_stack=len(self.parameters) + 2,
                            max_locals=len(self.parameters) + 2,
                            code=super_wrapper.opcodes
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
            ASTORE_name('#value'),
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),
            python.Str(self.module.full_name),
            python.Object.get_item(),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),

            ALOAD_name('#value'),
            python.Object.set_attr(name),
            free_name('#value')
        )

    def store_dynamic(self):
        self.add_opcodes(
            ASTORE_name('#value'),
            python.Type.for_name(self.module.class_name),
            JavaOpcodes.GETFIELD('org/python/types/Type', '__dict__', 'Ljava/util/Map;'),
            ALOAD_name('#value'),

            java.Map.putAll(),
            free_name('#value')
        )

    def load_name(self, name):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),
            python.Str(self.module.full_name),
            python.Object.get_item(),

            JavaOpcodes.CHECKCAST('org/python/types/Module'),
            python.Object.get_attribute(name),
        )

    def delete_name(self, name):
        self.add_opcodes(
            JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),
            python.Str(self.module.full_name),
            python.Object.get_item(),

            JavaOpcodes.CHECKCAST('org/python/types/Module'),
            python.Object.del_attr(name),
        )

    def visitor_setup(self):
        self.add_opcodes(
            # Set the Python version
            JavaOpcodes.LDC(sys.hexversion),
            JavaOpcodes.PUTSTATIC('org/Python', 'VERSION', 'I'),

            # Create storage for locals
            java.Map(),
            ASTORE_name('#locals'),

            # Add a TRY-CATCH for SystemExit
            TRY(),
        )
        self.add_opcodes(
                # Initialize this module
                java.New(self.module.class_descriptor),
                java.Init(self.module.class_descriptor),
                ASTORE_name('#module'),

                # Register the module by it's full name
                JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),
                python.Str(self.module.full_name),
                ALOAD_name('#module'),
                python.Object.set_item(),

                # Register the same module as __main__
                JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),
                python.Str('__main__'),
                ALOAD_name('#module'),
                python.Object.set_item(),

                # Set the module's __name__
                ALOAD_name('#module'),
                python.Str("__main__"),
                python.Object.set_attr('__name__'),

                # Set the module's __package__
                ALOAD_name('#module'),
                python.NONE(),
                python.Object.set_attr("__package__"),

                # Run the module block.
                ALOAD_name('#module'),
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
                ALOAD_name(name)
            )
        elif name in self.klass.closure_var_names:
            self.add_opcodes(
                ALOAD_name('<closure>'),
                JavaOpcodes.CHECKCAST('org/python/types/Closure'),
                JavaOpcodes.GETFIELD('org/python/types/Closure', 'closure_vars', 'Ljava/util/Map;'),

                java.Map.get(name),
            )
        else:
            self.add_opcodes(
                JavaOpcodes.GETSTATIC('python/sys/__init__', 'modules', 'Lorg/python/types/Dict;'),
                python.Str(self.module.full_name),
                python.Object.get_item(),
                JavaOpcodes.CHECKCAST('org/python/types/Module'),

                python.Object.get_attribute(name),
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
            java.Init(self.klass.extends_descriptor, 'Ljava/util/Map;'),

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
        self.add_opcodes(
            # Restore the variables needed for the entry of the generator.
            ALOAD_name('<generator>'),
            JavaOpcodes.GETFIELD('org/python/types/Generator', 'stack', 'Ljava/util/Map;'),
            ASTORE_name('#locals'),
        )

        for param in self.parameters:
            self.add_opcodes(
                ALOAD_name('#locals'),
                java.Map.get(param['name']),
                ASTORE_name(param['name'])
            )

    def visitor_teardown(self):
        if len(self.opcodes) == 0 or not isinstance(self.opcodes[-1], JavaOpcodes.ATHROW):
            self.add_opcodes(
                java.New('org/python/exceptions/StopIteration'),
                java.Init('org/python/exceptions/StopIteration'),
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
        wrapper = Accumulator()

        wrapper.add_opcodes(
            # Construct a generator instance
            java.New('org/python/types/Generator'),

            # p1: The name of the generator
            JavaOpcodes.LDC_W(self.generator),

            # p2: The actual generator method
            java.Class.forName(self.klass.class_name),

            JavaOpcodes.LDC_W(self.method_name + "$generator"),
            java.Array(1, 'java/lang/Class'),

            JavaOpcodes.DUP(),
            ICONST_val(0),
            java.Class.forName('org.python.types.Generator'),
            JavaOpcodes.AASTORE(),

            JavaOpcodes.INVOKEVIRTUAL(
                'java/lang/Class',
                'getMethod',
                args=['Ljava/lang/String;', '[Ljava/lang/Class;'],
                returns='Ljava/lang/reflect/Method;'
            ),

            # p3: The arguments passed to the generator method. These will be
            # restored on the first call to the generator.
            java.Map(),
        )

        for i, param in enumerate(self.parameters):
            wrapper.add_opcodes(
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W(param['name']),

                JavaOpcodes.ALOAD(i + (0 if self.static else 1)),
                java.Map.put(),
            )

        # Construct and return the generator object.
        wrapper.add_opcodes(
            java.Init(
                'org/python/types/Generator',
                'Ljava/lang/String;',
                'Ljava/lang/reflect/Method;',
                'Ljava/util/Map;',
            ),
            JavaOpcodes.ARETURN(),
        )

        return [
            JavaMethod(
                self.method_name,
                self.signature,
                static=self.static,
                attributes=[
                    JavaCode(
                        max_stack=len(self.parameters) + 8,
                        max_locals=len(self.parameters) + 8,
                        code=wrapper.opcodes
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
