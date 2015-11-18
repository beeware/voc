package org.python.exceptions;

public class UnboundLocalError extends org.python.exceptions.NameError {
    public UnboundLocalError(String var) {
        super("local variable '" + var + "' referenced before assignment", true);
    }
}
