package org.python.exceptions;

@org.python.Class(
        __doc__ = "Common base class for all exceptions"
)
public class BaseException extends org.python.types.Object {
    @org.python.Attribute()
    org.python.types.Tuple args = new org.python.types.Tuple();

    public BaseException() {
        super();
    }

    public BaseException(String msg) {
        super(msg);
        this.args.value.add(new org.python.types.Str(msg));
    }

    public BaseException(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(buildTuple(args).toString());
        this.args = buildTuple(args);
    }

    private static org.python.types.Tuple buildTuple(org.python.Object[] args) {
        return new org.python.types.Tuple(java.util.Arrays.asList(args));
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        return new org.python.types.Str(this.getClass().getSimpleName() + "(\"" + this.getMessage() + "\",)");
    }

    @org.python.Method(
            __doc__ = "Return str(self)."
    )
    public org.python.Object __str__() {
        if (this.args.value.size() == 1) {
            return this.args.value.get(0).__str__();
        }
        return this.args.__str__();
    }

    public java.lang.String toString() {
        return this.getClass().getSimpleName() + ": " + this.getMessage();
    }
}
