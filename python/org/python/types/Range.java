package org.python.types;


public class Range extends org.python.types.Object implements org.python.Iterable {
    private long index;

    private long stop;
    private long start;
    private long step;

    public Range(org.python.types.Object stop) {
        this(new org.python.types.Object(0), stop, new org.python.types.Object(1));
    }

    public Range(org.python.types.Object start, org.python.types.Object stop) {
        this(start, stop, new org.python.types.Object(1));
    }

    public Range(org.python.types.Object start, org.python.types.Object stop, org.python.types.Object step) {
        super();
        if (start.type != Long.class) {
            throw new org.python.exceptions.TypeError("'" + start.type + "' object cannot be interpreted as an integer");
        }
        if (stop.type != Long.class) {
            throw new org.python.exceptions.TypeError("'" + stop.type + "' object cannot be interpreted as an integer");
        }
        if (step.type != Long.class) {
            throw new org.python.exceptions.TypeError("'" + step.type + "' object cannot be interpreted as an integer");
        }

        java.util.Hashtable<java.lang.String, org.python.types.Object> attrs = new java.util.Hashtable<java.lang.String, org.python.types.Object>();

        attrs.put("start", start);
        this.start = (long) start.value;

        attrs.put("stop", stop);
        this.stop = (long) stop.value;

        attrs.put("step", step);
        this.step = (long) step.value;

        value = attrs;
    }

    public org.python.types.Object __iter__() {
        return this;
    }

    public org.python.types.Object __next__() {
        if (this.index >= this.stop) {
            throw new org.python.exceptions.StopIteration();
        }
        this.index += this.step;
        return new org.python.types.Object(this.index);
    }

}
