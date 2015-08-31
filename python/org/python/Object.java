package org.python;

import java.lang.reflect.Type;
import java.util.Hashtable;
import java.util.Set;
import java.util.Map;
import java.util.ArrayList;

import org.python.exceptions.NotImplementedError;

public class Object {
    public Type type;
    public java.lang.Object value;

    /**
     * Copy Constructor
     */
    public Object(org.python.Object v, Type t) {
        value = v;
        type = t;
    }

    public Object() {
        type = java.lang.Object.class;
        value = new Hashtable<String, org.python.Object>();
    }

    public Object(boolean v) {
        type = Boolean.class;
        value = v;
    }

    public Object(byte v) {
        type = Long.class;
        value = (long)v;
    }

    public Object(short v) {
        type = Long.class;
        value = (long)v;
    }

    public Object(int v) {
        type = Long.class;
        value = (long)v;
    }

    public Object(long v) {
        type = Long.class;
        value = v;
    }

    public Object(float v) {
        type = Float.class;
        value = (double)v;
    }

    public Object(double v) {
        type = Float.class;
        value = v;
    }

    public Object(char v) {
        type = String.class;
        value = Character.toString(v);
    }

    public Object(String v) {
        type = String.class;
        value = v;
    }

    public Object(Map v) {
        type = Map.class;
        value = v;
    }

    public Object(Set v) {
        type = Set.class;
        value = v;
    }

    public Object(ArrayList v) {
        type = ArrayList.class;
        value = v;
    }

    /**
     * Proxy Java object methods onto their Python counterparts.
     */

    public boolean equals(org.python.Object other) {
        return (boolean) __eq__(other).value;
    }

    public int compareTo(org.python.Object other) {
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

    public org.python.Object __repr__() {
        return new org.python.Object("<org.python.Object: " + this.type + ">");
    }

    public org.python.Object __str__() {
        if (type == String.class) {
            return new org.python.Object((String) value);
        }
        else if (type == Long.class) {
            return new org.python.Object(((Long) value).toString());
        }
        return this.__repr__();
    }

    public org.python.Object __bytes__() {
        throw new NotImplementedError("Object method __bytes__ not implemented");
    }

    public org.python.Object __format__() {
        throw new NotImplementedError("Object method __format__ not implemented");
    }

    public org.python.Object __lt__(org.python.Object other) {
        throw new NotImplementedError("Object method __lt__ not implemented");
    }

    public org.python.Object __le__(org.python.Object other) {
        throw new NotImplementedError("Object method __le__ not implemented");
    }

    public org.python.Object __eq__(org.python.Object other) {
        throw new NotImplementedError("Object method __eq__ not implemented");
    }

    public org.python.Object __ne__(org.python.Object other) {
        throw new NotImplementedError("Object method __ne__ not implemented");
    }

    public org.python.Object __gt__(org.python.Object other) {
        throw new NotImplementedError("Object method __gt__ not implemented");
    }

    public org.python.Object __ge__(org.python.Object other) {
        throw new NotImplementedError("Object method __ge__ not implemented");
    }

    public org.python.Object __hash__() {
        return new org.python.Object(this.hashCode());
    }

    public org.python.Object __bool__() {
        throw new NotImplementedError("Object method __bool__ not implemented");
    }

    /**
     * Section 3.3.4 - Customizing instance and subclass checks
     */
    public org.python.Object __instancecheck__(org.python.Object instance) {
        throw new NotImplementedError("Object method __instancecheck__ not implemented");
    }

    public org.python.Object __subclasscheck__(org.python.Object subclass) {
        throw new NotImplementedError("Object method __subclasscheck__ not implemented");
    }

    /**
     * Section 3.3.5 - Emulating callable objects
     */
    public void __call__(org.python.Object... args) {
        throw new NotImplementedError("Object method __call__ not implemented");
    }

    /**
     * Section 3.3.6 - Emulating container types
     */

    public org.python.Object __len__() {
        throw new NotImplementedError("Object method __len__ not implemented");
    }

    public org.python.Object __length_hint__() {
        throw new NotImplementedError("Object method __length__ not implemented");
    }

    public org.python.Object __getitem__(org.python.Object key) {
        throw new NotImplementedError("Object method __getitem__ not implemented");
    }

    public org.python.Object __missing__(org.python.Object key) {
        throw new NotImplementedError("Object method __setitem__ not implemented");
    }

    public void __setitem__(org.python.Object key, org.python.Object value) {
        throw new NotImplementedError("Object method __setitem__ not implemented");
    }

    public void __delattr__(org.python.Object attr) {
        throw new NotImplementedError("Object method __delattr__ not implemented");
    }

    public org.python.Object __iter__() {
        throw new NotImplementedError("Object method __iter__ not implemented");
    }

    public org.python.Object __reversed__() {
        throw new NotImplementedError("Object method __reversed__ not implemented");
    }

    public org.python.Object __contains__(org.python.Object item) {
        throw new NotImplementedError("Object method __reversed__ not implemented");
    }

    /**
     * Section 3.3.7 - Emulating numeric types
     */

    public org.python.Object __add__(org.python.Object other) {
        // System.out.println("ADD " + this.type + " TO " + other.type);
        if (this.type == String.class) {
            if (other.type == String.class) {
                return new org.python.Object(((String) this.value) + ((String) other.value));
            } else if (other.type == Long.class) {
                return new org.python.Object(((String) this.value) + ((long) other.value));
            } else if (other.type == Float.class) {
                return new org.python.Object(((String) this.value) + ((float) other.value));
            } else if (other.type == Map.class) {
            } else if (other.type == Set.class) {
            } else if (other.type == Object.class) {
            } else if (other.type == ArrayList.class) {
            }
        } else if (this.type == Long.class) {
            if (other.type == String.class) {
                return new org.python.Object(((Long) other.value) + ((String) this.value));
            } else if (other.type == Long.class) {
                return new org.python.Object(((Long) this.value) + ((Long) other.value));
            } else if (other.type == Float.class) {
                return new org.python.Object(((float) this.value) + ((float) other.value));
            } else if (other.type == Map.class) {
            } else if (other.type == Set.class) {
            } else if (other.type == Object.class) {
            } else if (other.type == ArrayList.class) {
            }
        } else if (this.type == Float.class) {
            if (other.type == String.class) {
                return new org.python.Object(((float) other.value) + ((String) this.value));
            } else if (other.type == Long.class) {
                return new org.python.Object(((float) this.value) + ((float) other.value));
            } else if (other.type == Float.class) {
            } else if (other.type == Map.class) {
            } else if (other.type == Set.class) {
            } else if (other.type == Object.class) {
            } else if (other.type == ArrayList.class) {
            }
        } else if (this.type == Map.class) {
        } else if (this.type == Set.class) {
        } else if (this.type == Object.class) {
        } else if (this.type == ArrayList.class) {
        }
        return null;
    }

    public org.python.Object __sub__(org.python.Object other) {
        return null;
    }

    public org.python.Object __mul__(org.python.Object other) {
        // System.out.println("MUL " + this.type + " TO " + other.type);
        if (this.type == String.class) {
        } else if (this.type == Long.class) {
            if (other.type == String.class) {
            } else if (other.type == Long.class) {
                return new org.python.Object(((Long) this.value) * ((Long) other.value));
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

    public org.python.Object __truediv__(org.python.Object other) {
        return null;
    }

    public org.python.Object __floordiv__(org.python.Object other) {
        return null;
    }

    public org.python.Object __mod__(org.python.Object other) {
        return null;
    }

    public org.python.Object __divmod__(org.python.Object other) {
        return null;
    }

    public org.python.Object __pow__(org.python.Object other) {
        // System.out.println("POW " + this.type + " TO " + other.type);
        if (this.type == String.class) {
        } else if (this.type == Long.class) {
            if (other.type == String.class) {
            } else if (other.type == Long.class) {
                return new org.python.Object((long)Math.pow((Long) this.value, (Long) other.value));
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

    public org.python.Object __lshift__(org.python.Object other) {
        return null;
    }

    public org.python.Object __rshift__(org.python.Object other) {
        return null;
    }

    public org.python.Object __and__(org.python.Object other) {
        return null;
    }

    public org.python.Object __xor__(org.python.Object other) {
        return null;
    }

    public org.python.Object __or__(org.python.Object other) {
        return null;
    }

    public org.python.Object __radd__(org.python.Object other) {
        return other.__add__(this);
    }

    public org.python.Object __rsub__(org.python.Object other) {
        return other.__sub__(this);
    }

    public org.python.Object __rmul__(org.python.Object other) {
        return other.__mul__(this);
    }

    public org.python.Object __rtruediv__(org.python.Object other) {
        return other.__truediv__(this);
    }

    public org.python.Object __rfloordiv__(org.python.Object other) {
        return other.__floordiv__(this);
    }

    public org.python.Object __rmod__(org.python.Object other) {
        return other.__mod__(this);
    }

    public org.python.Object __rdivmod__(org.python.Object other) {
        return other.__divmod__(this);
    }

    public org.python.Object __rpow__(org.python.Object other) {
        return other.__pow__(this);
    }

    public org.python.Object __rlshift__(org.python.Object other) {
        return other.__lshift__(this);
    }

    public org.python.Object __rrshift__(org.python.Object other) {
        return other.__rshift__(this);
    }

    public org.python.Object __rand__(org.python.Object other) {
        return other.__and__(this);
    }

    public org.python.Object __rxor__(org.python.Object other) {
        return other.__xor__(this);
    }

    public org.python.Object __ror__(org.python.Object other) {
        return other.__or__(this);
    }


    public void __iadd__(org.python.Object other) {
        this.value = this.__add__(other).value;
    }

    public void __isub__(org.python.Object other) {
        this.value = this.__sub__(other).value;
    }

    public void __imul__(org.python.Object other) {
        this.value = this.__mul__(other).value;
    }

    public void __itruediv__(org.python.Object other) {
        this.value = this.__truediv__(other).value;
    }

    public void __ifloordiv__(org.python.Object other) {
        this.value = this.__floordiv__(other).value;
    }

    public void __imod__(org.python.Object other) {
        this.value = this.__mod__(other).value;
    }

    public void __ipow__(org.python.Object other) {
        this.value = this.__pow__(other).value;
    }

    public void __ilshift__(org.python.Object other) {
        this.value = this.__lshift__(other).value;
    }

    public void __irshift__(org.python.Object other) {
        this.value = this.__rshift__(other).value;
    }

    public void __iand__(org.python.Object other) {
        this.value = this.__and__(other).value;
    }

    public void __ixor__(org.python.Object other) {
        this.value = this.__xor__(other).value;
    }

    public void __ior__(org.python.Object other) {
        this.value = this.__or__(other).value;
    }

    public org.python.Object __neg__() {
        throw new NotImplementedError("Object method __neg__ not implemented");
    }

    public org.python.Object __pos__() {
        throw new NotImplementedError("Object method __pos__ not implemented");
    }

    public org.python.Object __abs__() {
        throw new NotImplementedError("Object method __abs__ not implemented");
    }

    public org.python.Object __invert__() {
        throw new NotImplementedError("Object method __invert__ not implemented");
    }

    public org.python.Object __not__() {
        return new org.python.Object(!((boolean)(__bool__().value)));
    }

    public org.python.Object __complex__(org.python.Object other) {
        throw new NotImplementedError("Object method __complex__ not implemented");
    }

    public org.python.Object __int__() {
        return new org.python.Object((int) this.value);
    }

    public org.python.Object __float__() {
        return new org.python.Object((float) this.value);
    }

    public org.python.Object __round__() {
        throw new NotImplementedError("Object method __round__ not implemented");
    }

    /**
     * Section 3.3.8 - With statement context
     */
    public org.python.Object __enter__() {
        throw new NotImplementedError("Object method __enter__ not implemented");
    }

    public org.python.Object __exit__(org.python.Object exc_type, org.python.Object exc_value, org.python.Object traceback) {
        throw new NotImplementedError("Object method __exit__ not implemented");
    }

}
