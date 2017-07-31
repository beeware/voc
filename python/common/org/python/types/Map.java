package org.python.types;

public class Map extends org.python.types.Object implements org.python.Object {
    private org.python.Object callable;
    private org.python.Object[] iterators;

    public Map(org.python.Object callable, org.python.types.Tuple iterables) {
        this.callable = callable;
        this.iterators = new org.python.Object[iterables.value.size()];
        for (int i = 0; i < iterables.value.size(); i++) {
            this.iterators[i] = org.Python.iter(iterables.value.get(i));
        }
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
        org.python.Object[] args = new org.python.Object[iterators.length];
        for (int i = 0; i < iterators.length; i++) {
            args[i] = iterators[i].__next__();
        }
        return ((org.python.Callable) callable).invoke(args, new java.util.HashMap());
    }
}
