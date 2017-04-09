package org.python.types;

public class FrozenSet extends org.python.types.Object {
    public java.util.Set<org.python.Object> value;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Set
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.FrozenSet) obj).value;
    }

    public java.lang.Object toJava() {
        return this.value;
    }

    public int hashCode() {
        return this.value.hashCode();
    }

    public FrozenSet() {
        super();
        this.value = java.util.Collections.emptySet();
    }

    public FrozenSet(java.util.Set<org.python.Object> frozenSet) {
        super();
        this.value = java.util.Collections.unmodifiableSet(frozenSet);
    }

    @org.python.Method(
            __doc__ = "frozenset() -> empty frozenset object" +
                    "frozenset(iterable) -> frozenset object\n" +
                    "\n" +
                    "Build an immutable unordered collection of unique elements.\n",
            default_args = {"iterable"}
    )
    public FrozenSet(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args[0] == null) {
            this.value = java.util.Collections.emptySet();
        } else {
            if (args[0] instanceof org.python.types.Set) {
                this.value = java.util.Collections.unmodifiableSet(
                        ((org.python.types.Set) args[0]).value
                );
            } else if (args[0] instanceof org.python.types.List) {
                this.value = java.util.Collections.unmodifiableSet(
                        new java.util.HashSet<org.python.Object>(
                        ((org.python.types.List) args[0]).value)
                );
            } else if (args[0] instanceof org.python.types.Tuple) {
                this.value = java.util.Collections.unmodifiableSet(
                        new java.util.HashSet<org.python.Object>(
                        ((org.python.types.Tuple) args[0]).value)
                );
            } else {
                org.python.Iterable iterator = org.Python.iter(args[0]);
                java.util.Set<org.python.Object> generated = new java.util.HashSet<org.python.Object>();
                try {
                    while (true) {
                        org.python.Object next = iterator.__next__();
                        generated.add(next);
                    }
                } catch (org.python.exceptions.StopIteration si) {
                }
                this.value = java.util.Collections.unmodifiableSet(generated);
            }
        }
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'frozenset'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Iterable __iter__() {
        return new org.python.types.Set_Iterator(this);
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary +: 'frozenset'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: 'frozenset'");
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
    public org.python.types.Str __repr__() {
        // Representation of an empty set is different
        if (this.value.size() == 0) {
            return new org.python.types.Str("frozenset()");
        }

        java.lang.StringBuilder buffer = new java.lang.StringBuilder("frozenset({");
        boolean first = true;
        for (org.python.Object obj : this.value) {
            if (first) {
                first = false;
            } else {
                buffer.append(", ");
            }
            buffer.append(obj.__repr__());
        }
        buffer.append("})");
        return new org.python.types.Str(buffer.toString());
    }


    @org.python.Method(
            __doc__ = ""
    )
    public org.python.types.Int __len__() {
        return new org.python.types.Int(this.value.size());
    }

    @org.python.Method(
            __doc__ = "",
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
            __doc__ = "Return a shallow copy of a FrozenSet."
    )
    public org.python.Object copy() {
        return this;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        if (other instanceof org.python.types.FrozenSet) {
            org.python.types.FrozenSet otherSet = (org.python.types.FrozenSet) other;
            return new org.python.types.Bool(otherSet.value.containsAll(this.value) && !this.value.equals(otherSet.value));
        } else if (other instanceof org.python.types.Set) {
            org.python.types.Set otherSet = (org.python.types.Set) other;
            return new org.python.types.Bool(otherSet.value.containsAll(this.value) && !this.value.equals(otherSet.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        if (other instanceof org.python.types.FrozenSet) {
            org.python.types.FrozenSet otherSet = (org.python.types.FrozenSet) other;
            return new org.python.types.Bool(otherSet.value.containsAll(this.value));
        } else if (other instanceof org.python.types.Set) {
            org.python.types.Set otherSet = (org.python.types.Set) other;
            return new org.python.types.Bool(otherSet.value.containsAll(this.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.FrozenSet) {
            org.python.types.FrozenSet otherSet = (org.python.types.FrozenSet) other;
            return new org.python.types.Bool(this.value.equals(otherSet.value));
        } else if (other instanceof org.python.types.Set) {
            org.python.types.Set otherSet = (org.python.types.Set) other;
            return new org.python.types.Bool(this.value.equals(otherSet.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        if (other instanceof org.python.types.FrozenSet) {
            org.python.types.FrozenSet otherSet = (org.python.types.FrozenSet) other;
            return new org.python.types.Bool(this.value.containsAll(otherSet.value) && !this.value.equals(otherSet.value));
        } else if (other instanceof org.python.types.Set) {
            org.python.types.Set otherSet = (org.python.types.Set) other;
            return new org.python.types.Bool(this.value.containsAll(otherSet.value) && !this.value.equals(otherSet.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        if (other instanceof org.python.types.FrozenSet) {
            org.python.types.FrozenSet otherSet = (org.python.types.FrozenSet) other;
            return new org.python.types.Bool(this.value.containsAll(otherSet.value));
        } else if (other instanceof org.python.types.Set) {
            org.python.types.Set otherSet = (org.python.types.Set) other;
            return new org.python.types.Bool(this.value.containsAll(otherSet.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }


    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __sub__(org.python.Object other) {
        java.util.Set frozenSet = new java.util.HashSet<org.python.Object>(this.value);
        if (other instanceof org.python.types.FrozenSet) {
            frozenSet.removeAll(((org.python.types.FrozenSet) other).value);
            return new org.python.types.FrozenSet(frozenSet);
        } else if (other instanceof org.python.types.Set) {
            frozenSet.removeAll(((org.python.types.Set) other).value);
            return new org.python.types.FrozenSet(frozenSet);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for -: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.List ||
                other instanceof org.python.types.Tuple ||
                other instanceof org.python.types.Str ||
                other instanceof org.python.types.Bytes ||
                other instanceof org.python.types.ByteArray
            ) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + this.typeName() + "'");
        }
        return super.__mul__(other);
    }
}
