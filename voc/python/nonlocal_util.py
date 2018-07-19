from ..java import opcodes as JavaOpcodes
from .types import java, python
from .types.primitives import ALOAD_name


def resolve_nonlocal(current_context, name):
    # updates value of `name` in `current_context` if it is modified as nonlocal
    if hasattr(current_context, 'nonlocal_resolve_list') and name in current_context.nonlocal_resolve_list:
        current_context.nonlocal_resolve_list.pop(current_context.nonlocal_resolve_list.index(name))
        current_context.add_opcodes(
            python.Type.for_name(current_context.class_descriptor),
            JavaOpcodes.LDC_W(name),
            JavaOpcodes.INVOKEVIRTUAL(
                'org/python/types/Type',
                'get_nonlocal_var',
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
    # store in parent_context's nonlocal_vars
    context = _get_enclosing_context(current_context, name)
    current_context.add_opcodes(
        python.Type.for_name(context.class_descriptor),
        JavaOpcodes.SWAP(),
        JavaOpcodes.LDC_W(name),
        JavaOpcodes.SWAP(),
        JavaOpcodes.INVOKEVIRTUAL(
            'org/python/types/Type',
            'set_nonlocal_var',
            args=['Ljava/lang/String;', 'Lorg/python/Object;'],
            returns='V'
        ),
    )

    if hasattr(context, 'nonlocal_resolve_list'):
        context.nonlocal_resolve_list.append(name)
    else:
        setattr(context, 'nonlocal_resolve_list', [name])

