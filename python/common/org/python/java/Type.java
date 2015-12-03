package org.python.java;

public class Type extends org.python.types.Type implements org.python.Callable {

    public Type(java.lang.Class klass) {
        super(klass, org.python.types.Type.Origin.JAVA);
    }

    // public org.python.Object __getattribute__(java.lang.String name) {
    //     System.out.println("GETATTRIBUTE NATIVE TYPE " + this + " " + name);
    //     return super.
    //     // org.python.Object value;
    //     // try {
    //     //     // First try the normal approach attribute
    //     //     org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
    //     //     // System.out.println("instance attrs = " + this.attrs);
    //     //     // System.out.println("class attrs = " + cls.attrs);
    //     //     value = cls.attrs.get(name);

    //     //     if (value == null) {
    //     //         throw new org.python.exceptions.AttributeError(this, name);
    //     //     }
    //     // } catch (org.python.exceptions.AttributeError e) {
    //     //     // System.out.println("TYPE NO ATTRIBUTE");
    //     //     value = org.Python.builtins.get(name);

    //     //     if (value == null) {
    //             throw new org.python.exceptions.NameError(name);
    //     //     }
    //     // }

    //     // return value;
    // }

    // public void __setattr__(java.lang.String name, org.python.Object value) {
    //     // The base object can't have attribute set on it unless the attribute already exists.
    //     System.out.println("SETATTRIBUTE TYPE " + this + " " + name + " = " + value);
    //     org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
    //     System.out.println("instance attrs = " + this.attrs);
    //     System.out.println("class attrs = " + cls.attrs);

    //     cls.attrs.put(name, value);

    //     // // If there is a native field of the same name, set it.
    //     // try {
    //     //     java.lang.reflect.Field field = this.getClass().getField(name);
    //     //     field.set(this, value);
    //     // } catch (NoSuchFieldException e) {
    //     //     // System.out.println("Not a native field");
    //     // } catch (IllegalAccessException e) {
    //         // throw new org.python.exceptions.RuntimeError("Illegal access to native field " + name);
    //     // }
    // }

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
