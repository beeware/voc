package org.python.exceptions;

public class StopIteration extends org.python.exceptions.Exception {
    public StopIteration() {
        super();
    }

    public StopIteration(String msg) {
        super(msg);
    }

    public StopIteration(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
