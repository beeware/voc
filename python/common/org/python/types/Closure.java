package org.python.types;

public class Closure extends org.python.types.Object {
    public java.util.List<java.util.Map<java.lang.String, org.python.Object>> locals_list;

    public Closure(java.util.List<java.util.Map<java.lang.String, org.python.Object>> locals_list) {
        super();
        this.locals_list = locals_list;
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        return new org.python.types.Str(String.format("<function %s at 0x%x>", this.typeName(), this.hashCode()));
    }

    public java.util.Map get_locals(int level) {
        return this.locals_list.get(level - 1);
    }
}
