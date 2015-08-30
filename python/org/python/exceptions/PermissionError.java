package org.python.exceptions;

public class PermissionError extends org.python.exceptions.OSError {
    public PermissionError() {
        super();
    }

    public PermissionError(String msg) {
        super(msg);
    }
}
