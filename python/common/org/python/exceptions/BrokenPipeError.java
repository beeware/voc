package org.python.exceptions;

public class BrokenPipeError extends org.python.exceptions.ConnectionError {
    public BrokenPipeError() {
        super();
    }

    public BrokenPipeError(String msg) {
        super(msg);
    }
}
