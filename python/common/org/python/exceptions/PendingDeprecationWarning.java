package org.python.exceptions;

public class PendingDeprecationWarning extends org.python.exceptions.Warning {
    public PendingDeprecationWarning() {
        super();
    }

    public PendingDeprecationWarning(String msg) {
        super(msg);
    }

    public PendingDeprecationWarning(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
