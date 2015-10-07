package org.python.exceptions;

public class BlockingIOError extends org.python.exceptions.OSError {
    public BlockingIOError() {
        super();
    }

    public BlockingIOError(String msg) {
        super(msg);
    }
}
