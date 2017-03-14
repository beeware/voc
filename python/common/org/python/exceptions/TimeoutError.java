package org.python.exceptions;

public class TimeoutError extends org.python.exceptions.OSError {
    public TimeoutError() {
        super();
    }

    public TimeoutError(String msg) {
        super(msg);
    }

    public TimeoutError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
