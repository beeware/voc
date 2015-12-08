package org.python.types;

public class NoneType extends org.python.types.Object {
    public static org.python.Object NONE = new org.python.types.NoneType();
    public static final java.lang.String PYTHON_TYPE_NAME = "NoneType";

    NoneType() {}

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str("None");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __setattr__(org.python.Object name, org.python.Object value) {
        java.lang.String attr_name;
        try {
            attr_name = ((org.python.types.Str) name).value;
        } catch (java.lang.ClassCastException e) {
            throw new org.python.exceptions.TypeError("__setattribute__(): attribute name must be string");
        }

        // None has no attributes.
        throw new org.python.exceptions.AttributeError(this, attr_name);
    }
}