package org.python.types;

class DictValues_Iterator extends org.python.types.Iterator {
    public DictValues_Iterator(org.python.types.DictValues dict_values) {
        this.iterator = dict_values.value.iterator();
    }
}
