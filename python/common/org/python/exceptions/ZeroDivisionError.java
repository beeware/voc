package org.python.exceptions;

public class ZeroDivisionError extends org.python.exceptions.ArithmeticError {
    public ZeroDivisionError() {
        super();
    }

    public ZeroDivisionError(String msg) {
        super(msg);
    }

    public ZeroDivisionError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
