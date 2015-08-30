package org.python;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;

import org.python.exceptions.RuntimeError;


public class PyConstructor implements Callable {
    public Constructor constructor;

    public PyConstructor(Constructor constructor) {
        this.constructor = constructor;
    }

    public PyObject invoke(PyObject... args) {
        try {
            return (PyObject) this.constructor.newInstance();
        } catch (IllegalAccessException e) {
            throw new RuntimeError("Illegal access to Java constructor " + this.constructor);
        } catch (InvocationTargetException e) {
            throw new RuntimeError(e.getCause().toString());
        } catch (InstantiationException e) {
            throw new RuntimeError(e.getCause().toString());
        }
    }

}
