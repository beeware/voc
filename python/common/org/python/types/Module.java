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

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str(String.format("<module '%s' from '%s'>", this.typeName(), this.getClass()));
    }

    public org.python.Object __getattribute__(java.lang.String name) {
        org.python.Object value = this.__getattribute_null(name);
        if (value == null) {
            throw new org.python.exceptions.NameError(name);
        }
        return value;
    }

    public org.python.Object __getattribute_null(java.lang.String name) {
        // System.out.println("GETATTRIBUTE MODULE " + this + " " + name);
        // System.out.println("MODULE ATTRS " + this.__dict__);
        org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
        // System.out.println("MODULE CLS = " + cls);
        // System.out.println("MODULE CLS ATTRS = " + cls.__dict__);

        // org.python.Object value = this.__dict__.get(name);
        org.python.Object value = cls.__dict__.get(name);
        if (value == null) {
            // The class attributes didn't contain the object. We must
            // differentiate between "doesn't exist" and "value is null";
            // If the key *doesn't* exist in the attributes dictionary,
            // try to look it up. If it doesn't exist as a field, then
            // store a null to represent this fact, so we won't look again.
            if (!cls.__dict__.containsKey(name)) {
                try {
                    value = new org.python.java.Field(klass.getField(name));
                } catch (java.lang.NoSuchFieldException e) {
                    value = null;
                }
                // If the field doesn't exist, store a value of null
                // so that we don't try to look up the field again.
                cls.__dict__.put(name, value);
            }
        }

        // If we don't have a module attribute, look for a builtin.
        if (value == null) {
            value = org.Python.builtins.get(name);
        }
        return value;
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        if (!this.__setattr_null(name, value)) {
            throw new org.python.exceptions.TypeError("can't set attributes of built-in/extension type '" + org.Python.typeName(this.klass) + "'");
        }
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // System.out.println("SETATTRIBUTE MODULE " + this + " " + name + " = " + value);
        org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
        // System.out.println("instance __dict__ = " + this.__dict__);
        // System.out.println("class __dict__ = " + cls.__dict__);
        org.python.Object attr = cls.__getattribute_null(name);

        // System.out.println("attr = " + attr);
        if (attr == null) {
            cls.__dict__.put(name, value);
        } else {
            attr.__set__(this, value);
        }

        return true;
    }

    public void __delattr__(java.lang.String name) {
        if (!this.__delattr_null(name)) {
            throw new org.python.exceptions.NameError(name);
        }
    }

    public boolean __delattr_null(java.lang.String name) {
        // System.out.println("DELETE ATTR from " + this.__dict__);
        org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
        org.python.Object result = cls.__dict__.remove(name);
        return (result != null);
    }
}
