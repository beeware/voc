package org.python.types;


public class Function extends org.python.types.Object implements org.python.Callable {
    public static final int CO_OPTIMIZED = 0x1;
    public static final int CO_NEWLOCALS = 0x2;
    public static final int CO_VARARGS = 0x4;
    public static final int CO_VARKEYWORDS = 0x8;
    public static final int CO_NESTED = 0x10;
    public static final int CO_GENERATOR = 0x20;
    public static final int CO_NOFREE = 0x40;

    org.python.types.Str name;
    org.python.types.Code code;
    java.lang.reflect.Method method;
    java.util.Map<java.lang.String, org.python.Object> globals;
    java.util.List<org.python.Object> default_args;
    java.util.Map<java.lang.String, org.python.Object> default_kwargs;
    java.util.List<org.python.Object> closure;

    private void populateAttrs() {
        org.python.types.Str name = new org.python.types.Str(method.getName());
        this.attrs.put("__name__", this.name);

        if (this.name != null) {
            this.attrs.put("__qualname__", this.name);
        } else {
            org.python.Object co_name = this.code.attrs.get("co_consts");
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

        // System.out.println("CREATE FUNCTION 1 " + this.name);
        // java.lang.Thread.currentThread().dumpStack();

        // this.code = new org.python.types.Code(
        //     new org.python.types.Int(),  // co_argcount
        //     new org.python.types.Tuple(),  // co_cellvars
        //     new org.python.types.Bytes(),  // co_code
        //     new org.python.types.Tuple(),  // co_consts
        //     new org.python.types.Str(),  // co_filename
        //     new org.python.types.Int(),  // co_firstlineno
        //     new org.python.types.Int(),  // co_flags
        //     new org.python.types.Tuple(),  // co_freevars
        //     new org.python.types.Int(),  // co_kwonlyargcount
        //     new org.python.types.Bytes(),  // co_lnotab
        //     new org.python.types.Str(),  // co_name
        //     new org.python.types.Tuple(),  // co_names
        //     new org.python.types.Int(),  // co_nlocals
        //     new org.python.types.Int(),  // co_stacksize
        //     new org.python.types.Tuple(),  // co_varnames
        // );
        populateAttrs();
    }

    // Constructor for Java shims of Python modules

    // Constructor for normal Python functions
    public Function(
            org.python.types.Str name,
            org.python.types.Code code,
            java.lang.reflect.Method method,
            java.util.Map<java.lang.String, org.python.Object> globals,
            java.util.List<org.python.Object> default_args,
            java.util.Map<java.lang.String, org.python.Object> default_kwargs,
            java.util.List<org.python.Object> closure) {
        super();

        // System.out.println("Create function 2 " + name);
        // java.lang.Thread.currentThread().dumpStack();

        this.name = name;
        this.code = code;
        this.method = method;
        this.globals = globals;
        this.default_args = default_args;
        this.default_kwargs = default_kwargs;
        this.closure = closure;

        populateAttrs();
    }

    public org.python.Object __get__(org.python.Object instance, org.python.types.Type klass) {
        if (instance != null && !(instance instanceof org.python.types.Module)) {
            return new Method(instance, klass, this);
        }
        return this;
    }

    public org.python.Object invoke(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        return this.invoke(null, args, kwargs);
    }

    public org.python.Object invoke(org.python.Object instance, java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            // System.out.println("Function:" + this.method);
            // System.out.println("           args:" + args);
            // System.out.println("         kwargs:" + kwargs);
            // System.out.println("   default args: " + this.default_args);
            // System.out.println(" default kwargs: " + this.default_kwargs);

            // if this.attrs.__code__.co_flags & CO_GENERATOR:
            //     gen = Generator(frame, self._vm)
            //     frame.generator = gen
            //     retval = gen
            // else:

            if (this.default_args != null) {
                return (org.python.Object) this.method.invoke(instance, args, kwargs, this.default_args, this.default_kwargs);
            } else {
                return (org.python.Object) this.method.invoke(instance, args, kwargs);
            }
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java method " + this.method);
        } catch (java.lang.reflect.InvocationTargetException e) {
            try {
                // e.getTargetException().printStackTrace();
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
