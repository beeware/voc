package org.python.exceptions;

public class GeneratorExit extends org.python.exceptions.BaseException {
    public GeneratorExit() {
        super();
    }

    public GeneratorExit(String msg) {
        super(msg);
    }

    public GeneratorExit(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
