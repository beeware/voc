package org.python.types;

public class Str extends org.python.types.Object {
    public java.lang.String value;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Str
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.Str) obj).value;
    }

    public java.lang.Object toJava() {
        return this.value;
    }

    public int hashCode() {
        return this.value.hashCode();
    }

    public Str(java.lang.String str) {
        this.value = str;
    }

    public Str(char chr) {
        this.value = new java.lang.String(new char [] {chr});
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("__new__() has not been implemented.");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("__init__() has not been implemented.");
    // }

    public org.python.types.Str __repr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__repr__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        return new org.python.types.Str("'" + this.value + "'");
    }

    public org.python.types.Str __str__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__repr__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        return new org.python.types.Str(this.value);
    }

    public org.python.types.Str __format__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__format__() has not been implemented.");
    }

    public org.python.types.Int __int__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        try {
            return new org.python.types.Int(Long.parseLong(this.value));
        } catch (NumberFormatException e) {
            throw new org.python.exceptions.ValueError("invalid literal for int() with base 10: '" + this.value + "'");
        }
    }

    public org.python.types.Float __float__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        try {
            return new org.python.types.Float(Double.parseDouble(this.value));
        } catch (NumberFormatException e) {
            throw new org.python.exceptions.ValueError("could not convert string to float: '" + this.value + "'");
        }
    }

    public org.python.Object __lt__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__lt__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        if (other instanceof org.python.types.Str) {
            java.lang.String value = ((org.python.types.Str) other).value;
            return new org.python.types.Bool(this.value.compareTo(value) < 0);
        } else {
            throw new org.python.exceptions.TypeError("unorderable types: " + this.typeName() + "() < " + other.typeName() + "()");
        }
    }

    public org.python.Object __le__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__le__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        if (other instanceof org.python.types.Str) {
            java.lang.String value = ((org.python.types.Str) other).value;
            return new org.python.types.Bool(this.value.compareTo(value) <= 0);
        } else {
            throw new org.python.exceptions.TypeError("unorderable types: " + this.typeName() + "() <= " + other.typeName() + "()");
        }
    }

    public org.python.Object __eq__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__eq__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        if (other instanceof org.python.types.Str) {
            java.lang.String value = ((org.python.types.Str) other).value;
            return new org.python.types.Bool(this.value.equals(value));
        } else {
            return new org.python.types.Bool(false);
        }
    }

    public org.python.Object __ne__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__ne__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        if (other instanceof org.python.types.Str) {
            java.lang.String value = ((org.python.types.Str) other).value;
            return new org.python.types.Bool(!this.value.equals(value));
        } else {
            return new org.python.types.Bool(true);
        }
    }

    public org.python.Object __gt__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__gt__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        if (other instanceof org.python.types.Str) {
            java.lang.String value = ((org.python.types.Str) other).value;
            return new org.python.types.Bool(this.value.compareTo(value) > 0);
        } else {
            throw new org.python.exceptions.TypeError("unorderable types: " + this.typeName() + "() > " + other.typeName() + "()");
        }
    }

    public org.python.Object __ge__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__ge__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        if (other instanceof org.python.types.Str) {
            java.lang.String value = ((org.python.types.Str) other).value;
            return new org.python.types.Bool(this.value.compareTo(value) >= 0);
        } else {
            throw new org.python.exceptions.TypeError("unorderable types: " + this.typeName() + "() >= " + other.typeName() + "()");
        }
    }

    public org.python.Object __getattribute__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__getattribute__() has not been implemented.");
    }

    public void __setattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__setattr__() has not been implemented.");
    }

    public void __delattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__delattr__() has not been implemented.");
    }

    public org.python.types.List __dir__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__dir__() has not been implemented.");
    }

    public org.python.types.Int __len__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__len__() has not been implemented.");
    }

    public org.python.Object __getitem__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __getattribute__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object index = args.get(0);
        try {
            if (index instanceof org.python.types.Slice) {
                org.python.types.Slice slice = (org.python.types.Slice) index;
                java.lang.String sliced;

                if (slice.start == null && slice.stop == null && slice.step == null) {
                    sliced = this.value;
                }
                else {
                    long start;
                    if (slice.start != null) {
                        start = slice.start.value;
                    } else {
                        start = 0;
                    }

                    long stop;
                    if (slice.stop != null) {
                        stop = slice.stop.value;
                    } else {
                        stop = this.value.length();
                    }

                    long step;
                    if (slice.step != null) {
                        step = slice.step.value;
                    } else {
                        step = 1;
                    }

                    if (step == 1) {
                        sliced = this.value.substring((int) start, (int) stop);
                    } else {
                        java.lang.StringBuffer buffer = new java.lang.StringBuffer();
                        for (long i = start; i < stop; i += step) {
                            buffer.append(this.value.charAt((int)i));
                        }
                        sliced = buffer.toString();
                    }
                }
                return new org.python.types.Str(sliced);

            } else {
                int idx = (int)((org.python.types.Int) index).value;
                if (idx < 0) {
                    if (-idx > this.value.length()) {
                        throw new org.python.exceptions.IndexError("string index out of range");
                    } else {
                        return new org.python.types.Str(this.value.charAt(this.value.length() + idx));
                    }
                } else {
                    if (idx >= this.value.length()) {
                        throw new org.python.exceptions.IndexError("string index out of range");
                    } else {
                        return new org.python.types.Str(this.value.charAt(idx));
                    }
                }
            }
        } catch (ClassCastException e) {
            throw new org.python.exceptions.TypeError("string indices must be integers, not " + index.typeName());
        }
    }

    public org.python.Iterable __iter__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__iter__() has not been implemented.");
    }

    public org.python.types.Int __contains__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__contains__() has not been implemented.");
    }

    public org.python.Object __add__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__add__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        if (other instanceof org.python.types.Str) {
            Str other_str = (Str)other;
            if (0 == other_str.value.length()) {
                return this;
            }
            java.lang.StringBuffer sb = new java.lang.StringBuffer(value);
            sb.append(other_str.value);
            return new Str(sb.toString());
        }
        throw new org.python.exceptions.TypeError("Can't convert '" + other.typeName() + "' object to str implicitly");
    }

    public org.python.Object __mul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__add__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        if (other instanceof org.python.types.Int) {
            long other_int = ((org.python.types.Int)other).value;
            if (other_int < 1) {
                return new Str("");
            }
            java.lang.StringBuffer res = new java.lang.StringBuffer(value.length() * (int)other_int);
            for (int i = 0; i < other_int; i++) {
                res.append(value);
            }
            return new Str(res.toString());
        }
        throw new org.python.exceptions.NotImplementedError("__mul__() has not been implemented.");
    }

    public org.python.Object __mod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("__add__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        java.util.List<java.lang.Object> format_args = new java.util.ArrayList<java.lang.Object>();
        if (other instanceof org.python.types.List) {
            org.python.types.List oth = (org.python.types.List) other;
            for (org.python.Object obj: oth.value) {
                format_args.add(obj.toJava());
            }
        } else if (other instanceof org.python.types.Tuple) {
            org.python.types.Tuple oth = (org.python.types.Tuple) other;
            for (org.python.Object obj: oth.value) {
                format_args.add(obj.toJava());
            }
        } else {
            format_args.add(other.toJava());
        }

        return new org.python.types.Str(String.format(this.value, format_args.toArray()));
    }

    public org.python.Object __rmul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__rmul__() has not been implemented.");
    }

    public org.python.Object __rmod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("__rmod__() has not been implemented.");
    }

}
