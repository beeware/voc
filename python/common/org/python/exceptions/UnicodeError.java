package org.python.exceptions;

public class UnicodeError extends org.python.exceptions.ValueError {
    public UnicodeError() {
        super();
    }

    public UnicodeError(String msg) {
        super(msg);
    }

    public UnicodeError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
