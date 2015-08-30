package org.python;

import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;

import org.python.exceptions.RuntimeError;


public class InstanceMethod implements Callable {
    public java.lang.reflect.Method method;

    public InstanceMethod(java.lang.reflect.Method method) {
        this.method = method;
    }

    public org.python.Object invoke(org.python.Object... args) {
        try {
            return (org.python.Object) this.method.invoke(args);
        } catch (IllegalAccessException e) {
            throw new RuntimeError("Illegal access to Java instance method " + this.method);
        } catch (InvocationTargetException e) {
            throw new RuntimeError(e.getCause().toString());
        }
    }
}
