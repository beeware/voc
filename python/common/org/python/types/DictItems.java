package org.python.types;

public class DictItems extends org.python.types.Object {
    java.util.Set<java.util.Map.Entry<org.python.Object, org.python.Object>> value;

    static {
        org.python.types.Type.declarePythonType(DictItems.class, "dict_items", null, null);
    }

    /**
     * A utility method to update the internal value of this object.
     * <p>
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.DictItems
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.DictItems) obj).value;
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

    public DictItems(org.python.types.Dict dict) {
        this.value = dict.value.entrySet();
    }

    private java.util.Set<org.python.Object> toTupleSet() {
        java.util.Set<org.python.Object> set = new java.util.HashSet<org.python.Object>();
        for (java.util.Map.Entry<org.python.Object, org.python.Object> entry : this.value) {
            java.util.List<org.python.Object> tmp = new java.util.ArrayList<org.python.Object>();
            tmp.add(entry.getKey());
            tmp.add(entry.getValue());
            set.add(new org.python.types.Tuple(tmp));
        }
        return set;
    }

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
        java.lang.StringBuilder buffer = new java.lang.StringBuilder("dict_items([");
        boolean first = true;
        for (java.util.Map.Entry<org.python.Object, org.python.Object> entry : this.value) {
            if (first) {
                first = false;
            } else {
                buffer.append(", ");
            }
            buffer.append(String.format("(%s, %s)", entry.getKey().__repr__(), entry.getValue().__repr__()));
        }
        buffer.append("])");
        return new org.python.types.Str(buffer.toString());
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
        throw new org.python.exceptions.TypeError("bad operand type for unary +: 'dict_items'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: 'dict_items'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'dict_items'");
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
        return new org.python.types.Set_Iterator(new org.python.types.Set(this.toTupleSet()));
    }

    @org.python.Method(
            __doc__ = "",
            args = {"index"}
    )
    public org.python.Object __getitem__(org.python.Object index) {
        if (index instanceof org.python.types.Int || index instanceof org.python.types.Bool) {
            throw new org.python.exceptions.TypeError("'dict_items' object does not support indexing");
        } else {
            throw new org.python.exceptions.TypeError("'dict_items' object is not subscriptable");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"index", "value"}
    )
    public void __setitem__(org.python.Object item, org.python.Object value) {
        throw new org.python.exceptions.TypeError("'dict_items' object does not support item assignment");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"index"}
    )
    public void __delitem__(org.python.Object item) {
        throw new org.python.exceptions.TypeError("'dict_items' object doesn't support item deletion");
    }

    @org.python.Method(
            __doc__ = "True if D has a value v, else False.",
            args = {"item"}
    )
    public org.python.Object __contains__(org.python.Object item) {
        org.python.types.Set set = new org.python.types.Set(this.toTupleSet());
        return set.__contains__(item);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"item"}
    )
    public org.python.Object __not_contains__(org.python.Object other) {
        org.python.types.Set set = new org.python.types.Set(this.toTupleSet());
        return set.__not_contains__(other);
    }

    @org.python.Method(
            __doc__ = "Return self<value.",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        if (other instanceof org.python.types.DictItems) {
            org.python.types.DictItems otherItems = (org.python.types.DictItems) other;
            return org.python.types.Bool.getBool(otherItems.value.containsAll(this.value) && !this.value.equals(otherItems.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self<=value.",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        if (other instanceof org.python.types.DictItems) {
            org.python.types.DictItems otherItems = (org.python.types.DictItems) other;
            return org.python.types.Bool.getBool(otherItems.value.containsAll(this.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self==value.",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.DictItems) {
            org.python.types.DictItems otherItems = (org.python.types.DictItems) other;
            return org.python.types.Bool.getBool(this.value.equals(otherItems.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self>value.",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        if (other instanceof org.python.types.DictItems) {
            org.python.types.DictItems otherItems = (org.python.types.DictItems) other;
            return org.python.types.Bool.getBool(this.value.containsAll(otherItems.value) && !this.value.equals(otherItems.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self>=value.",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        if (other instanceof org.python.types.DictItems) {
            org.python.types.DictItems otherItems = (org.python.types.DictItems) other;
            return org.python.types.Bool.getBool(this.value.containsAll(otherItems.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self&value."
    )
    public org.python.types.Set __and__(org.python.Object other) {
        java.util.Set<org.python.Object> generated = this.fromIter(other);
        generated.retainAll(this.toTupleSet());
        return new org.python.types.Set(generated);
    }

    @org.python.Method(
            __doc__ = "Return self|value."
    )
    public org.python.types.Set __or__(org.python.Object other) {
        java.util.Set<org.python.Object> generated = this.fromIter(other);
        generated.addAll(this.toTupleSet());
        return new org.python.types.Set(generated);
    }

    @org.python.Method(
            __doc__ = "Return self-value."
    )
    public org.python.types.Set __sub__(org.python.Object other) {
        java.util.Set<org.python.Object> set1 = new java.util.HashSet<org.python.Object>(this.toTupleSet());
        java.util.Set<org.python.Object> set2 = this.fromIter(other);
        set1.removeAll(set2);
        return new org.python.types.Set(set1);
    }

    @org.python.Method(
            __doc__ = "Return self^value."
    )
    public org.python.types.Set __xor__(org.python.Object other) {
        java.util.Set<org.python.Object> tupleset = this.toTupleSet();
        java.util.Set<org.python.Object> s1 = this.fromIter(other);
        java.util.Set<org.python.Object> sym_dif = new java.util.HashSet<org.python.Object>(s1);
        sym_dif.addAll(tupleset);
        java.util.Set<org.python.Object> tmp = new java.util.HashSet<org.python.Object>(s1);
        tmp.retainAll(tupleset);
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
        generated.removeAll(this.toTupleSet());
        return new org.python.types.Set(generated);
    }

    @org.python.Method(
            __doc__ = "Return True if the set has no elements in common with other. Sets are\n" +
                      "disjoint if and only if their intersection is the empty set.",
            args = {"other"}
    )
    public org.python.Object isdisjoint(org.python.Object other) {
        java.util.Set<org.python.Object> generated = this.fromIter(other);
        generated.retainAll(this.value);
        return org.python.types.Bool.getBool(generated.size() > 0);
    }
}
