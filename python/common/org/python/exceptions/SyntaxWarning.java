package org.python.exceptions;

public class SyntaxWarning extends org.python.exceptions.Warning {
    public SyntaxWarning() {
        super();
    }

    public SyntaxWarning(String msg) {
        super(msg);
    }

    public SyntaxWarning(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
