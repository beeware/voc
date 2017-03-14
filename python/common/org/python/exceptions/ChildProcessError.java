package org.python.exceptions;

public class ChildProcessError extends org.python.exceptions.OSError {
    public ChildProcessError() {
        super();
    }

    public ChildProcessError(String msg) {
        super(msg);
    }

    public ChildProcessError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
