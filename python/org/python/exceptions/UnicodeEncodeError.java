package org.python.exceptions;

public class UnicodeEncodeError extends PythonException {
    public UnicodeEncodeError() {
        super();
    }

    public UnicodeEncodeError(String msg) {
        super(msg);
    }
}
