package org.python.java;

public class Function extends org.python.types.Object implements org.python.Callable {
    java.lang.String name;
    java.util.Map<java.lang.String, java.lang.reflect.Method> methods;

    static java.lang.String descriptor(java.lang.Class klass, boolean weak) {
        if (klass.getName().startsWith("[")) {
            return klass.getName();
        }

        switch (klass.getName()) {
            case "boolean":
            case "java.lang.Boolean":
                return "Z";

            case "byte":
            case "java.lang.Byte":
                return "B";

            case "char":
            case "java.lang.Char":
                return "C";

            case "short":
            case "java.lang.Short":
                return "S";

            case "int":
            case "java.lang.Integer":
                return "I";

            case "long":
            case "java.lang.Long":
                return "J";

            case "float":
            case "java.lang.Float":
                return "F";

            case "double":
            case "java.lang.Double":
                return "D";

            default:
                if (weak) {
                    return "Ljava/lang/Object;";
                } else {
                    return "L" + klass.getName().replace('.', '/') + ";";
                }
        }
    }

    public Function(java.lang.Class klass, java.lang.String name) {
        super();
        this.name = name;
        this.methods = new java.util.HashMap<java.lang.String, java.lang.reflect.Method>();
        for (java.lang.reflect.Method method: klass.getMethods()) {
            // System.out.println("METHOD:" + method);
            java.lang.StringBuilder signature = new java.lang.StringBuilder();
            if (method.getName().equals(name)) {

                for (java.lang.Class c: method.getParameterTypes()) {
                    signature.append(org.python.java.Function.descriptor(c, false));
                }

                this.methods.put(
                    signature.toString(),
                    method
                );
            }
        }
        // System.out.println("FUNCTION " + this.name + " " + this.methods);
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
        return new org.python.java.Method(instance.toJava(), this);
    }

    java.lang.reflect.Method selectMethod(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        // System.out.println("Options " + this.methods);
        java.lang.reflect.Method method;
        java.lang.StringBuilder signature = new java.lang.StringBuilder();
        for (org.python.Object arg: args) {
            signature.append(org.python.java.Function.descriptor(arg.toJava().getClass(), false));
        }
        // System.out.println("Signature " + signature.toString());
        method = this.methods.get(signature.toString());

        // No match - need to try alternatives for signature.
        if (method == null) {
            signature = new java.lang.StringBuilder();
            for (org.python.Object arg: args) {
                signature.append(org.python.java.Function.descriptor(arg.toJava().getClass(), true));
            }
            // System.out.println("Signature " + signature.toString());
            method = this.methods.get(signature.toString());
        }

        // If there is still no match, raise an error.
        if (method == null) {
            throw new org.python.exceptions.RuntimeError(String.format("Parameter mismatch calling native Java method '%s'", this.name));
        }
        return method;
    }

    java.lang.Object [] adjustArguments(java.lang.reflect.Method method, org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
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

    public org.python.Object invoke(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        return this.invoke(null, args, kwargs);
    }

    public org.python.Object invoke(java.lang.Object instance, org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            // System.out.println("Native Function:" + this.name);
            // System.out.println("           args:" + args);
            // System.out.println("         kwargs:" + kwargs);

            java.lang.reflect.Method method = selectMethod(args, kwargs);

            java.lang.Object [] adjusted_args = adjustArguments(method, args, kwargs);

            // System.out.println("Invoke method " + method + " with ");
            // System.out.print("           args:");
            // for (java.lang.Object arg: adjusted_args) {
            //     System.out.print(arg + ", ");
            // }
            // System.out.println();
            return org.python.types.Type.toPython(method.invoke(instance, adjusted_args));

        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java function");
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
