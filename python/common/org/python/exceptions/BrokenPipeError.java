package org.python.exceptions;

public class BrokenPipeError extends org.python.exceptions.ConnectionError {
    public BrokenPipeError() {
        super();
    }

    public BrokenPipeError(String msg) {
        super(msg);
    }

    public BrokenPipeError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
