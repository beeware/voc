package org.python.types;

class Tuple_Iterator extends org.python.types.Iterator {
    public Tuple_Iterator(org.python.types.Tuple tuple) {
        this.iterator = tuple.value.iterator();
    }
}
