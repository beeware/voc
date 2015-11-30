package org.python.types;

public class NoneType extends org.python.types.Object {
    public static org.python.Object NONE = new org.python.types.NoneType();

    public java.lang.String typeName() {
        return "NoneType";
    }

    NoneType() {}

    public org.python.types.Str __repr__() {
        return new org.python.types.Str("None");
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        // None has no attributes.
        throw new org.python.exceptions.AttributeError(this, name);
    }
}