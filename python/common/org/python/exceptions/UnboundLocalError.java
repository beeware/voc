package org.python.exceptions;

public class UnboundLocalError extends org.python.exceptions.NameError {
    public UnboundLocalError(String var) {
        super("local variable '" + var + "' referenced before assignment", true);
    }

    public UnboundLocalError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        this(args[0].toString());
    }
}
