package org.python.exceptions;

public class OverflowError extends org.python.exceptions.ArithmeticError {
    public OverflowError() {
        super();
    }

    public OverflowError(String msg) {
        super(msg);
    }

    public OverflowError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
