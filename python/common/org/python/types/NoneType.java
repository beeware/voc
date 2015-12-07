package org.python.types;

public class NoneType extends org.python.types.Object {
    public static org.python.Object NONE = new org.python.types.NoneType();
    public static final java.lang.String PYTHON_TYPE_NAME = "NoneType";

    NoneType() {}

    public org.python.types.Str __repr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__repr__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        return new org.python.types.Str("None");
    }

    public void __setattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__setattr__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 2) {
            throw new org.python.exceptions.TypeError("Expected 2 arguments, got " + args.size());
        } else if (!(args.get(0) instanceof org.python.types.Str)) {
            throw new org.python.exceptions.TypeError("__setattr__(): attribute name must be string");
        }

        // None has no attributes.
        throw new org.python.exceptions.AttributeError(this, ((org.python.types.Str) args.get(0)).value);
    }
}