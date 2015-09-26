package org.python.types;

public class Function extends org.python.types.Object implements org.python.Callable {
    java.lang.reflect.Method value;

    public Function(java.lang.reflect.Method method) {
        super();
        this.value = method;
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
            throw new org.python.exceptions.RuntimeError(e.getCause().toString());
        }
    }
}
