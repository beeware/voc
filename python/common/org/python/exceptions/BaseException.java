package org.python.exceptions;

@org.python.Class(
        __doc__ = "Common base class for all exceptions"
)
public class BaseException extends org.python.types.Object {
    public BaseException() {
        super();
        // System.out.println("EX: " + this);
    }

    public BaseException(String msg) {
        super(msg);
        // System.out.println("EX: " + this);
    }

    public BaseException(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args[0].toString());
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
        return new org.python.types.Str(this.getMessage());
    }

    public java.lang.String toString() {
        return this.getClass().getSimpleName() + ": " + this.getMessage();
    }
}
