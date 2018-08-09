package org.python.stdlib.collections;

public class DefaultDict extends org.python.types.Dict {
    private org.python.Object default_factory;

    @org.python.Method(
            __doc__ =
                "defaultdict(default_factory[, ...]) --> dict with default factory\n" +
                    "\n" +
                    "The default factory is called without arguments to produce\n" +
                    "a new value when a key is not present, in __getitem__ only.\n" +
                    "A defaultdict compares equal to a dict with the same items.\n" +
                    "All remaining arguments are treated the same as if they were\n" +
                    "passed to the dict constructor, including keyword arguments.\n" +
                    "\n" +
                    "\n",
            default_args = {"default_factory", "iterable"}
    )
    public DefaultDict(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(new org.python.Object[]{args[1]}, kwargs);

        if (args[0] != null) {
            this.default_factory = args[0];

            if (!(this.default_factory instanceof org.python.Callable ||
                    this.default_factory instanceof org.python.types.NoneType)) {
                throw new org.python.exceptions.TypeError("first argument must be callable or None");
            }
        } else {
            this.default_factory = org.python.types.NoneType.NONE;
        }
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str(
            "defaultdict(" + this.default_factory.__repr__() + ", " + super.__repr__() + ")");
    }

    @org.python.Method(
            __doc__ =
                "__missing__(key) # Called by __getitem__ for missing key; pseudo-code:\n" +
                "  if self.default_factory is None: raise KeyError((key,))\n" +
                "  self[key] = value = self.default_factory()\n" +
                "  return value",
            args = {"key"}
    )
    public org.python.Object __missing__(org.python.Object key) {
        if (default_factory instanceof org.python.types.NoneType) {
            throw new org.python.exceptions.KeyError(key);
        }

        try {
            org.python.Object value;
            if (this.default_factory instanceof org.python.types.Function) {
                // invoke function without argument
                value = ((org.python.types.Function) this.default_factory).invoke(null, null);
            } else {
                // use default constructor to get default value
                java.lang.reflect.Constructor constructor = ((org.python.types.Type) this.default_factory).constructor;
                value = (org.python.Object) constructor.newInstance(new org.python.Object[1], null);
            }
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
