package org.python.exceptions;

public class StopIteration extends org.python.exceptions.Exception {
    org.python.Object value;

    public StopIteration() {
        super("");
    }

    public StopIteration(org.python.Object value) {
        super();
        this.value = value;
    }

    public StopIteration(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        this(args[0]);
    }
}
