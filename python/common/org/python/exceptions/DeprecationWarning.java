package org.python.exceptions;

public class DeprecationWarning extends org.python.exceptions.Warning {
    public DeprecationWarning() {
        super();
    }

    public DeprecationWarning(String msg) {
        super(msg);
    }

    public DeprecationWarning(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
