package org.python.exceptions;

@org.python.Class(
        __doc__ = "Common base class for all exceptions"
)
public class BaseException extends org.python.types.Object {
    @org.python.Attribute()
    public org.python.types.Tuple args = new org.python.types.Tuple();

    public BaseException() {
        super();
    }

    public BaseException(String msg) {
        super(msg);
        this.args.value.add(new org.python.types.Str(msg));
    }

    public BaseException(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super();
        this.args = buildTuple(args);
    }

    private static org.python.types.Tuple buildTuple(org.python.Object[] args) {
        return new org.python.types.Tuple(java.util.Arrays.asList(args));
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        if (org.Python.VERSION < 0x03070000 || this.args.value.size() != 1) {
            return new org.python.types.Str(this.getClass().getSimpleName() + this.args.toString());
        } else {
            return new org.python.types.Str(this.getClass().getSimpleName() + "(" + this.args.value.get(0).__repr__() + ")");
        }
    }

    @org.python.Method(
            __doc__ = "Return str(self)."
    )
    public org.python.Object __str__() {
        if (this.args.value.size() == 0) {
            return new org.python.types.Str("");
        } else if (this.args.value.size() == 1) {
            return this.args.value.get(0).__str__();
        }
        return this.args.__str__();
    }

    public java.lang.String toString() {
        return this.getClass().getSimpleName() + ": " + this.getMessage();
    }

    public java.lang.String getMessage() {
        return this.__str__().toString();
    }
}
