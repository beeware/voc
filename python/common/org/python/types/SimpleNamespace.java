package org.python.types;

public class SimpleNamespace extends org.python.types.Object {
    @org.python.Method(
            __doc__ = "A simple attribute-based namespace.\n" +
                "\n" +
                "SimpleNamespace(**kwargs)"
    )
    public SimpleNamespace(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length > 0) {
            throw new org.python.exceptions.TypeError("no positional arguments expected");
        }

        for (java.util.Map.Entry<java.lang.String, org.python.Object> entry : kwargs.entrySet()) {
            this.__setattr__(entry.getKey(), entry.getValue());
        }
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.types.Str __repr__() {
        java.lang.StringBuilder buffer = new java.lang.StringBuilder("namespace(");
        java.lang.Object[] sorted_keys = this.__dict__.keySet().toArray();
        java.util.Arrays.sort(sorted_keys);
        boolean first = true;
        for (java.lang.Object key : sorted_keys) {
            if (!first) {
                buffer.append(", ");
            }
            first = false;
            buffer.append(key);
            buffer.append("=");
            buffer.append(this.__dict__.get((java.lang.String) key).__repr__());
        }
        buffer.append(")");

        return new org.python.types.Str(buffer.toString());
    }

    @org.python.Method(
            __doc__ = "Return self==value.",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (this.__dict__.equals(((org.python.types.Object) other).__dict__)) {
            return org.python.types.Bool.TRUE;
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }
}
