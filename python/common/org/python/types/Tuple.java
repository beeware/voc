package org.python.types;

public class Tuple extends org.python.types.Object {
    public java.util.List<org.python.Object> value;

    /**
     * A utility method to update the internal value of this object.
     * <p>
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Tuple
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.Tuple) obj).value;
    }

    public java.lang.Object toJava() {
        return this.value;
    }

    public int hashCode() {
        return this.value.hashCode();
    }

    public Tuple() {
        super();
        this.value = new java.util.ArrayList<org.python.Object>();
    }

    public Tuple(java.util.List<org.python.Object> tuple) {
        super();
        this.value = tuple;
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("__new__() has not been implemented.");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("__init__() has not been implemented.");
    // }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        java.lang.StringBuilder buffer = new java.lang.StringBuilder("(");
        boolean first = true;
        for (org.python.Object obj : this.value) {
            if (first) {
                first = false;
            } else {
                buffer.append(", ");
            }
            buffer.append(obj.__repr__());
        }
        buffer.append(")");
        return new org.python.types.Str(buffer.toString());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __format__(org.python.Object format_string) {
        throw new org.python.exceptions.NotImplementedError("__format__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary +: 'tuple'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: 'tuple'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'tuple'");
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __bool__() {
        return new org.python.types.Bool(!this.value.isEmpty());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __lt__(org.python.Object other) {
        if (other instanceof org.python.types.Tuple) {
            org.python.types.Tuple otherTuple = (org.python.types.Tuple) other;
            int size = this.value.size();
            int otherSize = otherTuple.value.size();
            int count = Math.min(size, otherSize);

            boolean cmp = false;
            for (int i = 0; i < count; i++) {
                org.python.types.Bool b =
                    (org.python.types.Bool) this.value.get(i).__lt__(otherTuple.value.get(i));

                cmp = cmp & b.value;
            }

            if (cmp) {
                return new org.python.types.Bool(cmp);
            }

            // At this point the lists are different sizes or every comparison is true.
            return new org.python.types.Bool(size < otherSize);

        } else {
            throw new org.python.exceptions.TypeError(
                String.format("unorderable types: tuple() < %s()",
                    org.Python.typeName(other.getClass())));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __le__(org.python.Object other) {
        if (other instanceof org.python.types.Tuple) {
            org.python.types.Tuple otherTuple = (org.python.types.Tuple) other;
            int size = this.value.size();
            int otherSize = otherTuple.value.size();
            int count = Math.min(size, otherSize);

            boolean cmp = false;
            for (int i = 0; i < count; i++) {
                org.python.types.Bool b =
                    (org.python.types.Bool) this.value.get(i).__le__(otherTuple.value.get(i));

                cmp = cmp & b.value;
            }

            if (cmp) {
                return new org.python.types.Bool(cmp);
            }

            // At this point the lists are different sizes or every comparison is true.
            return new org.python.types.Bool(size <= otherSize);

        } else {
            throw new org.python.exceptions.TypeError(
                String.format("unorderable types: tuple() <= %s()",
                    org.Python.typeName(other.getClass())));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __eq__(org.python.Object other) {
        boolean eq = false;
        if (other instanceof org.python.types.Tuple) {
            org.python.types.Tuple otherTuple = (org.python.types.Tuple) other;
            eq = this.value.equals(otherTuple.value);
        }
        return new org.python.types.Bool(eq);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ne__(org.python.Object other) {
        return new org.python.types.Bool(!((org.python.types.Bool) this.__eq__(other)).value);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __gt__(org.python.Object other) {
        if (other instanceof org.python.types.Tuple) {
            org.python.types.Tuple otherTuple = (org.python.types.Tuple) other;
            int size = this.value.size();
            int otherSize = otherTuple.value.size();
            int count = Math.min(size, otherSize);

            boolean cmp = true;
            for (int i = 0; i < count; i++) {
                org.python.types.Bool b =
                    (org.python.types.Bool) this.value.get(i).__gt__(otherTuple.value.get(i));

                cmp = cmp & b.value;
            }
            if (!cmp) {
                return new org.python.types.Bool(cmp);
            }

            // At this point the lists are different sizes or every comparison is true.
            return new org.python.types.Bool(size > otherSize);

        } else {
            throw new org.python.exceptions.TypeError(
                String.format("unorderable types: tuple() > %s()",
                    org.Python.typeName(other.getClass())));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ge__(org.python.Object other) {
        if (other instanceof org.python.types.Tuple) {
            org.python.types.Tuple otherTuple = (org.python.types.Tuple) other;
            int size = this.value.size();
            int otherSize = otherTuple.value.size();
            int count = Math.min(size, otherSize);

            boolean cmp = true;
            for (int i = 0; i < count; i++) {
                org.python.types.Bool b =
                    (org.python.types.Bool) this.value.get(i).__ge__(otherTuple.value.get(i));

                cmp = cmp & b.value;
            }

            if (!cmp) {
                return new org.python.types.Bool(cmp);
            }

            // At this point the lists are different sizes or every comparison is true.
            return new org.python.types.Bool(size >= otherSize);

        } else {
            throw new org.python.exceptions.TypeError(
                String.format("unorderable types: tuple() >= %s()",
                    org.Python.typeName(other.getClass())));
        }
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // Builtin types can't have attributes set on them.
        return false;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("__dir__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Int __len__() {
        throw new org.python.exceptions.NotImplementedError("__len__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getitem__(org.python.Object index) {
        try {
            if (index instanceof org.python.types.Slice) {
                org.python.types.Slice slice = (org.python.types.Slice) index;
                java.util.List<org.python.Object> sliced = new java.util.ArrayList<org.python.Object>();

                if (slice.start == null && slice.stop == null && slice.step == null) {
                    sliced.addAll(this.value);
                } else {
                    long start;
                    if (slice.start != null) {
                        start = slice.start.value;
                    } else {
                        start = 0;
                    }

                    long stop;
                    if (slice.stop != null) {
                        stop = slice.stop.value;
                    } else {
                        stop = this.value.size();
                    }

                    long step;
                    if (slice.step != null) {
                        step = slice.step.value;
                    } else {
                        step = 1;
                    }

                    for (long i = start; i < stop; i += step) {
                        sliced.add(this.value.get((int) i));
                    }
                }
                return new org.python.types.Tuple(sliced);

            } else {
                int idx = (int) ((org.python.types.Int) index).value;
                if (idx < 0) {
                    if (-idx > this.value.size()) {
                        throw new org.python.exceptions.IndexError("tuple index out of range");
                    } else {
                        return this.value.get(this.value.size() + idx);
                    }
                } else {
                    if (idx >= this.value.size()) {
                        throw new org.python.exceptions.IndexError("tuple index out of range");
                    } else {
                        return this.value.get(idx);
                    }
                }
            }
        } catch (ClassCastException e) {
            throw new org.python.exceptions.TypeError("tuple indices must be integers, not " + index.typeName());
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __setitem__(org.python.Object index, org.python.Object value) {
        try {
            int idx = (int) ((org.python.types.Int) index).value;
            if (idx < 0) {
                if (-idx > this.value.size()) {
                    throw new org.python.exceptions.IndexError("tuple index out of range");
                } else {
                    this.value.set(this.value.size() + idx, value);
                }
            } else {
                if (idx >= this.value.size()) {
                    throw new org.python.exceptions.IndexError("tuple index out of range");
                } else {
                    this.value.set(idx, value);
                }
            }
        } catch (ClassCastException e) {
            throw new org.python.exceptions.TypeError("tuple indices must be integers, not " + index.typeName());
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __delitem__(org.python.Object item) {
        throw new org.python.exceptions.TypeError("'tuple' object doesn't support item deletion");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Iterable __iter__() {
        return new org.python.types.Iterator(this);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __contains__(org.python.Object item) {
        throw new org.python.exceptions.NotImplementedError("__contains__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __add__(org.python.Object other) {
        if (other instanceof org.python.types.Tuple) {
            org.python.types.Tuple result = new org.python.types.Tuple();
            result.value.addAll(this.value);
            result.value.addAll(((org.python.types.Tuple) other).value);
            return result;
        } else {
            throw new org.python.exceptions.TypeError(
                String.format("can only concatenate tuple (not \"%s\") to tuple", org.Python.typeName(other.getClass())));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            long count = ((org.python.types.Int) other).value;
            org.python.types.Tuple result = new org.python.types.Tuple();
            for (long i = 0; i < count; i++) {
                result.value.addAll(this.value);
            }
            return result;
        } else if (other instanceof org.python.types.Bool) {
            boolean count = ((org.python.types.Bool) other).value;
            org.python.types.Tuple result = new org.python.types.Tuple();
            if (count) {
                result.value.addAll(this.value);
            }
            return result;
        }
        throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rmul__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("__rmul__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object count() {
        return new org.python.types.Int(this.value.size());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __iadd__(org.python.Object other) {
        if (other instanceof org.python.types.Tuple) {
            this.value.addAll(((org.python.types.Tuple) other).value);
            return this;
        } else {
            throw new org.python.exceptions.TypeError(
                String.format("can only concatenate tuple (not \"%s\") to tuple", org.Python.typeName(other.getClass())));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object index(org.python.Object item, org.python.Object start, org.python.Object end) {
        throw new org.python.exceptions.NotImplementedError("tuple.index() has not been implemented.");
    }
    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __round__(org.python.Object ndigits) {
           
         throw new org.python.exceptions.TypeError("type tuple doesn't define __round__ method");    
        
    }
}
