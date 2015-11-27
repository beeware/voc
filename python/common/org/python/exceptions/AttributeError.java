package org.python.exceptions;

public class AttributeError extends org.python.exceptions.Exception {
    public AttributeError(org.python.Object obj, String attr) {
        super(org.Python.typeName(obj) + " has no attribute '" + attr + "'");
    }
}
