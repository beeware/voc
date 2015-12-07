package org.python.java;


public class Object extends org.python.types.Object {
    static
    // public static org.python.Object convert(java.lang.Object java) {
    //     if (java instanceof java.lang.String) {
    //         return new org.python.types.Str((java.lang.String) java);
    //     } else {
    //         return new org.python.java.Object(java);
    //     }
    // }

    public java.lang.Object object;

    public int hashCode() {
        return this.object.hashCode();
    }

    public java.lang.Object toJava() {
        return this.object;
    }

    public Object(java.lang.Object object) {
        super(org.python.types.Type.Origin.JAVA, object.getClass());
        this.object = object;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__repr__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        return new org.python.types.Str(String.format("<Native %s object at 0x>", this.object.getClass(), this.object.hashCode()));
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __str__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__str__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        return new org.python.types.Str(this.object.toString());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getattribute__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__getitem__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object name = args.get(0);
        // System.out.println("GETATTRIBUTE NATIVE OBJECT " + this + " " + name);
        // Look for a cached attribute.
        org.python.Object value = this.attrs.get(name);

        if (value == null) {
            // Look for a cached class-level attribute.
            org.python.types.Type klass = (org.python.types.Type) this.attrs.get("__class__");
            value = klass.__getattribute__(args, kwargs, default_args, default_kwargs).__get__(this, klass);
        }

        return value;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __setattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__setattribute__() doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        } else if (!(args.get(0) instanceof org.python.types.Str)) {
            throw new org.python.exceptions.TypeError("__setattribute__(): attribute name must be string");
        }

        org.python.types.Str name = (org.python.types.Str) args.get(0);
        // System.out.println("SETATTRIBUTE NATIVE OBJECT " + this + " " + name);
        // Look for a cached attribute.
        org.python.Object value = args.get(1);

        // System.out.println("SETATTRIBUTE NATIVE OBJECT " + this + " " + name + " = " + value);
        try {
            java.util.List<org.python.Object> get_args = new java.util.ArrayList<org.python.Object>(1);
            get_args.add(args.get(0));

            org.python.Object attr = this.__getattribute__(get_args, null, null, null);

            if (attr instanceof org.python.java.Attribute) {
                ((org.python.java.Attribute) attr).__set__(this, value);
            }
        } catch(org.python.exceptions.AttributeError e) {
        }

        this.attrs.put(name.value, value);
    }

}
