from ..java import (
    Method as JavaMethod,
    opcodes as JavaOpcodes,
)

from .blocks import Block
from .opcodes import ALOAD_name, ASTORE_name, ICONST_val


POSITIONAL_OR_KEYWORD = 1
VAR_POSITIONAL = 2
KEYWORD_ONLY = 3
VAR_KEYWORD = 4

CO_VARARGS = 0x0004
CO_VARKEYWORDS = 0x0008


class Method(Block):
    def __init__(self, parent, name, parameters, returns=None, static=False, commands=None):
        super().__init__(parent, commands=commands)
        self.name = name
        self.parameters = parameters

        if returns is None:
            self.returns = {}
        else:
            self.returns = returns

        # Load args and kwargs, but don't expose those names into the localvars.
        self.add_self()
        self.localvars['##__args__##'] = len(self.localvars)
        self.localvars['##__kwargs__##'] = len(self.localvars)

        # Then reserve space for all the *actual* arguments.
        for i, arg in enumerate(self.parameters):
            self.localvars[arg['name']] = len(self.localvars)

        self.static = static

    def __repr__(self):
        return '<Method %s (%s parameters>' % (self.name, len(self.parameters))

    @property
    def is_constructor(self):
        return False

    @property
    def is_instancemethod(self):
        return False

    @property
    def is_closuremethod(self):
        return False

    @property
    def has_void_return(self):
        return self.returns.get('annotation', object()) is None

    def add_return(self):
        if self.has_void_return:
            self.add_opcodes(JavaOpcodes.RETURN())
        else:
            self.add_opcodes(JavaOpcodes.ARETURN())

    @property
    def callable(self):
        return 'org/python/types/Function'

    @property
    def signature(self):
        return_descriptor = 'V' if self.has_void_return else 'Lorg/python/Object;'
        return '([Lorg/python/Object;Ljava/util/Hashtable;)%s' % return_descriptor

    def add_self(self):
        pass

    @property
    def method_name(self):
        return self.name

    @property
    def module(self):
        return self.parent

    def add_method(self, method_name, code):
        # If a method is added to a method, it is added as an anonymous
        # inner class.
        from .klass import AnonymousInnerClass
        callable = AnonymousInnerClass(
            parent=self.parent,
            super_name='org/python/types/Object',
            interfaces=['org/python/Callable'],
            public=False,
            final=True,
        )

        method = ClosureMethod(callable, 'invoke', extract_parameters(code))
        method.extract(code)
        callable.methods.append(method.transpile())

        self.parent.classes.append(callable.transpile())

        return method

    def tweak(self):
        # Load all the arguments into locals
        setup = []
        for i, arg in enumerate(self.parameters):
            setup.extend([
                ALOAD_name(self, '##__args__##'),
                ICONST_val(i + 1 if self.is_instancemethod else 0),
                JavaOpcodes.AALOAD(),
                ASTORE_name(self, arg['name']),
            ])

        # Then run the code as normal.
        self.code = setup + self.code

        # If the method has a void return, clean up the final opcodes.
        if self.has_void_return:
            self.void_return()

    def transpile(self):
        code = super().transpile()

        return JavaMethod(
            self.method_name,
            self.signature,
            static=self.static,
            attributes=[
                code
            ]
        )


class InitMethod(Method):
    def __init__(self, parent, parameters, commands=None):
        super().__init__(
            parent, '__init__',
            parameters=parameters[1:],
            returns={'annotation': None},
            commands=commands
        )

    def __repr__(self):
        return '<Constructor %s (%s parameters>' % (self.klass.name, len(self.parameters))

    @property
    def is_constructor(self):
        return True

    @property
    def method_name(self):
        return '<init>'

    @property
    def klass(self):
        return self.parent

    @property
    def module(self):
        return self.klass.module

    def add_self(self):
        self.localvars['self'] = len(self.localvars)

    def tweak(self):
        # If the block is an init method, make sure it invokes super().<init>
        super_found = False
        # FIXME: Search for existing calls on <init>
        # for opcode in code:
        #     if isinstance(opcode, JavaOpcodes.INVOKESPECIAL) and opcode.method.name == '<init>':
        #         super_found = True
        #         break

        # Load all the arguments into locals
        setup = []
        for i, arg in enumerate(self.parameters):
            setup.extend([
                ALOAD_name(self, '##__args__##'),
                ICONST_val(i),
                JavaOpcodes.AALOAD(),
                ASTORE_name(self, arg['name']),
            ])

        if not super_found:
            setup.extend([
                JavaOpcodes.ALOAD_0(),
                JavaOpcodes.INVOKESPECIAL(self.klass.super_name, '<init>', '()V'),
            ])

        self.code = setup + self.code
        self.void_return()
        self.ignore_empty()


class InstanceMethod(Method):
    def __init__(self, parent, name, parameters, returns=None, static=False, commands=None):
        super().__init__(
            parent, name,
            parameters=parameters[1:],
            returns=returns,
            static=static,
            commands=commands
        )

    def __repr__(self):
        return '<InstanceMethod %s.%s (%s parameters>' % (self.klass.name, self.name, len(self.parameters))

    @property
    def is_instancemethod(self):
        return True

    @property
    def callable(self):
        return 'org/python/types/Method'

    @property
    def klass(self):
        return self.parent

    @property
    def module(self):
        return self.klass.module

    def add_self(self):
        self.localvars['self'] = len(self.localvars)


class MainMethod(Method):
    def __init__(self, parent, commands=None):
        super().__init__(
            parent, '__main__',
            parameters=[{'name': 'args', 'annotation': 'argv'}],
            returns={'annotation': None},
            static=True,
            commands=commands
        )

    def __repr__(self):
        return '<MainMethod %s' % self.module.name

    @property
    def method_name(self):
        return 'main'

    @property
    def module(self):
        return self.parent

    @property
    def signature(self):
        return '([Ljava/lang/String;)V'

    def tweak(self):
        self.void_return()
        self.ignore_empty()


class ClosureMethod(Method):
    def __init__(self, parent, name, parameters, returns=None, static=False, commands=None):
        super().__init__(
            parent, name,
            parameters=parameters,
            returns=returns,
            static=static,
            commands=commands
        )

    def __repr__(self):
        return '<ClosureMethod %s (%s parameters>' % (self.name, len(self.parameters))

    @property
    def is_instancemethod(self):
        return True

    @property
    def is_closuremethod(self):
        return True

    @property
    def callable(self):
        return self.parent.descriptor

    def add_self(self):
        self.localvars['self'] = len(self.localvars)


def extract_parameters(code):
    pos_count = code.co_argcount
    arg_names = code.co_varnames
    positional = arg_names[0: pos_count]
    keyword_only_count = code.co_kwonlyargcount
    keyword_only = arg_names[pos_count:pos_count + keyword_only_count]
    annotations = {}  # func.__annotations__
    defs = None  # func.__defaults__
    kwdefaults = None  # func.__kwdefaults__

    if defs:
        pos_default_count = len(defs)
    else:
        pos_default_count = 0

    parameters = []

    # Non-keyword-only parameters w/o defaults.
    non_default_count = pos_count - pos_default_count
    for name in positional[0: non_default_count]:
        parameters.append({
            'name': name,
            'annotation': annotations.get(name),
            'kind': POSITIONAL_OR_KEYWORD
        })

    # ... w/ defaults.
    for offset, name in enumerate(positional[non_default_count: len(positional)]):
        parameters.append({
            'name': name,
            'annotation': annotations.get(name),
            'kind': POSITIONAL_OR_KEYWORD,
            'default': defs[offset]
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
    for name in keyword_only:
        default = None
        if kwdefaults is not None:
            default = kwdefaults.get(name)

        parameters.append({
            'name': name,
            'annotation': annotations.get(name),
            'kind': KEYWORD_ONLY,
            'default': default
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
