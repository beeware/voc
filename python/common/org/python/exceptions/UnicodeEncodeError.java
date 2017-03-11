package org.python.exceptions;

public class UnicodeEncodeError extends org.python.exceptions.UnicodeError {
    public UnicodeEncodeError() {
        super();
    }

    public UnicodeEncodeError(String msg) {
        super(msg);
    }

    public UnicodeEncodeError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
