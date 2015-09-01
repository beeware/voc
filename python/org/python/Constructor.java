package org.python;


public class Constructor extends org.python.Object implements Callable {
    public Constructor(java.lang.reflect.Constructor constructor) {
        super(constructor, java.lang.reflect.Constructor.class);
    }

    public org.python.Object invoke(org.python.Object[] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        try {
            return (org.python.Object) ((java.lang.reflect.Constructor) this.value).newInstance(args, kwargs);
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java constructor " + this.value);
        } catch (java.lang.reflect.InvocationTargetException e) {
            throw new org.python.exceptions.RuntimeError(e.getCause().toString());
        } catch (java.lang.InstantiationException e) {
            throw new org.python.exceptions.RuntimeError(e.getCause().toString());
        }
    }

}
