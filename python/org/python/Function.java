package org.python;

import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;

import org.python.exceptions.RuntimeError;


public class Function extends org.python.Object implements Callable {
    public Method method;

    public Function(Method method) {
        this.method = method;
    }

    public org.python.Object invoke(java.lang.Object... args) {
        System.out.println("INVOKING " + method + ", args: " + args);
        try {
            return (org.python.Object) this.method.invoke(null, args);
        } catch (IllegalAccessException e) {
            throw new RuntimeError("Illegal access to Java function " + this.method);
        } catch (InvocationTargetException e) {
            throw new RuntimeError(e.getCause().toString());
        }
    }
}
