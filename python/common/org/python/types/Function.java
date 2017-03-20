package org.python.types;

import java.util.ArrayList;

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
    org.python.types.Closure closure;

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
        org.python.Object doc;
        try {
            org.python.types.Tuple consts = (org.python.types.Tuple) this.code.co_consts;
            if (consts != null && ((org.python.types.Int) consts.count()).value != 0) {
                doc = consts.__getitem__(new org.python.types.Int(0));
            } else {
                doc = org.python.types.NoneType.NONE;
            }
        } catch (java.lang.NullPointerException e) {
            doc = org.python.types.NoneType.NONE;
        } catch (java.lang.ClassCastException e) {
            doc = org.python.types.NoneType.NONE;
        } catch (java.lang.IndexOutOfBoundsException e) {
            doc = org.python.types.NoneType.NONE;
        }
        this.__dict__.put("__doc__", doc);

        // this.__dict__.put("__call__")
    }

    // Constructor for builtins
    public Function(
            java.lang.reflect.Method method,
            java.lang.String[] args,
            java.lang.String[] default_args,
            java.lang.String vararg_name,
            java.lang.String[] kwonlyargs,
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

        for (java.lang.String arg : args) {
            varnames.add(new org.python.types.Str(arg));
        }

        this.default_args = new java.util.ArrayList<org.python.Object>();
        for (java.lang.String arg : default_args) {
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
        for (java.lang.String arg : kwonlyargs) {
            varnames.add(new org.python.types.Str(arg));
            this.default_kwargs.put(arg, null);
        }

        if (kwargs_name != null) {
            flags |= CO_VARKEYWORDS;
            varnames.add(new org.python.types.Str(kwargs_name));
        }

        this.code = new org.python.types.Code(
                new org.python.types.Int(argcount),  // co_argcount
                new org.python.types.Tuple(),  // co_cellvars
                null,  // new org.python.types.Bytes(),  // co_code
                null,  // new org.python.types.Tuple(),  // co_consts
                null,  // new org.python.types.Str(),  // co_filename
                null,  // new org.python.types.Int(),  // co_firstlineno
                new org.python.types.Int(flags),  // co_flags
                new org.python.types.Tuple(),  // co_freevars
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
            org.python.types.Closure closure) {
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
            __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        return new org.python.types.Str(String.format("<%s %s at 0x%x>", this.typeName(), this.name, this.hashCode()));
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __get__(org.python.Object instance, org.python.Object klass) {
        // System.out.println("__GET__ on function " + this + " " + this.getClass() + " " + instance + " " + instance.getClass());
        if (instance != klass) {
            if (instance instanceof org.python.types.Closure) {
                return new org.python.types.Function(this.name, this.code, this.method, this.globals, this.default_args, this.default_kwargs, (org.python.types.Closure) instance);
            } else if (!(instance instanceof org.python.types.Module)) {
                return new org.python.types.Method(instance, (org.python.types.Type) klass, this);
            }
        }
        return this;
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __bool__() {
        return new org.python.types.Bool(true);
    }

    private void checkMissingArgs(int requiredArgs, int passedArgs, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> varnames, int first_arg) {
        int n_missing_pos_args = requiredArgs - passedArgs;
        java.util.List<String> missingArgs = new ArrayList<String>();
        if (n_missing_pos_args > 0) {
            // build list of actual missing args, checking if haven't been passed as kwargs
            for (int i = first_arg; i < n_missing_pos_args; i++) {
                java.lang.String argname = ((String) varnames.get(i + passedArgs).toJava());
                if (!kwargs.containsKey(argname)) {
                    missingArgs.add(argname);
                }
            }

            if (missingArgs.size() > 0) {
                // we show missing args using Oxford comma, as CPython does
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < missingArgs.size(); i++) {
                    sb.append("'" + missingArgs.get(i) + "'");
                    if (i <= missingArgs.size() - 2) {
                        sb.append(", ");
                    }
                    if (i == missingArgs.size() - 2) {
                        sb.append("and ");
                    }
                }

                throw new org.python.exceptions.TypeError(this.name + "() missing " + missingArgs.size() + " required positional "
                        + (missingArgs.size() == 1 ? "argument" : "arguments") + ": " + sb.toString());
            }
        }
    }

    private void throwUnexpectedPositionalArgumentsError(int numExpected, int numGot) {
        String posArgs = numExpected + " positional argument" + (numExpected == 1 ? "" : "s");
        String givenArgs = numGot + (numGot == 1 ? " was given" : " were given");
        String mesg = this.name.value + "() takes " + posArgs + " but " + givenArgs;
        throw new org.python.exceptions.TypeError(mesg);
    }

    java.lang.Object[] adjustArguments(org.python.Object instance, org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        // if (kwargs.size() > 0) {
        //     // TODO: This doesn't have to be so - we *could* introspect argument names.
        //     throw new org.python.exceptions.RuntimeError("Cannot use kwargs to invoke a native Java method.");
        // }
        int argcount = (int) this.code.co_argcount.value;
        int kwonlyargcount = (int) this.code.co_kwonlyargcount.value;
        int flags = (int) this.code.co_flags.value;
        java.util.List<org.python.Object> varnames = this.code.co_varnames.value;

        int first_arg = 0;
        int has_varargs = 0;
        int has_varkwargs = 0;
        // System.out.println("Instance = " + instance);
        // System.out.println("method:" + method);
        // System.out.println("args:" + args.length);
        // System.out.println("kwargs:" + kwargs);
        // System.out.println("argcount = " + argcount);
        // System.out.println("kwonlyargcount = " + kwonlyargcount);

        int n_args = argcount + kwonlyargcount;
        if ((flags & CO_VARARGS) != 0) {
            // System.out.println("HAS VARARGS");
            n_args += 1;
            has_varargs = 1;
        }
        if ((flags & CO_VARKEYWORDS) != 0) {
            // System.out.println("HAS VARKEYWORDS");
            n_args += 1;
            has_varkwargs = 1;
        }

        int required_args = argcount - this.default_args.size();
        // System.out.println("nargs = " + n_args);
        // System.out.println("first default = " + required_args);

        if (0 == has_varargs && args != null && args.length > n_args) {
            throwUnexpectedPositionalArgumentsError(n_args, args.length);
        }

        // If there are genuinely *no* arguments - not even self - return null;
        if (n_args == 0) {
            return null;
        }

        java.lang.Object[] adjusted = new java.lang.Object[n_args];

        // If this is an instance, the first argument will be self; we don't
        // need to pass this to the Java function.
        if (instance != null && (java.lang.reflect.Modifier.isStatic(method.getModifiers()) || this.closure != null)) {
            // System.out.println("CALL USING INSTANCE");
            first_arg = 1;
            adjusted[0] = instance;
            // System.out.println("   aARG 0: " + instance);
        }

        checkMissingArgs(required_args, (args == null ? 0 : args.length), kwargs, varnames, first_arg);

        // System.out.println("First arg = " + first_arg);
        // Populate the positional args.
        for (int i = 0; i < argcount - first_arg; i++) {
            if (i < args.length) {
                // System.out.println("   b" + (i + first_arg));
                adjusted[i + first_arg] = args[i];
                // System.out.println("   bARG " + (i + first_arg) + ": " + args[i]);
                if (kwargs != null) {
                    java.lang.String varname = ((org.python.types.Str) varnames.get(i)).value;
                    org.python.Object value = kwargs.remove(varname);
                    if (value != null) {
                        throw new org.python.exceptions.TypeError(this.name + "() got multiple values for argument '" + varname + "'");
                    }
                }
            } else {
                // Use a default argument. They might be specified as a kwarg.
                // System.out.println("   c" + (i + first_arg));
                org.python.Object value = null;
                if (kwargs != null) {
                    java.lang.String varname = ((org.python.types.Str) varnames.get(i + first_arg)).value;
                    value = kwargs.remove(varname);
                }
                if (value == null) {
                    value = this.default_args.get(i + first_arg - required_args);
                }
                adjusted[i + first_arg] = value;
                // System.out.println("   cARG " + i + ": " + value);
            }
        }

        // Create a tuple for the varargs
        if ((flags & CO_VARARGS) != 0) {
            // System.out.println("Handle varargs");
            // Construct Python tuple object
            org.python.types.Tuple tuple = new org.python.types.Tuple(
                    java.util.Arrays.asList(java.util.Arrays.copyOfRange(args, argcount - first_arg, args.length)));

            adjusted[argcount] = tuple;
            // System.out.println("   dARG " + argcount + ": " + tuple);
        }

        // Populate the kwonly args
        for (int i = 0; i < kwonlyargcount; i++) {
            java.lang.String varname = ((org.python.types.Str) varnames.get(argcount + has_varargs + i)).value;
            // System.out.println("   e" + (argcount + has_varargs + i) + " " + varname);
            org.python.Object value = kwargs.remove(varname);
            if (value == null) {
                value = this.default_kwargs.get(varname);
            }
            adjusted[argcount + has_varargs + i] = value;
            // System.out.println("   eARG " + (argcount + has_varargs + i) + ": " + value);
        }

        // Add remaining kwargs to kwargs argument if we have one.
        if ((flags & CO_VARKEYWORDS) != 0) {
            // System.out.println("Handle varkwargs = " + kwargs);
            org.python.types.Dict kwargDict = new org.python.types.Dict();
            for (java.util.Map.Entry<java.lang.String, org.python.Object> entry : kwargs.entrySet()) {
                // System.out.println("Add KWARG" + entry.getKey());
                kwargDict.__setitem__(new org.python.types.Str(entry.getKey()), entry.getValue());
            }
            adjusted[adjusted.length - 1] = kwargDict;
            // System.out.println("   fARG " + (adjusted.length - 1) + ": " + kwargDict);
        }

        return adjusted;
    }

    public org.python.Object invoke(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        return this.invoke(null, args, kwargs);
    }

    public org.python.Object invoke(org.python.Object instance, org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
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

            java.lang.Object[] adjusted_args = adjustArguments(instance, args, kwargs);

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
            } else if (this.closure != null) {
                return org.python.types.Type.toPython(this.method.invoke(this.closure, adjusted_args));
            } else {
                return org.python.types.Type.toPython(this.method.invoke(instance, adjusted_args));
            }
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java method " + this.method);
        } catch (java.lang.reflect.InvocationTargetException e) {
            try {
                // org.Python.debug("Exception:", e.getTargetException());
                // for (java.lang.StackTraceElement ste: e.getTargetException().getStackTrace()) {
                //     org.Python.debug("     ", ste);
                // }

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
        // } finally {
            //     System.out.println("INVOKE METHOD DONE");
        }
    }
}
