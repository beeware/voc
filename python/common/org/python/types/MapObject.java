package org.python.types;

public class MapObject extends org.python.types.Object implements org.python.Iterable {
    private org.python.Object callable;
    private java.util.List<org.python.Iterable> iterators;

    public MapObject(org.python.Object callable, org.python.Object [] iterables) {
        this.callable = callable;
        this.iterators = new java.util.ArrayList();
        for (org.python.Object iterable: iterables) {
            this.iterators.add(org.Python.iter(iterable));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str(String.format("<map object at 0x%s>", this.hashCode()));
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
        org.python.Object[] args = new org.python.Object[iterators.size()];
        int i = 0;
        for (org.python.Iterable iterator: iterators) {
            args[i] = iterator.__next__();
            assert(args[i] != null);
            i++;
        }
        return ((org.python.Callable)callable).invoke(args, new java.util.HashMap());
    }
}
