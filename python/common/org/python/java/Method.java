package org.python.java;

public class Method extends org.python.types.Object implements org.python.Callable {
    org.python.Object instance;
    org.python.java.Function function;

    public Method(org.python.Object instance, org.python.java.Function function) {
        super();
        this.instance = instance;
        this.function = function;
        // System.out.println("Create method " + function.name);
    }

    public org.python.types.Str __repr__() {
        if (this.instance == null) {
            return this.function.__repr__();
        } else {
            return new org.python.types.Str(
                    String.format("<bound native method %s.%s of %s>",
                            this.function.klass.getName(),
                            this.function.name,
                            this.instance.__repr__()
                    )
            );
        }
    }

    public org.python.Object invoke(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        return this.function.invoke(this.instance, args, kwargs);
    }

    public org.python.Object __get__(org.python.Object instance, org.python.types.Type klass) {
        return this;
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __bool__() {
        return new org.python.types.Bool(true);
    }
}
