package org.python;


public class Constructor extends org.python.types.Object implements Callable {
    public Constructor(java.lang.reflect.Constructor constructor) {
        super(constructor, java.lang.reflect.Constructor.class);
    }

    public org.python.types.Object invoke(org.python.types.Object[] args, java.util.Hashtable<java.lang.String, org.python.types.Object> kwargs) {
        try {
            // System.out.println("CONSTRUCTOR ARGS:");
            // for (org.python.types.Object arg: args) {
            //     System.out.println("  " + arg);
            // }
            return (org.python.types.Object) ((java.lang.reflect.Constructor) this.value).newInstance(args, kwargs);
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java constructor " + this.value);
        } catch (java.lang.reflect.InvocationTargetException e) {
            throw new org.python.exceptions.RuntimeError(e.getCause().toString());
        } catch (java.lang.InstantiationException e) {
            throw new org.python.exceptions.RuntimeError(e.getCause().toString());
        }
    }
}
