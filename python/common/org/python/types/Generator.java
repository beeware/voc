package org.python.types;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;

public class Generator extends org.python.types.Object {
    java.lang.String name;
    java.lang.reflect.Method expression;
    public int yield_point;
    public java.util.Map<java.lang.String, org.python.Object> stack;

    private boolean just_started = true;
    public org.python.Object message;
    public org.python.Object exception;

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
        this.message = org.python.types.NoneType.NONE;
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
            __doc__ = "Implement send(message).",
            args = {"message"}
    )
    public org.python.Object send(org.python.Object message) {
        if (just_started && !(message instanceof org.python.types.NoneType)) {
            throw new org.python.exceptions.TypeError("can't send non-None value to a just-started generator");
        }
        this.message = message;
        return this.__next__();
    }

    public void reset_message() {
        this.message = org.python.types.NoneType.NONE;
    }

    @org.python.Method(
            __doc__ = "Implement throw(type, value=None, traceback=None).",
            args = {"type"},
            default_args = {"value", "traceback"}
    )
    public org.python.Object _throw(org.python.Object type, org.python.Object value, org.python.Object traceback) {
        if (value == null) {
            value = org.python.types.NoneType.NONE;
        }

        if (traceback == null) {
            traceback = org.python.types.NoneType.NONE;
        } else {
            throw new org.python.exceptions.NotImplementedError("traceback currently not supported");
        }

        String exception_name;

        try {
            exception_name = org.Python.typeName(((org.python.types.Type) type).klass);
        } catch (ClassCastException e) {
            throw new org.python.exceptions.TypeError(
                "exceptions must be classes or instances deriving from BaseException, not " + type.typeName());
        }

        // TODO: check whether the klass inherits org.python.exception.BasseException

        try {
            Class exception_class = Class.forName("org.python.exceptions." + exception_name);
            Constructor exception_constructor;
            if (value instanceof org.python.types.NoneType) {
                exception_constructor = exception_class.getConstructor();
                this.exception = Type.toPython(exception_constructor.newInstance());
            }
            // TODO: parse for signature String msg and
            // TODO: (org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs)
        } catch (ClassNotFoundException e) {
            throw new org.python.exceptions.NameError(exception_name);
        } catch (NoSuchMethodException |
            InstantiationException | IllegalAccessException | InvocationTargetException e) {
            throw new org.python.exceptions.RuntimeError(e.getMessage());
        }

        if (just_started) {
            // TODO: close the generator before throwing exception
            throw (org.python.exceptions.BaseException) this.exception;
        }

        try {
            return this.__next__();
        } catch (org.python.exceptions.BaseException e) {
            this.expression = null; // close this generator if it did not catch the exception
            throw e; // re-throw exception after closing
        }
    }

    public void throw_exception() {
        if (this.exception != null) {
            org.python.exceptions.BaseException exception = (org.python.exceptions.BaseException) this.exception;
            this.exception = null;
            throw exception;
        }
    }

    @org.python.Method(
            __doc__ = "Implement close(self)."
    )
    public org.python.Object close() {
        if (this.just_started) {
            this.expression = null;
        }

        if (this.expression == null) {
            // Do nothing if generator has already exited
            return org.python.types.NoneType.NONE;
        }

        boolean has_exit_normally = false;
        try {
            this.exception = new org.python.exceptions.GeneratorExit();
            this.__next__();
        } catch (org.python.exceptions.GeneratorExit | org.python.exceptions.StopIteration e) {
            has_exit_normally = true;
        }
        if (!has_exit_normally) {
            // Generator caught GeneratorExit exception and yields
            throw new org.python.exceptions.RuntimeError("generator ignored GeneratorExit");
        }

        this.expression = null; // cleanup
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
            __doc__ = "Return del(self)."
    )
    public void __del__() {
        try {
            this.close();
        } catch (Exception e) {
            //TODO: log error message in java equivalent of sys.stderr
        }
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
    public org.python.Object __iter__() {
        return this;
    }

    @org.python.Method(
            __doc__ = "Implement next(self)."
    )
    public org.python.Object __next__() {
        if (this.expression == null) {
            // Generator has already exited
            throw new org.python.exceptions.StopIteration();
        }
        try {
            just_started = false;
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
