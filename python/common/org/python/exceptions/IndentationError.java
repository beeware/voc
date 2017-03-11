package org.python.exceptions;

public class IndentationError extends org.python.exceptions.SyntaxError {
    public IndentationError() {
        super();
    }

    public IndentationError(String msg) {
        super(msg);
    }

    public IndentationError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
