package org.python.exceptions;

public class FutureWarning extends org.python.exceptions.Warning {
    public FutureWarning() {
        super();
    }

    public FutureWarning(String msg) {
        super(msg);
    }

    public FutureWarning(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
