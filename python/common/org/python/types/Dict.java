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

    @org.python.Method(
            __doc__ = "dict() -> new empty dictionary" +
                    "dict(mapping) -> new dictionary initialized from a mapping object's\n" +
                    "    (key, value) pairs\n" +
                    "dict(iterable) -> new dictionary initialized as if via:\n" +
                    "    d = {}\n" +
                    "    for k, v in iterable:\n" +
                    "        d[k] = v\n" +
                    "dict(**kwargs) -> new dictionary initialized with the name=value pairs\n" +
                    "    in the keyword argument list.  For example:  dict(one=1, two=2)\n",
            default_args = {"iterable"}
    )
    public Dict(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args[0] == null) {
            this.value = new java.util.HashMap<org.python.Object, org.python.Object>();
        } else {
            if (args[0] instanceof org.python.types.Dict) {
                this.value = new java.util.HashMap<org.python.Object, org.python.Object>(
                        ((org.python.types.Dict) args[0]).value
                );
            } else {
                org.python.Iterable iterator = org.Python.iter(args[0]);
                java.util.Map<org.python.Object, org.python.Object> generated = new java.util.HashMap<org.python.Object, org.python.Object>();
                try {
                    while (true) {
                        org.python.Object next = iterator.__next__();
                        java.util.List<org.python.Object> data;
                        if (next instanceof org.python.types.Tuple) {
                            data = ((org.python.types.Tuple) next).value;
                        } else if (next instanceof org.python.types.List) {
                            data = ((org.python.types.List) next).value;
                        } else {
                            throw new org.python.exceptions.TypeError(
                                    "cannot convert dictionary update sequence element #" + generated.size() +
                                            " to a sequence"
                            );
                        }

                        if (data.size() != 2) {
                            throw new org.python.exceptions.ValueError(
                                    "dictionary update sequence element #" + generated.size() +
                                            " has length " + data.size() +
                                            "; 2 is required"
                            );
                        }

                        generated.put(data.get(0), data.get(1));
                    }
                } catch (org.python.exceptions.StopIteration si) {
                }
                this.value = generated;
            }
        }
        for (java.util.Map.Entry<java.lang.String, org.python.Object> entry : kwargs.entrySet()) {
            this.value.put(new Str(entry.getKey()), entry.getValue());
        }
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
        for (org.python.Object key : this.value.keySet()) {
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
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.Dict) {
            org.python.types.Dict otherDict = (org.python.types.Dict) other;
            return new org.python.types.Bool(this.value.equals(otherDict.value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
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
        return new org.python.types.Dict_KeyIterator(this);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"item"}
    )
    public org.python.Object __contains__(org.python.Object item) {
        // allow unhashable type error to be percolated up.
        try {
            __getitem__(item);
            return new org.python.types.Bool(true);
        } catch (org.python.exceptions.KeyError e) {
            return new org.python.types.Bool(false);
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"item"}
    )
    public org.python.Object __not_contains__(org.python.Object item) {
        // allow unhashable type error to be percolated up.
        try {
            __getitem__(item);
            return new org.python.types.Bool(false);
        } catch (org.python.exceptions.KeyError e) {
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
            __doc__ = "D.copy() -> dict -- a shallow copy of D"
    )
    public org.python.Object copy() {
        return new org.python.types.Dict(new java.util.HashMap<org.python.Object, org.python.Object>(this.value));
    }

    @org.python.Method(
            __doc__ = "",
            args = {"iterable"},
            default_args = {"value"}
    )
    public org.python.Object fromkeys(org.python.Object iterable, org.python.Object value) {
        org.python.types.Dict result = new org.python.types.Dict();
        try {
            org.python.Iterable iter = iterable.__iter__();
            if (value == null) {
                value = org.python.types.NoneType.NONE;
            }
            while (true) {
                result.__setitem__(iter.__next__(), value);
            }
        } catch (org.python.exceptions.AttributeError e) {
            throw new org.python.exceptions.TypeError("'" + iterable.typeName() + "' object is not iterable");
        } catch (org.python.exceptions.StopIteration e) { }

        return result;
    }

    @org.python.Method(
            __doc__ = "D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.",
            default_args = {"k", "d"}
    )
    public org.python.Object get(org.python.Object k, org.python.Object d) {
        try {
            return this.__getitem__(k);
        } catch (org.python.exceptions.KeyError e) { // allow unhashable type error to be percolated up.
            if (d == null) {
                return org.python.types.NoneType.NONE;
            }
            return d;
        }
    }

    @org.python.Method(
            __doc__ = "D.items() -> a set-like object providing a view on D's items"
    )
    public org.python.Object items() {
        // FIXME: This should return a dict_view object, not compose a new list.
        org.python.types.List result = new org.python.types.List();
        java.util.List<org.python.Object> item;
        org.python.types.Tuple tuple;

        for (org.python.Object key : this.value.keySet()) {
            item = new java.util.ArrayList<org.python.Object>();
            item.add(key);
            item.add(this.value.get(key));

            tuple = new org.python.types.Tuple(item);
            result.append(tuple);
        }
        return result;
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object keys() {
        throw new org.python.exceptions.NotImplementedError("dict.keys() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "D.pop(k[,d]) -> v, remove specified key and return the corresponding value.\nIf key is not found, d is returned if given, otherwise KeyError is raised",
            args = {"k"},
            default_args = {"d"}
    )
    public org.python.Object pop(org.python.Object k, org.python.Object d) {
        org.python.Object value = this.value.remove(k);
        if (value == null) {
            if (d == null) {
                throw new org.python.exceptions.KeyError(k);
            } else {
                value = d;
            }
        }
        return value;
    }

    @org.python.Method(
            __doc__ = "D.popitem() -> (k, v), remove and return some (key, value) pair as a\n2-tuple; but raise KeyError if D is empty."
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
            __doc__ = "D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D",
            default_args = {"k", "d"}
    )
    public org.python.Object setdefault(org.python.Object k, org.python.Object d) {
        try {
            return this.__getitem__(k);
        } catch (org.python.exceptions.KeyError e) { // allow unhashable type error to be percolated up.
            if (d == null) {
                d = org.python.types.NoneType.NONE;
            }
            __setitem__(k, d);
            return d;
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
