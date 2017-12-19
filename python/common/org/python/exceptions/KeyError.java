package org.python.exceptions;

public class KeyError extends org.python.exceptions.LookupError {
    public KeyError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }

    @org.python.Method(
            __doc__ = "Return str(self)."
    )
    public org.python.Object __str__() {
        if (this.args.value.size() == 1) {
            return this.args.value.get(0).__repr__();
        }
        return this.args.__str__();
    }

    public KeyError(org.python.Object key) {
        super(new org.python.Object[] {key}, null);
    }
}
