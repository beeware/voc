package org.python.stdlib.collections;

public class DefaultDict extends org.python.types.Dict {
    private org.python.Object default_factory;

    public DefaultDict(
            org.python.Object default_factory,
            org.python.Object[] args,
            java.util.Map<java.lang.String, org.python.Object> kwargs
    ) {
        super(args, kwargs);

        this.default_factory = default_factory;
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str(
            "defaultdict(" + this.default_factory.__repr__() + ", " + super.__repr__() + ")");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"key"}
    )
    public org.python.Object __missing__(org.python.Object key) {
        if (default_factory instanceof org.python.types.NoneType) {
            throw new org.python.exceptions.KeyError(key);
        }

        try {
            java.lang.reflect.Constructor constructor = ((org.python.types.Type) this.default_factory).constructor;
            org.python.Object value = (org.python.Object) constructor.newInstance(new org.python.Object[1], null);
            this.__setitem__(key, value);

            return this.__getitem__(key);
        } catch (IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to constructor " + e.getMessage());
        } catch (InstantiationException | java.lang.reflect.InvocationTargetException e) {
            try {
                throw (org.python.exceptions.BaseException) e.getCause();
            } catch (ClassCastException java_e) {
                java.lang.String message = e.getCause().getMessage();
                if (message == null) {
                    message = e.getCause().getClass().getName();
                }
                throw new org.python.exceptions.RuntimeError(message);
            }
        }
    }
}
