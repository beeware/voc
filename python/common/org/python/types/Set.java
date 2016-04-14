package org.python.types;

public class Set extends org.python.types.Object {
    public java.util.Set<org.python.Object> value;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Set
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.Set) obj).value;
    }

    public java.lang.Object toJava() {
        return this.value;
    }

    public int hashCode() {
        return this.value.hashCode();
    }

    public Set() {
        super();
        this.value = new java.util.HashSet<org.python.Object>();
    }

    public Set(java.util.Set<org.python.Object> set) {
        super();
        this.value = set;
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("__new__() has not been implemented");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("__init__() has not been implemented");
    // }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        // Representation of an empty set is different
        if (this.value.size() == 0) {
            return new org.python.types.Str("set()");
        }

        java.lang.StringBuilder buffer = new java.lang.StringBuilder("{");
        boolean first = true;
        for (org.python.Object obj: this.value) {
            if (first) {
                first = false;
            } else {
                buffer.append(", ");
            }
            buffer.append(obj.__repr__());
        }
        buffer.append("}");
        return new org.python.types.Str(buffer.toString());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __format__(org.python.Object format_string) {
        throw new org.python.exceptions.NotImplementedError("__format__() has not been implemented");
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
        throw new org.python.exceptions.NotImplementedError("__dir__() has not been implemented");
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
    public org.python.Iterable __iter__() {
        throw new org.python.exceptions.NotImplementedError("__iter__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __contains__(org.python.Object other) {
        return new org.python.types.Bool(this.value.contains(other));
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __not_contains__(org.python.Object other) {
        return new org.python.types.Bool(!this.value.contains(other));
    }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public org.python.Object __sub__(org.python.Object other) {
    //     throw new org.python.exceptions.NotImplementedError("__sub__() has not been implemented");
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public org.python.Object __and__(org.python.Object other) {
    //     throw new org.python.exceptions.NotImplementedError("__and__() has not been implemented");
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public org.python.Object __xor__(org.python.Object other) {
    //     throw new org.python.exceptions.NotImplementedError("__xor__() has not been implemented");
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public org.python.Object __or__(org.python.Object other) {
    //     throw new org.python.exceptions.NotImplementedError("__or__() has not been implemented");
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public org.python.Object __rsub__(org.python.Object other) {
    //     throw new org.python.exceptions.NotImplementedError("__rsub__() has not been implemented");
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public org.python.Object __rand__(org.python.Object other) {
    //     throw new org.python.exceptions.NotImplementedError("__rand__() has not been implemented");
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public org.python.Object __rxor__(org.python.Object other) {
    //     throw new org.python.exceptions.NotImplementedError("__rxor__() has not been implemented");
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public org.python.Object __ror__(org.python.Object other) {
    //     throw new org.python.exceptions.NotImplementedError("__ror__() has not been implemented");
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public void __isub__(org.python.Object other) {
    //     throw new org.python.exceptions.NotImplementedError("__isub__() has not been implemented");
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public void __iand__(org.python.Object other) {
    //     throw new org.python.exceptions.NotImplementedError("__iand__() has not been implemented");
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public void __ixor__(org.python.Object other) {
    //     throw new org.python.exceptions.NotImplementedError("__ixor__() has not been implemented");
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public void __ior__(org.python.Object other) {
    //     throw new org.python.exceptions.NotImplementedError("__ior__() has not been implemented");
    // }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object add(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("add() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object clear() {
        this.value.clear();
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object copy() {
        throw new org.python.exceptions.NotImplementedError("copy() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object difference(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("difference() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object difference_update(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("difference_update() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object discard(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("discard() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object intersection(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("intersection() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object intersection_update(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("intersection_update() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object isdisjoint(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("isdisjoint() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object issubset(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("issubset() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object issuperset(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("issuperset() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object pop(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("pop() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object remove(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("remove() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object symmetric_difference(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("symmetric_difference() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object symmetric_difference_update(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("symmetric_difference_update() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object union(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("union() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object update(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("update() has not been implemented.");
    }
}
