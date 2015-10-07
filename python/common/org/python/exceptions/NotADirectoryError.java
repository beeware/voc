package org.python.exceptions;

public class NotADirectoryError extends org.python.exceptions.OSError {
    public NotADirectoryError() {
        super();
    }

    public NotADirectoryError(String msg) {
        super(msg);
    }
}
