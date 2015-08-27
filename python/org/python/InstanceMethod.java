package org.python;

import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;
import org.python.exceptions.RuntimeError;

public class InstanceMethod implements Callable {
    public Method method;

    public InstanceMethod(Method method) {
        this.method = method;
    }

    public PyObject invoke(PyObject... args) throws Throwable {
        try {
            return (PyObject) this.method.invoke(args);
        } catch (IllegalAccessException e) {
            throw new RuntimeError("Illegal access to Java instance method " + this.method);
        } catch (InvocationTargetException e) {
            throw e.getCause();
        }
    }
}
