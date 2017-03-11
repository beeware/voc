package org.python.exceptions;

public class FloatingPointError extends org.python.exceptions.ArithmeticError {
    public FloatingPointError() {
        super();
    }

    public FloatingPointError(String msg) {
        super(msg);
    }

    public FloatingPointError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
