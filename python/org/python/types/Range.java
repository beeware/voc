package org.python.types;


public class Range extends org.python.Object implements org.python.Iterable {
    private long index;

    private long stop;
    private long start;
    private long step;

    public Range(org.python.Object stop) {
        this(new org.python.Object(0), stop, new org.python.Object(1));
    }

    public Range(org.python.Object start, org.python.Object stop) {
        this(start, stop, new org.python.Object(1));
    }

    public Range(org.python.Object start, org.python.Object stop, org.python.Object step) {
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

        java.util.Hashtable<java.lang.String, org.python.Object> attrs = new java.util.Hashtable<java.lang.String, org.python.Object>();

        attrs.put("start", start);
        this.start = (long) start.value;

        attrs.put("stop", stop);
        this.stop = (long) stop.value;

        attrs.put("step", step);
        this.step = (long) step.value;

        value = attrs;
    }

    public org.python.Object __iter__() {
        return this;
    }

    public org.python.Object __next__() {
        if (this.index >= this.stop) {
            throw new org.python.exceptions.StopIteration();
        }
        this.index += this.step;
        return new org.python.Object(this.index);
    }

}
