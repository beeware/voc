package org.python.types;

public class Module extends org.python.types.Object {
    public java.lang.Class klass;

    public int hashCode() {
        return this.klass.hashCode();
    }

    public void module$import() {
        org.Python.initializeModule(this.getClass(), this.__dict__);
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
        return new org.python.types.Str(
                String.format(
                        "<module '%s' from '%s.class'>",
                        this.getClass().getPackage().getName(),
                        this.getClass()
                )
        );
    }

    public org.python.Object __getattribute__(java.lang.String name) {
        org.python.Object value = this.__getattribute_null(name);
        if (value == null) {
            throw new org.python.exceptions.NameError(name);
        }
        return value;
    }

    public org.python.Object __getattribute_null(java.lang.String name) {
        //     System.out.println("GETATTRIBUTE MODULE " + this + " " + name);
        //     // System.out.println("MODULE ATTRS " + this.__dict__);
        //     org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
        //     // System.out.println("MODULE CLS = " + cls);
        //     // System.out.println("MODULE CLS ATTRS = " + cls.__dict__);

        org.python.Object value = super.__getattribute_null(name);

        // If we don't have a module attribute, look for a builtin.
        if (value == null) {
            value = org.Python.builtins.get(name);
        }

        // System.out.println("GETATTR Module value " + name + " = " + value);
        return value;
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        if (!this.__setattr_null(name, value)) {
            throw new org.python.exceptions.TypeError("can't set attributes of built-in/extension type '" + org.Python.typeName(this.klass) + "'");
        }
    }

    public void __delattr__(java.lang.String name) {
        if (!this.__delattr_null(name)) {
            throw new org.python.exceptions.NameError(name);
        }
    }
}
