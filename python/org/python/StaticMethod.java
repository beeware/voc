package org.python;

import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;
import org.python.exceptions.RuntimeError;

public class StaticMethod implements Callable {
    public Method method;

    public StaticMethod(Method method) {
        this.method = method;
    }

    public PyObject invoke(PyObject... args) throws Throwable {
        try {
            return (PyObject) this.method.invoke(args);
        } catch (IllegalAccessException e) {
            throw new RuntimeError("Illegal access to Java static method " + this.method);
        } catch (InvocationTargetException e) {
            throw e.getCause();
        }
    }
}
