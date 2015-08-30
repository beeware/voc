package org.python.exceptions;

public class FileNotFoundError extends org.python.exceptions.OSError {
    public FileNotFoundError() {
        super();
    }

    public FileNotFoundError(String msg) {
        super(msg);
    }
}
