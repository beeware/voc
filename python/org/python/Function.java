package org.python;

import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;

import org.python.exceptions.RuntimeError;


public class Function extends PyObject implements Callable {
    public Method method;

    public Function(Method method) {
        this.method = method;
    }

    public PyObject invoke(PyObject... args) {
        try {
            return (PyObject) this.method.invoke(null, (Object [])args);
        } catch (IllegalAccessException e) {
            throw new RuntimeError("Illegal access to Java function " + this.method);
        } catch (InvocationTargetException e) {
            throw new RuntimeError(e.getCause().toString());
        }
    }
}
