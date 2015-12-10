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
        // System.out.println("GETATTRIBUTE CLASS " + this + " " + name);
        // System.out.println("CLASS ATTRS " + this.attrs);
        org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
        org.python.Object value = cls.attrs.get(name);

        if (value == null) {
            // The class attributes didn't contain the object. We must
            // differentiate between "doesn't exist" and "value is null";
            // If the key *doesn't* exist in the attributes dictionary,
            // try to look it up. If it doesn't exist as a field, then
            // store a null to represent this fact, so we won't look again.
            if (!cls.attrs.containsKey(name)) {
                try {
                    value = new org.python.java.Field(klass.getField(name));
                } catch (java.lang.NoSuchFieldException e) {
                    value = null;
                }
                // If the field doesn't exist, store a value of null
                // so that we don't try to look up the field again.
                cls.attrs.put(name, value);
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
        // System.out.println("instance attrs = " + this.attrs);
        // System.out.println("class attrs = " + cls.attrs);
        org.python.Object attr = cls.__getattribute_null(name);

        if (attr == null) {
            this.attrs.put(name, value);
        } else {
            attr.__set__(this, value);
        }

        cls.attrs.put(name, value);
        return true;
    }
}
