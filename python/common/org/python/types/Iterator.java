package org.python.types;

class Iterator extends org.python.types.Object implements org.python.Iterable {
    java.util.Iterator<org.python.Object> iterator;

    public Iterator(org.python.types.List list) {
        this.iterator = list.value.iterator();
    }

    public Iterator(org.python.types.Tuple tuple) {
        this.iterator = tuple.value.iterator();
    }

    public org.python.Iterable __iter__() {
        return this;
    }

    public org.python.Object __next__() {
        try {
            return this.iterator.next();
        } catch (java.util.NoSuchElementException e) {
            throw new org.python.exceptions.StopIteration();
        }
    }
}
