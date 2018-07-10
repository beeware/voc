package org.python.types;

public class Module extends org.python.types.Object {
    public java.lang.Class klass;

    // Keeps track of all closure variables in current module.
    // Each variable name is identified by id of the context that owns the variable.
    // Used as value lookup for loading and storing of Python `nonlocal` variables
    // Also used by generator and method to access closure variables
    public org.python.types.Dict closure_vars;

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

    public void set_closure_var(java.lang.String name, org.python.Object value) {
        if (this.closure_vars == null) {
            this.closure_vars = new org.python.types.Dict();
        }
        this.closure_vars.__setitem__(new org.python.types.Str(name), value);
    }

    public org.python.Object get_closure_var(java.lang.String name) {
        return this.closure_vars.get(new org.python.types.Str(name), null);
    }

    public void cleanup_closure_vars(java.lang.String id) {
        // cleanup closure variables owned by context with id `id` before it goes out of scope
        if (this.closure_vars == null) {
            return;
        }
        java.util.Iterator key_iterator = this.closure_vars.value.keySet().iterator();
        while (key_iterator.hasNext()) {
            String key = ((org.python.types.Str) key_iterator.next()).value;
            String[] split_key = key.split("-");
            if (split_key[split_key.length - 1].equals(id)) {
                //System.out.println("removing " + key);
                key_iterator.remove();
            }
        }
    }
}
