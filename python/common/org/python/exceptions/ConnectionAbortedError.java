package org.python.exceptions;

public class ConnectionAbortedError extends org.python.exceptions.ConnectionError {
    public ConnectionAbortedError() {
        super();
    }

    public ConnectionAbortedError(String msg) {
        super(msg);
    }

    public ConnectionAbortedError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
