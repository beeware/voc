package org.python.types;

public class Method extends org.python.types.Object implements org.python.Callable {
    org.python.Object im_self;
    org.python.types.Type im_class;
    org.python.types.Function im_func;

    public Method(org.python.Object instance, org.python.types.Type klass, org.python.types.Function function) {
        super();
        this.im_self = instance;
        this.im_class = klass;
        this.im_func = function;
    }

    public org.python.types.Str __repr__() {
        if (this.im_self == null) {
            return new org.python.types.Str(
                String.format("<unbound method %s.%s>",
                    this.im_class.attrs.get("__name__"),
                    this.im_func.attrs.get("__name__")
                )
            );
        } else if (org.python.types.Closure.class.isAssignableFrom(this.im_class.klass)) {
            // Closures *should* just be just functions, but they're implemented as
            // methods on an instance in Java, so we have to fake it a little bit.
            return new org.python.types.Str(String.format("<function object at 0x%x>", this.im_func.hashCode()));
        } else {
            return new org.python.types.Str(
                String.format("<bound method %s.%s of %s>",
                    this.im_class.attrs.get("__name__"),
                    this.im_func.attrs.get("__name__"),
                    this.im_self
                )
            );
        }
    }

    public org.python.Object invoke(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            // System.out.println("INVOKE METHOD:" + this.im_func + " " + this.im_self + " " + this.im_func.method + " " + this.im_func.code.attrs.get("co_varnames"));

            // System.out.println("PRE ARGS:");
            // for (org.python.Object arg: args) {
            //     System.out.println("  " + arg);
            // }

            // System.out.println("PRE KWARGS:");
            // for (java.lang.String argname: kwargs.keySet()) {
            //     System.out.println("  " + argname + " = " + kwargs.get(argname));
            // }

            // System.out.println("PRE DEFAULTS:");
            // for (org.python.Object arg: this.im_func.default_args) {
            //     System.out.println("  " + arg);
            // }

            // for (java.lang.String argname: this.im_func.default_kwargs.keySet()) {
            //     System.out.println("  " + argname + " = " + this.im_func.default_kwargs.get(argname));
            // }

            int pos_count = (int)((org.python.types.Int) this.im_func.code.attrs.get("co_argcount")).value;
            java.util.List<org.python.Object> arg_names = ((org.python.types.Tuple) this.im_func.code.attrs.get("co_varnames")).value;

            // Iterate over all the positional arguments provided; check that
            // we have enough of them. If we don't, populate them from kwargs,
            // or if there's no kwargs, from defaults.
            for (int a = 0; a < pos_count; a++) {
                java.lang.String arg_name = ((org.python.types.Str) arg_names.get(a)).value;
                if (a >= args.size()) {
                    // This argument wasn't provided as a positional; check to
                    // see if it was provided as a keyword.
                    org.python.Object value = kwargs.remove(arg_name);

                    // If it wasn't provided as a kwarg, use the
                    // defaults list.
                    if (value == null) {
                        value = this.im_func.default_args.get(a - (pos_count - this.im_func.default_args.size()));
                    }

                    // Add the value to the full args list.
                    args.add(value);
                } else {
                    // We've been given a position argument at this index; check that
                    // it isn't also provided as a kwarg.
                    if (kwargs.containsKey(arg_name)) {
                        throw new org.python.exceptions.TypeError(this.im_func.name + "() for multiple values for argument '" + arg_name + "'");
                    }
                }
            }

            // If this function provides VARARGS, extract them and add them as
            // a Python list as the last positional argument.
            int co_flags = (int)((org.python.types.Int) this.im_func.code.attrs.get("co_flags")).value;
            if ((co_flags & org.python.types.Function.CO_VARARGS) != 0) {
                java.util.List<org.python.Object> var_args;
                if (args.size() > pos_count) {
                    var_args = args.subList(pos_count, args.size());
                    args = new java.util.ArrayList<org.python.Object>(args.subList(0, pos_count));
                } else {
                    // No positional arguments - add an empty list.
                    var_args = new java.util.ArrayList<org.python.Object>();
                }
                args.add(new org.python.types.List(var_args));
            }

            // System.out.println("POST ARGS:");
            // for (org.python.Object arg: args) {
            //     System.out.println("  " + arg);
            // }

            // System.out.println("POST KWARGS:");
            // for (java.lang.String argname: kwargs.keySet()) {
            //     System.out.println("  " + argname + " = " + kwargs.get(argname));
            // }

            return (org.python.Object) this.im_func.method.invoke(this.im_self, args, kwargs);
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java instance method " + this.im_func);
        } catch (java.lang.reflect.InvocationTargetException e) {
            try {
                // e.getTargetException().printStackTrace();
                // If the Java method raised an Python exception, re-raise that
                // exception as-is. If it wasn't a Python exception, wrap it
                // as one and continue.
                throw (org.python.exceptions.BaseException) e.getCause();
            } catch (ClassCastException java_e) {
                throw new org.python.exceptions.RuntimeError(e.getCause().toString());
            }
        } finally {
        //     System.out.println("INVOKE METHOD DONE");
        }
    }
}