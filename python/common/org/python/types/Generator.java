package org.python.types;

public class Generator extends org.python.types.Object implements org.python.Iterable {
    java.lang.String name;
    java.lang.reflect.Method expression;
    public int yield_point;
    public java.util.Map<java.lang.String, org.python.Object> stack;

    public int hashCode() {
        return this.expression.hashCode();
    }

    public Generator(
            java.lang.String name,
            java.lang.reflect.Method expression,
            java.util.Map<java.lang.String, org.python.Object> stack
    ) {
        // System.out.println("GENERATOR: " + expression);
        // for (org.python.Object obj: stack) {
        //     System.out.println("     : " + obj);
        // }
        this.name = name;
        this.expression = expression;
        this.yield_point = 0;
        this.stack = stack;
    }

    public void yield(java.util.Map<java.lang.String, org.python.Object> stack, int yield_point) {
        // System.out.println("YIELD: " + yield_point);
        // for (org.python.Object obj: stack) {
        //     System.out.println("     : " + obj);
        // }
        this.yield_point = yield_point;
        this.stack = stack;
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        // if (this.expression.getName().startswith("genexpr_"))
        return new org.python.types.Str(String.format("<%s object (%s) at 0x%x>", this.typeName(), this.name, this.hashCode()));
    }

    @org.python.Method(
            __doc__ = "Implement iter(self)."
    )
    public org.python.Iterable __iter__() {
        return this;
    }

    @org.python.Method(
            __doc__ = "Implement next(self)."
    )
    public org.python.Object __next__() {
        try {
            return (org.python.Object) this.expression.invoke(null, new java.lang.Object[]{this});
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java method " + this.expression);
        } catch (java.lang.reflect.InvocationTargetException e) {
            try {
                // org.Python.debug("Exception:", e.getTargetException());
                // for (java.lang.StackTraceElement ste: e.getTargetException().getStackTrace()) {
                //     org.Python.debug("     ", ste);
                // }

                // If the Java method raised an Python exception, re-raise that
                // exception as-is. If it wasn"t a Python exception, wrap it
                // as one and continue.
                throw (org.python.exceptions.BaseException) e.getCause();
            } catch (ClassCastException java_e) {
                java.lang.String message = e.getCause().getMessage();
                if (message == null) {
                    message = e.getCause().getClass().getName();
                }
                throw new org.python.exceptions.RuntimeError(message);
            }
        // } finally {
            //     System.out.println("INVOKE METHOD DONE");
        }
    }
}
