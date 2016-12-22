package org.python.types;


public class Dict extends org.python.types.Object {
    public java.util.Map<org.python.Object, org.python.Object> value;

    /**
     * A utility method to update the internal value of this object.
     * <p>
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Dict
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.Dict) obj).value;
    }

    public java.lang.Object toJava() {
        return this.value;
    }

    public int hashCode() {
        return this.value.hashCode();
    }

    @Override
    public org.python.Object __hash__() {
        throw new org.python.exceptions.AttributeError(this, "__hash__");
    }

    public Dict() {
        super();
        this.value = new java.util.HashMap<org.python.Object, org.python.Object>();
    }

    public Dict(java.util.Map<org.python.Object, org.python.Object> dict) {
        this.value = dict;
    }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("dict.__new__() has not been implemented.");
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("dict.__init__() has not been implemented.");
    // }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        java.lang.StringBuilder buffer = new java.lang.StringBuilder("{");
        boolean first = true;
        for (org.python.Object key: this.value.keySet()) {
            if (first) {
                first = false;
            } else {
                buffer.append(", ");
            }
            org.python.Object val = this.value.get(key);
            if (val.toJava() instanceof org.python.internals.Scope) {
                buffer.append(
                    String.format("%s: {...}", key.__repr__())
                );
            } else {
                buffer.append(
                    String.format("%s: %s", key.__repr__(), val.__repr__())
                );
            }
        }
        buffer.append("}");
        return new org.python.types.Str(buffer.toString());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __format__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.__format__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary +: 'dict'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __iadd__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: 'dict' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: 'dict'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'dict'");
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __bool__() {
        return new org.python.types.Bool(!this.value.isEmpty());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __lt__(org.python.Object other) {
        throw new org.python.exceptions.TypeError(
            String.format("unorderable types: dict() < %s()",
                org.Python.typeName(other.getClass())));
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __le__(org.python.Object other) {
        throw new org.python.exceptions.TypeError(
            String.format("unorderable types: dict() <= %s()",
                org.Python.typeName(other.getClass())));
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __eq__(org.python.Object other) {
        boolean eq = false;
        if (other instanceof org.python.types.Dict) {
            org.python.types.Dict otherDict = (org.python.types.Dict) other;
            eq = this.value.equals(otherDict.value);
        }
        return new org.python.types.Bool(eq);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ne__(org.python.Object other) {
        return new org.python.types.Bool(!((org.python.types.Bool) this.__eq__(other)).value);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __gt__(org.python.Object other) {
        throw new org.python.exceptions.TypeError(
            String.format("unorderable types: dict() > %s()",
                org.Python.typeName(other.getClass())));
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ge__(org.python.Object other) {
        throw new org.python.exceptions.TypeError(
            String.format("unorderable types: dict() >= %s()",
                org.Python.typeName(other.getClass())));
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.List) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + this.typeName() + "'");
        } else if (other instanceof org.python.types.Tuple) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + this.typeName() + "'");
        } else if (other instanceof org.python.types.Str) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + this.typeName() + "'");
        } else if (other instanceof org.python.types.Bytes) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + this.typeName() + "'");
        }
        return super.__mul__(other);
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // Builtin types can't have attributes set on them.
        return false;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("dict.__dir__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Int __len__() {
        return new org.python.types.Int(this.value.size());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getitem__(org.python.Object item) {
        try {
            // While hashcode is not used, it is not a redundant line.
            // We are determining if the item is hashable by seeing if an
            // exception is thrown.
            org.python.Object hashcode = item.__hash__();

            org.python.Object value = this.value.get(item);
            if (value == null) {
                throw new org.python.exceptions.KeyError(item);
            }
            return value;

        } catch (org.python.exceptions.AttributeError ae) {
            throw new org.python.exceptions.TypeError(
                String.format("unhashable type: '%s'", org.Python.typeName(item.getClass())));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __setitem__(org.python.Object item, org.python.Object value) {
        try {
            // While hashcode is not used, it is not a redundant line.
            // We are determining if the item is hashable by seeing if an
            // exception is thrown.
            org.python.Object hashcode = item.__hash__();

            this.value.put(item, value);
        } catch (org.python.exceptions.AttributeError ae) {
            throw new org.python.exceptions.TypeError(
                String.format("unhashable type: '%s'", org.Python.typeName(item.getClass())));
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __delitem__(org.python.Object item) {
        org.python.Object value = this.value.remove(item);
        if (value == null) {
            throw new org.python.exceptions.KeyError(item);
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Iterable __iter__() {
        // FIXME: Once this is implemented, update org.Python.addToKwargs()
        throw new org.python.exceptions.NotImplementedError("dict.__iter__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __contains__(org.python.Object item) {
         // allow unhashable type error to be percolated up.
        try{
            __getitem__(item);
            return new org.python.types.Bool(true);
        } catch(org.python.exceptions.KeyError e) {
            return new org.python.types.Bool(false);
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __not_contains__(org.python.Object item) {
         // allow unhashable type error to be percolated up.
        try{
            __getitem__(item);
            return new org.python.types.Bool(false);
        } catch(org.python.exceptions.KeyError e) {
            return new org.python.types.Bool(true);
        }
    }

    @org.python.Method(
        __doc__ = "D.clear() -> None.  Remove all items from D."
    )
    public org.python.Object clear() {
        this.value.clear();
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object copy() {
        throw new org.python.exceptions.NotImplementedError("dict.copy() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object fromkeys(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.fromkeys() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = "",
        default_args = {"other", "default_value"}
    )
    public org.python.Object get(org.python.Object other, org.python.Object default_value) {
        try {
            return this.__getitem__(other);
        } catch (org.python.exceptions.KeyError e){ // allow unhashable type error to be percolated up.
            if (default_value == null) {
                return org.python.types.NoneType.NONE;
            }
            return default_value;
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object items() {
        throw new org.python.exceptions.NotImplementedError("dict.items() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object keys() {
        throw new org.python.exceptions.NotImplementedError("dict.keys() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object pop(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.pop() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object popitem() {
        if (this.value.size() == 0) {
            throw new org.python.exceptions.KeyError(new org.python.types.Str("popitem(): dictionary is empty"));
        }
        java.util.Map.Entry<org.python.Object, org.python.Object> entry = this.value.entrySet().iterator().next();
        org.python.Object key = entry.getKey();
        org.python.Object value = this.value.remove(key);

        java.util.List<org.python.Object> item_pair = new java.util.ArrayList<org.python.Object>();
        item_pair.add(key);
        item_pair.add(value);
        return new org.python.types.Tuple(item_pair);
    }

    @org.python.Method(
        __doc__ = "",
        default_args = {"other", "default_value"}
    )
    public org.python.Object setdefault(org.python.Object other, org.python.Object default_value) {
        try {
            return this.__getitem__(other);
        } catch (org.python.exceptions.KeyError e){ // allow unhashable type error to be percolated up.
            if (default_value == null) {
                default_value = org.python.types.NoneType.NONE;
            }
            __setitem__(other, default_value);
            return default_value;
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object update(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("dict.update() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object values() {
        throw new org.python.exceptions.NotImplementedError("dict.values() has not been implemented.");
    }

}
