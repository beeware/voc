package org.python.exceptions;

public class AssertionError extends org.python.exceptions.Exception {
    public AssertionError() {
        super();
    }

    public AssertionError(String msg) {
        super(msg);
    }

    public AssertionError(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
