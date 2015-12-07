package org.python.java;

public class Type extends org.python.types.Type implements org.python.Callable {

    public Type(java.lang.Class klass) {
        super(klass, org.python.types.Type.Origin.JAVA);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getattribute__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __getattribute__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        } else if (!(args.get(0) instanceof org.python.types.Str)) {
            throw new org.python.exceptions.TypeError("__getattribute__(): attribute name must be string");
        }

        java.lang.String name = ((org.python.types.Str) args.get(0)).value;

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
            if (this.attrs.containsKey(name)) {
                throw new org.python.exceptions.AttributeError(this, name);
            } else {
                try {
                    value = new org.python.java.Function(this.klass, name);
                    this.attrs.put(name, value);
                } catch (org.python.exceptions.AttributeError fe) {
                    // No function; look for an attribute with the same name.
                    try {
                        value = new org.python.java.Attribute(this.klass, name);
                        this.attrs.put(name, value);
                    } catch (org.python.exceptions.AttributeError ae) {
                        // Field does not exist. Record this fact,
                        // and raise an AttributError.
                        this.attrs.put(name, null);
                        throw new org.python.exceptions.AttributeError(this, name);
                    }
                }
            }
        }
        return value;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __setattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__setattribute__() doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        } else if (!(args.get(0) instanceof org.python.types.Str)) {
            throw new org.python.exceptions.TypeError("__setattribute__(): attribute name must be string");
        }

        java.lang.String name = ((org.python.types.Str) args.get(0)).value;
        org.python.Object value = args.get(1);

        // The base object can't have attribute set on it unless the attribute already exists.
        // System.out.println("SETATTRIBUTE TYPE " + this + " " + name + " = " + value);
        org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
        // System.out.println("instance attrs = " + this.attrs);
        // System.out.println("class attrs = " + cls.attrs);

        cls.attrs.put(name, value);
    }

    public org.python.Object invoke(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
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

            // FIXME: Get the constructor matching the args.
            java.lang.reflect.Constructor constructor = this.klass.getConstructor();

            return new org.python.java.Object(constructor.newInstance());
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to native Java constructor for " + this.klass);
        } catch (java.lang.NoSuchMethodException e) {
            throw new org.python.exceptions.RuntimeError("Couldn't find native Java constructor for " + this.klass);
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
