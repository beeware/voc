package org.python.exceptions;

public class NameError extends org.python.exceptions.Exception {
    public NameError(String var_name) {
        super("name '" + var_name + "' is not defined");
    }

    NameError(String msg_or_var, boolean raw_msg) {
        super(msg_or_var);
    }

    public NameError(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super("name '" + args[0] + "' is not defined");
    }
}
