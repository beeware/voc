package org.python.types;

public class Method extends org.python.types.Object implements org.python.Callable {
    boolean is_static;
    java.lang.reflect.Method value;

    public Method(java.lang.reflect.Method method, boolean is_static) {
        super();
        this.value = method;
        this.is_static = is_static;
    }

    public org.python.Object invoke(org.python.Object[] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        try {
            // System.out.println(this.value + " ARGS:");
            // for (org.python.Object arg: args) {
            //     System.out.println("  " + arg);
            // }
            if (this.is_static) {
                return (org.python.Object) this.value.invoke(null, args, kwargs);
            } else {
                return (org.python.Object) this.value.invoke(args[0], args, kwargs);
            }
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java instance method " + this.value);
        } catch (java.lang.reflect.InvocationTargetException e) {
            throw new org.python.exceptions.RuntimeError(e.getCause().toString());
        }
    }
}