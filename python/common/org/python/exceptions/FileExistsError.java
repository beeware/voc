package org.python.exceptions;

public class FileExistsError extends org.python.exceptions.OSError {
    public FileExistsError() {
        super();
    }

    public FileExistsError(String msg) {
        super(msg);
    }

    public FileExistsError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
