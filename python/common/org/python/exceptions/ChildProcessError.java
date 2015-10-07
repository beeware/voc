package org.python.exceptions;

public class ChildProcessError extends org.python.exceptions.OSError {
    public ChildProcessError() {
        super();
    }

    public ChildProcessError(String msg) {
        super(msg);
    }
}
