package org.python.exceptions;

public class AttributeError extends org.python.exceptions.Exception {
    public AttributeError(java.lang.String msg) {
        super(msg);
    }

    public AttributeError(org.python.Object obj, java.lang.String attr) {
        super("'" + obj.typeName() + "' object has no attribute '" + attr + "'");
    }

    public AttributeError(java.lang.Class klass, java.lang.String attr) {
        super("'" + org.python.types.Type.pythonType(klass).typeName() + "' object has no attribute '" + attr + "'");
    }

    public AttributeError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super("'" + args[0] + "' object has no attribute '" + args[1] + "'");
    }
}
