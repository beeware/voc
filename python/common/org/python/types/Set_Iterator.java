package org.python.types;

class Set_Iterator extends org.python.types.Iterator {
    public Set_Iterator(org.python.types.Set set) {
        this.iterator = set.value.iterator();
    }

    public Set_Iterator(org.python.types.FrozenSet set) {
        this.iterator = set.value.iterator();
    }
}
