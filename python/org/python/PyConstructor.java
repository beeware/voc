package org.python;

import java.lang.reflect.Constructor;


public class PyConstructor implements Callable {
    public Constructor constructor;

    public PyConstructor(Constructor constructor) {
        this.constructor = constructor;
    }

    public PyObject invoke(PyObject... args) throws Throwable {
        return (PyObject) this.constructor.newInstance();
    }

}
