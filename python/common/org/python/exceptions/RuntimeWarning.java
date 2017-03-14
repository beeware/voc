package org.python.exceptions;

public class RuntimeWarning extends org.python.exceptions.Warning {
    public RuntimeWarning() {
        super();
    }

    public RuntimeWarning(String msg) {
        super(msg);
    }

    public RuntimeWarning(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
