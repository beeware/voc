package org.python.exceptions;

public class ConnectionResetError extends org.python.exceptions.ConnectionError {
    public ConnectionResetError() {
        super();
    }

    public ConnectionResetError(String msg) {
        super(msg);
    }

    public ConnectionResetError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
