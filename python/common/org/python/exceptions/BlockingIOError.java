package org.python.exceptions;

public class BlockingIOError extends org.python.exceptions.OSError {
    public BlockingIOError() {
        super();
    }

    public BlockingIOError(String msg) {
        super(msg);
    }

    public BlockingIOError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
