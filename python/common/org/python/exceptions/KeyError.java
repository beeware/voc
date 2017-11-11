package org.python.exceptions;

public class KeyError extends org.python.exceptions.LookupError {
    public KeyError(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(convertToReprIfOneArgument(args), kwargs);
    }

    private static org.python.Object[] convertToReprIfOneArgument(org.python.Object[] args) {
        if (args.length == 1) {
            return new org.python.Object[] { args[0].__repr__() };
        }
        return args;
    }

    public KeyError(org.python.Object key) {
        super(key.__repr__().toString());
    }
}
