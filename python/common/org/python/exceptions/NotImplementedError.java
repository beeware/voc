package org.python.exceptions;

public class NotImplementedError extends org.python.exceptions.RuntimeError {
    public NotImplementedError() {
        super();
    }

    public NotImplementedError(String msg) {
        super(msg);
    }

    public NotImplementedError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
