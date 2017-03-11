package org.python.exceptions;

public class UnicodeDecodeError extends org.python.exceptions.UnicodeError {
    public UnicodeDecodeError() {
        super();
    }

    public UnicodeDecodeError(String msg) {
        super(msg);
    }

    public UnicodeDecodeError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
