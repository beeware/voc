package org.python.exceptions.concurrent;

/**
 * Base class for all future-related exceptions.
 */
public class Error extends org.python.exceptions.Exception {
    Error() {
        super();
    }

    public Error(java.lang.String msg) {
        super(msg);
    }
}
