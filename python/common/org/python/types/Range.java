package org.python.types;


public class Range extends org.python.types.Object implements org.python.Iterable {
    private long index;

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
        this.__dict__.put("step", step);

        index = this.start;
        // value = __dict__;
    }

    @org.python.Method(
        __doc__ = "Implement iter(self)."
    )
    public org.python.types.Str __repr__() {
        if (this.step == 1) {
            return new org.python.types.Str(String.format("range(%d, %d)", this.start, this.stop));
        } else {
            return new org.python.types.Str(String.format("range(%d, %d, %d)", this.start, this.stop, this.step));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __iadd__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: 'range' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = "Implement iter(self)."
    )
    public org.python.Iterable __iter__() {
        return this;
    }

    @org.python.Method(
        __doc__ = "Implement iter(self)."
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
        __doc__ = "Implement __getitem__(self).",
        args = {"index"}
    )
    public org.python.Object __getitem__(org.python.Object index) {
        try {
            if (index instanceof org.python.types.Slice) {
                org.python.types.Slice slice = (org.python.types.Slice) index;
                return new org.python.types.Range(
                    slice.start == null ? this.__dict__.get("start") : slice.start,
                    slice.stop == null ? this.__dict__.get("stop") : slice.stop,
                    slice.step == null ? this.__dict__.get("step") : slice.step
                );
            } else {
                long idx = ((org.python.types.Int)index).value;
                long value;
                if (idx >= 0) {
                    value = this.start + idx * this.step;
                } else {
                    value = this.stop + idx * this.step;
                }

                if (this.step > 0 && value >= this.stop) {
                    throw new org.python.exceptions.IndexError("range object index out of range");
                } else if (this.step < 0 && value <= this.stop) {
                    throw new org.python.exceptions.IndexError("range object index out of range");
                }
                org.python.Object result = new org.python.types.Int(value);
                return result;
            }
        } catch (ClassCastException e) {
            throw new org.python.exceptions.TypeError("list indices must be integers, not " + index.typeName());
        }
    }

}
