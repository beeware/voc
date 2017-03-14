package org.python.exceptions;

public class TypeError extends org.python.exceptions.Exception {
    public TypeError() {
        super();
    }

    public TypeError(String msg) {
        super(msg);
    }

    public TypeError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
