package org.python.types;

public class Dict extends org.python.types.Object {
    public java.util.Map<org.python.Object, org.python.Object> value;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Dict
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.Dict) obj).value;
    }

    public java.lang.Object toJava() {
        return this.value;
    }

    public int hashCode() {
        return this.value.hashCode();
    }

    public Dict() {
        super();
        this.value = new java.util.HashMap<org.python.Object, org.python.Object>();
    }

    public Dict(java.util.Map<org.python.Object, org.python.Object> dict) {
        this.value = dict;
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("dict.__new__() has not been implemented.");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("dict.__init__() has not been implemented.");
    // }

    public org.python.types.Str __repr__() {
        java.lang.StringBuilder buffer = new java.lang.StringBuilder("{");
        boolean first = true;
        for (org.python.Object key: this.value.keySet()) {
            if (first) {
                first = false;
            } else {
                buffer.append(", ");
            }
            buffer.append(String.format("%s: %s", key.__repr__(), value.get(key).__repr__()));
        }
        buffer.append("}");
        return new org.python.types.Str(buffer.toString());
    }

    public org.python.types.Str __format__() {
        throw new org.python.exceptions.NotImplementedError("dict.__format__() has not been implemented.");
    }

    public org.python.Object __lt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.__lt__() has not been implemented.");
    }

    public org.python.Object __le__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.__le__() has not been implemented.");
    }

    public org.python.Object __eq__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.__eq__() has not been implemented.");
    }

    public org.python.Object __ne__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.__ne__() has not been implemented.");
    }

    public org.python.Object __gt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.__gt__() has not been implemented.");
    }

    public org.python.Object __ge__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.__ge__() has not been implemented.");
    }

    public org.python.Object __getattribute__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("dict.__getattribute__() has not been implemented.");
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        throw new org.python.exceptions.NotImplementedError("dict.__setattr__() has not been implemented.");
    }

    public void __delattr__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("dict.__delattr__() has not been implemented.");
    }

    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("dict.__dir__() has not been implemented.");
    }

    public org.python.types.Int __len__() {
        throw new org.python.exceptions.NotImplementedError("dict.__len__() has not been implemented.");
    }

    public org.python.Object __getitem__(org.python.Object index) {
        org.python.Object value = this.value.get(index);
        if (value == null) {
            throw new org.python.exceptions.KeyError(index);
        }
        return value;
    }

    public void __setitem__(org.python.Object index, org.python.Object value) {
        this.value.put(index, value);
    }

    public org.python.Iterable __iter__() {
        throw new org.python.exceptions.NotImplementedError("dict.__iter__() has not been implemented.");
    }

    public org.python.Object __contains__(org.python.Object key) {
        return new org.python.types.Bool(this.value.get(key) != null);
    }

    public org.python.Object __not_contains__(org.python.Object key) {
        return new org.python.types.Bool(this.value.get(key) == null);
    }

    public org.python.Object clear(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs != null || kwargs.size() > 0) {
            throw new org.python.exceptions.TypeError("clear() takes no keyword arguments");
        }
        if (args != null || args.size() > 0) {
            throw new org.python.exceptions.TypeError("clear() takes no arguments (" + args.size() + " given)");
        }
        this.clear();
        return org.python.types.NoneType.NONE;
    }

    public org.python.Object clear() {
        this.value.clear();
        return org.python.types.NoneType.NONE;
    }

    public org.python.Object copy(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("dict.copy() has not been implemented.");
    }

    public org.python.Object copy() {
        throw new org.python.exceptions.NotImplementedError("dict.copy() has not been implemented.");
    }

    public org.python.Object fromkeys(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("dict.fromkeys() has not been implemented.");
    }

    public org.python.Object get(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("dict.get() has not been implemented.");
    }

    public org.python.Object items(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("dict.items() has not been implemented.");
    }

    public org.python.Object items() {
        throw new org.python.exceptions.NotImplementedError("dict.items() has not been implemented.");
    }

    public org.python.Object keys(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("dict.keys() has not been implemented.");
    }

    public org.python.Object keys() {
        throw new org.python.exceptions.NotImplementedError("dict.keys() has not been implemented.");
    }

    public org.python.Object pop(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("dict.pop() has not been implemented.");
    }

    public org.python.Object popitem(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("dict.popitem() has not been implemented.");
    }

    public org.python.Object setdefault(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("dict.setdefault() has not been implemented.");
    }

    public org.python.Object update(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("dict.update() has not been implemented.");
    }

    public org.python.Object values(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("dict.values() has not been implemented.");
    }

    public org.python.Object values() {
        throw new org.python.exceptions.NotImplementedError("dict.values() has not been implemented.");
    }

}
