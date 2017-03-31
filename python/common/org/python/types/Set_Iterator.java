package org.python.types;

class Set_Iterator extends org.python.types.Iterator {
    public Set_Iterator(org.python.types.Set set) {
        super(set);
    }

    public Set_Iterator(org.python.types.FrozenSet set) {
        super(new org.python.types.Set(set.value));
    }
}
