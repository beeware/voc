package org.python.types;

import java.util.Arrays;

public class Bytes extends org.python.types.Object {
    public byte [] value;

    // ugly hack to allow for Python 3.4 / 3.5 differences
    public static final float PYTHON_VERSION = 3.4f;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Bytes
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.Bytes) obj).value;
    }

    public int hashCode() {
        return this.value.hashCode();
    }

    public Bytes(byte [] value) {
        this.value = Arrays.copyOf(value, value.length);
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("str.__new__() has not been implemented.");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("str.__init__() has not been implemented.");
    // }
            
    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        return this.__str__();
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __str__() {
        StringBuilder sb = new StringBuilder();
        sb.append("b'");
        for (int c : this.value) {
            if (c >= 32 && c < 128) {
                sb.append((char)c);
            } else {
                sb.append(String.format("\\x%02d",c));
            }
        }
        sb.append("'");
        return new org.python.types.Str(sb.toString());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_value = ((org.python.types.Bytes) other).value;
            return new org.python.types.Bool(Arrays.equals(this.value, other_value));
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_value = ((org.python.types.ByteArray) other).value;
            if (other_value == null) other_value = new byte[0];
            return new org.python.types.Bool(Arrays.equals(this.value, other_value));
        } else {
            return new org.python.types.Bool(false);
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __add__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_bytes = (byte[])((org.python.types.Bytes) other).value;
            byte[] new_bytes = new byte[this.value.length + other_bytes.length];
            System.arraycopy(this.value, 0, new_bytes, 0, this.value.length);
            System.arraycopy(other_bytes, 0, new_bytes, this.value.length, other_bytes.length);
            return new Bytes(new_bytes);
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_bytes = (byte[])((org.python.types.ByteArray) other).value;
            if (other_bytes == null) return this;
            byte[] new_bytes = new byte[this.value.length + other_bytes.length];
            System.arraycopy(this.value, 0, new_bytes, 0, this.value.length);
            System.arraycopy(other_bytes, 0, new_bytes, this.value.length, other_bytes.length);
            return new Bytes(new_bytes);
        }
        throw new org.python.exceptions.TypeError("can't concat bytes to " + other.typeName());
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __iadd__(org.python.Object other) {
        return this.__add__(other);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __and__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for &: 'bytes' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__=""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary +: 'bytes'");
    }

    @org.python.Method(
        __doc__=""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: 'bytes'");
    }

    @org.python.Method(
        __doc__=""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'bytes'");
    }

    @org.python.Method(
        __doc__=""
    )
    public org.python.Object __bool__() {
        return new org.python.types.Bool(this.value.length > 0);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __contains__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.__contains__ has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __format__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.__format__ has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ge__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_bytes = (byte[])((org.python.types.Bytes) other).value;
            for (int i=0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] > other_bytes[i]) return new org.python.types.Bool(1);
                if (this.value[i] < other_bytes[i]) return new org.python.types.Bool(0);
            }
            if (this.value.length < other_bytes.length) return new org.python.types.Bool(0);
            return new org.python.types.Bool(1);
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_bytes = (byte[])((org.python.types.ByteArray) other).value;
            if (other_bytes == null) return new org.python.types.Bool(1);
            for (int i=0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] > other_bytes[i]) return new org.python.types.Bool(1);
                if (this.value[i] < other_bytes[i]) return new org.python.types.Bool(0);
            }
            if (this.value.length < other_bytes.length) return new org.python.types.Bool(0);
            return new org.python.types.Bool(1);
        }
        throw new org.python.exceptions.TypeError("unorderable types: bytes() >= " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __gt__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_bytes = (byte[])((org.python.types.Bytes) other).value;
            for (int i=0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] > other_bytes[i]) return new org.python.types.Bool(1);
                if (this.value[i] < other_bytes[i]) return new org.python.types.Bool(0);
            }
            if (this.value.length <= other_bytes.length) return new org.python.types.Bool(0);
            return new org.python.types.Bool(1);
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_bytes = (byte[])((org.python.types.ByteArray) other).value;
            if (other_bytes == null) other_bytes = new byte[0];
            for (int i=0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] > other_bytes[i]) return new org.python.types.Bool(1);
                if (this.value[i] < other_bytes[i]) return new org.python.types.Bool(0);
            }
            if (this.value.length <= other_bytes.length) return new org.python.types.Bool(0);
            return new org.python.types.Bool(1);
        }
        throw new org.python.exceptions.TypeError("unorderable types: bytes() > " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __le__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_bytes = (byte[])((org.python.types.Bytes) other).value;
            for (int i=0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] < other_bytes[i]) return new org.python.types.Bool(1);
                if (this.value[i] > other_bytes[i]) return new org.python.types.Bool(0);
            }
            if (this.value.length <= other_bytes.length) return new org.python.types.Bool(1);
            return new org.python.types.Bool(0);
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_bytes = (byte[])((org.python.types.ByteArray) other).value;
            if (other_bytes == null) other_bytes = new byte[0];
            for (int i=0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] < other_bytes[i]) return new org.python.types.Bool(1);
                if (this.value[i] > other_bytes[i]) return new org.python.types.Bool(0);
            }
            if (this.value.length <= other_bytes.length) return new org.python.types.Bool(1);
            return new org.python.types.Bool(0);
        }
        throw new org.python.exceptions.TypeError("unorderable types: bytes() <= " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __lt__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_bytes = (byte[])((org.python.types.Bytes) other).value;
            for (int i=0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] < other_bytes[i]) return new org.python.types.Bool(1);
                if (this.value[i] > other_bytes[i]) return new org.python.types.Bool(0);
            }
            if (this.value.length < other_bytes.length) return new org.python.types.Bool(1);
            return new org.python.types.Bool(0);
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_bytes = (byte[])((org.python.types.ByteArray) other).value;
            if (other_bytes == null) return new org.python.types.Bool(0);
            for (int i=0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] < other_bytes[i]) return new org.python.types.Bool(1);
                if (this.value[i] > other_bytes[i]) return new org.python.types.Bool(0);
            }
            if (this.value.length < other_bytes.length) return new org.python.types.Bool(1);
            return new org.python.types.Bool(0);
        }
        throw new org.python.exceptions.TypeError("unorderable types: bytes() < " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mod__(org.python.Object other) {
        if (this.PYTHON_VERSION < 3.5) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for %: 'bytes' and '" + other.typeName() + "'");
        } else {
            if (other instanceof org.python.types.List || other instanceof org.python.types.Range) {
                return this;
            }
            throw new org.python.exceptions.TypeError("not all arguments converted during bytes formatting");
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getitem__(org.python.Object index) {
        if (index instanceof org.python.types.Slice) {
            org.python.types.Slice slice = (org.python.types.Slice) index;
            byte[] sliced;

            if (slice.start == null && slice.stop == null && slice.step == null) {
                sliced = this.value;
            } else {
                int start;
                if (slice.start != null) {
                    start = (int)slice.start.value;
                } else {
                    start = 0;
                }

                int stop;
                if (slice.stop != null) {
                    stop = (int)slice.stop.value;
                } else {
                    stop = this.value.length;
                }

                int step;
                if (slice.step != null) {
                    step = (int)slice.step.value;
                } else {
                    step = 1;
                }

                // System.err.format("start:%d, stop:%d, step:%d\n", start, stop, step);
                if (step > 0) {
                    if (start >= this.value.length || stop >= this.value.length || start > stop) {
                        return new Bytes(new byte[0]);
                    }

                    int len = (int)Math.ceil((float)(stop - start) / step);
                    sliced = new byte[len];
                
                    for (int i=0, j=start ; j < stop ; i++, j += step) {
                        // System.err.format("this.value[%d] -> sliced[%d]\n", j, i);
                        sliced[i] = this.value[j];
                    }
                } else { // step < 0
                    if (Math.abs(start) >= this.value.length || Math.abs(stop) >= this.value.length || stop > start) {
                        return new Bytes(new byte[0]);
                    }

                    int len = (int)Math.ceil((float)(stop - start) / step);
                    sliced = new byte[len];
                
                    for (int i=0, j=start ; j > stop ; i++, j += step) {
                        // System.err.format("this.value[%d] -> sliced[%d]\n", j, i);
                        sliced[i] = this.value[j];
                    }
                }
            }
            return new Bytes(sliced);

        } else if (index instanceof org.python.types.Bool || index instanceof org.python.types.Int) {
            int idx;
            if (index instanceof org.python.types.Bool) {
                boolean index_bool = ((org.python.types.Bool)index).value;
                if (index_bool) {
                    idx = 1;
                } else {
                    idx = 0;
                }
            }
            else {
                 idx = (int) ((org.python.types.Int) index).value;
            }

            if (idx < 0) {
                if (-idx > this.value.length) {
                    throw new org.python.exceptions.IndexError("index out of range");
                } else {
                    idx = this.value.length + idx;
                    // return new Bytes(java.util.Arrays.copyOfRange(this.value, idx, idx));
                    return new org.python.types.Int(this.value[idx]);
                }
            } else {
                if (idx >= this.value.length) {
                    throw new org.python.exceptions.IndexError("index out of range");
                } else {
                    // return new Bytes(java.util.Arrays.copyOfRange(this.value, idx, idx));
                    return new org.python.types.Int(this.value[idx]);
                }
            }
        } else if (this.PYTHON_VERSION < 3.5) {
            throw new org.python.exceptions.TypeError("byte indices must be integers, not " + index.typeName());
        } else {
            throw new org.python.exceptions.TypeError("byte indices must be integers or slices, not " + index.typeName());
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getnewargs__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.__getnewargs__ has not been implemented.");
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // Builtin types can't have attributes set on them.
        return false;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Iterable __iter__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.__iter__ has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Int __len__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        return new org.python.types.Int(this.value.length);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
                boolean other_bool = ((org.python.types.Bool)other).value;
                if (other_bool) {
                        return this;
                } else {
                        return new Bytes(new byte[0]);
                }
        }
        if (other instanceof org.python.types.Int) {
            int other_value = Math.max(0, (int) ((org.python.types.Int) other).value);
            int len = this.value.length;
            byte[] bytes = new byte[other_value * len];
            for (int i=0 ; i < other_value ; i++) {
                System.arraycopy(this.value, 0, bytes, i * len, len);
            }
            return new Bytes(bytes);
        }
        else {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __imul__(org.python.Object other) {
        return this.__mul__(other);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ne__(org.python.Object other) {
        return new org.python.types.Bool(((org.python.types.Bool)this.__eq__(other)).value ? 0 : 1);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __reduce__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.__reduce__ has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __reduce_ex__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.__reduce_ex__ has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rmul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.__rmul__ has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
     public org.python.Object capitalize(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.capitalize has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object center(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.center has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object count(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.count has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object decode(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        try {
            return new org.python.types.Str(new java.lang.String(this.value, "UTF-8"));
            // return new org.python.types.Str(new java.lang.String(this.value, encoding));
        } catch (java.io.UnsupportedEncodingException e) {
            throw new org.python.exceptions.UnicodeDecodeError();
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object endswith(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.endswith has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object expandtabs(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.expandtabs has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object find(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.find has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object fromhex(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.fromhex has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object index(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.index has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object isalnum(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.isalnum has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object isalpha(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.isalpha has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object isdigit(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.isdigit has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object islower(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.islower has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object isspace(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.isspace has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object istitle(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.istitle has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object isupper(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.isupper has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object join(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.join has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object ljust(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.ljust has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object lower(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.lower has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object lstrip(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.lstrip has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object maketrans(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.maketrans has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object partition(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.partition has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object replace(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.replace has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object rfind(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.rfind has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object rindex(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.rindex has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object rjust(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.rjust has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object rpartition(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.rpartition has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object rsplit(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.rsplit has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object rstrip(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.rstrip has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object split(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.split has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object splitlines(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.splitlines has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object startswith(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.startswith has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object strip(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.strip has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object swapcase(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.swapcase has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object title(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.title has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object translate(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.translate has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object upper(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.upper has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object zfill(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.zfill has not been implemented.");
    }


}
