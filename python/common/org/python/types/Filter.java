package org.python.types;

public class Filter extends org.python.types.Object implements org.python.Object {
    private org.python.Callable callable;
    private org.python.Object iterator;

    public Filter(org.python.Object callable, org.python.Object iterator) {
        if (org.python.types.NoneType.NONE == callable) {
            this.callable = null;
        } else {
            this.callable = (org.python.Callable) callable;
        }
        this.iterator = iterator;
    }

    @org.python.Method(
            __doc__ = "Implement iter(self)."
    )
    public org.python.Object __iter__() {
        return this;
    }

    @org.python.Method(
            __doc__ = "Implement next(self)."
    )
    public org.python.Object __next__() {
        while (true) {           // loop until we find first true
            org.python.Object current = iterator.__next__();
            org.python.Object value = current;
            if (callable != null) {
                org.python.Object[] args = new org.python.Object[] {current};
                value = callable.invoke(args, new java.util.HashMap());
            }
            if (value.toBoolean()) {
                return current;
            }
        }
    }
}
