package org.python.types;

public class NoneType extends org.python.types.Object {
    public static org.python.Object NONE = new org.python.types.NoneType();
    public static final java.lang.String PYTHON_TYPE_NAME = "NoneType";

    NoneType() {}

    public java.lang.Object toJava() {
        return null;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str("None");
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        return false;
    }
}