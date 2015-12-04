package org.python.exceptions;


public class AttributeError extends org.python.exceptions.Exception {
    public AttributeError(org.python.Object obj, String attr) {
        super("'" + obj.typeName() + "' object has no attribute '" + attr + "'");
    }

    public AttributeError(java.lang.Class klass, String attr) {
        super("'" + org.python.types.Type.pythonType(klass).typeName() + "' object has no attribute '" + attr + "'");
    }
}
