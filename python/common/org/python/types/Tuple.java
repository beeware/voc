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

    @org.python.Method(
            __doc__ = "tuple() -> empty tuple" +
                    "tuple(iterable) -> tuple initialized from iterable's items\n" +
                    "\n" +
                    "If the argument is a tuple, the return value is the same object.\n"
    )
    public Tuple(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'tuple' not implemented");
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
        if (this.value.size() == 1) {
            buffer.append(",");
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
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        if (other instanceof org.python.types.Tuple) {
            org.python.types.Tuple otherTuple = (org.python.types.Tuple) other;
            int size = this.value.size();
            int otherSize = otherTuple.value.size();
            int count = Math.min(size, otherSize);

            // check how many items are identical on the lists
            int i = 0;
            for (i = 0; i < count; i++) {
                org.python.types.Bool result = (org.python.types.Bool) org.python.types.Object.__cmp_bool__(
                        this.value.get(i), otherTuple.value.get(i), org.python.types.Object.CMP_OP.EQ);
                if (!result.value) {
                    break;
                }
            }

            // not all items were identical, result is that of the first non-identical item
            if (i < count) {
                return org.python.types.Object.__cmp_bool__(this.value.get(i), otherTuple.value.get(i),
                        org.python.types.Object.CMP_OP.LT);
            }

            // all items were identical, break tie by size
            return new org.python.types.Bool(size < otherSize);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        if (other instanceof org.python.types.Tuple) {
            org.python.types.Tuple otherTuple = (org.python.types.Tuple) other;
            int size = this.value.size();
            int otherSize = otherTuple.value.size();
            int count = Math.min(size, otherSize);

            // check how many items are identical on the lists
            int i = 0;
            for (i = 0; i < count; i++) {
                org.python.types.Bool result = (org.python.types.Bool) org.python.types.Object.__cmp_bool__(
                        this.value.get(i), otherTuple.value.get(i), org.python.types.Object.CMP_OP.EQ);
                if (!result.value) {
                    break;
                }
            }

            // not all items were identical, result is that of the first non-identical item
            if (i < count) {
                return org.python.types.Object.__cmp_bool__(this.value.get(i), otherTuple.value.get(i),
                        org.python.types.Object.CMP_OP.LE);
            }

            // all items were identical, break tie by size
            return new org.python.types.Bool(size <= otherSize);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.Tuple) {
            org.python.types.Tuple otherTuple = (org.python.types.Tuple) other;
            return new org.python.types.Bool(this.value.equals(otherTuple.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        if (other instanceof org.python.types.Tuple) {
            org.python.types.Tuple otherTuple = (org.python.types.Tuple) other;
            int size = this.value.size();
            int otherSize = otherTuple.value.size();
            int count = Math.min(size, otherSize);

            // check how many items are identical on the lists
            int i = 0;
            for (i = 0; i < count; i++) {
                org.python.types.Bool result = (org.python.types.Bool) org.python.types.Object.__cmp_bool__(
                        this.value.get(i), otherTuple.value.get(i), org.python.types.Object.CMP_OP.EQ);
                if (!result.value) {
                    break;
                }
            }

            // not all items were identical, result is that of the first non-identical item
            if (i < count) {
                return org.python.types.Object.__cmp_bool__(this.value.get(i), otherTuple.value.get(i),
                        org.python.types.Object.CMP_OP.GT);
            }

            // all items were identical, break tie by size
            return new org.python.types.Bool(size > otherSize);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        if (other instanceof org.python.types.Tuple) {
            org.python.types.Tuple otherTuple = (org.python.types.Tuple) other;
            int size = this.value.size();
            int otherSize = otherTuple.value.size();
            int count = Math.min(size, otherSize);

            // check how many items are identical on the lists
            int i = 0;
            for (i = 0; i < count; i++) {
                org.python.types.Bool result = (org.python.types.Bool) org.python.types.Object.__cmp_bool__(
                        this.value.get(i), otherTuple.value.get(i), org.python.types.Object.CMP_OP.EQ);
                if (!result.value) {
                    break;
                }
            }

            // not all items were identical, result is that of the first non-identical item
            if (i < count) {
                return org.python.types.Object.__cmp_bool__(this.value.get(i), otherTuple.value.get(i),
                        org.python.types.Object.CMP_OP.GE);
            }

            // all items were identical, break tie by size
            return new org.python.types.Bool(size >= otherSize);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
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
        return new org.python.types.Int(this.value.size());
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
            if (org.Python.VERSION < 0x03050000) {
                throw new org.python.exceptions.TypeError(
                        "tuple indices must be integers, not " + index.typeName()
                );
            } else {
                throw new org.python.exceptions.TypeError(
                        "tuple indices must be integers or slices, not " + index.typeName()
                );
            }
        }
    }

    @org.python.Method(
            __doc__ = ""
    )
    public void __setitem__(org.python.Object index, org.python.Object value) {
        throw new org.python.exceptions.TypeError(
                "'tuple' object does not support item assignment"
        );
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
        return new org.python.types.Tuple_Iterator(this);
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __contains__(org.python.Object item) {
        return new org.python.types.Bool(this.value.contains(item));
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
            __doc__ = "index of the first occurrence of x in s (at or after index i and before index j)",
            default_args = {"item", "start", "end"}
    )
    public org.python.Object index(org.python.Object item, org.python.Object start, org.python.Object end) {
        if (item == null) {
            throw new org.python.exceptions.TypeError("index() takes at least 1 argument (0 given)");
        }
        long st, en;
        if (start == null || (((org.python.types.Int) start).value + (this.value).size() < 0)) {
            st = 0;
        } else if (((org.python.types.Int) start).value < 0) {
            st = (this.value).size() + ((org.python.types.Int) start).value;
        } else if (((org.python.types.Int) start).value >= (this.value).size()) {
            st = (this.value).size();
        } else {
            st = ((org.python.types.Int) start).value;
        }
        if (end == null || ((org.python.types.Int) end).value >= (this.value).size()) {
            en = (this.value).size();
        } else if ((((org.python.types.Int) end).value + (this.value).size() < 0)) {
            en = 0;
        } else if (((org.python.types.Int) end).value < 0) {
            en = (this.value).size() + ((org.python.types.Int) end).value;
        } else {
            en = ((org.python.types.Int) end).value;
        }
        for (long i = st; i < en; i++) {
            try {
                if (((org.python.types.Bool) ((value.get((int) i)).__eq__(item))).value) {
                    return new org.python.types.Int(i);
                }
            } catch (ClassCastException cce) {
                throw new org.python.exceptions.ValueError("tuple.index(x): x not in tuple");
            }
        }
        throw new org.python.exceptions.ValueError("tuple.index(x): x not in tuple");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __round__(org.python.Object ndigits) {

        throw new org.python.exceptions.TypeError("type tuple doesn't define __round__ method");
    }
}
