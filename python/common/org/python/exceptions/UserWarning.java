package org.python.exceptions;

public class UserWarning extends org.python.exceptions.Warning {
    public UserWarning() {
        super();
    }

    public UserWarning(String msg) {
        super(msg);
    }

    public UserWarning(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
