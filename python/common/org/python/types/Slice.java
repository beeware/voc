package org.python.types;

public class Slice extends org.python.types.Object {
    private org.python.Object start;
    private org.python.Object stop;
    private org.python.Object step;

    public Slice(org.python.Object stop) {
        this(null, stop, null);
    }

    public Slice(org.python.Object start, org.python.Object stop) {
        this(start, stop, null);
    }

    public Slice(org.python.Object start, org.python.Object stop, org.python.Object step) {
        super();
        this.start = start == null ? org.python.types.NoneType.NONE : start;
        this.stop = stop == null ? org.python.types.NoneType.NONE : stop;
        this.step = step == null ? org.python.types.NoneType.NONE : step;
        this.__dict__.put("start", this.start);
        this.__dict__.put("stop", this.stop);
        this.__dict__.put("step", this.step);
    }

    /* Adaptation of _PySlice_GetLongIndices from CPython's Objects/sliceobject.c */
    @org.python.Method(
            __doc__ = "Return indices(self, length).",
            args = {"length"}
    )
    public org.python.types.Tuple indices(org.python.types.Object length) {
        boolean step_is_negative;
        long lower, upper, start, stop, len;
        org.python.types.Int step;

        if (length == org.python.types.NoneType.NONE) {
            throw new org.python.exceptions.TypeError("'NoneType' object cannot be interpreted as an integer");
        }
        len = ((org.python.types.Int) length).value;
        if (len < 0) {
            throw new org.python.exceptions.ValueError("length should not be negative");
        }
        if (this.step == org.python.types.NoneType.NONE) {
            step = new org.python.types.Int(1);
        } else {
            step = (org.python.types.Int) this.step;
        }
        step_is_negative = (step.value < 0);

        /* Compute upper and lower bounds */
        if (step_is_negative) {
            lower = -1;
            upper = lower + len;
        } else {
            lower = 0;
            upper = len;
        }

        /* Compute start */
        if (this.start == org.python.types.NoneType.NONE) {
            start = step_is_negative ? upper : lower;
        } else {
            start = ((org.python.types.Int) this.start).value;
            if (start < 0) {
                start += len;
                if (start < lower) {
                    start = lower;
                }
            } else {
                if (start > upper) {
                    start = upper;
                }
            }
        }

        /* Compute stop */
        if (this.stop == org.python.types.NoneType.NONE) {
            stop = step_is_negative ? lower : upper;
        } else {
            stop = ((org.python.types.Int) this.stop).value;
            if (stop < 0) {
                stop += len;
                if (stop < lower) {
                    stop = lower;
                }
            } else {
                if (stop > upper) {
                    stop = upper;
                }
            }
        }

        java.util.List<org.python.Object> tuple = new java.util.ArrayList<org.python.Object>();
        tuple.add(new org.python.types.Int(start));
        tuple.add(new org.python.types.Int(stop));
        tuple.add(step);
        return new org.python.types.Tuple(tuple);
    }

    private org.python.types.Int validateValueType(org.python.Object value) {
        if (value instanceof org.python.types.Int) {
            return (org.python.types.Int) value;
        } else if (value == null || value instanceof org.python.types.NoneType) {
            return null;
        } else {
            org.python.Object index_object = null;
            boolean error_caught = false;
            try {
                index_object = value.__index__();
            } catch (org.python.exceptions.TypeError error) {
                error_caught = true;
            } catch (org.python.exceptions.AttributeError error) {
                error_caught = true;
            }
            if (error_caught) {
                throw new org.python.exceptions.TypeError("slice indices must be integers or None or have an __index__ method");
            }
            if (index_object instanceof org.python.types.Int) {
                return (org.python.types.Int) index_object;
            } else {
                throw new org.python.exceptions.TypeError("TypeError: __index__ returned non-int (type " + index_object.typeName() + ")");
            }
        }
    }

    public class ValidatedValue {
        public org.python.types.Int start;
        public org.python.types.Int stop;
        public org.python.types.Int step;

        ValidatedValue(org.python.types.Int start, org.python.types.Int stop, org.python.types.Int step) {
            this.start = start;
            this.stop = stop;
            this.step = step;
        }
    }

    public ValidatedValue validateValueTypes() {
        ValidatedValue result = new ValidatedValue(
                this.validateValueType(this.start),
                this.validateValueType(this.stop),
                this.validateValueType(this.step));
        if (result.step != null && result.step.value == 0) {
            throw new org.python.exceptions.ValueError("slice step cannot be zero");
        }

        return result;
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        return new org.python.types.Str(String.format(
            "slice(%s, %s, %s)",
            this.start.__repr__(),
            this.stop.__repr__(),
            this.step.__repr__()));
    }

    private org.python.types.Tuple convertSliceToTuple(org.python.types.Slice slice) {
        org.python.types.Tuple tupleFromSlice = new org.python.types.Tuple();
        tupleFromSlice.value.add(slice.start);
        tupleFromSlice.value.add(slice.stop);
        tupleFromSlice.value.add(slice.step);
        return tupleFromSlice;
    }

    @org.python.Method(
            __doc__ = "Return self>=value.",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {

        if (other instanceof org.python.types.Slice) {
            org.python.types.Tuple otherSliceAsTuple = convertSliceToTuple((org.python.types.Slice) other);
            org.python.types.Tuple thisSliceAsTuple = convertSliceToTuple(this);
            return thisSliceAsTuple.__ge__(otherSliceAsTuple);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }

    @org.python.Method(
            __doc__ = "Return self>value.",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {

        if (other instanceof org.python.types.Slice) {
            org.python.types.Tuple otherSliceAsTuple = convertSliceToTuple((org.python.types.Slice) other);
            org.python.types.Tuple thisSliceAsTuple = convertSliceToTuple(this);
            return thisSliceAsTuple.__gt__(otherSliceAsTuple);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }

    @org.python.Method(
            __doc__ = "Return self==value.",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {

        if (other instanceof org.python.types.Slice) {
            org.python.types.Tuple otherSliceAsTuple = convertSliceToTuple((org.python.types.Slice) other);
            org.python.types.Tuple thisSliceAsTuple = convertSliceToTuple(this);
            return thisSliceAsTuple.__eq__(otherSliceAsTuple);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }

    @org.python.Method(
            __doc__ = "Return self<value.",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {

        if (other instanceof org.python.types.Slice) {
            org.python.types.Tuple otherSliceAsTuple = convertSliceToTuple((org.python.types.Slice) other);
            org.python.types.Tuple thisSliceAsTuple = convertSliceToTuple(this);
            return thisSliceAsTuple.__lt__(otherSliceAsTuple);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }

    @org.python.Method(
            __doc__ = "Return self<=value.",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {

        if (other instanceof org.python.types.Slice) {
            org.python.types.Tuple otherSliceAsTuple = convertSliceToTuple((org.python.types.Slice) other);
            org.python.types.Tuple thisSliceAsTuple = convertSliceToTuple(this);
            return thisSliceAsTuple.__le__(otherSliceAsTuple);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }
}
