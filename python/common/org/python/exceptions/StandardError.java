package org.python.exceptions;

public class StandardError extends org.python.exceptions.Exception {
    public StandardError() {
        super();
    }

    public StandardError(String msg) {
        super(msg);
    }

    public StandardError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
