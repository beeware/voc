package org.python.stdlib.time;

/**
 * Data structure for the return value of time.get_clock_info
 */
public class Namespace extends org.python.types.Object {
    @org.python.Attribute
    public org.python.types.Bool adjustable;
    @org.python.Attribute
    public org.python.types.Str implementation;
    @org.python.Attribute
    public org.python.types.Bool monotonic;
    @org.python.Attribute
    public org.python.types.Float resolution;

    public Namespace(boolean adjustable, String implementation, boolean monotonic, double resolution) {
        this.adjustable = org.python.types.Bool.getBool(adjustable);
        this.implementation = new org.python.types.Str(implementation);
        this.monotonic = org.python.types.Bool.getBool(monotonic);
        this.resolution = new org.python.types.Float(resolution);
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.types.Str __repr__() {
        java.lang.StringBuilder buffer = new java.lang.StringBuilder("namespace(");
        buffer.append("adjustable=");
        buffer.append(this.adjustable.__repr__());
        buffer.append(", implementation=");
        buffer.append(this.implementation.__repr__());
        buffer.append(", monotonic=");
        buffer.append(this.monotonic.__repr__());
        buffer.append(", resolution=");
        buffer.append(this.resolution.__repr__());
        buffer.append(")");

        return new org.python.types.Str(buffer.toString());
    }
}
