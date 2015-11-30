package org.python.types;


public class Slice extends org.python.types.Object {
    org.python.types.Int start;
    org.python.types.Int stop;
    org.python.types.Int step;

    public Slice(org.python.Object stop) {
        this(new org.python.types.Int(0), stop, new org.python.types.Int(1));
    }

    public Slice(org.python.Object start, org.python.Object stop) {
        this(start, stop, new org.python.types.Int(1));
    }

    public Slice(org.python.Object start, org.python.Object stop, org.python.Object step) {
        super();
        if (start instanceof org.python.types.Int) {
            attrs.put("start", start);
            this.start = (org.python.types.Int) start;
        } else if (start instanceof org.python.types.NoneType) {
            attrs.put("start", start);
        } else {
            throw new org.python.exceptions.TypeError("'" + start.typeName() + "' object cannot be interpreted as an integer");
        }

        if (stop instanceof org.python.types.Int) {
            attrs.put("stop", stop);
            this.stop = (org.python.types.Int) stop;
        } else if (stop instanceof org.python.types.NoneType) {
            attrs.put("stop", stop);
        } else {
            throw new org.python.exceptions.TypeError("'" + stop.typeName() + "' object cannot be interpreted as an integer");
        }

        if (step instanceof org.python.types.Int) {
            attrs.put("step", step);
            this.step = (org.python.types.Int) step;
        } else if (step instanceof org.python.types.NoneType) {
            attrs.put("step", step);
        } else {
            throw new org.python.exceptions.TypeError("'" + step.typeName() + "' object cannot be interpreted as an integer");
        }

    }
}
