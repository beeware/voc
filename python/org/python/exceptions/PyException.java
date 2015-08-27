package org.python.exceptions;

public class PyException extends RuntimeException {
    public PyException() {
        super();
    }

    public PyException(String msg) {
        super(msg);
    }
}
