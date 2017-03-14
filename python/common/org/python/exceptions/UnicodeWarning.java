package org.python.exceptions;

public class UnicodeWarning extends org.python.exceptions.Warning {
    public UnicodeWarning() {
        super();
    }

    public UnicodeWarning(String msg) {
        super(msg);
    }

    public UnicodeWarning(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
