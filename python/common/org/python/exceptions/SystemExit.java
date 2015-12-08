package org.python.exceptions;

public class SystemExit extends org.python.exceptions.BaseException {
    public int return_code;

    public SystemExit() {
        super("0");
        return_code = 0;
    }

    public SystemExit(org.python.Object val) {
        super(java.lang.String.format("%s", org.Python.int_cast(val, null)));
        this.return_code = (int) org.Python.int_cast(val, null).value;
    }
}
