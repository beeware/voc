package org.python.types;


public class Function extends org.python.types.Object implements org.python.Callable {
    public static final int CO_OPTIMIZED = 0x1;
    public static final int CO_NEWLOCALS = 0x2;
    public static final int CO_VARARGS = 0x4;
    public static final int CO_VARKEYWORDS = 0x8;
    public static final int CO_NESTED = 0x10;
    public static final int CO_GENERATOR = 0x20;
    public static final int CO_NOFREE = 0x40;

    org.python.types.Type.Origin origin;

    org.python.types.Str name;
    org.python.types.Code code;
    java.lang.reflect.Method method;

    java.util.Map<java.lang.String, org.python.Object> globals;
    java.util.List<org.python.Object> default_args;
    java.util.Map<java.lang.String, org.python.Object> default_kwargs;
    java.util.List<org.python.Object> closure;

    private void populateAttrs() {
        org.python.types.Str name = new org.python.types.Str(method.getName());
        this.__dict__.put("__name__", this.name);

        if (this.name != null) {
            this.__dict__.put("__qualname__", this.name);
        } else {
            org.python.Object co_name = this.code.__dict__.get("co_consts");
            this.__dict__.put("__qualname__", co_name);
        }

        this.__dict__.put("__code__", this.code);

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
        // this.__dict__.put("__doc__", doc);

        // this.__dict__.put("__call__")
    }

    // Constructor for builtins
    public Function(
            java.lang.reflect.Method method,
            java.lang.String [] args,
            java.lang.String [] default_args,
            java.lang.String vararg_name,
            java.lang.String [] kwonlyargs,
            java.lang.String kwargs_name) {
        super();
        this.origin = org.python.types.Type.Origin.BUILTIN;
        this.name = new org.python.types.Str(method.getName());
        this.method = method;

        // System.out.println("CREATE FUNCTION 1 " + this.name);
        // java.lang.Thread.currentThread().dumpStack();

        long flags = 0;
        long argcount = 0;
        long kwonly = 0;
        java.util.List<org.python.Object> varnames = new java.util.ArrayList<org.python.Object>();

        for (java.lang.String arg: args) {
            varnames.add(new org.python.types.Str(arg));
        }

        this.default_args = new java.util.ArrayList<org.python.Object>();
        for (java.lang.String arg: default_args) {
            this.default_args.add(null);
            varnames.add(new org.python.types.Str(arg));
        }

        // The base argument count is the length of the arguments collected so far.
        argcount = varnames.size();

        if (vararg_name != null) {
            flags |= CO_VARARGS;
            varnames.add(new org.python.types.Str(vararg_name));
        }

        this.default_kwargs = new java.util.HashMap<java.lang.String, org.python.Object>();
        for (java.lang.String arg: kwonlyargs) {
            varnames.add(new org.python.types.Str(arg));
            this.default_kwargs.put(arg, null);
        }

        if (kwargs_name != null) {
            flags |= CO_VARKEYWORDS;
            varnames.add(new org.python.types.Str(kwargs_name));
        }

        this.code = new org.python.types.Code(
            new org.python.types.Int(argcount),  // co_argcount
            null,  // new org.python.types.Tuple(),  // co_cellvars
            null,  // new org.python.types.Bytes(),  // co_code
            null,  // new org.python.types.Tuple(),  // co_consts
            null,  // new org.python.types.Str(),  // co_filename
            null,  // new org.python.types.Int(),  // co_firstlineno
            new org.python.types.Int(flags),  // co_flags
            null,  // new org.python.types.Tuple(),  // co_freevars
            new org.python.types.Int(kwonlyargs.length),  // co_kwonlyargcount
            null,  // new org.python.types.Bytes(),  // co_lnotab
            this.name,  // co_name
            null,  // new org.python.types.Tuple(),  // co_names
            null,  // new org.python.types.Int(),  // co_nlocals
            null,  // new org.python.types.Int(),  // co_stacksize
            new org.python.types.Tuple(varnames)  // co_varnames
        );
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

        this.origin = org.python.types.Type.Origin.PYTHON;

        this.name = name;
        this.code = code;
        this.method = method;
        this.globals = globals;
        this.default_args = default_args;
        this.default_kwargs = default_kwargs;
        this.closure = closure;

        populateAttrs();
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __get__(org.python.Object instance, org.python.Object klass) {
        // System.out.println("__GET__ on function " + this + " " + this.getClass() + " " + instance + " " + instance.getClass());
        if (instance != klass && !(instance instanceof org.python.types.Module)) {
            return new Method(instance, (org.python.types.Type) klass, this);
        }
        return this;
    }

    java.lang.Object [] adjustArguments(org.python.Object instance, org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        // if (kwargs.size() > 0) {
        //     // TODO: This doesn't have to be so - we *could* introspect argument names.
        //     throw new org.python.exceptions.RuntimeError("Cannot use kwargs to invoke a native Java method.");
        // }
        // System.out.println("CODE " + this.code + " ");

        int pos_count = (int) this.code.co_argcount.value;
        int keyword_only_count = (int) this.code.co_kwonlyargcount.value;
        int flags = (int) this.code.co_flags.value;
        java.util.List<org.python.Object> varnames = this.code.co_varnames.value;

        int first_arg;
        int first_default;
        // System.out.println("counts " + pos_count + " " + keyword_only_count + " " + flags);

        int n_args = pos_count + keyword_only_count;
        if ((flags & CO_VARARGS) != 0) {
            n_args += 1;
        }
        if ((flags & CO_VARKEYWORDS) != 0) {
            n_args += 1;
        }

        first_default = pos_count - this.default_args.size();
        // System.out.println("nargs " + n_args);

        if (n_args == 0) {
            return null;
        }

        java.lang.Object [] adjusted = new java.lang.Object [n_args];

        // If this is an instance, the first argument will be self; we don't
        // need to pass this to the Java function.
        if (instance == null || !java.lang.reflect.Modifier.isStatic(method.getModifiers())) {
            first_arg = 0;
        } else {
            first_arg = 1;
            adjusted[0] = instance;
        }

        for (int i = first_arg; i < pos_count; i++) {
            java.lang.String varname = ((org.python.types.Str) varnames.get(i)).value;
            if (i < args.length + first_arg) {
                adjusted[i] = args[i - first_arg];
                org.python.Object value = kwargs.remove(varname);
                if (value != null) {
                    throw new org.python.exceptions.TypeError(this.name + "() got multiple values for argument '" + varname + "'");
                }
            } else {
                org.python.Object value = kwargs.remove(varname);
                if (value == null) {
                    value = this.default_args.get(i - first_default);
                }
                adjusted[i] = value;
            }
        }

        if ((flags & CO_VARARGS) != 0) {
            adjusted[pos_count] = java.util.Arrays.copyOfRange(args, pos_count, args.length);
        }

        return adjusted;
    }

    public org.python.Object invoke(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        return this.invoke(null, args, kwargs);
    }

    public org.python.Object invoke(org.python.Object instance, org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            // org.Python.debug("Function:", this.name);
            // org.Python.debug("       instance: ", instance);
            // for (org.python.Object arg: args) {
            //     org.Python.debug("            arg: ", arg);
            //     if (arg != null) {
            //         org.Python.debug("           type: ", arg.getClass());
            //     }
            // }
            // org.Python.debug("         kwargs: ", kwargs);
            // org.Python.debug("   default args: ", this.default_args);
            // org.Python.debug(" default kwargs: ", this.default_kwargs);

            // if this.__dict__.__code__.co_flags & CO_GENERATOR:
            //     gen = Generator(frame, self._vm)
            //     frame.generator = gen
            //     retval = gen
            // else:

            java.lang.Object [] adjusted_args = adjustArguments(instance, args, kwargs);

            // if (adjusted_args != null) {
            //     for (java.lang.Object arg: adjusted_args) {
            //         org.Python.debug("   Adjusted arg: ", arg);
            //         if (arg != null) {
            //             org.Python.debug("           type: ", arg.getClass());
            //         }
            //     }
            // } else {
            //     org.Python.debug("No adjusted args");
            // }

            // Python methods are stored as static methods on the class, so
            // the instance argument is passed in as a regular method argument,
            // not as the implied Java register 0. Builtins and closure methods
            // require the instance to be passed as the explicit instance.
            if (java.lang.reflect.Modifier.isStatic(this.method.getModifiers())) {
                return org.python.types.Type.toPython(this.method.invoke(null, adjusted_args));
            } else {
                return org.python.types.Type.toPython(this.method.invoke(instance, adjusted_args));
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
                java.lang.String message = e.getCause().getMessage();
                if (message == null) {
                    message = e.getCause().getClass().getName();
                }
                throw new org.python.exceptions.RuntimeError(message);
            }
        } finally {
        //     System.out.println("INVOKE METHOD DONE");
        }
    }
}
