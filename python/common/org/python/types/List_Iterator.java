package org.python.types;

class List_Iterator extends org.python.types.Iterator {
    public List_Iterator(org.python.types.List list) {
        this.iterator = list.value.iterator();
    }
}
