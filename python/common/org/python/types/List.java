package org.python.types;

import org.Python;

import java.util.Collections;
import java.util.Comparator;

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
        } else if (other instanceof org.python.types.Tuple) {
	    this.value.addAll(((org.python.types.Tuple) other).value);
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
                        start = Math.min(slice.start.value, this.value.size());
                    } else {
                        start = 0;
                    }

                    long stop;
                    if (slice.stop != null) {
                        stop = Math.min(slice.stop.value, this.value.size());
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
            if (org.Python.VERSION < 30500) {
                throw new org.python.exceptions.TypeError("list indices must be integers");
            } else {
                throw new org.python.exceptions.TypeError(
                    "list indices must be integers or slices, not " + index.typeName()
                );
            }
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
                    throw new org.python.exceptions.IndexError("list assignment index out of range");
                } else {
                    this.value.set(this.value.size() + idx, value);
                }
            } else {
                if (idx >= this.value.size()) {
                    throw new org.python.exceptions.IndexError("list assignment index out of range");
                } else {
                    this.value.set(idx, value);
                }
            }
        } catch (ClassCastException e) {
            if (org.Python.VERSION < 30500) {
                throw new org.python.exceptions.TypeError("list indices must be integers");
            } else {
                throw new org.python.exceptions.TypeError(
                    "list indices must be integers or slices, not " + index.typeName()
                );
            }
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
            if (org.Python.VERSION < 30500) {
                throw new org.python.exceptions.TypeError("list indices must be integers");
            } else {
                throw new org.python.exceptions.TypeError(
                    "list indices must be integers or slices, not " + index.typeName()
                );
            }
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
        boolean found = false;
        int len = (int) this.__len__().value;
        for(int i=0;i<len;i++) {
            if(((org.python.types.Bool)item.__eq__(this.value.get(i))).value){
                found = true;
                break;
            }
        }
        return new org.python.types.Bool(found);
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
    public org.python.Object __imul__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            long count = ((org.python.types.Int) other).value;
            org.python.types.List result = new org.python.types.List();
            for (long i = 0; i < count; i++) {
                result.value.addAll(this.value);
            }
            return result;
        } else if (other instanceof org.python.types.Bool) {
            boolean bool = ((org.python.types.Bool) other).value;
            if (bool) {
                return this;
            }
            else {
                return new org.python.types.List();
            }
        }
        else {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + other.typeName() + "'");
        }
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
        __doc__ = "L.copy() -> list -- a shallow copy of L"
    )
    public org.python.Object copy() {
        return new org.python.types.List(new java.util.ArrayList<org.python.Object>(this.value));
    }

    @org.python.Method(
        __doc__ = "",
        args = {"other"}
    )
    public org.python.Object count(org.python.Object other) {
        int count = 0;
        int len = (int) this.__len__().value;
        for(int i=0;i<len;i++) {
            if(((org.python.types.Bool)other.__eq__(this.value.get(i))).value){
                count++;
            }
        }
        return new org.python.types.Int(count);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object extend(org.python.Object other) {
        return org.python.types.NoneType.NONE;
    }

    private int toPositiveIndex(int index) {
        if (index < 0) {
            return this.value.size() + index;
        }
        return index;
    }

    @org.python.Method(
        __doc__ = "L.index(value, [start, [stop]]) -> integer -- return first index of value.\nRaises ValueError if the value is not present.",
        args = {"item"},
        default_args = {"start", "end"}
    )
    public org.python.Object index(org.python.Object item, org.python.Object start, org.python.Object end) {
        if (start != null && !(start instanceof org.python.types.Int)) {
            if (org.Python.VERSION < 30500) {
                throw new org.python.exceptions.TypeError("list indices must be integers");
            } else {
                throw new org.python.exceptions.TypeError(
                    "list indices must be integers or slices, not " + start.typeName()
                );
            }
        }
        if (end != null && !(end instanceof org.python.types.Int)) {
            if (org.Python.VERSION < 30500) {
                throw new org.python.exceptions.TypeError("list indices must be integers");
            } else {
                throw new org.python.exceptions.TypeError(
                    "list indices must be integers or slices, not " + end.typeName()
                );
            }
        }

        int iStart = 0, iEnd = this.value.size();
        if (end != null) {
            iEnd = toPositiveIndex(((Long) end.toJava()).intValue());
        }
        if (start != null) {
            iStart = toPositiveIndex(((Long) start.toJava()).intValue());
        }

        for (int i = iStart; i < Math.min(iEnd, this.value.size()); i++) {
            if (((org.python.types.Bool) this.value.get(i).__eq__(item)).value) {
                return new org.python.types.Int(i);
            }
        }
        throw new org.python.exceptions.ValueError(String.format("%d is not in list",  ((org.python.types.Int)item).value));
    }

    @org.python.Method(
        __doc__ = "L.pop([index]) -> item -- remove and return item at index (default last).",
        default_args = {"item"}
    )
    public org.python.Object pop(org.python.Object item) {
        int index = this.value.size() - 1;
        if (item != null) {
            index = ((Long) ((org.python.types.Int) item).toJava()).intValue();
            if (index < 0) {
                index = this.value.size() + index;
            }
        }
        if (this.value.isEmpty()) {
            throw new org.python.exceptions.IndexError("pop from empty list");
        } else if (index < 0 || index >= this.value.size()) {
            throw new org.python.exceptions.IndexError("pop index out of range");
        }
        return this.value.remove(index);
    }

    @org.python.Method(
        __doc__ = "",
        args = {"item"}
    )
    public org.python.Object remove(org.python.Object item) {
        for(int i = 0; i < this.value.size(); i++) {
            if(((org.python.types.Bool)item.__eq__(this.value.get(i))).value){
                this.value.remove(i);
                return org.python.types.NoneType.NONE;
            }
        }
        throw new org.python.exceptions.ValueError("list.remove(x): x not in list");
    }

    @org.python.Method(
        __doc__ = "L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*",
        args = {},
        default_args = {"key", "reverse"}
    )
    public org.python.Object sort(final org.python.Object key, org.python.Object reverse) {
        if (key == null && reverse == null) {
            Collections.sort(this.value);
        } else {
            // needs to be final in order to use inside the comparator
            final boolean shouldReverse = reverse == null ? false :
                ((org.python.types.Bool) reverse.__bool__()).value;

            Collections.sort(this.value, new Comparator<org.python.Object>() {
                @Override
                public int compare(org.python.Object o1, org.python.Object o2) {
                    org.python.Object val1 = o1;
                    org.python.Object val2 = o2;
                    if (key != null) {
                        val1 = ((org.python.types.Function) key).invoke(o1, null, null);
                        val2 = ((org.python.types.Function) key).invoke(o2, null, null);
                    }
                    return shouldReverse ? val2.compareTo(val1) : val1.compareTo(val2);
                }
            });
        }
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __round__(org.python.Object ndigits) {
        throw new org.python.exceptions.TypeError("type list doesn't define __round__ method");
    }
}
