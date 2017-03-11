package org.python.exceptions;

public class ValueError extends org.python.exceptions.Exception {
    public ValueError() {
        super();
    }

    public ValueError(String msg) {
        super(msg);
    }

    public ValueError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
