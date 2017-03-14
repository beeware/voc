package org.python.types;

public class Method extends org.python.types.Object implements org.python.Callable {
    org.python.Object im_self;
    org.python.types.Type im_class;
    org.python.types.Function im_func;

    public Method(org.python.Object instance, org.python.types.Type klass, org.python.types.Function function) {
        super();
        this.im_self = instance;
        this.im_class = klass;
        this.im_func = function;
        // System.out.println("Create method " + function.name + " on " + instance);
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        if (this.im_self == null) {
            return new org.python.types.Str(
                    String.format("<unbound method %s.%s>",
                            this.im_class.__dict__.get("__name__"),
                            this.im_func.__dict__.get("__name__")
                    )
            );
        } else {
            return new org.python.types.Str(
                    String.format("<bound method %s.%s of %s>",
                            this.im_class.__dict__.get("__name__"),
                            this.im_func.__dict__.get("__name__"),
                            this.im_self
                    )
            );
        }
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __bool__() {
        return new org.python.types.Bool(true);
    }

    public org.python.Object invoke(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        // System.out.println("METHOD Invocation: " + this.im_self);
        return this.im_func.invoke(this.im_self, args, kwargs);
    }
}
