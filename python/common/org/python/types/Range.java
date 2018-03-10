package org.python.types;

public class Range extends org.python.types.Object {
    private long start;
    private long stop;
    private long step;

    public Range(org.python.Object stop) {
        this(new org.python.types.Int(0), stop, new org.python.types.Int(1));
    }

    public Range(org.python.Object start, org.python.Object stop) {
        this(start, stop, new org.python.types.Int(1));
    }

    public Range(org.python.Object start, org.python.Object stop, org.python.Object step) {
        super();
        if (start instanceof org.python.types.Int) {
            this.start = ((org.python.types.Int) start).value;
        } else {
            throw new org.python.exceptions.TypeError("'" + start.typeName() + "' object cannot be interpreted as an integer");
        }
        this.__dict__.put("start", start);

        if (stop instanceof org.python.types.Int) {
            this.stop = ((org.python.types.Int) stop).value;
        } else {
            throw new org.python.exceptions.TypeError("'" + stop.typeName() + "' object cannot be interpreted as an integer");
        }
        this.__dict__.put("stop", stop);

        if (step instanceof org.python.types.Int) {
            this.step = ((org.python.types.Int) step).value;
        } else {
            throw new org.python.exceptions.TypeError("'" + step.typeName() + "' object cannot be interpreted as an integer");
        }
        if (this.step == 0) {
            throw new org.python.exceptions.ValueError("range() arg 3 must not be zero");
        }
        this.__dict__.put("step", step);
    }

    @org.python.Method(
            __doc__ = "Implement repr(self)."
    )
    public org.python.Object __repr__() {
        if (this.step == 1) {
            return new org.python.types.Str(String.format("range(%d, %d)", this.start, this.stop));
        } else {
            return new org.python.types.Str(String.format("range(%d, %d, %d)", this.start, this.stop, this.step));
        }
    }

    @org.python.Method(
            __doc__ = "Implement iter(self)."
    )
    public org.python.Object __iter__() {
        return new RangeIterator(start, stop, step);
    }

    @org.python.Method(
            __doc__ = "Reverse the list in place and returns\n" +
                      "an iterator that iterates over all the objects\n" +
                      "in the list in reverse order. Does not\n" +
                      "modify the original list."
    )
    public org.python.Object __reversed__() {
        // TODO: Will need to check for overflows and underflows and many
        // other edge cases in the future...
        long n = (this.stop - this.start + 1) / this.step;
        long start = this.start + (n - 1) * this.step;
        long stop = this.start - this.step;
        long step = 0 - this.step;
        return new RangeIterator(start, stop, step);
    }

    @org.python.Method(
            __doc__ = "Implement __getitem__(self).",
            args = {"index"}
    )
    public org.python.Object __getitem__(org.python.Object index) {
        try {
            if (index instanceof org.python.types.Slice) {
                org.python.types.Slice.ValidatedValue val = ((org.python.types.Slice) index).validateValueTypes();
                org.python.types.Slice slice = new org.python.types.Slice(val.start, val.stop, val.step);
                org.python.types.Tuple indices = slice.indices((org.python.types.Int) (this.__len__()));
                org.python.Object start = indices.__getitem__(new org.python.types.Int(0));
                org.python.Object stop = indices.__getitem__(new org.python.types.Int(1));
                org.python.Object step = indices.__getitem__(new org.python.types.Int(2));
                org.python.Object rstart = this.__dict__.get("start");
                org.python.Object rstep = this.__dict__.get("step");
                org.python.Object substep = step.__mul__(rstep);
                org.python.Object substart = rstart.__add__(rstep.__mul__(start));
                org.python.Object substop = rstart.__add__(rstep.__mul__(stop));
                return new org.python.types.Range(substart, substop, substep);
            } else {
                long len = ((org.python.types.Int) (this.__len__())).value;
                long idx;
                if (index instanceof org.python.types.Bool) {
                    idx = ((org.python.types.Bool) index).value ? 1 : 0;
                } else {
                    idx = ((org.python.types.Int) index).value;
                }

                if (idx < 0) {
                    idx = len + idx;
                }
                if (idx < 0 || idx >= len) {
                    throw new org.python.exceptions.IndexError("range object index out of range");
                }

                return new org.python.types.Int(this.start + idx * this.step);
            }
        } catch (ClassCastException e) {
            if (org.Python.VERSION < 0x03050000) {
                throw new org.python.exceptions.TypeError("range indices must be integers");
            } else {
                throw new org.python.exceptions.TypeError(
                        "range indices must be integers or slices, not " + index.typeName()
                );
            }
        }
    }

    @org.python.Method(
            __doc__ = "Implement __len__(self)."
    )
    public org.python.Object __len__() {
        if (this.step > 0 && this.start < this.stop) {
            return new org.python.types.Int(
                    1 + (this.stop - 1 - this.start) / this.step
            );
        } else if (this.step < 0 && this.start > this.stop) {
            return new org.python.types.Int(
                    1 + (this.start - 1 - this.stop) / (-this.step)
            );
        } else {
            return new org.python.types.Int(0);
        }
    }

    @org.python.Method(
            __doc__ = "Implement __bool__(self)."
    )
    public org.python.Object __bool__() {
        return new org.python.types.Bool(
                ((org.python.types.Int) this.__len__()).value > 0
        );
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'range'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: 'range'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary +: 'range'");
    }

    @org.python.Method(
            __doc__ = "Return self>=value.",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self>value.",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self==value.",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.Range) {
            org.python.types.Range range2 = (org.python.types.Range) other;
            return new org.python.types.Bool(
                (this.start == range2.start) &&
                (this.stop == range2.stop) &&
                (this.step == range2.step)
            );
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self<value.",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self<=value.",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Implement self*value.",
            args = {"other"}
    )
    public org.python.Object __mul__(org.python.Object other) {
        if ((other instanceof org.python.types.ByteArray) ||
                (other instanceof org.python.types.Bytes) ||
                (other instanceof org.python.types.List) ||
                (other instanceof org.python.types.Str) ||
                (other instanceof org.python.types.Tuple)) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type 'range'");
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'range' and '" + other.typeName() + "'");
    }

    public class RangeIterator extends org.python.types.Object implements org.python.Object {

        public static final java.lang.String PYTHON_TYPE_NAME = "range_iterator";

        private long index;

        private long start;
        private long stop;
        private long step;

        public RangeIterator(long start, long stop, long step) {
            super();
            this.start = start;
            this.stop = stop;
            this.step = step;
            index = this.start;
        }

        @org.python.Method(
                 __doc__ = "Implement iter(self)."
        )
        public org.python.Object __iter__() {
            return this;
        }

        @org.python.Method(
                __doc__ = "Implement next(self)."
        )
        public org.python.Object __next__() {
            if (this.step > 0 && this.index >= this.stop) {
                throw new org.python.exceptions.StopIteration();
            } else if (this.step < 0 && this.index <= this.stop) {
                throw new org.python.exceptions.StopIteration();
            }

            org.python.Object result = new org.python.types.Int(this.index);
            this.index += this.step;
            return result;
        }

        @org.python.Method(
                __doc__ = ""
        )
        public org.python.Object __invert__() {
            throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'range'");
        }

        @org.python.Method(
                __doc__ = ""
        )
        public org.python.Object __neg__() {
            throw new org.python.exceptions.TypeError("bad operand type for unary -: 'range'");
        }

        @org.python.Method(
                __doc__ = ""
        )
        public org.python.Object __pos__() {
            throw new org.python.exceptions.TypeError("bad operand type for unary +: 'range'");
        }
    }
}
