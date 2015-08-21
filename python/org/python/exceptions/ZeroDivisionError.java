package org.python.exceptions;

public class ZeroDivisionError extends PythonException {
    public ZeroDivisionError() {
        super();
    }

    public ZeroDivisionError(String msg) {
        super(msg);
    }
}
