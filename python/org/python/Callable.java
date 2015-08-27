package org.python;

public interface Callable {
    public PyObject invoke(PyObject... args) throws Throwable;
}
