package org.python.exceptions;

public class IndexError extends org.python.exceptions.LookupError {
    public IndexError() {
        super();
    }

    public IndexError(String msg) {
        super(msg);
    }

    public IndexError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
