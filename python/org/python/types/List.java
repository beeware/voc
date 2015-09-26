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

    public org.python.Object __getattribute__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("list.__getattribute__() has not been implemented.");
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        throw new org.python.exceptions.NotImplementedError("list.__setattr__() has not been implemented.");
    }

    public void __delattr__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("list.__delattr__() has not been implemented.");
    }

    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("list.__dir__() has not been implemented.");
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
        throw new org.python.exceptions.NotImplementedError("list.__iter__() has not been implemented.");
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

    public void __iadd__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__iadd__() has not been implemented.");
    }

    public void __imul__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__imul__() has not been implemented.");
    }


}