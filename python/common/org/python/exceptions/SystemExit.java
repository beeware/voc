package org.python.exceptions;

public class SystemExit extends org.python.exceptions.BaseException {
    public int return_code;

    public SystemExit() {
        super("0");
        return_code = 0;
    }

    public SystemExit(int val) {
        super(java.lang.String.format("%s", val));
        this.return_code = val;
    }
}
