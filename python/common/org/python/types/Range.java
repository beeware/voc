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
        attrs.put("start", start);

        if (stop instanceof org.python.types.Int) {
            this.stop = ((org.python.types.Int) stop).value;
        } else {
            throw new org.python.exceptions.TypeError("'" + stop.typeName() + "' object cannot be interpreted as an integer");
        }
        attrs.put("stop", stop);

        if (step instanceof org.python.types.Int) {
            this.step = ((org.python.types.Int) step).value;
        } else {
            throw new org.python.exceptions.TypeError("'" + step.typeName() + "' object cannot be interpreted as an integer");
        }
        attrs.put("step", step);

        index = this.start;
        // value = attrs;
    }

    public org.python.types.Str __repr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__repr__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        if (this.step == 1) {
            return new org.python.types.Str(String.format("range(%d, %d)", this.start, this.stop));
        } else {
            return new org.python.types.Str(String.format("range(%d, %d, %d)", this.start, this.stop, this.step));
        }
    }

    @org.python.Method(
        __doc__ = "Implement iter(self)."
    )
    public org.python.Iterable __iter__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__repr__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        return this;
    }

    public org.python.Iterable __iter__() {
        return this.__iter__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = "Implement iter(self)."
    )
    public org.python.Object __next__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__repr__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        if (this.step > 0 && this.index >= this.stop) {
            throw new org.python.exceptions.StopIteration();
        } else if (this.step < 0 && this.index <= this.stop) {
            throw new org.python.exceptions.StopIteration();
        }

        org.python.Object result = new org.python.types.Int(this.index);
        this.index += this.step;
        return result;
    }

    public org.python.Object __next__() {
        return this.__next__(null, null, null, null);
    }

    public org.python.Object __getitem__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__getitem__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object index = args.get(0);
        try {
            if (index instanceof org.python.types.Slice) {
                org.python.types.Slice slice = (org.python.types.Slice) index;
                return new org.python.types.Range(
                    slice.start == null ? this.attrs.get("start") : slice.start,
                    slice.stop == null ? this.attrs.get("stop") : slice.stop,
                    slice.step == null ? this.attrs.get("step") : slice.step
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
