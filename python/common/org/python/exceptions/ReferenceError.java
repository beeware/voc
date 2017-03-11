package org.python.exceptions;

public class ReferenceError extends org.python.exceptions.Exception {
    public ReferenceError() {
        super();
    }

    public ReferenceError(String msg) {
        super(msg);
    }

    public ReferenceError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
