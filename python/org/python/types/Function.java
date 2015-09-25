package org.python.types;

public class Function extends org.python.types.Object implements org.python.Callable {
    public Function(java.lang.reflect.Method method) {
        super(method, java.lang.reflect.Method.class);
    }

    public org.python.types.Object invoke(org.python.types.Object[] args, java.util.Hashtable<java.lang.String, org.python.types.Object> kwargs) {
        try {
            // System.out.println("ARGS:");
            // for (org.python.types.Object arg: args) {
            //     System.out.println("  " + arg);
            // }
            return (org.python.types.Object) ((java.lang.reflect.Method) this.value).invoke(null, args, kwargs);
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java function " + this.value);
        } catch (java.lang.reflect.InvocationTargetException e) {
            throw new org.python.exceptions.RuntimeError(e.getCause().toString());
        }
    }
}
