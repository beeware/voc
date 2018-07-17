from ..java import opcodes as JavaOpcodes
from .types import python


def add_closure_variables(current_context, child_context, co_freevars):
    if co_freevars:
        from .klass import Class
        # stores closure variables in `current_context`
        child_context.closure_vars = co_freevars

        class_descriptor = current_context.descriptor if isinstance(current_context, Class) \
            else current_context.class_descriptor

        current_context.add_opcodes(
            python.Type.for_name(class_descriptor),
        )
        for var_name in co_freevars:
            if var_name == '__class__':
                # don't load super class, as it is resolved and handled differently in voc
                continue

            current_context.add_opcodes(
                JavaOpcodes.DUP(),
                JavaOpcodes.LDC_W(var_name),
            )
            current_context.load_name(var_name)
            current_context.add_opcodes(
                JavaOpcodes.INVOKEVIRTUAL(
                    'org/python/types/Type',
                    'set_closure_var',
                    args=['Ljava/lang/String;', 'Lorg/python/Object;'],
                    returns='V'
                ),
            )
        current_context.add_opcodes(
            JavaOpcodes.POP()
        )


def resolve_nonlocal(current_context, name):
    # updates value of `name` in `current_context` if it is modified as nonlocal
    if hasattr(current_context, 'nonlocal_resolve_list') and name in current_context.nonlocal_resolve_list:
        current_context.nonlocal_resolve_list.pop(current_context.nonlocal_resolve_list.index(name))
        current_context.add_opcodes(
            python.Type.for_name(current_context.class_descriptor),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKEVIRTUAL(
                'org/python/types/Type',
                'get_closure_var',
                args=['Ljava/lang/String;'],
                returns='Lorg/python/Object;'
            ),
        )
        current_context.store_name(name)


def _get_enclosing_context(child_context, name):
    from .methods import Closure
    # finds which outer scope of `child_context` owns the `name` variable
    for context in child_context.outer_scopes[::-1]:
        if name in context.local_vars:
            if isinstance(context, Closure) and name in context.closure_vars:
                continue  # not the actual owner
            return context

    return None  # None may imply that `name` if found in globals


def store_nonlocal(current_context, name):
    context = _get_enclosing_context(current_context, name)
    current_context.add_opcodes(
        python.Type.for_name(context.class_descriptor),
        JavaOpcodes.SWAP(),
        JavaOpcodes.LDC_W(name),
        JavaOpcodes.SWAP(),
        JavaOpcodes.INVOKEVIRTUAL(
            'org/python/types/Type',
            'set_closure_var',
            args=['Ljava/lang/String;', 'Lorg/python/Object;'],
            returns='V'
        ),
    )

    if hasattr(context, 'nonlocal_resolve_list'):
        context.nonlocal_resolve_list.append(name)
    else:
        setattr(context, 'nonlocal_resolve_list', [name])


def load_closure_var(current_context, name):
    context = _get_enclosing_context(current_context, name)
    if context is None:
        # Can't find owner of `name`, try to load it from global
        current_context.add_opcodes(
            JavaOpcodes.GETSTATIC('python/sys', 'modules', 'Lorg/python/types/Dict;'),

            python.Str(current_context.module.full_name),

            python.Object.get_item(),
            JavaOpcodes.CHECKCAST('org/python/types/Module'),
            python.Object.get_attribute(name),
        )
    else:
        current_context.add_opcodes(
            python.Type.for_name(context.class_descriptor),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKEVIRTUAL(
                'org/python/types/Type',
                'get_closure_var',
                args=['Ljava/lang/String;'],
                returns='Lorg/python/Object;'
            ),
        )
