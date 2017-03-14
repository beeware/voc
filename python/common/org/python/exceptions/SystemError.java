package org.python.exceptions;

public class SystemError extends org.python.exceptions.Exception {
    public SystemError() {
        super();
    }

    public SystemError(String msg) {
        super(msg);
    }

    public SystemError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
