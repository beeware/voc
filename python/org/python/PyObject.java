package org.python;

import java.lang.reflect.Type;
import java.util.Hashtable;
import java.util.Set;
import java.util.Map;
import java.util.ArrayList;

import org.python.exceptions.NotImplementedError;

public class PyObject {
    static public String __name__;
    static public String __module__;
    static public String __qualname__;

    public Type type;
    public Object value;

    static {
        // Field[] declaredFields = String.class.getDeclaredFields();
        // List<Field> staticFields = new ArrayList<Field>();
        // for (Field field : declaredFields) {
        //     if (java.lang.reflect.Modifier.isStatic(field.getModifiers())) {
        //         staticFields.add(field);
        //     }
        // }
    }

    /**
     * Copy Constructor
     */
    public PyObject(Object v, Type t) {
        value = v;
        type = t;
    }

    public PyObject() {
        type = Object.class;
        value = new Hashtable<String, PyObject>();
    }

    public PyObject(boolean v) {
        type = Boolean.class;
        value = v;
    }

    public PyObject(byte v) {
        type = Long.class;
        value = (long)v;
    }

    public PyObject(short v) {
        type = Long.class;
        value = (long)v;
    }

    public PyObject(int v) {
        type = Long.class;
        value = (long)v;
    }

    public PyObject(long v) {
        type = Long.class;
        value = v;
    }

    public PyObject(float v) {
        type = Float.class;
        value = (double)v;
    }

    public PyObject(double v) {
        type = Float.class;
        value = v;
    }

    public PyObject(char v) {
        type = String.class;
        value = Character.toString(v);
    }

    public PyObject(String v) {
        type = String.class;
        value = v;
    }

    public PyObject(Map v) {
        type = Map.class;
        value = v;
    }

    public PyObject(Set v) {
        type = Set.class;
        value = v;
    }

    public PyObject(ArrayList v) {
        type = ArrayList.class;
        value = v;
    }

    /**
     * Proxy Java object methods onto their Python counterparts.
     */

    public boolean equals(PyObject other) {
        return (boolean) __eq__(other).value;
    }

    public int compareTo(PyObject other) {
        if ((boolean) __lt__(other).value) {
            return -1;
        } else if ((boolean) __gt__(other).value) {
            return 1;
        }
        return 0;
    }

    public String toString() {
        return (String) __str__().value;
    }

    protected void finalize() throws Throwable {
         try {
             this.__del__();
         } finally {
             super.finalize();
         }
     }
    /**
     * Python interface compatibility
     * Section 3.3.1 - Basic customization
     */

    // public void __new__() {
    // }

    // public void __init__() {
    // }

    public void __del__() {
    }

    public PyObject __repr__() {
        return new PyObject("<PyObject: " + this.type + ">");
    }

    public PyObject __str__() {
        if (type == String.class) {
            return new PyObject((String) value);
        }
        else if (type == Long.class) {
            return new PyObject(((Long) value).toString());
        }
        return this.__repr__();
    }

    public PyObject __bytes__() {
        throw new NotImplementedError("Object method __bytes__ not implemented");
    }

    public PyObject __format__() {
        throw new NotImplementedError("Object method __format__ not implemented");
    }

    public PyObject __lt__(PyObject other) {
        throw new NotImplementedError("Object method __lt__ not implemented");
    }

    public PyObject __le__(PyObject other) {
        throw new NotImplementedError("Object method __le__ not implemented");
    }

    public PyObject __eq__(PyObject other) {
        throw new NotImplementedError("Object method __eq__ not implemented");
    }

    public PyObject __ne__(PyObject other) {
        throw new NotImplementedError("Object method __ne__ not implemented");
    }

    public PyObject __gt__(PyObject other) {
        throw new NotImplementedError("Object method __gt__ not implemented");
    }

    public PyObject __ge__(PyObject other) {
        throw new NotImplementedError("Object method __ge__ not implemented");
    }

    public PyObject __hash__() {
        return new PyObject(this.hashCode());
    }

    public PyObject __bool__() {
        throw new NotImplementedError("Object method __bool__ not implemented");
    }

    /**
     * Section 3.3.4 - Customizing instance and subclass checks
     */
    public PyObject __instancecheck__(PyObject instance) {
        throw new NotImplementedError("Object method __instancecheck__ not implemented");
    }

    public PyObject __subclasscheck__(PyObject subclass) {
        throw new NotImplementedError("Object method __subclasscheck__ not implemented");
    }

    /**
     * Section 3.3.5 - Emulating callable objects
     */
    public void __call__(PyObject... args) {
        throw new NotImplementedError("Object method __call__ not implemented");
    }

    /**
     * Section 3.3.6 - Emulating container types
     */

    public PyObject __len__() {
        throw new NotImplementedError("Object method __len__ not implemented");
    }

    public PyObject __length_hint__() {
        throw new NotImplementedError("Object method __length__ not implemented");
    }

    public PyObject __getitem__(PyObject key) {
        throw new NotImplementedError("Object method __getitem__ not implemented");
    }

    public PyObject __missing__(PyObject key) {
        throw new NotImplementedError("Object method __setitem__ not implemented");
    }

    public void __setitem__(PyObject key, PyObject value) {
        throw new NotImplementedError("Object method __setitem__ not implemented");
    }

    public void __delattr__(PyObject attr) {
        throw new NotImplementedError("Object method __delattr__ not implemented");
    }

    public PyObject __iter__() {
        throw new NotImplementedError("Object method __iter__ not implemented");
    }

    public PyObject __reversed__() {
        throw new NotImplementedError("Object method __reversed__ not implemented");
    }

    public PyObject __contains__(PyObject item) {
        throw new NotImplementedError("Object method __reversed__ not implemented");
    }

    /**
     * Section 3.3.7 - Emulating numeric types
     */

    public PyObject __add__(PyObject other) {
        // System.out.println("ADD " + this.type + " TO " + other.type);
        if (this.type == String.class) {
            if (other.type == String.class) {
                return new PyObject(((String) this.value) + ((String) other.value));
            } else if (other.type == Long.class) {
            } else if (other.type == Float.class) {
            } else if (other.type == Map.class) {
            } else if (other.type == Set.class) {
            } else if (other.type == Object.class) {
            } else if (other.type == ArrayList.class) {
            }
        } else if (this.type == Long.class) {
            if (other.type == String.class) {
            } else if (other.type == Long.class) {
                return new PyObject(((Long) this.value) + ((Long) other.value));
            } else if (other.type == Float.class) {
            } else if (other.type == Map.class) {
            } else if (other.type == Set.class) {
            } else if (other.type == Object.class) {
            } else if (other.type == ArrayList.class) {
            }
        } else if (this.type == Float.class) {
        } else if (this.type == Map.class) {
        } else if (this.type == Set.class) {
        } else if (this.type == Object.class) {
        } else if (this.type == ArrayList.class) {
        }
        return null;
    }

    public PyObject __sub__(PyObject other) {
        return null;
    }

    public PyObject __mul__(PyObject other) {
        // System.out.println("MUL " + this.type + " TO " + other.type);
        if (this.type == String.class) {
        } else if (this.type == Long.class) {
            if (other.type == String.class) {
            } else if (other.type == Long.class) {
                return new PyObject(((Long) this.value) * ((Long) other.value));
            } else if (other.type == Float.class) {
            } else if (other.type == Map.class) {
            } else if (other.type == Set.class) {
            } else if (other.type == Object.class) {
            } else if (other.type == ArrayList.class) {
            }
        } else if (this.type == Float.class) {
        } else if (this.type == Map.class) {
        } else if (this.type == Set.class) {
        } else if (this.type == Object.class) {
        } else if (this.type == ArrayList.class) {
        }
        return null;

    }

    public PyObject __truediv__(PyObject other) {
        return null;
    }

    public PyObject __floordiv__(PyObject other) {
        return null;
    }

    public PyObject __mod__(PyObject other) {
        return null;
    }

    public PyObject __divmod__(PyObject other) {
        return null;
    }

    public PyObject __pow__(PyObject other) {
        // System.out.println("POW " + this.type + " TO " + other.type);
        if (this.type == String.class) {
        } else if (this.type == Long.class) {
            if (other.type == String.class) {
            } else if (other.type == Long.class) {
                return new PyObject((long)Math.pow((Long) this.value, (Long) other.value));
            } else if (other.type == Float.class) {
            } else if (other.type == Map.class) {
            } else if (other.type == Set.class) {
            } else if (other.type == Object.class) {
            } else if (other.type == ArrayList.class) {
            }
        } else if (this.type == Float.class) {
        } else if (this.type == Map.class) {
        } else if (this.type == Set.class) {
        } else if (this.type == Object.class) {
        } else if (this.type == ArrayList.class) {
        }
        return null;
    }

    public PyObject __lshift__(PyObject other) {
        return null;
    }

    public PyObject __rshift__(PyObject other) {
        return null;
    }

    public PyObject __and__(PyObject other) {
        return null;
    }

    public PyObject __xor__(PyObject other) {
        return null;
    }

    public PyObject __or__(PyObject other) {
        return null;
    }

    public PyObject __radd__(PyObject other) {
        return other.__add__(this);
    }

    public PyObject __rsub__(PyObject other) {
        return other.__sub__(this);
    }

    public PyObject __rmul__(PyObject other) {
        return other.__mul__(this);
    }

    public PyObject __rtruediv__(PyObject other) {
        return other.__truediv__(this);
    }

    public PyObject __rfloordiv__(PyObject other) {
        return other.__floordiv__(this);
    }

    public PyObject __rmod__(PyObject other) {
        return other.__mod__(this);
    }

    public PyObject __rdivmod__(PyObject other) {
        return other.__divmod__(this);
    }

    public PyObject __rpow__(PyObject other) {
        return other.__pow__(this);
    }

    public PyObject __rlshift__(PyObject other) {
        return other.__lshift__(this);
    }

    public PyObject __rrshift__(PyObject other) {
        return other.__rshift__(this);
    }

    public PyObject __rand__(PyObject other) {
        return other.__and__(this);
    }

    public PyObject __rxor__(PyObject other) {
        return other.__xor__(this);
    }

    public PyObject __ror__(PyObject other) {
        return other.__or__(this);
    }


    public void __iadd__(PyObject other) {
        this.value = this.__add__(other).value;
    }

    public void __isub__(PyObject other) {
        this.value = this.__sub__(other).value;
    }

    public void __imul__(PyObject other) {
        this.value = this.__mul__(other).value;
    }

    public void __itruediv__(PyObject other) {
        this.value = this.__truediv__(other).value;
    }

    public void __ifloordiv__(PyObject other) {
        this.value = this.__floordiv__(other).value;
    }

    public void __imod__(PyObject other) {
        this.value = this.__mod__(other).value;
    }

    public void __ipow__(PyObject other) {
        this.value = this.__pow__(other).value;
    }

    public void __ilshift__(PyObject other) {
        this.value = this.__lshift__(other).value;
    }

    public void __irshift__(PyObject other) {
        this.value = this.__rshift__(other).value;
    }

    public void __iand__(PyObject other) {
        this.value = this.__and__(other).value;
    }

    public void __ixor__(PyObject other) {
        this.value = this.__xor__(other).value;
    }

    public void __ior__(PyObject other) {
        this.value = this.__or__(other).value;
    }

    public PyObject __neg__() {
        throw new NotImplementedError("Object method __neg__ not implemented");
    }

    public PyObject __pos__() {
        throw new NotImplementedError("Object method __pos__ not implemented");
    }

    public PyObject __abs__() {
        throw new NotImplementedError("Object method __abs__ not implemented");
    }

    public PyObject __invert__() {
        throw new NotImplementedError("Object method __invert__ not implemented");
    }

    public PyObject __not__() {
        return new PyObject(!((boolean)(__bool__().value)));
    }

    public PyObject __complex__(PyObject other) {
        throw new NotImplementedError("Object method __complex__ not implemented");
    }

    public PyObject __int__() {
        return new PyObject((int) this.value);
    }

    public PyObject __float__() {
        return new PyObject((float) this.value);
    }

    public PyObject __round__() {
        throw new NotImplementedError("Object method __round__ not implemented");
    }

    /**
     * Section 3.3.8 - With statement context
     */
    public PyObject __enter__() {
        throw new NotImplementedError("Object method __enter__ not implemented");
    }

    public PyObject __exit__(PyObject exc_type, PyObject exc_value, PyObject traceback) {
        throw new NotImplementedError("Object method __exit__ not implemented");
    }

}
