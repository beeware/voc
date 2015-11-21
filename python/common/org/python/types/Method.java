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

    public org.python.Object invoke(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            // System.out.println("INVOKE METHOD:" + this.im_func + " " + this.im_self + " " + this.im_func.method);
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

            // // Add default args
            // int argcount = (int)((org.python.types.Int) this.im_func.code.attrs.get("co_argcount")).value;
            // int n_defaults = this.im_func.default_args.size();
            // System.out.println("argcount = " + argcount + " ndefaults = " + n_defaults + " args " + args.length);
            // if (args.length < argcount) {
            //     org.python.Object[] full_args = java.util.Arrays.copyOf(args, argcount);
            //     for (int i = args.length; i < argcount; i++) {
            //         System.out.println(i + " = " + this.im_func.default_args.get(i - n_defaults));
            //         full_args[i] = this.im_func.default_args.get(i - n_defaults);
            //     }
            //     args = full_args;
            // }

            // System.out.println("POST ARGS:");
            // for (org.python.Object arg: args) {
            //     System.out.println("  " + arg);
            // }

            // // Add default kwargs
            // for (java.lang.String argname: this.im_func.default_kwargs.keySet()) {
            //     System.out.println("Check for " + argname);
            //     if (!kwargs.containsKey(argname)) {
            //         System.out.println("Add default " + this.im_func.default_kwargs.get(argname));
            //         kwargs.put(argname, this.im_func.default_kwargs.get(argname));
            //     }
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