package org.python.exceptions;

public class RuntimeError extends org.python.exceptions.Exception {
    public RuntimeError() {
        super();
    }

    public RuntimeError(String msg) {
        super(msg);
    }

    public RuntimeError(org.python.Object msg) {
        this(msg.toString());
    }

    public RuntimeError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
