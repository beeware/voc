package org.python.types;

public class Function extends org.python.types.Object implements org.python.Callable {
    java.lang.reflect.Method value;
    boolean is_static;

    public Function(java.lang.reflect.Method method, boolean is_static) {
        super();
        this.value = method;
        this.is_static = is_static;
    }

    public org.python.Object invoke(org.python.Object[] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        try {
            // System.out.println("Function:" + this.value);
            // System.out.println("ARGS:");
            // for (org.python.Object arg: args) {
            //     System.out.println("  " + arg);
            // }
            return (org.python.Object) this.value.invoke(null, args, kwargs);
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java function " + this.value);
        } catch (java.lang.reflect.InvocationTargetException e) {
            try {
                // If the Java method raised an Python exception, re-raise that
                // exception as-is. If it wasn't a Python exception, wrap it
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
