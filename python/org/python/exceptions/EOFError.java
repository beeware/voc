package org.python.exceptions;

public class EOFError extends PythonException {
    public EOFError() {
        super();
    }

    public EOFError(String msg) {
        super(msg);
    }
}
