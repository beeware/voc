package org.python.exceptions;

public class BufferError extends org.python.exceptions.Exception {
    public BufferError() {
        super();
    }

    public BufferError(String msg) {
        super(msg);
    }

    public BufferError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
