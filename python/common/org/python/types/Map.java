package org.python.types;

public class Map extends org.python.types.Object implements org.python.Iterable {
    private org.python.Object callable;
    private org.python.Iterable[] iterators;

    public Map(org.python.Object callable, org.python.Object [] iterables) {
        this.callable = callable;
        this.iterators = new org.python.Iterable[iterables.length];
        for (int i = 0; i < iterables.length; i++) {
            this.iterators[i] = org.Python.iter(iterables[i]);
        }
    }

    @org.python.Method(
        __doc__ = "Implement iter(self)."
    )
    public org.python.Iterable __iter__() {
        return this;
    }

    @org.python.Method(
        __doc__ = "Implement next(self)."
    )
    public org.python.Object __next__() {
        org.python.Object[] args = new org.python.Object[iterators.length];
        for (int i = 0; i < iterators.length; i++) {
            args[i] = iterators[i].__next__();
        }
        return ((org.python.Callable)callable).invoke(args, new java.util.HashMap());
    }
}
