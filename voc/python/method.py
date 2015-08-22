from ..java import Method as JavaMethod


POSITIONAL_OR_KEYWORD = 1
VAR_POSITIONAL = 2
KEYWORD_ONLY = 3
VAR_KEYWORD = 4

CO_VARARGS = 0x0004
CO_VARKEYWORDS = 0x0008


def signature(code):
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
            'annotation': annotations[name],
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
            'annotation': annotations[name],
            'kind': VAR_KEYWORD
        })

    return parameters


def transpile(methodname, signature, parts, static=False):
    method = JavaMethod(
        methodname,
        '(%s)Lorg/python/PyObject;' % ('Lorg/python/PyObject;' * len(signature)),
        static=static,
        attributes=[
            parts.block
        ]
    )
    return method
