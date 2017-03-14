package org.python.exceptions;

public class NotADirectoryError extends org.python.exceptions.OSError {
    public NotADirectoryError() {
        super();
    }

    public NotADirectoryError(String msg) {
        super(msg);
    }

    public NotADirectoryError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
