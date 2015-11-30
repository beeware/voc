from ..java import (
    Method as JavaMethod,
    opcodes as JavaOpcodes,
    RuntimeVisibleAnnotations,
    Annotation,
    ConstantElementValue,
)

from .blocks import Block
from .opcodes import (
    ALOAD_name, ASTORE_name, free_name,
    ICONST_val,
    Opcode, TRY, CATCH, END_TRY, IF, END_IF
)

POSITIONAL_OR_KEYWORD = 1
VAR_POSITIONAL = 2
KEYWORD_ONLY = 3
VAR_KEYWORD = 4

CO_VARARGS = 0x0004
CO_VARKEYWORDS = 0x0008


class Method(Block):
    def __init__(self, parent, name, parameters, returns=None, static=False, commands=None, code=None):
        super().__init__(parent, commands=commands)
        self.name = name
        self.parameters = parameters

        if returns is None:
            self.returns = {}
        else:
            self.returns = returns

        # Load args and kwargs, but don't expose those names into the local_vars.
        self.add_arguments()
        for i in range(self.self_offset, len(self.parameters)):
            param = self.parameters[i]
            self.local_vars[param['name']] = len(self.local_vars)

        self.static = static
        self.code_obj = code

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

    def add_argument_variables(self, parameters):
        for param in parameters:
            self.parameters.append(param)
            if len(self.parameters) >= self.self_offset:
                self.local_vars[param['name']] = len(self.local_vars)

    @property
    def has_void_return(self):
        return self.returns.get('annotation', object()) is None or self.name == '__init__'

    @property
    def can_ignore_empty(self):
        return False

    def add_return(self):
        if self.has_void_return:
            self.add_opcodes(JavaOpcodes.RETURN())
        else:
            self.add_opcodes(JavaOpcodes.ARETURN())

    @property
    def signature(self):
        return_descriptor = 'V' if self.has_void_return else 'Lorg/python/Object;'
        return '(Ljava/util/List;Ljava/util/Map;Ljava/util/List;Ljava/util/Map;)%s' % return_descriptor

    def add_arguments(self):
        self.local_vars['##__args__##'] = len(self.local_vars)
        self.local_vars['##__kwargs__##'] = len(self.local_vars)
        self.local_vars['##__default_args__##'] = len(self.local_vars)
        self.local_vars['##__default_kwargs__##'] = len(self.local_vars)

    @property
    def method_name(self):
        return self.name

    @property
    def module(self):
        return self.parent

    def add_method(self, method_name, code):
        # If a method is added to a method, it is added as an anonymous
        # inner class.
        from .klass import ClosureClass
        callable = ClosureClass(
            parent=self.parent,
            name='%s$%s' % (self.parent.name, method_name.replace('.<locals>.', '$')),
            closure_var_names=code.co_names,
            super_name='org/python/types/Closure',
            interfaces=['org/python/Callable'],
            public=True,
            final=True,
        )

        method = ClosureMethod(callable, 'invoke', extract_parameters(code), code=code)
        method.extract(code)
        callable.methods.append(method)

        callable.fields = dict(
            (name, 'Lorg/python/Object;')
            for name in code.co_names
        )

        self.parent.classes.append(callable)

        return method

    @property
    def self_offset(self):
        return 0

    def transpile_args(self):
        self.add_opcodes(
            JavaOpcodes.LDC_W(self.code_obj.co_name),  # func_name
            ALOAD_name(self, '##__args__##'),  # args
            ALOAD_name(self, '##__kwargs__##'),  # kwargs

            # argnames
            ICONST_val(len(self.parameters) - self.self_offset),
            JavaOpcodes.ANEWARRAY('java/lang/String'),
        )

        for a in range(self.self_offset, len(self.parameters)):
            self.add_opcodes(
                JavaOpcodes.DUP(),
                ICONST_val(a - self.self_offset),
                JavaOpcodes.LDC_W(self.code_obj.co_varnames[a]),
                JavaOpcodes.AASTORE(),
            )

        self.add_opcodes(
            ALOAD_name(self, '##__default_args__##'),
            ALOAD_name(self, '##__default_kwargs__##'),
            ICONST_val(self.code_obj.co_argcount - self.self_offset),
            ICONST_val(self.code_obj.co_flags),

            JavaOpcodes.INVOKESTATIC(
                'org/Python',
                'adjustArguments',
                '(Ljava/lang/String;Ljava/util/List;Ljava/util/Map;[Ljava/lang/String;Ljava/util/List;Ljava/util/Map;II)V'
            ),
        )
        for i in range(self.self_offset, len(self.parameters)):
            param = self.parameters[i]
            if param['kind'] == POSITIONAL_OR_KEYWORD:
                self.add_opcodes(
                    ALOAD_name(self, '##__args__##'),
                    ICONST_val(i - self.self_offset),
                    JavaOpcodes.INVOKEINTERFACE('java/util/List', 'get', '(I)Ljava/lang/Object;'),
                    ASTORE_name(self, param['name']),
                )
            elif param['kind'] == VAR_POSITIONAL:
                self.add_opcodes(
                    ALOAD_name(self, '##__args__##'),
                    ICONST_val(i - self.self_offset),
                    JavaOpcodes.INVOKEINTERFACE('java/util/List', 'get', '(I)Ljava/lang/Object;'),
                    ASTORE_name(self, param['name']),
                )
            elif param['kind'] == KEYWORD_ONLY:
                self.add_opcodes(
                    ALOAD_name(self, '##__kwargs__##'),
                    JavaOpcodes.LDC_W(param['name']),
                    JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),
                    ASTORE_name(self, param['name']),
                )
            elif param['kind'] == VAR_KEYWORD:
                self.add_opcodes(
                    ALOAD_name(self, '##__kwargs__##'),
                    JavaOpcodes.LDC_W(param['name']),
                    JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'get', '(Ljava/lang/Object;)Ljava/lang/Object;'),
                    ASTORE_name(self, param['name']),
                )

    def transpile_setup(self):
        self.transpile_args()

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

    def transpile(self):
        code = super().transpile()

        return JavaMethod(
            self.method_name,
            self.signature,
            static=self.static,
            attributes=[code] + self.method_attributes()
        )


class InitMethod(Method):
    def __init__(self, parent):
        super().__init__(
            parent, '<init>',
            parameters=[{
                'name': 'self',
                'kind': POSITIONAL_OR_KEYWORD
            }],
            returns={'annotation': None},
        )

    def __repr__(self):
        return '<Constructor %s (%s parameters)>' % (self.klass.name, len(self.parameters))

    @property
    def signature(self):
        return '(Ljava/util/List;Ljava/util/Map;)V'

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
    def has_void_return(self):
        return True

    @property
    def can_ignore_empty(self):
        return False

    @property
    def self_offset(self):
        return 1

    def add_arguments(self):
        self.local_vars['self'] = len(self.local_vars)
        self.local_vars['##__args__##'] = len(self.local_vars)
        self.local_vars['##__kwargs__##'] = len(self.local_vars)

    def transpile_setup(self):
        if self.klass.super_name == 'org/python/types/Object':
            self.add_opcodes(
                JavaOpcodes.ALOAD_0(),
                JavaOpcodes.INVOKESPECIAL(self.klass.super_name, '<init>', '()V'),
            )
        else:
            self.add_opcodes(
                JavaOpcodes.ALOAD_0(),
                ALOAD_name(self, '##__args__##'),
                ALOAD_name(self, '##__kwargs__##'),
                JavaOpcodes.INVOKESPECIAL(self.klass.super_name, '<init>', '(Ljava/util/List;Ljava/util/Map;)V'),
            )

        self.add_opcodes(
            TRY(),
                JavaOpcodes.ALOAD_0(),
                JavaOpcodes.LDC_W('__init__'),
                JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getattribute__', '(Ljava/lang/String;)Lorg/python/Object;'),

                ALOAD_name(self, '##__args__##'),
                ALOAD_name(self, '##__kwargs__##'),

                JavaOpcodes.INVOKEINTERFACE('org/python/Callable', 'invoke', '(Ljava/util/List;Ljava/util/Map;)Lorg/python/Object;'),
            CATCH('org/python/exceptions/AttributeError'),
            END_TRY(),
        )

    def method_attributes(self):
        return [
        ]


class InstanceMethod(Method):
    def __init__(self, parent, name, parameters, returns=None, static=False, commands=None, code=None):
        super().__init__(
            parent, name,
            parameters=parameters,
            returns=returns,
            static=static,
            commands=commands,
            code=code
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
    def self_offset(self):
        return 1

    def add_arguments(self):
        self.local_vars['self'] = len(self.local_vars)
        self.local_vars['##__args__##'] = len(self.local_vars)
        self.local_vars['##__kwargs__##'] = len(self.local_vars)
        self.local_vars['##__default_args__##'] = len(self.local_vars)
        self.local_vars['##__default_kwargs__##'] = len(self.local_vars)


class MainMethod(Method):
    def __init__(self, parent, commands=None, code=None, end_offset=None):
        super().__init__(
            parent, '__main__',
            parameters=[{'name': 'args', 'annotation': 'argv'}],
            returns={'annotation': None},
            static=True,
            commands=commands,
            code=code
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
    def has_void_return(self):
        return True

    @property
    def can_ignore_empty(self):
        return True

    @property
    def globals_module(self):
        return self.module

    def add_arguments(self):
        self.local_vars['##__args__##'] = len(self.local_vars)

    def add_return(self):
        # Main method is a special case - it always returns Null,
        # but the code doesn't contain this return, so the jump
        # target doesn't exist. Fake a jump target for the return
        if self.end_offset:
            python_op = Opcode(self.end_offset, None, True)
            java_op = JavaOpcodes.RETURN()
            python_op.start_op = java_op
            self.jump_targets[self.end_offset] = python_op
        else:
            java_op = JavaOpcodes.RETURN()

        self.add_opcodes(java_op)

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
            JavaOpcodes.LDC_W(self.module.descriptor.replace('/', '.')),
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
        # If there are any commands in this main method,
        # finish the TRY-CATCH for SystemExit
        if self.commands:
            self.add_opcodes(
                CATCH('org/python/exceptions/SystemExit'),
                    JavaOpcodes.GETFIELD('org/python/exceptions/SystemExit', 'return_code', 'I'),
                    JavaOpcodes.INVOKESTATIC('java/lang/System', 'exit', '(I)V'),
                END_TRY()
            )

    def method_attributes(self):
        return [
        ]


class ClosureMethod(Method):
    def __init__(self, parent, name, parameters, returns=None, static=False, commands=None, code=None):
        super().__init__(
            parent, name,
            parameters=parameters,
            returns=returns,
            static=static,
            commands=commands,
            code=code
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

    def add_arguments(self):
        self.local_vars['self'] = len(self.local_vars)
        self.local_vars['##__args__##'] = len(self.local_vars)
        self.local_vars['##__kwargs__##'] = len(self.local_vars)
        self.local_vars['##__default_args__##'] = len(self.local_vars)
        self.local_vars['##__default_kwargs__##'] = len(self.local_vars)

    # def _insert_closure_vars(self):
    #     # Load all the arguments into locals
    #     setup = []
    #     for i, closure_var_name in enumerate(self.parent.closure_var_names):
    #         setup.extend([
    #             ALOAD_name(self, 'self'),
    #             JavaOpcodes.GETFIELD('org/python/types/Function', closure_var_name, 'Lorg/python/Object;'),
    #             ASTORE_name(self, closure_var_name),
    #         ])
    #     self.code = setup + self.code


def extract_parameters(code):
    pos_count = code.co_argcount
    arg_names = code.co_varnames
    keyword_only_count = code.co_kwonlyargcount
    annotations = {}  # func.__annotations__

    parameters = []

    # Non-keyword-only parameters.
    for offset, name in enumerate(arg_names[0:pos_count]):
        parameters.append({
            'name': name,
            'annotation': annotations.get(name),
            'kind': POSITIONAL_OR_KEYWORD,
        })

    # *args
    if code.co_flags & CO_VARARGS:
        name = arg_names[pos_count + keyword_only_count]
        annotation = annotations.get(name)
        parameters.append({
            'name': name,
            'annotation': annotation,
            'kind': VAR_POSITIONAL
        })

    # Keyword-only parameters.
    for name in arg_names[pos_count:pos_count + keyword_only_count]:
        parameters.append({
            'name': name,
            'annotation': annotations.get(name),
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
            'annotation': annotations.get(name),
            'kind': VAR_KEYWORD
        })

    return parameters
