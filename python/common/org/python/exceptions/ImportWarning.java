package org.python.exceptions;

public class ImportWarning extends org.python.exceptions.Warning {
    public ImportWarning() {
        super();
    }

    public ImportWarning(String msg) {
        super(msg);
    }

    public ImportWarning(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
