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

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("list.__repr__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

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

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __format__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.__format__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __lt__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.__lt__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __le__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.__le__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __eq__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.__eq__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ne__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.__ne__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __gt__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.__gt__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ge__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.__ge__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Int __len__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        return new org.python.types.Int(this.value.size());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getitem__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__getitem__() doesn't take keyword arguments");
        } else if (args == null && args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 argument, got " + args.size());
        }

        org.python.Object index = args.get(0);
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

    @org.python.Method(
        __doc__ = ""
    )
    public void __setitem__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__getitem__() doesn't take keyword arguments");
        } else if (args == null && args.size() != 2) {
            throw new org.python.exceptions.TypeError("Expected 2 arguments, got " + args.size());
        }

        org.python.Object index = args.get(0);
        org.python.Object value = args.get(1);
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
    public void __delitem__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__getitem__() doesn't take keyword arguments");
        } else if (args == null && args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 argument, got " + args.size());
        }

        org.python.Object index = args.get(0);
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
    public org.python.Iterable __iter__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        return new org.python.types.Iterator(this);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Iterable __reversed__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.__reversed__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __contains__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.__contains__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __add__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.__add__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__mul__() takes no keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("__mul__() takes exactly 1 argument (" + args.size() + " given)");
        }

        org.python.Object other = args.get(0);
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

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rmul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.__rmul__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object append(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("append() takes no keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("append() takes exactly 1 argument (" + args.size() + " given)");
        }

        this.value.add(args.get(0));
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object clear(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null || kwargs.size() > 0) {
            throw new org.python.exceptions.TypeError("clear() takes no keyword arguments");
        } else if (args != null || args.size() > 0) {
            throw new org.python.exceptions.TypeError("clear() takes no arguments (" + args.size() + " given)");
        }

        this.value.clear();
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object copy(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.copy() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object count(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.count() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object extend(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.extend() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object index(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("list.index() takes no keyword arguments");
        } else if (args == null || args.size() == 0) {
            throw new org.python.exceptions.TypeError("descriptor 'index' of 'list' object needs an argument");
        } else if (args.size() > 3) {
            throw new org.python.exceptions.NotImplementedError("list.index() with > 2 arguments indices has not been implemented.");
        }

        if (args.size() >= 1 && !(args.get(1) instanceof org.python.types.Int)) {
            throw new org.python.exceptions.TypeError("list indices must be integers, not " + args.get(0).typeName());
        }

        if (args.size() == 3 && !(args.get(2) instanceof org.python.types.Int)) {
            throw new org.python.exceptions.TypeError("list indices must be integers, not " + args.get(1).typeName());
        }

        throw new org.python.exceptions.NotImplementedError("list.index() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object pop(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.pop() has not been implemented.");
    }

    public void remove(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.remove() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object sort(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("list.sort() has not been implemented.");
    }

}
