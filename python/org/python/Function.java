package org.python;

import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;

import org.python.exceptions.RuntimeError;


public class Function extends org.python.Object implements Callable {
    public Method method;

    public Function(Method method) {
        this.method = method;
    }

    public org.python.Object invoke(org.python.Object[] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        try {
            return (org.python.Object) this.method.invoke(null, args, kwargs);
        } catch (IllegalAccessException e) {
            throw new RuntimeError("Illegal access to Java function " + this.method);
        } catch (InvocationTargetException e) {
            throw new RuntimeError(e.getCause().toString());
        }
    }
}
