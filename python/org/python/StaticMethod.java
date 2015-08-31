package org.python;

import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;

import org.python.exceptions.RuntimeError;


public class StaticMethod implements Callable{
    public java.lang.reflect.Method method;

    public StaticMethod(java.lang.reflect.Method method) {
        this.method = method;
    }

    public org.python.Object invoke(java.lang.Object... args) {
        try {
            return (org.python.Object) this.method.invoke(args);
        } catch (IllegalAccessException e) {
            throw new RuntimeError("Illegal access to Java static method " + this.method);
        } catch (InvocationTargetException e) {
            throw new RuntimeError(e.getCause().toString());
        }
    }
}
