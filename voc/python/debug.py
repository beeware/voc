import ast

from ..java import opcodes as JavaOpcodes
from .types.primitives import ALOAD_name

##########################################################################
# Debugging helpers
##########################################################################


def dump(node, annotate_fields=True, include_attributes=True, indent='  '):
    """
    Return a formatted dump of the tree in *node*.  This is mainly useful for
    debugging purposes.  The returned string will show the names and the values
    for fields.  This makes the code impossible to evaluate, so if evaluation is
    wanted *annotate_fields* must be set to False.  Attributes such as line
    numbers and column offsets are not dumped by default.  If this is wanted,
    *include_attributes* can be set to True.
    """
    def _format(node, level=0):
        if isinstance(node, ast.AST):
            fields = [(a, _format(b, level)) for a, b in ast.iter_fields(node)]
            if include_attributes and node._attributes:
                fields.extend([(a, _format(getattr(node, a), level))
                               for a in node._attributes])
            return ''.join([
                node.__class__.__name__,
                '(',
                ', '.join(
                    ('%s=%s' % field for field in fields)
                    if annotate_fields else (b for a, b in fields)),
                ')'])
        elif isinstance(node, list):
            lines = ['[']
            lines.extend((indent * (level + 2) + _format(x, level + 2) + ','
                         for x in node))
            if len(lines) > 1:
                lines.append(indent * (level + 1) + ']')
            else:
                lines[-1] += ']'
            return '\n'.join(lines)
        return repr(node)

    if not isinstance(node, ast.AST):
        raise TypeError('expected AST, got %r' % node.__class__.__name__)

    return _format(node)


class DEBUG:
    def __init__(self, msg):
        self.msg = msg

    def process(self, context):
        context.add_opcodes(
            JavaOpcodes.LDC_W(self.msg),
            JavaOpcodes.INVOKESTATIC(
                'org/Python',
                'debug',
                args=['Ljava/lang/String;'],
                returns='V'),
        )
        # This opcode isn't for the final output.
        return False


class DEBUG_name:
    def __init__(self, name):
        self.name = name

    def process(self, context):
        context.add_opcodes(
            JavaOpcodes.LDC_W(self.name),
            ALOAD_name(context, self.name),
            JavaOpcodes.INVOKESTATIC(
                'org/Python',
                'debug',
                args=['Ljava/lang/String;', 'Ljava/lang/Object;'],
                returns='V'
            ),
        )
        # This opcode isn't for the final output.
        return False


class DEBUG_value:
    def __init__(self, msg, dup=False):
        self.msg = msg
        self.dup = dup

    def process(self, context):
        if self.dup:
            context.add_opcodes(JavaOpcodes.DUP())
        context.add_opcodes(
            JavaOpcodes.LDC_W(self.msg),
            JavaOpcodes.SWAP(),
            JavaOpcodes.INVOKESTATIC(
                'org/Python',
                'debug',
                args=['Ljava/lang/String;', 'Ljava/lang/Object;'],
                returns='V'
            ),
        )
        # This opcode isn't for the final output.
        return False
