package org.python.types;

public class Tuple extends org.python.types.Object {
    public java.util.List<org.python.Object> value;

    /**
     * A utility method to update the internal value of this object.
     *
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

    public org.python.types.Str __repr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__repr__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        java.lang.StringBuilder buffer = new java.lang.StringBuilder("(");
        boolean first = true;
        for (org.python.Object obj: this.value) {
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

    public org.python.types.Str __format__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__format__() has not been implemented.");
    }

    public org.python.Object __lt__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__lt__() has not been implemented.");
    }

    public org.python.Object __le__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__le__() has not been implemented.");
    }

    public org.python.Object __eq__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__eq__() has not been implemented.");
    }

    public org.python.Object __ne__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__ne__() has not been implemented.");
    }

    public org.python.Object __gt__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__gt__() has not been implemented.");
    }

    public org.python.Object __ge__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__ge__() has not been implemented.");
    }

    public org.python.Object __getattribute__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__getattribute__() has not been implemented.");
    }

    public void __setattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__setattr__() has not been implemented.");
    }

    public void __delattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__delattr__() has not been implemented.");
    }

    public org.python.types.List __dir__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__dir__() has not been implemented.");
    }

    public org.python.types.Int __len__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__len__() has not been implemented.");
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
                return new org.python.types.Tuple(sliced);

            } else {
                int idx = (int)((org.python.types.Int) index).value;
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

    public void __delitem__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.TypeError("'tuple' object doesn't support item deletion");
    }


    public org.python.Iterable __iter__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__iter__() has not been implemented.");
    }

    public org.python.Object __contains__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__contains__() has not been implemented.");
    }

    public org.python.Object __add__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__add__() has not been implemented.");
    }

    public org.python.Object __mul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__mul__() has not been implemented.");
    }

    public org.python.Object __rmul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__rmul__() has not been implemented.");
    }

}