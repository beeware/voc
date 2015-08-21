package org.python.exceptions;

public class PythonException extends RuntimeException {
    public PythonException() {
        super();
    }

    public PythonException(String msg) {
        super(msg);
    }
}
