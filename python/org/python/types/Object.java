package org.python.types;


public class Object {
    public java.lang.reflect.Type type;
    public java.lang.Object value;

    // FIXME: This should be a class, and it should be static, too.
    // public java.lang.String __class__;
    // FIXME: This should be static, and it shouldn't exist on primitives.
    // public java.lang.String __module__;

    String internalClassName() {
        return this.getClass().getName();
    }
    private void set_class_attributes() {
        // if (type == java.lang.String.class) {
        //     __class__ = "str";
        // } else if (type == java.lang.Boolean.class) {
        //     __class__ = "bool";
        // } else if (type == java.lang.Long.class) {
        //     __class__ = "int";
        // } else if (type == java.lang.Float.class) {
        //     __class__ = "float";
        // } else if (type == java.util.Map.class) {
        //     __class__ = "map";
        // } else if (type == java.util.Set.class) {
        //     __class__ = "set";
        // } else if (type == java.lang.Object.class) {
        //     String [] parts = getClass().getName().split("\\.");
        //     __class__ = parts[parts.length];

        //     __module__ = parts[0];
        //     for (int i = 1; i < parts.length - 1; i++) {
        //         __module__ += __module__ + "." + parts[i];
        //     }
        // } else if (type == java.util.ArrayList.class) {
        //     __class__ = "list";
        // } else if (type == java.lang.reflect.Method.class) {
        //     __class__ = "function";
        // } else if (type == java.lang.reflect.Constructor.class) {
        //     __class__ = "type";
        // } else {
        //     throw new org.python.exceptions.RuntimeError("Unknown type " + type);
        // }
    }

    /**
     * Copy Constructor
     */

    public Object(org.python.types.Object v) {
        if (v.type == java.lang.String.class) {
            value = v.value;
        } else if (v.type == java.lang.Boolean.class) {
            value = v.value;
        } else if (v.type == java.lang.Long.class) {
            value = v.value;
        } else if (v.type == java.lang.Float.class) {
            value = v.value;
        } else if (v.type == java.util.Map.class) {
        } else if (v.type == java.util.Set.class) {
        } else if (v.type == java.lang.Object.class) {
        } else if (v.type == java.util.ArrayList.class) {
        } else if (v.type == java.lang.reflect.Method.class) {
            value = v.value;
        } else if (v.type == java.lang.reflect.Constructor.class) {
            value = v.value;
        } else if (v.type == org.python.exceptions.BaseException.class) {
            value = v.value;
        } else {
            throw new org.python.exceptions.RuntimeError("Unknown type " + type);
        }
        type = v.type;
        set_class_attributes();
    }

    /**
     * Do-it-yourself constructor
     */
    public Object(java.lang.Object v, java.lang.reflect.Type t) {
        value = v;
        type = t;
        set_class_attributes();
    }

    /**
     * Specific type constructors
     */
    public Object() {
        // System.out.println("Create Object");
        type = java.lang.Object.class;
        value = new java.util.Hashtable<String, org.python.types.Object>();
        set_class_attributes();
    }

    public Object(boolean v) {
        // System.out.println("Create boolean");
        type = Boolean.class;
        value = v;
        set_class_attributes();
    }

    public Object(byte v) {
        // System.out.println("Create byte");
        type = Long.class;
        value = (long)v;
        set_class_attributes();
    }

    public Object(short v) {
        // System.out.println("Create short");
        type = Long.class;
        value = (long)v;
        set_class_attributes();
    }

    public Object(int v) {
        // System.out.println("Create int");
        type = Long.class;
        value = (long)v;
        set_class_attributes();
    }

    public Object(long v) {
        // System.out.println("Create long");
        type = Long.class;
        value = v;
        set_class_attributes();
    }

    public Object(float v) {
        // System.out.println("Create float");
        type = Float.class;
        value = (double)v;
        set_class_attributes();
    }

    public Object(double v) {
        // System.out.println("Create double");
        type = Float.class;
        value = v;
        set_class_attributes();
    }

    public Object(char v) {
        // System.out.println("Create char");
        type = String.class;
        value = Character.toString(v);
        set_class_attributes();
    }

    public Object(String v) {
        // System.out.println("Create String");
        type = String.class;
        value = v;
        set_class_attributes();
    }

    public Object(java.util.Map<org.python.types.Object, org.python.types.Object> v) {
        // System.out.println("Create Map");
        type = java.util.Map.class;
        value = v;
        set_class_attributes();
    }

    public Object(java.util.Set<org.python.types.Object> v) {
        // System.out.println("Create java.util.Set");
        type = java.util.Set.class;
        value = v;
        set_class_attributes();
    }

    public Object(java.util.ArrayList<org.python.types.Object> v) {
        // System.out.println("Create List");
        type = java.util.ArrayList.class;
        value = v;
        set_class_attributes();
    }

    public Object(org.python.exceptions.BaseException v) {
        // System.out.println("Create List");
        type = org.python.exceptions.BaseException.class;
        value = v;
        set_class_attributes();
    }

    /**
     * Proxy Java object methods onto their Python counterparts.
     */

    @SuppressWarnings("unchecked")
    public boolean equals(java.lang.Object other) {
        return (boolean) __eq__((org.python.types.Object) other).value;
    }

    public int compareTo(java.lang.Object other) {
        if (other instanceof org.python.types.Object) {
            if ((boolean) this.__lt__((org.python.types.Object) other).value) {
                return -1;
            } else if ((boolean) this.__gt__((org.python.types.Object) other).value) {
                return 1;
            }
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

    public org.python.types.Object __repr__() {
        return new org.python.types.Object("<PY:" + this.getClass() + " " + System.identityHashCode(this) + ">");
    }

    public org.python.types.Object __str__() {
        if (type == String.class) {
            return new org.python.types.Object((String) value);
        }
        else if (type == Long.class) {
            return new org.python.types.Object(((Long) value).toString());
        }
        return this.__repr__();
    }

    public org.python.types.Object __bytes__() {
        throw new org.python.exceptions.NotImplementedError("Object method __bytes__ not implemented");
    }

    public org.python.types.Object __format__() {
        throw new org.python.exceptions.NotImplementedError("Object method __format__ not implemented");
    }

    public org.python.types.Object __lt__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__lt__(other);
    }

    public org.python.types.Object __lt__(org.python.types.Object other) {
        // System.out.println("Comparison " + this.__repr__() + " < " + other.__repr__());
        boolean result = false;
        if (this.type == String.class) {
            if (other.type == String.class) {
                return new org.python.types.Object(((String) this.value) + ((String) other.value));
            } else if (other.type == Long.class) {
                return new org.python.types.Object(((String) this.value) + ((long) other.value));
            } else if (other.type == Float.class) {
                return new org.python.types.Object(((String) this.value) + ((float) other.value));
            } else if (other.type == java.util.Map.class) {
            } else if (other.type == java.util.Set.class) {
            } else if (other.type == org.python.types.Object.class) {
            } else if (other.type == java.util.ArrayList.class) {
            }
        } else if (this.type == Long.class) {
            if (other.type == String.class) {
            } else if (other.type == Long.class) {
                result = (long) this.value < (long) other.value;
            } else if (other.type == Float.class) {
            } else if (other.type == java.util.Map.class) {
            } else if (other.type == java.util.Set.class) {
            } else if (other.type == org.python.types.Object.class) {
            } else if (other.type == java.util.ArrayList.class) {
            }
        } else if (this.type == Float.class) {
            if (other.type == String.class) {
                return new org.python.types.Object(((float) other.value) + ((String) this.value));
            } else if (other.type == Long.class) {
                return new org.python.types.Object(((float) this.value) + ((float) other.value));
            } else if (other.type == Float.class) {
            } else if (other.type == java.util.Map.class) {
            } else if (other.type == java.util.Set.class) {
            } else if (other.type == org.python.types.Object.class) {
            } else if (other.type == java.util.ArrayList.class) {
            }
        } else if (this.type == java.util.Map.class) {
        } else if (this.type == java.util.Set.class) {
        } else if (this.type == org.python.types.Object.class) {
        } else if (this.type == java.util.ArrayList.class) {
        }
        return new org.python.types.Object(result);
    }

    public org.python.types.Object __le__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__le__(other);
    }

    public org.python.types.Object __le__(org.python.types.Object other) {
        throw new org.python.exceptions.NotImplementedError("Object method __le__ not implemented");
    }

    public org.python.types.Object __eq__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__eq__(other);
    }

    public org.python.types.Object __eq__(org.python.types.Object other) {
        // System.out.println("Comparison " + this.__repr__() + " < " + other.__repr__());
        boolean result = false;
        if (this.type == String.class) {
            if (other.type == String.class) {
                return new org.python.types.Object(((String) this.value) == ((String) other.value));
            } else if (other.type == Long.class) {
            } else if (other.type == Float.class) {
            } else if (other.type == java.util.Map.class) {
            } else if (other.type == java.util.Set.class) {
            } else if (other.type == org.python.types.Object.class) {
            } else if (other.type == java.util.ArrayList.class) {
            }
        } else if (this.type == Long.class) {
            if (other.type == String.class) {
            } else if (other.type == Long.class) {
                return new org.python.types.Object(((Long) this.value) == ((Long) other.value));
            } else if (other.type == Float.class) {
            } else if (other.type == java.util.Map.class) {
            } else if (other.type == java.util.Set.class) {
            } else if (other.type == org.python.types.Object.class) {
            } else if (other.type == java.util.ArrayList.class) {
            }
        } else if (this.type == Float.class) {
            if (other.type == String.class) {
            } else if (other.type == Long.class) {
            } else if (other.type == Float.class) {
                return new org.python.types.Object(((Float) this.value) == ((Float) other.value));
            } else if (other.type == java.util.Map.class) {
            } else if (other.type == java.util.Set.class) {
            } else if (other.type == org.python.types.Object.class) {
            } else if (other.type == java.util.ArrayList.class) {
            }
        } else if (this.type == java.util.Map.class) {
        } else if (this.type == java.util.Set.class) {
        } else if (this.type == org.python.types.Object.class) {
        } else if (this.type == java.util.ArrayList.class) {
        }
        return new org.python.types.Object(result);
    }

    public org.python.types.Object __ne__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__ne__(other);
    }

    public org.python.types.Object __ne__(org.python.types.Object other) {
        throw new org.python.exceptions.NotImplementedError("Object method __ne__ not implemented");
    }

    public org.python.types.Object __gt__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__gt__(other);
    }

    public org.python.types.Object __gt__(org.python.types.Object other) {
        throw new org.python.exceptions.NotImplementedError("Object method __gt__ not implemented");
    }

    public org.python.types.Object __ge__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__ge__(other);
    }

    public org.python.types.Object __ge__(org.python.types.Object other) {
        throw new org.python.exceptions.NotImplementedError("Object method __ge__ not implemented");
    }

    public org.python.types.Object __hash__() {
        return new org.python.types.Object(this.hashCode());
    }

    public org.python.types.Object __bool__() {
        throw new org.python.exceptions.NotImplementedError("Object method __bool__ not implemented");
    }

    /**
     * Section 3.3.2 - Emulating container types
     */
    // The cast back from java Object to Hashtable is, strictly speaking,
    // unchecked, but given we know it's an Object, we know value is a Map.
    @SuppressWarnings("unchecked")
    public org.python.types.Object __getattr__(java.lang.String name) {
        // System.out.println("GET " + name + " on " + this.__repr__());
        if (this.type == java.lang.Object.class) {
            // Look in the instance attributes
            org.python.types.Object obj = ((java.util.Hashtable<java.lang.String, org.python.types.Object>) this.value).get(name);
            if (obj != null) {
                return obj;
            } else {
                // Look in the class attributes
                try {
                    java.lang.reflect.Field field = this.getClass().getField("attrs");
                    obj = ((java.util.Hashtable<java.lang.String, org.python.types.Object>) field.get(this)).get(name);
                    if (obj != null) {
                        return obj;
                    } else {
                        throw new org.python.exceptions.AttributeError("'" + internalClassName() + "' has no attribute '" + name + "'");
                    }
                } catch(NoSuchFieldException e) {
                    throw new org.python.exceptions.AttributeError("'" + internalClassName() + "' has no class");
                } catch(IllegalAccessException e) {
                    throw new org.python.exceptions.AttributeError("Cannot access class attributes on '" + internalClassName() + "'");
                }
            }
        } else {
            throw new org.python.exceptions.AttributeError("'" + internalClassName() + "' has no attribute '" + name + "'");
        }
    }

    public org.python.types.Object __getattribute__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("Object method __getattr__ not implemented");
    }

    @SuppressWarnings("unchecked")
    // The cast back from java Object to Hashtable is, strictly speaking,
    // unchecked, but given we know it's an Object, we know value is a Map.
    public void __setattr__(java.lang.String name, org.python.types.Object obj) {
        // System.out.println("SET " + name + " on " + this.__repr__() + " TO " + obj.__repr__());
        if (this.type == java.lang.Object.class) {
            ((java.util.Hashtable<java.lang.String, org.python.types.Object>) this.value).put(name, obj);
            return;
        } else {
            throw new org.python.exceptions.AttributeError("'" + internalClassName() + "' object has no attribute '" + name + "'");
        }
    }

    public void __delattr__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("Object method __delattr__ not implemented");
    }

    public void __dir__() {
        throw new org.python.exceptions.NotImplementedError("Object method __dir__ not implemented");
    }

    /**
     * Section 3.3.4 - Customizing instance and subclass checks
     */
    public org.python.types.Object __instancecheck__(org.python.types.Object instance) {
        throw new org.python.exceptions.NotImplementedError("Object method __instancecheck__ not implemented");
    }

    public org.python.types.Object __subclasscheck__(org.python.types.Object subclass) {
        throw new org.python.exceptions.NotImplementedError("Object method __subclasscheck__ not implemented");
    }

    /**
     * Section 3.3.5 - Emulating callable objects
     */
    public void __call__(org.python.types.Object... args) {
        throw new org.python.exceptions.NotImplementedError("Object method __call__ not implemented");
    }

    /**
     * Section 3.3.6 - Emulating container types
     */

    public org.python.types.Object __len__() {
        throw new org.python.exceptions.NotImplementedError("Object method __len__ not implemented");
    }

    public org.python.types.Object __length_hint__() {
        throw new org.python.exceptions.NotImplementedError("Object method __length__ not implemented");
    }

    public org.python.types.Object __getitem__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object index = args[0];
        return this.__getitem__(index);
    }

    @SuppressWarnings("unchecked")
    public org.python.types.Object __getitem__(org.python.types.Object index) {
        // System.out.println("ADD " + this.__repr__() + " TO " + other.__repr__());

        if (this.type == String.class) {
            if (index.type == Long.class) {
                return this.__getitem__(((Long)index.value).intValue());
            } else {
                throw new org.python.exceptions.TypeError("string indices must be integers");
            }
        } else if (this.type == Long.class) {
        } else if (this.type == Float.class) {
        } else if (this.type == java.util.Map.class) {
            return ((java.util.Map<org.python.types.Object, org.python.types.Object>) this.value).get(index);
        } else if (this.type == java.util.Set.class) {
        } else if (this.type == org.python.types.Object.class) {
        } else if (this.type == java.util.ArrayList.class) {
            if (index.type == Long.class) {
                return this.__getitem__(((Long)index.value).intValue());
            } else {
                throw new org.python.exceptions.TypeError("list indices must be integers");
            }
        }
        throw new org.python.exceptions.NotImplementedError("Object method __getitem__ not implemented");
    }

    @SuppressWarnings("unchecked")
    public org.python.types.Object __getitem__(int index) {
        // System.out.println("ADD " + this.__repr__() + " TO " + other.__repr__());
        if (this.type == String.class) {
            java.lang.String val = (java.lang.String) this.value;

            if (index >= 0) {
                if (index >= val.length()) {
                    throw new org.python.exceptions.IndexError("string index out of range");
                } else {
                    return new org.python.types.Object(val.charAt(index));
                }
            } else {
                if (index < -val.length()) {
                    throw new org.python.exceptions.IndexError("string index out of range");
                } else {
                    return new org.python.types.Object(val.charAt(val.length() + index));
                }
            }
        } else if (this.type == Long.class) {
        } else if (this.type == Float.class) {
        } else if (this.type == java.util.Map.class) {
            return ((java.util.Map<org.python.types.Object, org.python.types.Object>) this.value).get(index);
        } else if (this.type == java.util.Set.class) {
        } else if (this.type == org.python.types.Object.class) {
        } else if (this.type == java.util.ArrayList.class) {
            java.util.ArrayList<org.python.types.Object> val = (java.util.ArrayList<org.python.types.Object>) this.value;

            if (index >= 0) {
                if (index >= val.size()) {
                    throw new org.python.exceptions.IndexError("list index out of range");
                } else {
                    return val.get(index);
                }
            } else {
                if (index < -val.size()) {
                    throw new org.python.exceptions.IndexError("list index out of range");
                } else {
                    return val.get(val.size() + index);
                }
            }
        }
        throw new org.python.exceptions.NotImplementedError("Object method __getitem__ not implemented");
    }

    public org.python.types.Object __missing__(org.python.types.Object key) {
        throw new org.python.exceptions.NotImplementedError("Object method __missing__ not implemented");
    }

    public void __setitem__(org.python.types.Object key, org.python.types.Object value) {
        throw new org.python.exceptions.NotImplementedError("Object method __setitem__ not implemented");
    }

    public org.python.types.Object __iter__() {
        if (this.type == String.class) {
        } else if (this.type == Long.class) {
        } else if (this.type == Float.class) {
        } else if (this.type == java.util.Map.class) {
        } else if (this.type == java.util.Set.class) {
        } else if (this.type == org.python.types.Object.class) {
        } else if (this.type == java.util.ArrayList.class) {
        }
        return null;
    }

    public org.python.types.Object __reversed__() {
        throw new org.python.exceptions.NotImplementedError("Object method __reversed__ not implemented");
    }

    public org.python.types.Object __contains__(org.python.types.Object item) {
        throw new org.python.exceptions.NotImplementedError("Object method __reversed__ not implemented");
    }

    /**
     * Section 3.3.7 - Emulating numeric types
     */

    public org.python.types.Object __add__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__add__(other);
    }

    public org.python.types.Object __add__(org.python.types.Object other) {
        // System.out.println("ADD " + this.__repr__() + " TO " + other.__repr__());
        if (this.type == String.class) {
            if (other.type == String.class) {
                return new org.python.types.Object(((String) this.value) + ((String) other.value));
            } else if (other.type == Long.class) {
                return new org.python.types.Object(((String) this.value) + ((long) other.value));
            } else if (other.type == Float.class) {
                return new org.python.types.Object(((String) this.value) + ((float) other.value));
            } else if (other.type == java.util.Map.class) {
            } else if (other.type == java.util.Set.class) {
            } else if (other.type == org.python.types.Object.class) {
            } else if (other.type == java.util.ArrayList.class) {
            }
        } else if (this.type == Long.class) {
            if (other.type == String.class) {
                return new org.python.types.Object(((Long) other.value) + ((String) this.value));
            } else if (other.type == Long.class) {
                return new org.python.types.Object(((Long) this.value) + ((Long) other.value));
            } else if (other.type == Float.class) {
                return new org.python.types.Object(((float) this.value) + ((float) other.value));
            } else if (other.type == java.util.Map.class) {
            } else if (other.type == java.util.Set.class) {
            } else if (other.type == org.python.types.Object.class) {
            } else if (other.type == java.util.ArrayList.class) {
            }
        } else if (this.type == Float.class) {
            if (other.type == String.class) {
                return new org.python.types.Object(((float) other.value) + ((String) this.value));
            } else if (other.type == Long.class) {
                return new org.python.types.Object(((float) this.value) + ((float) other.value));
            } else if (other.type == Float.class) {
            } else if (other.type == java.util.Map.class) {
            } else if (other.type == java.util.Set.class) {
            } else if (other.type == org.python.types.Object.class) {
            } else if (other.type == java.util.ArrayList.class) {
            }
        } else if (this.type == java.util.Map.class) {
        } else if (this.type == java.util.Set.class) {
        } else if (this.type == org.python.types.Object.class) {
        } else if (this.type == java.util.ArrayList.class) {
        }
        return null;
    }

    public org.python.types.Object __sub__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__sub__(other);
    }

    public org.python.types.Object __sub__(org.python.types.Object other) {
        return null;
    }

    public org.python.types.Object __mul__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__mul__(other);
    }

    public org.python.types.Object __mul__(org.python.types.Object other) {
        // System.out.println("MUL " + this.__repr__() + " BY " + other.__repr__());
        if (this.type == String.class) {
        } else if (this.type == Long.class) {
            if (other.type == String.class) {
            } else if (other.type == Long.class) {
                return new org.python.types.Object(((Long) this.value) * ((Long) other.value));
            } else if (other.type == Float.class) {
            } else if (other.type == java.util.Map.class) {
            } else if (other.type == java.util.Set.class) {
            } else if (other.type == org.python.types.Object.class) {
            } else if (other.type == java.util.ArrayList.class) {
            }
        } else if (this.type == Float.class) {
        } else if (this.type == java.util.Map.class) {
        } else if (this.type == java.util.Set.class) {
        } else if (this.type == org.python.types.Object.class) {
        } else if (this.type == java.util.ArrayList.class) {
        }
        return null;

    }

    public org.python.types.Object __truediv__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__truediv__(other);
    }

    public org.python.types.Object __truediv__(org.python.types.Object other) {
        return null;
    }

    public org.python.types.Object __floordiv__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__floordiv__(other);
    }

    public org.python.types.Object __floordiv__(org.python.types.Object other) {
        return null;
    }

    public org.python.types.Object __mod__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__mod__(other);
    }

    public org.python.types.Object __mod__(org.python.types.Object other) {
        return null;
    }

    public org.python.types.Object __divmod__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__divmod__(other);
    }

    public org.python.types.Object __divmod__(org.python.types.Object other) {
        return null;
    }

    public org.python.types.Object __pow__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__pow__(other);
    }

    public org.python.types.Object __pow__(org.python.types.Object other) {
        // System.out.println("POW " + this.__repr__() + " TO " + other.__repr__());
        if (this.type == String.class) {
        } else if (this.type == Long.class) {
            if (other.type == String.class) {
            } else if (other.type == Long.class) {
                return new org.python.types.Object((long)Math.pow((Long) this.value, (Long) other.value));
            } else if (other.type == Float.class) {
            } else if (other.type == java.util.Map.class) {
            } else if (other.type == java.util.Set.class) {
            } else if (other.type == org.python.types.Object.class) {
            } else if (other.type == java.util.ArrayList.class) {
            }
        } else if (this.type == Float.class) {
        } else if (this.type == java.util.Map.class) {
        } else if (this.type == java.util.Set.class) {
        } else if (this.type == org.python.types.Object.class) {
        } else if (this.type == java.util.ArrayList.class) {
        }
        return null;
    }

    public org.python.types.Object __lshift__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__lshift__(other);
    }

    public org.python.types.Object __lshift__(org.python.types.Object other) {
        return null;
    }

    public org.python.types.Object __rshift__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__rshift__(other);
    }

    public org.python.types.Object __rshift__(org.python.types.Object other) {
        return null;
    }

    public org.python.types.Object __and__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__and__(other);
    }

    public org.python.types.Object __and__(org.python.types.Object other) {
        return null;
    }

    public org.python.types.Object __xor__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__xor__(other);
    }

    public org.python.types.Object __xor__(org.python.types.Object other) {
        return null;
    }

    public org.python.types.Object __or__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__or__(other);
    }

    public org.python.types.Object __or__(org.python.types.Object other) {
        return null;
    }

    public org.python.types.Object __radd__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__radd__(other);
    }

    public org.python.types.Object __radd__(org.python.types.Object other) {
        return other.__add__(this);
    }

    public org.python.types.Object __rsub__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__rsub__(other);
    }

    public org.python.types.Object __rsub__(org.python.types.Object other) {
        return other.__sub__(this);
    }

    public org.python.types.Object __rmul__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__rmul__(other);
    }

    public org.python.types.Object __rmul__(org.python.types.Object other) {
        return other.__mul__(this);
    }

    public org.python.types.Object __rtruediv__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__rtruediv__(other);
    }

    public org.python.types.Object __rtruediv__(org.python.types.Object other) {
        return other.__truediv__(this);
    }

    public org.python.types.Object __rfloordiv__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__rfloordiv__(other);
    }

    public org.python.types.Object __rfloordiv__(org.python.types.Object other) {
        return other.__floordiv__(this);
    }

    public org.python.types.Object __rmod__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__rmod__(other);
    }

    public org.python.types.Object __rmod__(org.python.types.Object other) {
        return other.__mod__(this);
    }

    public org.python.types.Object __rdivmod__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__rdivmod__(other);
    }

    public org.python.types.Object __rdivmod__(org.python.types.Object other) {
        return other.__divmod__(this);
    }

    public org.python.types.Object __rpow__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__rpow__(other);
    }

    public org.python.types.Object __rpow__(org.python.types.Object other) {
        return other.__pow__(this);
    }

    public org.python.types.Object __rlshift__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__rlshift__(other);
    }

    public org.python.types.Object __rlshift__(org.python.types.Object other) {
        return other.__lshift__(this);
    }

    public org.python.types.Object __rrshift__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__rrshift__(other);
    }

    public org.python.types.Object __rrshift__(org.python.types.Object other) {
        return other.__rshift__(this);
    }

    public org.python.types.Object __rand__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__rand__(other);
    }

    public org.python.types.Object __rand__(org.python.types.Object other) {
        return other.__and__(this);
    }

    public org.python.types.Object __rxor__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__rxor__(other);
    }

    public org.python.types.Object __rxor__(org.python.types.Object other) {
        return other.__xor__(this);
    }

    public org.python.types.Object __ror__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        return this.__ror__(other);
    }

    public org.python.types.Object __ror__(org.python.types.Object other) {
        return other.__or__(this);
    }


    public void __iadd__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        this.value = this.__add__(args, kwargs).value;
    }

    public void __iadd__(org.python.types.Object other) {
        this.value = this.__add__(other).value;
    }

    public void __isub__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        this.value = this.__sub__(args, kwargs).value;
    }

    public void __isub__(org.python.types.Object other) {
        this.value = this.__sub__(other).value;
    }

    public void __imul__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        this.value = this.__mul__(args, kwargs).value;
    }

    public void __imul__(org.python.types.Object other) {
        this.value = this.__mul__(other).value;
    }

    public void __itruediv__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        this.value = this.__truediv__(args, kwargs).value;
    }

    public void __itruediv__(org.python.types.Object other) {
        this.value = this.__truediv__(other).value;
    }

    public void __ifloordiv__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        this.value = this.__floordiv__(args, kwargs).value;
    }

    public void __ifloordiv__(org.python.types.Object other) {
        this.value = this.__or__(other).value;
    }

    public void __imod__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        this.value = this.__mod__(args, kwargs).value;
    }

    public void __imod(org.python.types.Object other) {
        this.value = this.__mod__(other).value;
    }

    public void __ipow__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        this.value = this.__pow__(args, kwargs).value;
    }

    public void __ipow__(org.python.types.Object other) {
        this.value = this.__pow__(other).value;
    }

    public void __ilshift__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        this.value = this.__lshift__(args, kwargs).value;
    }

    public void __ilshift(org.python.types.Object other) {
        this.value = this.__lshift__(other).value;
    }

    public void __irshift__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        this.value = this.__rshift__(args, kwargs).value;
    }

    public void __irshift(org.python.types.Object other) {
        this.value = this.__rshift__(other).value;
    }

    public void __iand__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        this.value = this.__and__(args, kwargs).value;
    }

    public void __iand(org.python.types.Object other) {
        this.value = this.__and__(other).value;
    }

    public void __ixor__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        this.value = this.__xor__(args, kwargs).value;
    }

    public void __ixor__(org.python.types.Object other) {
        this.value = this.__xor__(other).value;
    }

    public void __ior__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        this.value = this.__or__(args, kwargs).value;
    }

    public void __ior__(org.python.types.Object other) {
        this.value = this.__or__(other).value;
    }

    public org.python.types.Object __neg__() {
        throw new org.python.exceptions.NotImplementedError("Object method __neg__ not implemented");
    }

    public org.python.types.Object __pos__() {
        throw new org.python.exceptions.NotImplementedError("Object method __pos__ not implemented");
    }

    public org.python.types.Object __abs__() {
        throw new org.python.exceptions.NotImplementedError("Object method __abs__ not implemented");
    }

    public org.python.types.Object __invert__() {
        throw new org.python.exceptions.NotImplementedError("Object method __invert__ not implemented");
    }

    public org.python.types.Object __not__() {
        return new org.python.types.Object(!((boolean)(__bool__().value)));
    }

    public org.python.types.Object __complex__(org.python.types.Object [] args, java.util.Hashtable kwargs) {
        org.python.types.Object other = args[0];
        throw new org.python.exceptions.NotImplementedError("Object method __complex__ not implemented");
    }

    public org.python.types.Object __int__() {
        return new org.python.types.Object((int) this.value);
    }

    public org.python.types.Object __float__() {
        return new org.python.types.Object((float) this.value);
    }

    public org.python.types.Object __round__() {
        throw new org.python.exceptions.NotImplementedError("Object method __round__ not implemented");
    }

    /**
     * Section 3.3.8 - With statement context
     */
    public org.python.types.Object __enter__() {
        throw new org.python.exceptions.NotImplementedError("Object method __enter__ not implemented");
    }

    public org.python.types.Object __exit__(org.python.types.Object exc_type, org.python.types.Object exc_value, org.python.types.Object traceback) {
        throw new org.python.exceptions.NotImplementedError("Object method __exit__ not implemented");
    }

}
