package org.python.exceptions;

public class AssertionError extends PythonException {
    public AssertionError() {
        super();
    }

    public AssertionError(String msg) {
        super(msg);
    }
}
