package org.python.types;

public class DictKeys extends org.python.types.FrozenSet {
    static {
        org.python.types.Type.declarePythonType(DictKeys.class, "dict_keys", null, null);
    }

    @Override
    public org.python.Object __hash__() {
        throw new org.python.exceptions.AttributeError(this, "__hash__");
    }

    @Override
    public boolean isHashable() {
        return false;
    }

    public DictKeys(org.python.types.Dict dict) {
        this.value = dict.value.keySet();
    }

    /**
     * A utility method to create a set from an iterable object
     * <p>
     * Used by the __and__,__or__,__sub__ and __xor__ operations
     * obj must have a valid iterator
     */
    private java.util.Set<org.python.Object> fromIter(org.python.Object obj) {
        java.util.Set<org.python.Object> generated = new java.util.HashSet<org.python.Object>();
        org.python.Object iterator = org.Python.iter(obj);
        try {
            while (true) {
                org.python.Object next = iterator.__next__();
                generated.add(next);
            }
        } catch (org.python.exceptions.StopIteration si) {
        }
        return generated;
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.types.Str __repr__() {
        java.lang.StringBuilder buffer = new java.lang.StringBuilder(this.typeName() + "([");
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
        throw new org.python.exceptions.NotImplementedError(this.typeName() + ".__format__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "__dir__() -> list\ndefault dir() implementation"
    )
    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError(this.typeName() + ".__dir__() has not been implemented.");
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
            __doc__ = "",
            args = {"index"}
    )
    public org.python.Object __getitem__(org.python.Object index) {
        if (index instanceof org.python.types.Int || index instanceof org.python.types.Bool) {
            throw new org.python.exceptions.TypeError("'" + this.typeName() + "' object does not support indexing");
        } else {
            throw new org.python.exceptions.TypeError("'" + this.typeName() + "' object is not subscriptable");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"index", "value"}
    )
    public void __setitem__(org.python.Object item, org.python.Object value) {
        throw new org.python.exceptions.TypeError("'" + this.typeName() + "' object does not support item assignment");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"index"}
    )
    public void __delitem__(org.python.Object item) {
        throw new org.python.exceptions.TypeError("'" + this.typeName() + "' object doesn't support item deletion");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: '" + this.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary +: '" + this.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: '" + this.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self&value."
    )
    public org.python.types.Set __and__(org.python.Object other) {
        java.util.Set<org.python.Object> generated = this.fromIter(other);
        generated.retainAll(this.value);
        return new org.python.types.Set(generated);
    }

    @org.python.Method(
            __doc__ = "Return self|value."
    )
    public org.python.types.Set __or__(org.python.Object other) {
        java.util.Set<org.python.Object> generated = this.fromIter(other);
        generated.addAll(this.value);
        return new org.python.types.Set(generated);
    }

    @org.python.Method(
            __doc__ = "Return self-value."
    )
    public org.python.types.Set __sub__(org.python.Object other) {
        java.util.Set<org.python.Object> set1 = new java.util.HashSet<org.python.Object>(this.value);
        java.util.Set<org.python.Object> set2 = this.fromIter(other);
        set1.removeAll(set2);
        return new org.python.types.Set(set1);
    }

    @org.python.Method(
            __doc__ = "Return self^value."
    )
    public org.python.types.Set __xor__(org.python.Object other) {
        java.util.Set<org.python.Object> s1 = this.fromIter(other);
        java.util.Set<org.python.Object> sym_dif = new java.util.HashSet<org.python.Object>(s1);
        sym_dif.addAll(this.value);
        java.util.Set<org.python.Object> tmp = new java.util.HashSet<org.python.Object>(s1);
        tmp.retainAll(this.value);
        sym_dif.removeAll(tmp);
        return new org.python.types.Set(sym_dif);
    }

    @org.python.Method(
            __doc__ = "Return value&self."
    )
    public org.python.types.Set __rand__(org.python.Object other) {
        return this.__and__(other);
    }

    @org.python.Method(
            __doc__ = "Return value|self."
    )
    public org.python.types.Set __ror__(org.python.Object other) {
        return this.__or__(other);
    }

    @org.python.Method(
            __doc__ = "Return value^self."
    )
    public org.python.types.Set __rxor__(org.python.Object other) {
        return this.__xor__(other);
    }

    @org.python.Method(
            __doc__ = "Return value-self."
    )
    public org.python.types.Set __rsub__(org.python.Object other) {
        java.util.Set<org.python.Object> generated = this.fromIter(other);
        generated.removeAll(this.value);
        return new org.python.types.Set(generated);
    }

    @org.python.Method(
            __doc__ = "Return True if the set has no elements in common with other. Sets are\n" +
                      "disjoint if and only if their intersection is the empty set.",
            args = {"other"}
    )
    public org.python.Object isdisjoint(org.python.Object other) {
        java.util.Set<org.python.Object> generated = new java.util.HashSet<org.python.Object>();
        org.python.Object iterator = org.Python.iter(other);
        try {
            while (true) {
                org.python.Object next = iterator.__next__();
                generated.add(next);
            }
        } catch (org.python.exceptions.StopIteration si) {
        }
        generated.retainAll(this.value);
        return org.python.types.Bool.getBool(generated.size() > 0);
    }
    /**
     * The following methods are not present in Python's dict_keys but are present in DictKeys (inherited from FrozenSet)
     * <p>
     * Hence, throw an AttributeError every time any of these methods is called
     */
    public org.python.Object issubset(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "issubset");
    }

    public org.python.Object issuperset(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "issuperset");
    }

    public org.python.Object union(org.python.types.Tuple others) {
        throw new org.python.exceptions.AttributeError(this, "union");
    }

    public org.python.Object intersection(org.python.types.Tuple others) {
        throw new org.python.exceptions.AttributeError(this, "intersection");
    }

    public org.python.Object difference(org.python.types.Tuple others) {
        throw new org.python.exceptions.AttributeError(this, "difference");
    }

    public org.python.Object symmetric_difference(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "issuperset");
    }
}
