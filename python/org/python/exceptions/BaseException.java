package org.python.exceptions;

public class BaseException extends java.lang.RuntimeException implements org.python.Object {
    /**
     * Return the python name for this class.
     */
    public java.lang.String getPythonName() {
        return this.getClass().getName();
    }

    public BaseException() {
        super();
    }

    public BaseException(String msg) {
        super(msg);
    }

    /**
     * Proxy Java object methods onto their Python counterparts.
     */

    // @SuppressWarnings("unchecked")
    public boolean equals(java.lang.Object other) {
        try {
            return ((org.python.types.Bool) __eq__((org.python.types.Object) other)).value;
        } catch (ClassCastException e) {
            throw new org.python.exceptions.RuntimeError("Can't compare a Python object with non-Python object.");
        }
    }

    public int compareTo(java.lang.Object other) {
        try {
            if (((org.python.types.Bool) this.__lt__((org.python.types.Object) other)).value) {
                return -1;
            }
            else if (((org.python.types.Bool) this.__lt__((org.python.types.Object) other)).value) {
                return 1;
            }
            return 0;
        } catch (ClassCastException e) {
            throw new org.python.exceptions.RuntimeError("Can't compare a Python object with non-Python object.");
        }
    }

    // public String toString() {
    //     return (String) __str__().value;
    // }

    protected void finalize() throws Throwable {
        try {
            this.__del__();
        }
        finally {
            super.finalize();
        }
    }

    /**
     * Python interface compatibility
     * Section 3.3.1 - Basic customization
     */
    // public void __new__() {
    //     throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__new__'");
    // }

    // public void __init__() {
    //     throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__init__'");
    // }

    public void __del__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__del__'");
    }

    public org.python.types.Str __repr__() {
        return new org.python.types.Str(this.toString());
    }

    public org.python.types.Str __str__() {
        return this.__repr__();
    }

    public org.python.types.Bytes __bytes__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__bytes__'");
    }

    public org.python.types.Str __format__() {
        throw new org.python.exceptions.NotImplementedError("'" + this.getPythonName() + ".__format__' has not been implemented");
    }


    public org.python.Object __lt__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __lt__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__lt__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __lt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + this.getPythonName() + ".__lt__' has not been implemented");
    }


    public org.python.Object __le__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __le__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__le__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __le__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + this.getPythonName() + ".__le__' has not been implemented");
    }


    public org.python.Object __eq__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __eq__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__eq__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __eq__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + this.getPythonName() + ".__eq__' has not been implemented");
    }


    public org.python.Object __ne__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ne__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__ne__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __ne__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + this.getPythonName() + ".__ne__' has not been implemented");
    }

    public org.python.Object __gt__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __gt__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__gt__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __gt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + this.getPythonName() + ".__gt__' has not been implemented");
    }

    public org.python.Object __ge__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ge__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__ge__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __ge__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + this.getPythonName() + ".__ge__' has not been implemented");
    }

    public org.python.types.Int __hash__() {
        return new org.python.types.Int(this.hashCode());
    }

    public org.python.types.Bool __bool__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__bool__'");
    }


    /**
     * Section 3.3.2 - Emulating container types
     */

    public org.python.Object __getattr__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __getattr__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            if (args[0] instanceof org.python.types.Str) {
                return this.__getattr__(((org.python.types.Str) args[0]).value);
            } else {
                throw new org.python.exceptions.TypeError("getattr(): attribute name must be string");
            }
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __getattr__(org.python.Object name) {
        if (name instanceof org.python.types.Str) {
            return this.__getattr__(((org.python.types.Str) name).value);
        } else {
            throw new org.python.exceptions.TypeError("getattr(): attribute name must be string");
        }
    }

    public org.python.Object __getattr__(java.lang.String name) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__getattr__'");
    }

    public org.python.Object __getattribute__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __getattribute__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            if (args[0] instanceof org.python.types.Str) {
                return this.__getattribute__(((org.python.types.Str) args[0]).value);
            } else {
                throw new org.python.exceptions.TypeError("__getattribute__(): attribute name must be string");
            }
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __getattribute__(org.python.Object name) {
        if (name instanceof org.python.types.Str) {
            return this.__getattribute__(((org.python.types.Str) name).value);
        } else {
            throw new org.python.exceptions.TypeError("__getattribute__: attribute name must be string");
        }
    }

    public org.python.Object __getattribute__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("'" + this.getPythonName() + ".__getattribute__' has not been implemented");
    }

    public void __setattr__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __setattr__ doesn't take keyword arguments");
        }
        if (args.length == 2) {
            if (args[0] instanceof org.python.types.Str) {
                this.__setattr__(((org.python.types.Str) args[0]).value, args[1]);
            } else {
                throw new org.python.exceptions.TypeError("delattr(): attribute name must be string");
            }
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 2 arguments, got " + args.length);
        }
    }

    public void __setattr__(org.python.Object name, org.python.Object value) {
        if (name instanceof org.python.types.Str) {
            this.__setattr__(((org.python.types.Str) name).value, value);
        } else {
            throw new org.python.exceptions.TypeError("delattr(): attribute name must be string");
        }
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        throw new org.python.exceptions.NotImplementedError("'" + this.getPythonName() + ".__setattr__' has not been implemented");
    }

    public void __delattr__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __delattr__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            if (args[0] instanceof org.python.types.Str) {
                this.__delattr__(((org.python.types.Str) args[0]).value);
            } else {
                throw new org.python.exceptions.TypeError("delattr(): attribute name must be string");
            }
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __delattr__(org.python.Object name) {
        if (name instanceof org.python.types.Str) {
            this.__delattr__(((org.python.types.Str) name).value);
        } else {
            throw new org.python.exceptions.TypeError("deltattr(): attribute name must be string");
        }
    }

    public void __delattr__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("'" + this.getPythonName() + ".__delattr__' has not been implemented");
    }

    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("'" + this.getPythonName() + ".__dir__' has not been implemented");
    }


    /**
     * Section 3.3.4 - Customizing instance and subclass checks
     */
    public org.python.Object __instancecheck__(org.python.Object instance) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__instancecheck__'");
    }

    public org.python.Object __subclasscheck__(org.python.Object subclass) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__subclasscheck__'");
    }


    /**
     * Section 3.3.5 - Emulating callable objects
     */
    public org.python.Object __call__(org.python.Object... args) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__call__'");
    }


    /**
     * Section 3.3.6 - Emulating container types
     */

    public org.python.types.Int __len__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__len__'");
    }

    public org.python.types.Int __length_hint__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__length_hint__'");
    }


    public org.python.Object __getitem__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __getitem__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__getitem__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __getitem__(org.python.Object index) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__getitem__'");
    }

    public org.python.Object __getitem__(int index) {
        return this.__getitem__(new org.python.types.Int(index));
    }


    public org.python.Object __missing__(org.python.Object key) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__missing__'");
    }


    public void __setitem__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __setitem__ doesn't take keyword arguments");
        }
        if (args.length == 2) {
            this.__setitem__(args[0], args[1]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 2 arguments, got " + args.length);
        }
    }

    public void __setitem__(org.python.Object index, org.python.Object value) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__setitem__'");
    }

    public void __setitem__(int index, org.python.Object value) {
        this.__setitem__(new org.python.types.Int(index), value);
    }


    public void __delitem__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __delitem__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            this.__delitem__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __delitem__(org.python.Object index) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__delitem__'");
    }

    public void __delitem__(int index) {
        this.__delitem__(new org.python.types.Int(index));
    }


    public org.python.Iterable __iter__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__iter__'");
    }

    public org.python.Iterable __reversed__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__reversed__'");
    }

    public org.python.types.Bool __contains__(org.python.Object item) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__contains__'");
    }


    /**
     * Section 3.3.7 - Emulating numeric types
     */

    public org.python.Object __add__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __add__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__add__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __add__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__add__'");
    }


    public org.python.Object __sub__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __sub__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__sub__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __sub__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__sub__'");
    }


    public org.python.Object __mul__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __mul__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__mul__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __mul__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__mul__'");
    }


    public org.python.Object __truediv__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __truediv__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__truediv__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __truediv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__truediv__'");
    }


    public org.python.Object __floordiv__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __floordiv__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__floordiv__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __floordiv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__floordiv__'");
    }


    public org.python.Object __mod__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __mod__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__mod__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __mod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__mod__'");
    }


    public org.python.Object __divmod__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __divmod__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__divmod__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __divmod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__divmod__'");
    }


    public org.python.Object __pow__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __pow__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__pow__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __pow__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__pow__'");
    }


    public org.python.Object __lshift__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __lshift__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__lshift__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __lshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__lshift__'");
    }


    public org.python.Object __rshift__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rshift__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__rshift__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __rshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__rshift__'");
    }


    public org.python.Object __and__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __and__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__and__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __and__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__and__'");
    }


    public org.python.Object __xor__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __xor__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__xor__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __xor__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__xor__'");
    }


    public org.python.Object __or__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __or__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__or__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __or__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__or__'");
    }


    public org.python.Object __radd__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __radd__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__radd__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __radd__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__radd__'");
    }


    public org.python.Object __rsub__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rsub__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__rsub__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __rsub__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__rsub__'");
    }


    public org.python.Object __rmul__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rmul__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__rmul__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __rmul__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__rmul__'");
    }


    public org.python.Object __rtruediv__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rtruediv__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__rtruediv__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __rtruediv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__rtruediv__'");
    }


    public org.python.Object __rfloordiv__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rfloordiv__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__rfloordiv__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __rfloordiv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__rfloordiv__'");
    }


    public org.python.Object __rmod__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rmod__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__rmod__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __rmod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__rmod__'");
    }


    public org.python.Object __rdivmod__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rdivmod__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__rdivmod__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __rdivmod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__rdivmod__'");
    }


    public org.python.Object __rpow__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rpow__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__rpow__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __rpow__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__rpow__'");
    }


    public org.python.Object __rlshift__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rlshift__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__rlshift__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __rlshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__rlshift__'");
    }


    public org.python.Object __rrshift__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rrshift__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__rrshift__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __rrshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__rrshift__'");
    }


    public org.python.Object __rand__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rand__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__rand__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __rand__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__rand__'");
    }


    public org.python.Object __rxor__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rxor__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__rxor__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __rxor__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__rxor__'");
    }


    public org.python.Object __ror__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ror__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__ror__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __ror__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__ror__'");
    }


    public void __iadd__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __iadd__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            this.__iadd__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __iadd__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__iadd__'");
    }


    public void __isub__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __isub__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            this.__isub__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __isub__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__isub__'");
    }


    public void __imul__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __imul__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            this.__imul__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __imul__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__imul__'");
    }


    public void __itruediv__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __itruediv__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            this.__itruediv__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __itruediv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__itruediv__'");
    }


    public void __ifloordiv__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ifloordiv__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            this.__ifloordiv__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __ifloordiv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__ifloordiv__'");
    }


    public void __imod__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __imod__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            this.__imod__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __imod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__im__'");
    }


    public void __ipow__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ipow__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            this.__ipow__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __ipow__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__ipow__'");
    }


    public void __ilshift__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ilshift__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            this.__ilshift__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __ilshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__ilshi__'");
    }


    public void __irshift__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __irshift__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            this.__irshift__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __irshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__irshi__'");
    }


    public void __iand__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __iand__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            this.__iand__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __iand__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__ia__'");
    }


    public void __ixor__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ixor__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            this.__ixor__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __ixor__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__ixor__'");
    }


    public void __ior__(org.python.Object [] args, java.util.Hashtable kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ior__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            this.__ior__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __ior__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__ior__'");
    }


    public org.python.Object __neg__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__neg__'");
    }

    public org.python.Object __pos__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__pos__'");
    }

    public org.python.Object __abs__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__abs__'");
    }

    public org.python.Object __invert__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__invert__'");
    }


    public org.python.Object __not__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__not__'");
    }

    public org.python.Object __complex__(org.python.Object [] args, java.util.Hashtable kwargs) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__complex__'");
    }


    public org.python.types.Int __int__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__int__'");
    }

    public org.python.types.Float __float__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__float__'");
    }

    public org.python.Object __round__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__round__'");
    }


    /**
     * Section 3.3.8 - With statement context
     */
    public org.python.Object __enter__() {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__enter__'");
    }

    public org.python.Object __exit__(org.python.Object exc_type, org.python.Object exc_value, org.python.Object traceback) {
        throw new org.python.exceptions.AttributeError(this.getPythonName() + " has no attribute '__exit__'");
    }
}
