package org.python.exceptions;

public class TimeoutError extends org.python.exceptions.OSError {
    public TimeoutError() {
        super();
    }

    public TimeoutError(String msg) {
        super(msg);
    }
}
