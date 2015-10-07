package org.python.exceptions;

public class NameError extends org.python.exceptions.Exception {
    public NameError(String var_name) {
        super("name '" + var_name + "' is not defined");
    }
}
