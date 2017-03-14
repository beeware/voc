package org.python.exceptions;

public class SystemExit extends org.python.exceptions.BaseException {
    public int return_code;

    public SystemExit() {
        super("0");
        return_code = 0;
    }

    public SystemExit(org.python.Object val) {
        super(java.lang.String.format("%s", ((org.python.types.Int) val.__int__()).value));
        this.return_code = (int) ((org.python.types.Int) val.__int__()).value;
    }

    public SystemExit(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        this(args[0]);
    }
}
