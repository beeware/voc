package org.python.types;

class Iterator extends org.python.types.Object implements org.python.Object {
    java.util.Iterator<org.python.Object> iterator;

    public int hashCode() {
        return this.iterator.hashCode();
    }

    @org.python.Method(
            __doc__ = "Implement iter(self)."
    )
    public org.python.Object __iter__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__iter__ doesn't take keyword arguments");
        }
        if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }
        return this;
    }

    public org.python.Object __iter__() {
        return this.__iter__(null, null, null, null);
    }

    @org.python.Method(
            __doc__ = "Implement next(self)."
    )
    public org.python.Object __next__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__next__ doesn't take keyword arguments");
        }
        if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        try {
            return this.iterator.next();
        } catch (java.util.NoSuchElementException e) {
            throw new org.python.exceptions.StopIteration();
        }
    }

    public org.python.Object __next__() {
        return this.__next__(null, null, null, null);
    }
}
