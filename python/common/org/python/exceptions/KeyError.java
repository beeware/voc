package org.python.exceptions;

public class KeyError extends org.python.exceptions.LookupError {
    public KeyError(org.python.Object key) {
        super(key.__repr__().toString());
    }
}
