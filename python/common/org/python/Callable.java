package org.python;


public interface Callable {
    public org.python.Object invoke(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs);
}
