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
            return new org.python.types.Str(
                String.format("<unbound native method %s>",
                    this.function
                )
            );
        } else {
            return new org.python.types.Str(
                String.format("<bound native method %s of <%s object at 0x%x>>",
                    this.function.toString(),
                    this.instance.getClass(),
                    this.instance.hashCode()
                )
            );
        }
    }

    public org.python.Object invoke(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        return this.function.invoke(this.instance, args, kwargs);
    }

    public org.python.Object __get__(org.python.Object instance, org.python.types.Type klass) {
        return this;
    }
}
