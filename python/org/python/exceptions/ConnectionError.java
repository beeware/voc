package org.python.exceptions;

public class ConnectionError extends org.python.exceptions.OSError {
    public ConnectionError() {
        super();
    }

    public ConnectionError(String msg) {
        super(msg);
    }
}
