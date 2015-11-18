package org.python;


public interface Iterable {
    @org.python.Method(
        __doc__ = "Implement iter(self)."
    )
    public org.python.Iterable __iter__();

    @org.python.Method(
        __doc__ = "Implement next(self)."
    )
    public org.python.Object __next__();
}
