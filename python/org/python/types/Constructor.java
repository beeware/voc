package org.python.types;


public class Constructor extends org.python.types.Object implements org.python.Callable {
    java.lang.reflect.Constructor value;

    public Constructor(java.lang.reflect.Constructor constructor) {
        super();
        this.value = constructor;
    }

    public org.python.Object invoke(org.python.Object[] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        try {
            // System.out.println("CONSTRUCTOR ARGS:");
            // for (org.python.Object arg: args) {
            //     System.out.println("  " + arg);
            // }
            return (org.python.Object) this.value.newInstance(args, kwargs);
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java constructor " + this.value);
        } catch (java.lang.reflect.InvocationTargetException e) {
            throw new org.python.exceptions.RuntimeError(e.getCause().toString());
        } catch (java.lang.InstantiationException e) {
            throw new org.python.exceptions.RuntimeError(e.getCause().toString());
        }
    }
}
