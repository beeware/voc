package org.python.exceptions;

public class OSError extends org.python.exceptions.Exception {
    public OSError() {
        super();
    }

    public OSError(String msg) {
        super(msg);
    }

    public OSError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
