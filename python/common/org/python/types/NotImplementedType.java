package org.python.types;

public class NotImplementedType extends org.python.types.Object {
    public static org.python.Object NOT_IMPLEMENTED = new org.python.types.NotImplementedType();
    public static final java.lang.String PYTHON_TYPE_NAME = "NotImplementedType";

    NotImplementedType() {}

    public java.lang.Object toJava() {
        return null;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str("NotImplemented");
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        return false;
    }
}
