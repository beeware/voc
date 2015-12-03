package org.python.types;

public class List extends org.python.types.Object {
    public java.util.List<org.python.Object> value;

    /**
     * A utility method to update the internal value of this object.
     *
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

    public org.python.types.Str __repr__() {
        java.lang.StringBuilder buffer = new java.lang.StringBuilder("[");
        boolean first = true;
        for (org.python.Object obj: this.value) {
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

    public org.python.types.Str __format__() {
        throw new org.python.exceptions.NotImplementedError("list.__format__() has not been implemented.");
    }

    public org.python.Object __lt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__lt__() has not been implemented.");
    }

    public org.python.Object __le__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__le__() has not been implemented.");
    }

    public org.python.Object __eq__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__eq__() has not been implemented.");
    }

    public org.python.Object __ne__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__ne__() has not been implemented.");
    }

    public org.python.Object __gt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__gt__() has not been implemented.");
    }

    public org.python.Object __ge__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__ge__() has not been implemented.");
    }

    public org.python.types.Int __len__() {
        return new org.python.types.Int(this.value.size());
    }

    public org.python.Object __getitem__(org.python.Object index) {
        try {
            if (index instanceof org.python.types.Slice) {
                org.python.types.Slice slice = (org.python.types.Slice) index;
                java.util.List<org.python.Object> sliced = new java.util.ArrayList<org.python.Object>();

                if (slice.start == null && slice.stop == null && slice.step == null) {
                    sliced.addAll(this.value);
                }
                else {
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
                        sliced.add(this.value.get((int)i));
                    }
                }
                return new org.python.types.List(sliced);

            } else {
                int idx = (int)((org.python.types.Int) index).value;
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

    public org.python.Iterable __iter__() {
        return new org.python.types.Iterator(this);
    }

    public org.python.Iterable __reversed__() {
        throw new org.python.exceptions.NotImplementedError("list.__reversed__() has not been implemented.");
    }

    public org.python.Object __contains__(org.python.Object item) {
        throw new org.python.exceptions.NotImplementedError("list.__contains__() has not been implemented.");
    }

    public org.python.Object __add__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__add__() has not been implemented.");
    }

    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            long count = ((org.python.types.Int) other).value;
            org.python.types.List result = new org.python.types.List();
            for (long i = 0; i < count; i++) {
                result.value.addAll(this.value);
            }
            return result;
        }
        else if (other instanceof org.python.types.Bool) {
            boolean count = ((org.python.types.Bool) other).value;
            org.python.types.List result = new org.python.types.List();
            if (count) {
                result.value.addAll(this.value);
            }
            return result;
        }
        throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + other.typeName() + "'");
    }

    public org.python.Object __rmul__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("list.__rmul__() has not been implemented.");
    }

    public org.python.Object append(java.util.List<org.python.Object> args, java.util.HashMap kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("append() takes no keyword arguments");
        }
        if (args != null && args.size() == 1) {
            this.append(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("append() takes exactly 1 argument (" + args.size() + " given)");
        }
        return org.python.types.NoneType.NONE;
    }

    public org.python.Object append(org.python.Object value) {
        this.value.add(value);
        return org.python.types.NoneType.NONE;
    }

    public org.python.Object clear(java.util.List<org.python.Object> args, java.util.HashMap kwargs) {
        if (kwargs != null || kwargs.size() > 0) {
            throw new org.python.exceptions.TypeError("clear() takes no keyword arguments");
        }
        if (args != null || args.size() > 0) {
            throw new org.python.exceptions.TypeError("clear() takes no arguments (" + args.size() + " given)");
        }
        this.clear();
        return org.python.types.NoneType.NONE;
    }

    public org.python.Object clear() {
        this.value.clear();
        return org.python.types.NoneType.NONE;
    }

    public org.python.Object copy(java.util.List<org.python.Object> args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.copy() has not been implemented.");
    }

    public org.python.Object copy() {
        throw new org.python.exceptions.NotImplementedError("list.copy() has not been implemented.");
    }

    public org.python.Object count(java.util.List<org.python.Object> args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.count() has not been implemented.");
    }

    public org.python.Object count(org.python.Object value) {
        throw new org.python.exceptions.NotImplementedError("list.count() has not been implemented.");
    }

    public org.python.Object extend(java.util.List<org.python.Object> args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.extend() has not been implemented.");
    }

    public org.python.Object extend(org.python.Object iterable) {
        throw new org.python.exceptions.NotImplementedError("list.extend() has not been implemented.");
    }

    public org.python.Object index(java.util.List<org.python.Object> args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.index() has not been implemented.");
    }

    public org.python.Object index(org.python.Object value, org.python.Object start, org.python.Object stop) {
        throw new org.python.exceptions.NotImplementedError("list.index() has not been implemented.");
    }

    public org.python.Object index(org.python.Object value, org.python.Object start) {
        throw new org.python.exceptions.NotImplementedError("list.index() has not been implemented.");
    }

    public org.python.Object index(org.python.Object value, int start, int stop) {
        throw new org.python.exceptions.NotImplementedError("list.index() has not been implemented.");
    }

    public org.python.Object index(org.python.Object value, int start) {
        return this.index(value, start, -1);
    }

    public org.python.Object index(org.python.Object value) {
        return this.index(value, 0, -1);
    }

    public org.python.Object insert(java.util.List<org.python.Object> args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.insert() has not been implemented.");
    }

    public void insert(org.python.Object index, org.python.Object object) {
        throw new org.python.exceptions.NotImplementedError("list.insert() has not been implemented.");
    }

    public org.python.Object pop(java.util.List<org.python.Object> args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.pop() has not been implemented.");
    }

    public org.python.Object pop(org.python.Object index) {
        throw new org.python.exceptions.NotImplementedError("list.pop() has not been implemented.");
    }

    public org.python.Object pop(int index) {
        throw new org.python.exceptions.NotImplementedError("list.pop() has not been implemented.");
    }

    public org.python.Object pop() {
        return this.pop(-1);
    }

    public void remove(java.util.List<org.python.Object> args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.remove() has not been implemented.");
    }

    public void remove(org.python.Object value) {
        throw new org.python.exceptions.NotImplementedError("list.remove() has not been implemented.");
    }

    public void reverse(java.util.List<org.python.Object> args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.reverse() has not been implemented.");
    }

    public void reverse() {
        throw new org.python.exceptions.NotImplementedError("list.reverse() has not been implemented.");
    }

    public org.python.Object sort(java.util.List<org.python.Object> args, java.util.HashMap kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.sort() has not been implemented.");
    }

    public org.python.Object sort(org.python.Object key, org.python.Object reverse) {
        throw new org.python.exceptions.NotImplementedError("list.sort() has not been implemented.");
    }

}
