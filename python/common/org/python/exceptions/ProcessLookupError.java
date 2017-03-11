package org.python.exceptions;

public class ProcessLookupError extends org.python.exceptions.OSError {
    public ProcessLookupError() {
        super();
    }

    public ProcessLookupError(String msg) {
        super(msg);
    }

    public ProcessLookupError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
