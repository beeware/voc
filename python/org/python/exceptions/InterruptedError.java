package org.python.exceptions;

public class InterruptedError extends org.python.exceptions.OSError {
    public InterruptedError() {
        super();
    }

    public InterruptedError(String msg) {
        super(msg);
    }
}
