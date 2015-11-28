package org.python.types;


public class Constructor extends org.python.types.Object implements org.python.Callable {
    java.lang.reflect.Constructor constructor;

    public Constructor(java.lang.reflect.Constructor constructor) {
        super();
        this.constructor = constructor;
    }

    public org.python.Object invoke(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            // System.out.println("CONSTRUCTOR :" + this.constructor);
            // System.out.println("ARGS:");
            // for (org.python.Object arg: args) {
            //     System.out.println("  " + arg);
            // }

            // System.out.println("KWARGS:");
            // for (java.lang.String argname: kwargs.keySet()) {
            //     System.out.println("  " + argname + " = " + kwargs.get(argname));
            // }

            return (org.python.Object) this.constructor.newInstance(args, kwargs);
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java constructor " + this.constructor);
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
