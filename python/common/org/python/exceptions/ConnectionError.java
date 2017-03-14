package org.python.exceptions;

public class ConnectionError extends org.python.exceptions.OSError {
    public ConnectionError() {
        super();
    }

    public ConnectionError(String msg) {
        super(msg);
    }

    public ConnectionError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
