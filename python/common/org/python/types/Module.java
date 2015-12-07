package org.python.types;

public class Module extends org.python.types.Object {

    public java.lang.Class klass;

    public int hashCode() {
        return this.klass.hashCode();
    }

    protected Module() {
        this.klass = this.getClass();
    }

    public Module(java.lang.Class klass) {
        this.klass = klass;
    }

    public org.python.types.Str __repr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__repr__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        return new org.python.types.Str(String.format("<module '%s' from '%s'>", this.typeName(), this.getClass()));
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getattribute__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __getattribute__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        } else if (!(args.get(0) instanceof org.python.types.Str)) {
            throw new org.python.exceptions.TypeError("__getattribute__(): attribute name must be string");
        }

        java.lang.String name = ((org.python.types.Str) args.get(0)).value;

        // System.out.println("GETATTRIBUTE MODULE " + this + " " + name);
        org.python.Object value;
        try {
            // First try the normal approach attribute
            org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
            // System.out.println("instance attrs = " + this.attrs);
            // System.out.println("class attrs = " + cls.attrs);
            value = cls.attrs.get(name);

            if (value == null) {
                throw new org.python.exceptions.AttributeError(this, name);
            }
        } catch (org.python.exceptions.AttributeError e) {
            // System.out.println("MODULE NO ATTRIBUTE");
            value = org.Python.builtins.get(name);

            if (value == null) {
                throw new org.python.exceptions.NameError(name);
            }
        }

        return value;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __setattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__setattr__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 2) {
            throw new org.python.exceptions.TypeError("Expected 2 arguments, got " + args.size());
        } else if (!(args.get(0) instanceof org.python.types.Str)) {
            throw new org.python.exceptions.TypeError("__setattr__(): attribute name must be string");
        }

        java.lang.String name = ((org.python.types.Str) args.get(0)).value;
        org.python.Object value = args.get(1);

        // The base object can't have attribute set on it unless the attribute already exists.
        // System.out.println("SETATTRIBUTE MODULE " + this + " " + name + " = " + value);
        org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
        // System.out.println("instance attrs = " + this.attrs);
        // System.out.println("class attrs = " + cls.attrs);

        cls.attrs.put(name, value);

        // If there is a native field of the same name, set it.
        try {
            java.lang.reflect.Field field = this.getClass().getField(name);
            field.set(this, value);
        } catch (NoSuchFieldException e) {
            // System.out.println("Not a native field");
        } catch (IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to native field " + name);
        }
    }
}
