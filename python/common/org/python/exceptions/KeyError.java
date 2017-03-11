package org.python.exceptions;

public class KeyError extends org.python.exceptions.LookupError {
    public KeyError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args[0].__repr__().toString());
    }

    public KeyError(org.python.Object key) {
        super(key.__repr__().toString());
    }
}
