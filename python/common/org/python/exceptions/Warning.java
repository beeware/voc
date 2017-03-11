package org.python.exceptions;

public class Warning extends org.python.exceptions.Exception {
    public Warning() {
        super();
    }

    public Warning(String msg) {
        super(msg);
    }

    public Warning(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
