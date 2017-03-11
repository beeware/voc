package org.python.exceptions;

public class LookupError extends org.python.exceptions.Exception {
    public LookupError() {
        super();
    }

    public LookupError(String msg) {
        super(msg);
    }

    public LookupError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
