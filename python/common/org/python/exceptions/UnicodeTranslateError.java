package org.python.exceptions;

public class UnicodeTranslateError extends org.python.exceptions.UnicodeError {
    public UnicodeTranslateError() {
        super();
    }

    public UnicodeTranslateError(String msg) {
        super(msg);
    }

    public UnicodeTranslateError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
