package org.python.exceptions;

public class EOFError extends org.python.exceptions.Exception {
    public EOFError() {
        super();
    }

    public EOFError(String msg) {
        super(msg);
    }

    public EOFError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
