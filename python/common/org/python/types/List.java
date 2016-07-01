package org.python.types;

import org.Python;

public class List extends org.python.types.Object {
    public java.util.List<org.python.Object> value;

    /**
     * A utility method to update the internal value of this object.
     * <p>
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.List
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.List) obj).value;
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

    public List() {
        super();
        this.value = new java.util.ArrayList<org.python.Object>();
    }

    public List(java.util.List<org.python.Object> list) {
        super();
        this.value = list;
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("list.__new__() has not been implemented.");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("list.__init__() has not been implemented.");
    // }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary +: 'list'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: 'list'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __iadd__(org.python.Object other) {
        if (other instanceof org.python.types.List) {
            this.value.addAll(((org.python.types.List) other).value);
            return this;
        } else {
            throw new org.python.exceptions.TypeError(
                String.format("'%s' object is not iterable", Python.typeName(other.getClass())));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'list'");
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
    public org.python.types.Str __repr__() {
        java.lang.StringBuilder buffer = new java.lang.StringBuilder("[");
        boolean first = true;
        for (org.python.Object obj : this.value) {
            if (first) {
                first = false;
            } else {
                buffer.append(", ");
            }
            buffer.append(obj.__repr__());
        }
        buffer.append("]");
        return new org.python.types.Str(buffer.toString());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __format__() {
        throw new org.python.exceptions.NotImplementedError("list.__format__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __lt__(org.python.Object other) {
        if (other instanceof org.python.types.List) {
            org.python.types.List otherList = (org.python.types.List) other;
            int size = this.value.size();
            int otherSize = otherList.value.size();
            int count = Math.min(size, otherSize);

            for (int i = 0; i < count; i++) {
                org.python.types.Bool b =
                    (org.python.types.Bool) this.value.get(i).__lt__(otherList.value.get(i));

                if (b.value) {
                    return b;
                }
            }

            // At this point the lists are different sizes or every comparison is true.
            return new org.python.types.Bool(size < otherSize);

        } else {
            throw new org.python.exceptions.TypeError(
                String.format("unorderable types: list() < %s()",
                    Python.typeName(other.getClass())));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __le__(org.python.Object other) {
        if (other instanceof org.python.types.List) {
            org.python.types.List otherList = (org.python.types.List) other;
            int size = this.value.size();
            int otherSize = otherList.value.size();
            int count = Math.min(size, otherSize);

            for (int i = 0; i < count; i++) {
                org.python.types.Bool b =
                    (org.python.types.Bool) this.value.get(i).__le__(otherList.value.get(i));

                if (b.value) {
                    return b;
                }
            }

            // At this point the lists are different sizes or every comparison is true.
            return new org.python.types.Bool(size <= otherSize);

        } else {
            throw new org.python.exceptions.TypeError(
                String.format("unorderable types: list() <= %s()",
                    Python.typeName(other.getClass())));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __eq__(org.python.Object other) {
        boolean eq = false;
        if (other instanceof org.python.types.List) {
            org.python.types.List otherList = (org.python.types.List) other;
            eq = this.value.equals(otherList.value);
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
        if (other instanceof org.python.types.List) {
            org.python.types.List otherList = (org.python.types.List) other;
            int size = this.value.size();
            int otherSize = otherList.value.size();
            int count = Math.min(size, otherSize);

            for (int i = 0; i < count; i++) {
                org.python.types.Bool b =
                    (org.python.types.Bool) this.value.get(i).__gt__(otherList.value.get(i));

                if (!b.value) {
                    return b;
                }
            }

            // At this point the lists are different sizes or every comparison is true.
            return new org.python.types.Bool(size > otherSize);

        } else {
            throw new org.python.exceptions.TypeError(
                String.format("unorderable types: list() > %s()",
                    Python.typeName(other.getClass())));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ge__(org.python.Object other) {
        if (other instanceof org.python.types.List) {
            org.python.types.List otherList = (org.python.types.List) other;
            int size = this.value.size();
            int otherSize = otherList.value.size();
            int count = Math.min(size, otherSize);

            for (int i = 0; i < count; i++) {
                org.python.types.Bool b =
                    (org.python.types.Bool) this.value.get(i).__ge__(otherList.value.get(i));

                if (!b.value) {
                    return b;
                }
            }

            // At this point the lists are different sizes or every comparison is true.
            return new org.python.types.Bool(size >= otherSize);

        } else {
            throw new org.python.exceptions.TypeError(
                String.format("unorderable types: list() >= %s()",
                    Python.typeName(other.getClass())));
        }
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // Builtin types can't have attributes set on them.
        return false;
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
                return new org.python.types.List(sliced);

            } else {
                int idx = (int) ((org.python.types.Int) index).value;
                if (idx < 0) {
                    if (-idx > this.value.size()) {
                        throw new org.python.exceptions.IndexError("list index out of range");
                    } else {
                        return this.value.get(this.value.size() + idx);
                    }
                } else {
                    if (idx >= this.value.size()) {
                        throw new org.python.exceptions.IndexError("list index out of range");
                    } else {
                        return this.value.get(idx);
                    }
                }
            }
        } catch (ClassCastException e) {
            throw new org.python.exceptions.TypeError("list indices must be integers, not " + index.typeName());
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
                    throw new org.python.exceptions.IndexError("list index out of range");
                } else {
                    this.value.set(this.value.size() + idx, value);
                }
            } else {
                if (idx >= this.value.size()) {
                    throw new org.python.exceptions.IndexError("list index out of range");
                } else {
                    this.value.set(idx, value);
                }
            }
        } catch (ClassCastException e) {
            throw new org.python.exceptions.TypeError("list indices must be integers, not " + index.typeName());
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __delitem__(org.python.Object index) {
        try {
            int idx = (int) ((org.python.types.Int) index).value;
            if (idx < 0) {
                if (-idx > this.value.size()) {
                    throw new org.python.exceptions.IndexError("list index out of range");
                } else {
                    this.value.remove(this.value.size() + idx);
                }
            } else {
                if (idx >= this.value.size()) {
                    throw new org.python.exceptions.IndexError("list index out of range");
                } else {
                    this.value.remove(idx);
                }
            }
        } catch (ClassCastException e) {
            throw new org.python.exceptions.TypeError("list indices must be integers, not " + index.typeName());
        }
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
    public org.python.Iterable __reversed__() {
        throw new org.python.exceptions.NotImplementedError("list.__reversed__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __contains__(org.python.Object item) {
        throw new org.python.exceptions.NotImplementedError("list.__contains__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __add__(org.python.Object other) {
        if (other instanceof org.python.types.List) {
            org.python.types.List result = new org.python.types.List();
            result.value.addAll(this.value);
            result.value.addAll(((org.python.types.List) other).value);
            return result;
        } else {
            throw new org.python.exceptions.TypeError(
                String.format("can only concatenate list (not \"%s\") to list", Python.typeName(other.getClass())));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            long count = ((org.python.types.Int) other).value;
            org.python.types.List result = new org.python.types.List();
            for (long i = 0; i < count; i++) {
                result.value.addAll(this.value);
            }
            return result;
        } else if (other instanceof org.python.types.Bool) {
            boolean count = ((org.python.types.Bool) other).value;
            org.python.types.List result = new org.python.types.List();
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
        throw new org.python.exceptions.NotImplementedError("list.__rmul__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = "",
        args = {"item"}
    )
    public org.python.Object append(org.python.Object item) {
        this.value.add(item);
        return org.python.types.NoneType.NONE;
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
        throw new org.python.exceptions.NotImplementedError("list.copy() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object count() {
        throw new org.python.exceptions.NotImplementedError("list.count() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object extend(org.python.Object other) {
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object index(org.python.Object item, org.python.Object start, org.python.Object end) {
        if (start != null && !(start instanceof org.python.types.Int)) {
            throw new org.python.exceptions.TypeError("list indices must be integers, not " + start.typeName());
        }

        if (end != null && !(end instanceof org.python.types.Int)) {
            throw new org.python.exceptions.TypeError("list indices must be integers, not " + end.typeName());
        }

        throw new org.python.exceptions.NotImplementedError("list.index() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object pop(org.python.Object item) {
        throw new org.python.exceptions.NotImplementedError("list.pop() has not been implemented.");
    }

    public void remove(org.python.Object item) {
        throw new org.python.exceptions.NotImplementedError("list.remove() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object sort() {
        throw new org.python.exceptions.NotImplementedError("list.sort() has not been implemented.");
    }
    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __round__(org.python.Object ndigits) {

         throw new org.python.exceptions.TypeError("type list doesn't define __round__ method");

    }
}
