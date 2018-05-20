package org.python.types;

class Dict_KeyIterator extends org.python.types.Iterator {
    public Dict_KeyIterator(org.python.types.Dict dict) {
        this.iterator = dict.value.keySet().iterator();
    }
}
