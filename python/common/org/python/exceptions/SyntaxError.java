package org.python.exceptions;

public class SyntaxError extends org.python.exceptions.Exception {
    public SyntaxError() {
        super();
    }

    public SyntaxError(String msg) {
        super(msg);
    }

    public SyntaxError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
