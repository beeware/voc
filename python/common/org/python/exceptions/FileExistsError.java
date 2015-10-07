package org.python.exceptions;

public class FileExistsError extends org.python.exceptions.OSError {
    public FileExistsError() {
        super();
    }

    public FileExistsError(String msg) {
        super(msg);
    }
}
