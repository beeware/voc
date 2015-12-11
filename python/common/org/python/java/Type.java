package org.python.java;

public class Type extends org.python.types.Type implements org.python.Callable {
    java.util.Map<java.lang.String, java.lang.reflect.Constructor> constructors;

    public Type(java.lang.Class klass) {
        super(klass, org.python.types.Type.Origin.JAVA);

        this.constructors = new java.util.HashMap<java.lang.String, java.lang.reflect.Constructor>();
        for (java.lang.reflect.Constructor constructor: klass.getConstructors()) {
            java.lang.StringBuilder signature = new java.lang.StringBuilder();

            for (java.lang.Class c: constructor.getParameterTypes()) {
                signature.append(org.python.java.Function.descriptor(c, false));
            }

            this.constructors.put(
                signature.toString(),
                constructor
            );
        }
    }

    public org.python.Object __getattribute_null(java.lang.String name) {
        // System.out.println("GETATTRIBUTE NATIVE TYPE " + this + " " + name);
        // System.out.println("CLASS ATTRS " + this.attrs);
        org.python.Object value = this.attrs.get(name);

        // On a native type, attrs is a cache of lookups on actual functions.
        // If there's no hit, then we need to reflect on the underyling class
        // and populate the cache.
        if (value == null) {
            // java.lang.Map doesn't differentiate between "doesn't exist"
            // and "value is null"; so since we know the value is null, check
            // to see if it is an explicit null (i.e., attribute doesn't exist)
            if (!this.attrs.containsKey(name)) {
                try {
                    value = new org.python.java.Function(this.klass, name);
                } catch (org.python.exceptions.AttributeError ae) {
                    // No function; look for an attribute with the same name.
                    try {
                        value = new org.python.java.Field(klass.getField(name));
                    } catch (java.lang.NoSuchFieldException e) {
                        // Field does not exist.
                        value = null;
                    }
                }
                this.attrs.put(name, value);
            }
        }
        return value;
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // System.out.println("SETATTRIBUTE NATIVE TYPE " + this + " " + name + " = " + value);
        org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
        // System.out.println("instance attrs = " + this.attrs);
        // System.out.println("class attrs = " + cls.attrs);

        cls.attrs.put(name, value);
        return true;
    }

    public org.python.Object invoke(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            // System.out.println("NATIVE CONSTRUCTOR :" + this.klass);
            // System.out.println("ARGS:");
            // for (org.python.Object arg: args) {
            //     System.out.println("  " + arg);
            // }

            // System.out.println("KWARGS:");
            // for (java.lang.String argname: kwargs.keySet()) {
            //     System.out.println("  " + argname + " = " + kwargs.get(argname));
            // }

            java.lang.reflect.Constructor constructor = org.python.java.Function.selectMethod(this.constructors, args, kwargs);

            // If there is still no match, raise an error.
            if (constructor == null) {
                throw new org.python.exceptions.RuntimeError(String.format("Parameter mismatch calling native Java constructor."));
            }

            java.lang.Object [] adjusted_args = org.python.java.Function.adjustArguments(constructor, args, kwargs);

            return new org.python.java.Object(constructor.newInstance(adjusted_args));

        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to native Java constructor for " + this.klass);
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
        } catch (java.lang.InstantiationException e) {
            throw new org.python.exceptions.RuntimeError(e.getCause().toString());
        } finally {
        //     System.out.println("CONSTRUCTOR DONE");
        }
    }

}
