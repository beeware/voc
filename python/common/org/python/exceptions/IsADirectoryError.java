package org.python.exceptions;

public class IsADirectoryError extends org.python.exceptions.OSError {
    public IsADirectoryError() {
        super();
    }

    public IsADirectoryError(String msg) {
        super(msg);
    }
}
