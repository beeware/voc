package org.python.types;

public class Closure extends org.python.types.Object {
    public Closure() {
        super();
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        return new org.python.types.Str(String.format("<function %s at 0x%x>", this.typeName(), this.hashCode()));
    }
}
