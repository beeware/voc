package org.python;

import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;

import org.python.exceptions.RuntimeError;


public class Function extends org.python.Object implements Callable {
    public Method method;

    public Function(Method method) {
        this.method = method;
    }

    public org.python.Object invoke(org.python.Object... args) {
        try {
            return (org.python.Object) this.method.invoke(null, (java.lang.Object [])args);
        } catch (IllegalAccessException e) {
            throw new RuntimeError("Illegal access to Java function " + this.method);
        } catch (InvocationTargetException e) {
            throw new RuntimeError(e.getCause().toString());
        }
    }
}
