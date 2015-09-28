package org.python.types;

public class List extends org.python.types.Object {
    public java.util.ArrayList<org.python.Object> value;

    /**
     * Return the python name for this class.
     */
    public java.lang.String getPythonName() {
        return "list";
    }

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.List
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.List) obj).value;
    }

    public List(java.util.ArrayList<org.python.Object> list) {
        super();
        this.value = list;
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("list.__new__() has not been implemented.");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("list.__init__() has not been implemented.");
    // }

    public org.python.types.Str __repr__() {
        java.lang.StringBuilder buffer = new java.lang.StringBuilder("[");
        boolean first = true;
        for (org.python.Object obj: this.value) {
            if (first) {
                first = false;
            } else {
                buffer.append(", ");
            }
            buffer.append(obj.__repr__());
        }
        buffer.append("]");
        return new org.python.types.Str(buffer.toString());
    }

    public org.python.types.Str __format__() {
        throw new org.python.exceptions.NotImplementedError("list.__format__() has not been implemented.");
    }

    public org.python.Object __lt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__lt__() has not been implemented.");
    }

    public org.python.Object __le__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__le__() has not been implemented.");
    }

    public org.python.Object __eq__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__eq__() has not been implemented.");
    }

    public org.python.Object __ne__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__ne__() has not been implemented.");
    }

    public org.python.Object __gt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__gt__() has not been implemented.");
    }

    public org.python.Object __ge__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__ge__() has not been implemented.");
    }

    public org.python.types.Int __len__() {
        throw new org.python.exceptions.NotImplementedError("list.__len__() has not been implemented.");
    }

    public org.python.Object __getitem__(org.python.Object index) {
        try {
            return this.__getitem__((int)((org.python.types.Int) index).value);
        } catch (ClassCastException e) {
            throw new org.python.exceptions.TypeError("list indices must be integers, not str");
        }
    }

    public org.python.Object __getitem__(int index) {
        if (index < 0) {
            if (-index > this.value.size()) {
                throw new org.python.exceptions.IndexError("list index out of range");
            } else {
                return this.value.get(this.value.size() + index);
            }
        } else {
            if (index >= this.value.size()) {
                throw new org.python.exceptions.IndexError("list index out of range");
            } else {
                return this.value.get(index);
            }
        }
    }

    public void __setitem__(org.python.Object index, org.python.Object value) {
        throw new org.python.exceptions.NotImplementedError("list.__setitem__() has not been implemented.");
    }

    public org.python.Iterable __iter__() {
        return new org.python.types.Iterator(this);
    }

    public org.python.Iterable __reversed__() {
        throw new org.python.exceptions.NotImplementedError("list.__reversed__() has not been implemented.");
    }

    public org.python.types.Bool __contains__() {
        throw new org.python.exceptions.NotImplementedError("list.__contains__() has not been implemented.");
    }

    public org.python.Object __add__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__add__() has not been implemented.");
    }

    public org.python.Object __mul__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__mul__() has not been implemented.");
    }

    public org.python.Object __rmul__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__rmul__() has not been implemented.");
    }

    public void append(org.python.Object [] args, java.util.HashMap kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("append() takes no keyword arguments");
        }
        if (args.length == 1) {
            this.append(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("append() takes exactly 1 argument (" + args.length + " given)");
        }
    }

    public void append(org.python.Object value) {
        this.value.add(value);
    }

    public void clear(org.python.Object [] args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.clear() has not been implemented.");
    }

    public void clear() {
        throw new org.python.exceptions.NotImplementedError("list.clear() has not been implemented.");
    }

    public org.python.Object copy(org.python.Object [] args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.copy() has not been implemented.");
    }

    public org.python.Object copy() {
        throw new org.python.exceptions.NotImplementedError("list.copy() has not been implemented.");
    }

    public org.python.Object count(org.python.Object [] args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.count() has not been implemented.");
    }

    public org.python.Object count(org.python.Object value) {
        throw new org.python.exceptions.NotImplementedError("list.count() has not been implemented.");
    }

    public org.python.Object extend(org.python.Object [] args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.extend() has not been implemented.");
    }

    public org.python.Object extend(org.python.Object iterable) {
        throw new org.python.exceptions.NotImplementedError("list.extend() has not been implemented.");
    }

    public org.python.Object index(org.python.Object [] args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.index() has not been implemented.");
    }

    public org.python.Object index(org.python.Object value, org.python.Object start, org.python.Object stop) {
        throw new org.python.exceptions.NotImplementedError("list.index() has not been implemented.");
    }

    public org.python.Object index(org.python.Object value, org.python.Object start) {
        throw new org.python.exceptions.NotImplementedError("list.index() has not been implemented.");
    }

    public org.python.Object index(org.python.Object value, int start, int stop) {
        throw new org.python.exceptions.NotImplementedError("list.index() has not been implemented.");
    }

    public org.python.Object index(org.python.Object value, int start) {
        return this.index(value, start, -1);
    }

    public org.python.Object index(org.python.Object value) {
        return this.index(value, 0, -1);
    }

    public org.python.Object insert(org.python.Object [] args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.insert() has not been implemented.");
    }

    public void insert(org.python.Object index, org.python.Object object) {
        throw new org.python.exceptions.NotImplementedError("list.insert() has not been implemented.");
    }

    public org.python.Object pop(org.python.Object [] args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.pop() has not been implemented.");
    }

    public org.python.Object pop(org.python.Object index) {
        throw new org.python.exceptions.NotImplementedError("list.pop() has not been implemented.");
    }

    public org.python.Object pop(int index) {
        throw new org.python.exceptions.NotImplementedError("list.pop() has not been implemented.");
    }

    public org.python.Object pop() {
        return this.pop(-1);
    }

    public void remove(org.python.Object [] args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.remove() has not been implemented.");
    }

    public void remove(org.python.Object value) {
        throw new org.python.exceptions.NotImplementedError("list.remove() has not been implemented.");
    }

    public void reverse(org.python.Object [] args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.reverse() has not been implemented.");
    }

    public void reverse() {
        throw new org.python.exceptions.NotImplementedError("list.reverse() has not been implemented.");
    }

    public org.python.Object sort(org.python.Object [] args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.sort() has not been implemented.");
    }

    public org.python.Object sort(org.python.Object key, org.python.Object reverse) {
        throw new org.python.exceptions.NotImplementedError("list.sort() has not been implemented.");
    }

}
