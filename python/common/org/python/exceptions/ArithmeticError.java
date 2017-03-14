package org.python.exceptions;

public class ArithmeticError extends org.python.exceptions.Exception {
    public ArithmeticError() {
        super();
    }

    public ArithmeticError(String msg) {
        super(msg);
    }

    public ArithmeticError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
