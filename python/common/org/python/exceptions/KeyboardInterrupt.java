package org.python.exceptions;

public class KeyboardInterrupt extends org.python.exceptions.BaseException {
    public KeyboardInterrupt() {
        super();
    }

    public KeyboardInterrupt(String msg) {
        super(msg);
    }

    public KeyboardInterrupt(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
