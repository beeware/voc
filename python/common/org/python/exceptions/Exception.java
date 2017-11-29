package org.python.exceptions;

public class Exception extends org.python.exceptions.BaseException {
    public Exception() {
        super();
    }

    public Exception(java.lang.String msg) {
        super(msg);
    }

    @org.python.Method(__doc__="", varargs="args")
    public Exception(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
