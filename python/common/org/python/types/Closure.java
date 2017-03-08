package org.python.types;

public class Closure extends org.python.types.Object {
    public java.util.Map<java.lang.String, org.python.Object> closure_vars;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Closure
     */
    void setValue(org.python.Object obj) {
    }

    public Closure(java.util.Map<java.lang.String, org.python.Object> vars) {
        super();
        this.closure_vars = vars;
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        return new org.python.types.Str(String.format("<function %s at 0x%x>", this.typeName(), this.hashCode()));
    }
}
