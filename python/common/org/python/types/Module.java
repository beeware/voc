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

    public org.python.types.Str __repr__() {
        return new org.python.types.Str(String.format("<module '%s' from '%s'>", this.typeName(), this.getClass()));
    }

    public org.python.Object __getattribute__(java.lang.String name) {
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

    public void __setattr__(java.lang.String name, org.python.Object value) {
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
