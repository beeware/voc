package org.python.java;

public class Function extends org.python.types.Object {
    java.lang.String name;
    java.util.Map<java.lang.String, java.lang.reflect.Method> methods;

    static java.lang.String descriptor(java.lang.Class klass) {
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
                return "L" + klass.getName().replace('.', '/') + ";";
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
                    signature.append(org.python.java.Function.descriptor(c));
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

    public org.python.types.Str __str__() {
        return new org.python.types.Str(this.name + "()");
    }

    public org.python.Object __get__(org.python.Object instance, org.python.types.Type klass) {
        return new org.python.java.Method(instance.toJava(), this);
    }

    java.lang.reflect.Method selectMethod(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        java.lang.reflect.Method method;
        java.lang.StringBuilder signature = new java.lang.StringBuilder();
        for (org.python.Object arg: args) {
            signature.append(org.python.java.Function.descriptor(arg.toJava().getClass()));
        }
        return this.methods.get(signature.toString());
    }

    java.lang.Object [] adjustArguments(java.lang.reflect.Method method, java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() > 0) {
            // TODO: This doesn't have to be so - we *could* introspect argument names.
            throw new org.python.exceptions.RuntimeError("Cannot use kwargs to invoke a native Java method.");
        }

        java.lang.Object [] adjusted = new java.lang.Object [args.size()];
        for (int i = 0; i < args.size(); i++) {
            adjusted[i] = args.get(i).toJava();
        }
        return adjusted;
    }

    public org.python.Object invoke(java.lang.Object instance, java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            // System.out.println("Function:" + this.method);
            // System.out.println("           args:" + args);
            // System.out.println("         kwargs:" + kwargs);
            // System.out.println("   default args: " + this.default_args);
            // System.out.println(" default kwargs: " + this.default_kwargs);

            java.lang.reflect.Method method = selectMethod(args, kwargs);

            java.lang.Object [] adjusted_args = adjustArguments(method, args, kwargs);

            // System.out.println("Invoke method " + method + " with " + adjusted_args);
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
