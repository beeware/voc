package org.python.exceptions;

public class ImportError extends org.python.exceptions.Exception {
    public ImportError() {
        super();
    }

    public ImportError(String msg) {
        super(msg);
    }

    public ImportError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
