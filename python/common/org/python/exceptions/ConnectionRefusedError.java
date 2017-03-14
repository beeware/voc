package org.python.exceptions;

public class ConnectionRefusedError extends org.python.exceptions.ConnectionError {
    public ConnectionRefusedError() {
        super();
    }

    public ConnectionRefusedError(String msg) {
        super(msg);
    }

    public ConnectionRefusedError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
