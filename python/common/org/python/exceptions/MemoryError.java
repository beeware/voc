package org.python.exceptions;

public class MemoryError extends org.python.exceptions.Exception {
    public MemoryError() {
        super();
    }

    public MemoryError(String msg) {
        super(msg);
    }

    public MemoryError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
