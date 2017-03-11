package org.python.exceptions;

public class PermissionError extends org.python.exceptions.OSError {
    public PermissionError() {
        super();
    }

    public PermissionError(String msg) {
        super(msg);
    }

    public PermissionError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
