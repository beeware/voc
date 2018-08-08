package org.python.types;

public class DictValues extends org.python.types.Object {
    public java.util.Collection<org.python.Object> value;

    static {
        org.python.types.Type.declarePythonType(DictValues.class, "dict_values", null, null);
    }

    /**
     * A utility method to update the internal value of this object.
     * <p>
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.DictValues
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.DictValues) obj).value;
    }

    public java.lang.Object toJava() {
        return this.value;
    }

    public int hashCode() {
        return this.value.hashCode();
    }

    @Override
    public org.python.Object __hash__() {
        throw new org.python.exceptions.AttributeError(this, "__hash__");
    }

    @Override
    public boolean isHashable() {
        return false;
    }

    DictValues(org.python.types.Dict dict) {
        this.value = dict.value.values();
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.types.Str __repr__() {
        java.lang.StringBuilder buffer = new java.lang.StringBuilder("dict_values([");
        boolean first = true;
        for (org.python.Object item : this.value) {
            if (first) {
                first = false;
            } else {
                buffer.append(", ");
            }
            buffer.append(String.format("%s", item.__repr__()));
        }
        buffer.append("])");
        return new org.python.types.Str(buffer.toString());
    }

    @org.python.Method(
            __doc__ = "default object formatter"
    )
    public org.python.types.Str __format__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict_values.__format__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "__dir__() -> list\ndefault dir() implementation"
    )
    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("dict_keys.__dir__() has not been implemented.");
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // Builtin types can't have attributes set on them.
        return false;
    }

    public boolean __delattr_null(java.lang.String name) {
        // Can't delete attributes of Builtin types
        return false;
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary +: 'dict_values'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: 'dict_values'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'dict_values'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __bool__() {
        return org.python.types.Bool.getBool(!this.value.isEmpty());
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.List) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + this.typeName() + "'");
        } else if (other instanceof org.python.types.Tuple) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + this.typeName() + "'");
        } else if (other instanceof org.python.types.Str) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + this.typeName() + "'");
        } else if (other instanceof org.python.types.Bytes) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + this.typeName() + "'");
        }
        return super.__mul__(other);
    }

    @org.python.Method(
            __doc__ = "Return len(self)."
    )
    public org.python.types.Int __len__() {
        return org.python.types.Int.getInt(this.value.size());
    }

    @org.python.Method(
            __doc__ = "Implement iter(self)."
    )
    public org.python.Object __iter__() {
        return new org.python.types.DictValues_Iterator(this);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"index"}
    )
    public org.python.Object __getitem__(org.python.Object index) {
        if (index instanceof org.python.types.Int || index instanceof org.python.types.Bool) {
            throw new org.python.exceptions.TypeError("'dict_values' object does not support indexing");
        } else {
            throw new org.python.exceptions.TypeError("'dict_values' object is not subscriptable");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"index", "value"}
    )
    public void __setitem__(org.python.Object item, org.python.Object value) {
        throw new org.python.exceptions.TypeError("'dict_values' object does not support item assignment");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"index"}
    )
    public void __delitem__(org.python.Object item) {
        throw new org.python.exceptions.TypeError("'dict_values' object doesn't support item deletion");
    }

    @org.python.Method(
            __doc__ = "True if D has a value v, else False.",
            args = {"item"}
    )
    public org.python.Object __contains__(org.python.Object item) {
        return org.python.types.Bool.getBool(this.value.contains(item));
    }

    @org.python.Method(
            __doc__ = "",
            args = {"item"}
    )
    public org.python.Object __not_contains__(org.python.Object item) {
        return org.python.types.Bool.getBool(!this.value.contains(item));
    }
}
