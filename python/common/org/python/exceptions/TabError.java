package org.python.exceptions;

public class TabError extends org.python.exceptions.IndentationError {
    public TabError() {
        super();
    }

    public TabError(String msg) {
        super(msg);
    }

    public TabError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
