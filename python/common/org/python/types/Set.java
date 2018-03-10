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

    @Override
    public org.python.Object __hash__() {
        throw new org.python.exceptions.AttributeError(this, "__hash__");
    }

    public Set() {
        super();
        this.value = new java.util.HashSet<org.python.Object>();
    }

    public Set(java.util.Set<org.python.Object> set) {
        super();
        this.value = set;
    }

    @org.python.Method(
            __doc__ = "set() -> new empty set object" +
                    "set(iterable) -> new set object\n" +
                    "\n" +
                    "Build an unordered collection of unique elements.\n",
            default_args = {"iterable"}
    )
    public Set(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args[0] == null) {
            this.value = new java.util.HashSet<org.python.Object>();
        } else {
            if (args[0] instanceof org.python.types.Set) {
                this.value = new java.util.HashSet<org.python.Object>(
                        ((org.python.types.Set) args[0]).value
                );
            } else if (args[0] instanceof org.python.types.List) {
                this.value = new java.util.HashSet<org.python.Object>(
                        ((org.python.types.List) args[0]).value
                );
            } else if (args[0] instanceof org.python.types.Tuple) {
                this.value = new java.util.HashSet<org.python.Object>(
                        ((org.python.types.Tuple) args[0]).value
                );
            } else {
                org.python.Object iterator = org.Python.iter(args[0]);
                java.util.Set<org.python.Object> generated = new java.util.HashSet<org.python.Object>();
                try {
                    while (true) {
                        org.python.Object next = iterator.__next__();
                        generated.add(next);
                    }
                } catch (org.python.exceptions.StopIteration si) {
                }
                this.value = generated;
            }
        }
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("__new__() has not been implemented");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("__init__() has not been implemented");
    // }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.types.Str __repr__() {
        // Representation of an empty set is different
        if (this.value.size() == 0) {
            return new org.python.types.Str("set()");
        }

        java.lang.StringBuilder buffer = new java.lang.StringBuilder("{");
        boolean first = true;
        for (org.python.Object obj : this.value) {
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
            __doc__ = "default object formatter"
    )
    public org.python.types.Str __format__(org.python.Object format_string) {
        throw new org.python.exceptions.NotImplementedError("__format__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"index"}
    )
    public org.python.Object __getitem__(org.python.Object index) {
        if (index instanceof org.python.types.Int || index instanceof org.python.types.Bool) {
            throw new org.python.exceptions.TypeError("'set' object does not support indexing");
        } else {
            throw new org.python.exceptions.TypeError("'set' object is not subscriptable");
        }
    }

    @org.python.Method(
            __doc__ = "Return self<value.",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        if (other instanceof org.python.types.Set) {
            org.python.types.Set otherSet = (org.python.types.Set) other;
            return new org.python.types.Bool(otherSet.value.containsAll(this.value) && !this.value.equals(otherSet.value));
        } else if (other instanceof org.python.types.FrozenSet) {
            org.python.types.FrozenSet otherSet = (org.python.types.FrozenSet) other;
            return new org.python.types.Bool(otherSet.value.containsAll(this.value) && !this.value.equals(otherSet.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self<=value.",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        if (other instanceof org.python.types.Set) {
            org.python.types.Set otherSet = (org.python.types.Set) other;
            return new org.python.types.Bool(otherSet.value.containsAll(this.value));
        } else if (other instanceof org.python.types.FrozenSet) {
            org.python.types.FrozenSet otherSet = (org.python.types.FrozenSet) other;
            return new org.python.types.Bool(otherSet.value.containsAll(this.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self==value.",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.Set) {
            org.python.types.Set otherSet = (org.python.types.Set) other;
            return new org.python.types.Bool(this.value.equals(otherSet.value));
        } else if (other instanceof org.python.types.FrozenSet) {
            org.python.types.FrozenSet otherSet = (org.python.types.FrozenSet) other;
            return new org.python.types.Bool(this.value.equals(otherSet.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self>value.",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        if (other instanceof org.python.types.Set) {
            org.python.types.Set otherSet = (org.python.types.Set) other;
            return new org.python.types.Bool(this.value.containsAll(otherSet.value) && !this.value.equals(otherSet.value));
        } else if (other instanceof org.python.types.FrozenSet) {
            org.python.types.FrozenSet otherSet = (org.python.types.FrozenSet) other;
            return new org.python.types.Bool(this.value.containsAll(otherSet.value) && !this.value.equals(otherSet.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self>=value.",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        if (other instanceof org.python.types.Set) {
            org.python.types.Set otherSet = (org.python.types.Set) other;
            return new org.python.types.Bool(this.value.containsAll(otherSet.value));
        } else if (other instanceof org.python.types.FrozenSet) {
            org.python.types.FrozenSet otherSet = (org.python.types.FrozenSet) other;
            return new org.python.types.Bool(this.value.containsAll(otherSet.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // Builtin types can't have attributes set on them.
        return false;
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.types.Bool __bool__() {
        return new org.python.types.Bool(this.value.size() > 0);
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'set'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary +: 'set'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: 'set'");
    }

    @org.python.Method(
            __doc__ = "__dir__() -> list\ndefault dir() implementation"
    )
    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("__dir__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return len(self)."
    )
    public org.python.types.Int __len__() {
        return new org.python.types.Int(this.value.size());
    }

    @org.python.Method(
            __doc__ = "Implement iter(self)."
    )
    public org.python.Object __iter__() {
        return new org.python.types.Set_Iterator(this);
    }

    @org.python.Method(
            __doc__ = "x.__contains__(y) <==> y in x.",
            args = {"item"}
    )
    public org.python.Object __contains__(org.python.Object other) {
        return new org.python.types.Bool(this.value.contains(other));
    }

    @org.python.Method(
            __doc__ = "",
            args = {"item"}
    )
    public org.python.Object __not_contains__(org.python.Object other) {
        return new org.python.types.Bool(!this.value.contains(other));
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __mul__(org.python.Object other) {
        if ((other instanceof org.python.types.List) ||
                (other instanceof org.python.types.Tuple) ||
                (other instanceof org.python.types.Str) ||
                (other instanceof org.python.types.ByteArray) ||
                (other instanceof org.python.types.Bytes)) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + this.typeName() + "'");
        }
        return super.__mul__(other);
    }

    @org.python.Method(
            __doc__ = "Return self-value."
    )
    public org.python.Object __sub__(org.python.Object other) {
        java.util.Set set = ((org.python.types.Set) this.copy()).value;
        if (other instanceof org.python.types.Set) {
            set.removeAll(((org.python.types.Set) other).value);
            return new org.python.types.Set(set);
        } else if (other instanceof org.python.types.FrozenSet) {
            set.removeAll(((org.python.types.FrozenSet) other).value);
            return new org.python.types.Set(set);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for -: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self&value."
    )
    public org.python.Object __and__(org.python.Object other) {
        java.util.Set set = ((org.python.types.Set) this.copy()).value;
        if (other instanceof org.python.types.Set) {
            set.retainAll(((org.python.types.Set) other).value);
            return new org.python.types.Set(set);
        } else if (other instanceof org.python.types.FrozenSet) {
            set.retainAll(((org.python.types.FrozenSet) other).value);
            return new org.python.types.Set(set);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for &: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self^value."
    )
    public org.python.Object __xor__(org.python.Object other) {
        java.util.Set set = ((org.python.types.Set) this.copy()).value;
        java.util.Set intersect_set = ((org.python.types.Set) this.copy()).value;
        if (other instanceof org.python.types.Set) {
            set.addAll(((org.python.types.Set) other).value);
            intersect_set.retainAll(((org.python.types.Set) other).value);
            // take away the intersection from the union for XOR
            set.removeAll(intersect_set);
            return new org.python.types.Set(set);
        } else if (other instanceof org.python.types.FrozenSet) {
            set.addAll(((org.python.types.FrozenSet) other).value);
            intersect_set.retainAll(((org.python.types.FrozenSet) other).value);
            // take away the intersection from the union for XOR
            set.removeAll(intersect_set);
            return new org.python.types.Set(set);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ^: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self|value."
    )
    public org.python.Object __or__(org.python.Object other) {
        java.util.Set set = ((org.python.types.Set) this.copy()).value;
        if (other instanceof org.python.types.Set) {
            set.addAll(((org.python.types.Set) other).value);
            return new org.python.types.Set(set);
        } else if (other instanceof org.python.types.FrozenSet) {
            set.addAll(((org.python.types.FrozenSet) other).value);
            return new org.python.types.Set(set);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for |: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

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
    // public void __ixor__(org.python.Object other) {
    //     throw new org.python.exceptions.NotImplementedError("__ixor__() has not been implemented");
    // }

    @org.python.Method(
            __doc__ = "Add an element to a set.\n\nThis has no effect if the element is already present.",
            args = {"other"}
    )
    public org.python.Object add(org.python.Object other) {
        this.value.add(other);
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
            __doc__ = "Remove all elements from this set."
    )
    public org.python.Object clear() {
        this.value.clear();
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
            __doc__ = "Return a shallow copy of a set."
    )
    public org.python.Object copy() {
        return new Set(new java.util.HashSet<org.python.Object>(this.value));
    }

    @org.python.Method(
            __doc__ = "Return the difference of two or more sets as a new set.\n\n(i.e. all elements that are in this set but not the others.)",
            args = {"other"}
    )
    public org.python.Object difference(org.python.Object other) {
        try {
            org.python.types.Set otherSet = null;
            if (other instanceof org.python.types.Set) {
                otherSet = (org.python.types.Set) other;
            } else {
                otherSet = new org.python.types.Set(new org.python.Object[] {other}, null);
            }
            return this.__sub__(otherSet);
        } catch (org.python.exceptions.AttributeError e) {
            throw new org.python.exceptions.TypeError("'" + other.typeName() + "' object is not iterable");
        }
    }

    @org.python.Method(
            __doc__ = "Remove all elements of another set from this set.",
            args = {"other"}
    )
    public org.python.Object difference_update(org.python.Object other) {
        this.value.removeAll(((Set) other).value);
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
            __doc__ = "Remove an element from a set if it is a member.\n\nIf the element is not a member, do nothing.",
            args = {"item"}
    )
    public org.python.Object discard(org.python.Object item) {
        this.value.remove(item);
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
            __doc__ = "Return the intersection of two sets as a new set.\n\n(i.e. all elements that are in both sets.)",
            args = {"other"}
    )
    public org.python.Object intersection(org.python.Object other) {
        try {
            org.python.types.Set otherSet = null;
            if (other instanceof org.python.types.Set) {
                otherSet = (org.python.types.Set) other;
            } else {
                otherSet = new org.python.types.Set(new org.python.Object[] {other}, null);
            }
            return this.__and__(otherSet);
        } catch (org.python.exceptions.AttributeError e) {
            throw new org.python.exceptions.TypeError("'" + other.typeName() + "' object is not iterable");
        }
    }

    @org.python.Method(
            __doc__ = "Update a set with the intersection of itself and another.",
            args = {"other"}
    )
    public org.python.Object intersection_update(org.python.Object other) {
        try {
            this.value.retainAll(((Set) other).value);
        } catch (ClassCastException te) {
            throw new org.python.exceptions.TypeError("'" + other.typeName() + "' object is not iterable");
        }
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
            __doc__ = "Return True if the set has no elements in common with other. Sets are disjoint if and only if their intersection is the empty set.",
            default_args = {"other"}
    )
    public org.python.Object isdisjoint(org.python.Object other) {
        if (other == null) {
            throw new org.python.exceptions.TypeError("isdisjoint() takes exactly one argument (0 given)");
        }
        java.util.Set<org.python.Object> intersection = new java.util.HashSet<org.python.Object>(this.value);
        try {
            if (other instanceof org.python.types.Set) {
                intersection.retainAll(((org.python.types.Set) other).value);
            } else {
                org.python.types.Set otherSet = null;
                otherSet = new org.python.types.Set(new org.python.Object[] {other}, null);
                intersection.retainAll(((org.python.types.Set) otherSet).value);
            }
        } catch (org.python.exceptions.AttributeError e) {
            throw new org.python.exceptions.TypeError("'" + other.typeName() + "' object is not iterable");
        }
        if (intersection.size() == 0) {
            return new org.python.types.Bool(true);
        }
        return new org.python.types.Bool(false);
    }

    @org.python.Method(
            __doc__ = "Test whether every element in the set is in other.",
            default_args = {"other"}
    )
    public org.python.Object issubset(org.python.Object other) {
        try {
            org.python.types.Set otherSet = null;
            if (other instanceof org.python.types.Set) {
                otherSet = (org.python.types.Set) other;
            } else {
                otherSet = new org.python.types.Set(new org.python.Object[] {other}, null);
            }
            return this.__le__(otherSet);
        } catch (org.python.exceptions.AttributeError e) {
            throw new org.python.exceptions.TypeError("'" + other.typeName() + "' object is not iterable");
        }
    }

    @org.python.Method(
            __doc__ = "Test whether every element in other is in the set.",
            default_args = {"other"}
    )
    public org.python.Object issuperset(org.python.Object other) {
        try {
            org.python.types.Set otherSet = null;
            if (other instanceof org.python.types.Set) {
                otherSet = (org.python.types.Set) other;
            } else {
                otherSet = new org.python.types.Set(new org.python.Object[] {other}, null);
            }
            return this.__ge__(otherSet);
        } catch (org.python.exceptions.AttributeError e) {
            throw new org.python.exceptions.TypeError("'" + other.typeName() + "' object is not iterable");
        }
    }

    @org.python.Method(
            __doc__ = "Remove and return an arbitrary set element.\nRaises KeyError if the set is empty.",
            args = {}
    )
    public org.python.Object pop() {
        if (this.value.size() == 0) {
            throw new org.python.exceptions.KeyError(new org.python.types.Str("pop from an empty set"));
        }

        java.util.Iterator<org.python.Object> iterator = this.value.iterator();
        org.python.Object popped = iterator.next();
        iterator.remove();

        return popped;
    }

    @org.python.Method(
            __doc__ = "Remove an element from a set; it must be a member.\n\nIf the element is not a member, raise a KeyError.",
            args = {"item"}
    )
    public org.python.Object remove(org.python.Object item) {
        if (!this.value.remove(item)) {
            throw new org.python.exceptions.KeyError(item);
        }
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
            __doc__ = "Return a new set with elements in either the set or other but not both.",
            default_args = {"other"}
    )
    public org.python.Object symmetric_difference(org.python.Object other) {
        if (other == null) {
            throw new org.python.exceptions.TypeError("symmetric_difference() takes exactly one argument (0 given)");
        }
        Set union = (Set) (this.union(other));
        Set intersection = (Set) (this.intersection(other));
        return union.difference(intersection);
    }

    @org.python.Method(
            __doc__ = "Update the set, keeping only elements found in either set, but not in both.",
            default_args = {"other"}
    )
    public org.python.Object symmetric_difference_update(org.python.Object other) {
        if (other == null) {
            throw new org.python.exceptions.TypeError("symmetric_difference_update() takes exactly one argument (0 given)");
        }
        Set union = (Set) (this.union(other));
        Set intersection = (Set) (this.intersection(other));
        union = (Set) union.difference(intersection);
        this.value = union.value;
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
            __doc__ = "Return the union of sets as a new set.\n\n(i.e. all elements that are in either set.)",
            args = {"other"}
    )
    public org.python.Object union(org.python.Object other) {
        java.util.Set set = ((Set) this.copy()).value;
        try {
            set.addAll(((Set) other).value);
        } catch (ClassCastException te) {
            throw new org.python.exceptions.TypeError("'" + other.typeName() + "' object is not iterable");
        }
        return new Set(set);
    }

    @org.python.Method(
            __doc__ = "Update a set with the union of itself and others.",
            args = {"other"}
    )
    public org.python.Object update(org.python.Object other) {
        this.value.addAll(((Set) other).value);
        return org.python.types.NoneType.NONE;
    }
}
