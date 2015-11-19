package org.python.types;

public class NoneType extends org.python.types.Object {
    public static org.python.Object NONE = new org.python.types.NoneType();

    NoneType() {}

    public org.python.types.Str __repr__() {
        return new org.python.types.Str("None");
    }

}