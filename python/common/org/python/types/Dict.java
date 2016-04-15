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

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("dict.__new__() has not been implemented.");
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("dict.__init__() has not been implemented.");
    // }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        java.lang.StringBuilder buffer = new java.lang.StringBuilder("{");
        boolean first = true;
        for (org.python.Object key: this.value.keySet()) {
            if (first) {
                first = false;
            } else {
                buffer.append(", ");
            }
            buffer.append(
                String.format("%s: %s", key.__repr__(), value.get(key).__repr__())
            );
        }
        buffer.append("}");
        return new org.python.types.Str(buffer.toString());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __format__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.__format__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = "",
        args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
        __doc__ = "",
        args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
        __doc__ = "",
        args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
        __doc__ = "",
        args = {"other"}
    )
    public org.python.Object __ne__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
        __doc__ = "",
        args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
        __doc__ = "",
        args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // Builtin types can't have attributes set on them.
        return false;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("dict.__dir__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Int __len__() {
        return new org.python.types.Int(this.value.size());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getitem__(org.python.Object item) {
        org.python.Object value = this.value.get(item);
        if (value == null) {
            throw new org.python.exceptions.KeyError(item);
        }
        return value;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __setitem__(org.python.Object item, org.python.Object value) {
        this.value.put(item, value);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __delitem__(org.python.Object item) {
        org.python.Object value = this.value.remove(item);
        if (value == null) {
            throw new org.python.exceptions.KeyError(item);
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Iterable __iter__() {
        throw new org.python.exceptions.NotImplementedError("dict.__iter__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = "",
        args = {"item"}
    )
    public org.python.Object __contains__(org.python.Object item) {
        return new org.python.types.Bool(this.value.get(item) != null);
    }

    @org.python.Method(
        __doc__ = "",
        args = {"item"}
    )
    public org.python.Object __not_contains__(org.python.Object item) {
        return new org.python.types.Bool(this.value.get(item) == null);
    }

    @org.python.Method(
        __doc__ = "D.clear() -> None.  Remove all items from D."
    )
    public org.python.Object clear() {
        this.value.clear();
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object copy() {
        throw new org.python.exceptions.NotImplementedError("dict.copy() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object fromkeys(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.fromkeys() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object get(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.get() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object items() {
        throw new org.python.exceptions.NotImplementedError("dict.items() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object keys() {
        throw new org.python.exceptions.NotImplementedError("dict.keys() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object pop(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.pop() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object popitem(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.popitem() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object setdefault(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.setdefault() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object update(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.update() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object values() {
        throw new org.python.exceptions.NotImplementedError("dict.values() has not been implemented.");
    }

}
