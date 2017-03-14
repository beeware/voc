package org.python.exceptions;

public class InterruptedError extends org.python.exceptions.OSError {
    public InterruptedError() {
        super();
    }

    public InterruptedError(String msg) {
        super(msg);
    }

    public InterruptedError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
