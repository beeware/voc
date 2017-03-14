package org.python.exceptions;

public class FileNotFoundError extends org.python.exceptions.OSError {
    public FileNotFoundError() {
        super();
    }

    public FileNotFoundError(String msg) {
        super(msg);
    }

    public FileNotFoundError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
