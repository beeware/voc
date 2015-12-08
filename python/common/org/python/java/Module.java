package org.python.java;

public class Module extends org.python.types.Module {

    public java.lang.String java_namespace;

    public int hashCode() {
        return this.java_namespace.hashCode();
    }

    public Module(java.lang.String java_namespace) {
        super();
        this.java_namespace = java_namespace;
    }

    public org.python.types.Str __repr__() {
        return new org.python.types.Str(String.format("<Native module '%s'>", this.java_namespace));
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getattribute__(org.python.Object name) {
        java.lang.String attr_name;
        try {
            attr_name = ((org.python.types.Str) name).value;
        } catch (java.lang.ClassCastException e) {
            throw new org.python.exceptions.TypeError("__getattribute__(): attribute name must be string");
        }

        // System.out.println("GETATTRIBUTE NATIVE MODULE " + this + " " + name);
        org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
        // System.out.println("instance attrs = " + this.attrs);
        // System.out.println("class attrs = " + cls.attrs);
        org.python.Object value;

        value = cls.attrs.get(attr_name);
        if (value == null) {
            try {
                java.lang.Class java_class = java.lang.Class.forName(java_namespace + "." + attr_name);
                value = new org.python.java.Type(java_class);
                cls.attrs.put(attr_name, value);
            } catch (java.lang.ClassNotFoundException e) {
                throw new org.python.exceptions.NameError(attr_name);
            }
        }
        return value;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __setattr__(org.python.Object name, org.python.Object value) {
        java.lang.String attr_name;
        try {
            attr_name = ((org.python.types.Str) name).value;
        } catch (java.lang.ClassCastException e) {
            throw new org.python.exceptions.TypeError("__setattr__(): attribute name must be string");
        }

        // The base object can't have attribute set on it unless the attribute already exists.
        // System.out.println("SETATTRIBUTE NATIVE MODULE " + this + " " + name + " = " + value);
        org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
        // System.out.println("instance attrs = " + this.attrs);
        // System.out.println("class attrs = " + cls.attrs);

        cls.attrs.put(attr_name, value);
    }
}
