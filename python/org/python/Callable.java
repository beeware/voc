package org.python;


public interface Callable {
    public org.python.types.Object invoke(org.python.types.Object[] args, java.util.Hashtable<java.lang.String, org.python.types.Object> kwargs);
}
