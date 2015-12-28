package org.python.java;

public class Function extends org.python.types.Object implements org.python.Callable {
    java.lang.String name;
    java.util.Map<java.lang.String, java.lang.reflect.Method> methods;

    public static java.lang.String descriptor(java.lang.Class klass, boolean weak) {
        if (klass.getName().startsWith("[")) {
            return klass.getName();
        }

        if (   klass == java.lang.Boolean.TYPE
            || klass == java.lang.Boolean.class) {
            return "Z";
        } else if (   klass == java.lang.Byte.TYPE
                   || klass == java.lang.Byte.class) {
            return "B";
        } else if (   klass == java.lang.Character.TYPE
                   || klass == java.lang.Character.class) {
            return "C";
        } else if (   klass == java.lang.Short.TYPE
                   || klass == java.lang.Short.class) {
            return "S";
        } else if (   klass == java.lang.Integer.TYPE
                   || klass == java.lang.Integer.class) {
            return "I";
        } else if (   klass == java.lang.Long.TYPE
                   || klass == java.lang.Long.class) {
            return "J";
        } else if (   klass == java.lang.Float.TYPE
                   || klass == java.lang.Float.class) {
            return "F";
        } else if (   klass == java.lang.Double.TYPE
                   || klass == java.lang.Double.class) {
            return "D";
        } else if (weak) {
            return "Ljava/lang/Object;";
        } else {
            return "L" + klass.getName().replace('.', '/') + ";";
        }
    }

    public static <T> T selectMethod(java.util.Map<java.lang.String, T> options, org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        // System.out.println("Options " + options);
        T method;
        java.lang.StringBuilder signature = new java.lang.StringBuilder();
        for (org.python.Object arg: args) {
            signature.append(org.python.java.Function.descriptor(arg.toJava().getClass(), false));
        }
        // System.out.println("Signature " + signature.toString());
        method = options.get(signature.toString());

        // No match - need to try alternatives for signature.
        if (method == null) {
            signature = new java.lang.StringBuilder();
            for (org.python.Object arg: args) {
                signature.append(org.python.java.Function.descriptor(arg.toJava().getClass(), true));
            }
            // System.out.println("Signature " + signature.toString());
            method = options.get(signature.toString());
        }
        return method;
    }

    public static <T> java.lang.Object [] adjustArguments(T method, org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() > 0) {
            // TODO: This doesn't have to be so - we *could* introspect argument names.
            throw new org.python.exceptions.RuntimeError("Cannot use kwargs to invoke a native Java method.");
        }

        java.lang.Object [] adjusted = new java.lang.Object [args.length];
        for (int i = 0; i < args.length; i++) {
            adjusted[i] = args[i].toJava();
        }
        return adjusted;
    }

    public Function(java.lang.Class klass, java.lang.String name) {
        super();
        this.name = name;
        // org.Python.debug("FUNCTION ", this.name);
        this.methods = new java.util.HashMap<java.lang.String, java.lang.reflect.Method>();

        java.lang.Class<?> clazz = klass;
        while (clazz != null) {
            // org.Python.debug("CLAZZ:", clazz);
            for (java.lang.reflect.Method method: clazz.getDeclaredMethods()) {
                // org.Python.debug("METHOD:", method.getName());
                if (method.getName().equals(name)) {
                    java.lang.StringBuilder signature = new java.lang.StringBuilder();

                    for (java.lang.Class c: method.getParameterTypes()) {
                        signature.append(org.python.java.Function.descriptor(c, false));
                    }

                    // org.Python.debug("  match: ", signature.toString());
                    // org.Python.debug("    known: ", this.methods.containsKey(signature.toString()));
                    // org.Python.debug("    abstract: ", java.lang.reflect.Modifier.isAbstract(method.getModifiers()));

                    java.lang.String sig = signature.toString();
                    boolean is_abstract = java.lang.reflect.Modifier.isAbstract(method.getModifiers());
                    if (!this.methods.containsKey(sig) && !is_abstract) {
                        this.methods.put(sig, method);
                    }
                }
            }

            clazz = clazz.getSuperclass();
        }
        // org.Python.debug("methods: ", this.methods);
        if (this.methods.size() == 0) {
            throw new org.python.exceptions.AttributeError(klass, name);
        }
        this.attrs.put("__name__", new org.python.types.Str(this.name));
        this.attrs.put("__qualname__", new org.python.types.Str(this.name));
    }

    @org.python.Method(
        __doc__ = "Implement str(self)."
    )
    public org.python.types.Str __str__() {
        return new org.python.types.Str(this.name + "()");
    }

    @org.python.Method(
        __doc__ = "Implement __get__(self)."
    )
    public org.python.Object __get__(org.python.Object instance, org.python.Object klass) {
        // System.out.println("__GET__ on native function " + this + " " + this.getClass());
        return new org.python.java.Method(instance, this);
    }

    public org.python.Object invoke(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        return this.invoke(null, args, kwargs);
    }

    public org.python.Object invoke(org.python.Object instance, org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            java.lang.Object target = null;
            // org.Python.debug("Native Function:", this.name);
            // org.Python.debug("       instance: ", instance);
            if (instance != null) {
                target = instance.toObject();
                // org.Python.debug("       target: ", target);
            }

            // System.out.println("Native Function:" + this.name);
            // System.out.println("       instance: " + instance);
            // System.out.println("       target: " + target.getClass());
            // System.out.println("           args:");
            // for (org.python.Object arg: args) {
            //     System.out.println("                " + arg);
            // }
            // System.out.println("         kwargs:" + kwargs);

            java.lang.reflect.Method method = org.python.java.Function.selectMethod(this.methods, args, kwargs);

            // If there is still no match, raise an error.
            if (method == null) {
                throw new org.python.exceptions.RuntimeError(String.format("Parameter mismatch calling native Java method '%s'", name));
            }

            java.lang.Object [] adjusted_args = org.python.java.Function.adjustArguments(method, args, kwargs);

            // System.out.println("Invoke method " + method + " with ");
            // System.out.print("           args:");
            // for (java.lang.Object arg: adjusted_args) {
            //     System.out.print(arg + " (" + arg.getClass() + ")");
            // }
            // System.out.println();
            java.lang.Object result = method.invoke(target, adjusted_args);
            // System.out.println("RESULT " + result);
            return org.python.types.Type.toPython(result);
        } catch (java.lang.IllegalAccessException e) {
            e.printStackTrace();
            throw new org.python.exceptions.RuntimeError("Illegal access to Java function");
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
