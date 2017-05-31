package org.python.exceptions;

public class Exception extends org.python.exceptions.BaseException {
    public Exception() {
        super();
    }

    public Exception(java.lang.String msg) {
        super(msg);
    }

    public Exception(org.python.types.Tuple tuple) {
        super();
    }    

    public Exception(org.python.Object args) {
        super(args);
    }
}
