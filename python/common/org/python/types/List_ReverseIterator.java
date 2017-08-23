package org.python.types;

class List_ReverseIterator extends ReverseIterator {
    public List_ReverseIterator(org.python.types.List list) {
        this.iterator = list.value.listIterator(list.value.size());
    }
}
