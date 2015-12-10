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

    public org.python.Object __getattribute__(java.lang.String name) {
        // System.out.println("GETATTRIBUTE NATIVE MODULE " + this + " " + name);
        org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
        // System.out.println("instance attrs = " + this.attrs);
        // System.out.println("class attrs = " + cls.attrs);
        org.python.Object value;

        value = cls.attrs.get(name);
        if (value == null) {
            try {
                java.lang.Class java_class = java.lang.Class.forName(java_namespace + "." + name);
                value = new org.python.java.Type(java_class);
                cls.attrs.put(name, value);
            } catch (java.lang.ClassNotFoundException e) {
                throw new org.python.exceptions.NameError(name);
            }
        }
        return value;
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        // The base object can't have attribute set on it unless the attribute already exists.
        // System.out.println("SETATTRIBUTE NATIVE MODULE " + this + " " + name + " = " + value);
        org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
        // System.out.println("instance attrs = " + this.attrs);
        // System.out.println("class attrs = " + cls.attrs);

        cls.attrs.put(name, value);
    }
}
