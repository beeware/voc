package org.python.exceptions;

public class ResourceWarning extends org.python.exceptions.Warning {
    public ResourceWarning() {
        super();
    }

    public ResourceWarning(String msg) {
        super(msg);
    }

    public ResourceWarning(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
