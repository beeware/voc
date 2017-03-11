package org.python.exceptions;

public class IsADirectoryError extends org.python.exceptions.OSError {
    public IsADirectoryError() {
        super();
    }

    public IsADirectoryError(String msg) {
        super(msg);
    }

    public IsADirectoryError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
