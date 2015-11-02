package org.python.types;

public class Function extends org.python.types.Object implements org.python.Callable {
    org.python.types.Str name;
    org.python.types.Code code;
    java.lang.reflect.Method method;
    java.util.Map<java.lang.String, org.python.Object> globals;
    java.util.Map<java.lang.String, org.python.Object> defaults;
    java.util.ArrayList closure;

    private void populateAttrs() {
        org.python.types.Str name = new org.python.types.Str(method.getName());
        this.attrs.put("__name__", this.name);

        if (this.name != null) {
            this.attrs.put("__qualname__", this.name);
        } else {
            org.python.Object co_name = this.code.__getattribute__("co_consts");
            this.attrs.put("__qualname__", co_name);
        }

        // this.attrs.put("__code__", this.code);

        // org.python.Object doc;
        // try {
        //     org.python.types.Tuple consts = ((org.python.types.Tuple) this.code.__getattribute__("co_consts"));
        //     if (consts != null) {
        //         doc = consts.__getitem__(0);
        //     } else {
        //         doc = null;
        //     }
        // } catch (java.lang.ClassCastException e) {
        //     doc = null;
        // } catch (java.lang.IndexOutOfBoundsException e) {
        //     doc = null;
        // }
        // this.attrs.put("__doc__", doc);

        // this.attrs.put("__call__")
    }

    // Constructor for builtins
    public Function(java.lang.reflect.Method method) {
        super();
        this.name = new org.python.types.Str(method.getName());
        this.method = method;

        populateAttrs();
    }

    // Constructor for Java shims of Python modules

    // Constructor for normal Python functions
    public Function(
            org.python.types.Str name,
            org.python.types.Code code,
            java.lang.reflect.Method method,
            java.util.Map<java.lang.String, org.python.Object> globals,
            java.util.Map<java.lang.String, org.python.Object> defaults,
            java.util.ArrayList closure) {
        super();
        this.name = name;
        this.code = code;
        this.method = method;
        this.globals = globals;
        this.defaults = defaults;
        this.closure = closure;

        populateAttrs();
    }

    public org.python.Object __get__(org.python.Object instance, org.python.types.Type klass) {
        if (instance != null) {
            return new Method(instance, klass, this);
        }
        return this;
    }

    public org.python.Object invoke(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            // System.out.println("Function:" + this.method);
            // System.out.println("ARGS:");
            // for (org.python.Object arg: args) {
            //     System.out.println("  " + arg);
            // }

            // if this.attrs.__code__.co_flags & CO_GENERATOR:
            //     gen = Generator(frame, self._vm)
            //     frame.generator = gen
            //     retval = gen
            // else:

           return (org.python.Object) this.method.invoke(null, args, kwargs);
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java function " + this.method);
        } catch (java.lang.reflect.InvocationTargetException e) {
            try {
                // If the Java method raised an Python exception, re-raise that
                // exception as-is. If it wasn"t a Python exception, wrap it
                // as one and continue.
                throw (org.python.exceptions.BaseException) e.getCause();
            } catch (ClassCastException java_e) {
                throw new org.python.exceptions.RuntimeError(e.getCause().getMessage());
            }
        } finally {
        //     System.out.println("INVOKE METHOD DONE");
        }
    }
}
