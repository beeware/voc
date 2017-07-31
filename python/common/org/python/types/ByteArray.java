package org.python.types;

import java.util.Arrays;

public class ByteArray extends org.python.types.Object {
    public byte[] value;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.ByteArray
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.ByteArray) obj).value;
    }

    public int hashCode() {
        return this.value.hashCode();
    }

    public ByteArray() {
        this.value = new byte[0];
    }

    public ByteArray(int length) {
        this.value = new byte[length];
    }

    public ByteArray(byte[] value) {
        this.value = Arrays.copyOf(value, value.length);
    }

    @org.python.Method(
            __doc__ = "bytearray(iterable_of_ints) -> bytearray" +
                    "bytearray(string, encoding[, errors]) -> bytearray\n" +
                    "bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer\n" +
                    "bytearray(int) -> bytes array of size given by the parameter initialized with null bytes\n" +
                    "bytearray() -> empty bytes array\n" +
                    "\n" +
                    "Construct an mutable bytearray object from:\n" +
                    " - an iterable yielding integers in range(256)\n" +
                    " - a text string encoded using the specified encoding\n" +
                    " - a bytes or a buffer object\n" +
                    " - any object implementing the buffer API.\n" +
                    " - an integer\n",
            default_args = {"source", "encoding", "errors"}
    )
    public ByteArray(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args[0] == null) {
            // bytearray()
            this.value = new byte[0];
        } else {
            if (args[1] == null) {
                if (args[0] instanceof org.python.types.Int) {
                    // bytearray(int)
                    this.value = new byte[(int) ((org.python.types.Int) args[0].__int__()).value];
                } else {

                    org.python.Object iterator = null;
                    try {
                        iterator = org.Python.iter(args[0]);
                    } catch (org.python.exceptions.TypeError e) {
                        // Not an iterator
                    }
                    if (iterator != null) {
                        // bytearray(iterable_of_ints)
                        java.util.List<Byte> generated = new java.util.ArrayList<Byte>();
                        try {
                            while (true) {
                                org.python.Object next = iterator.__next__();
                                if (next instanceof org.python.types.Int) {
                                    long value = ((org.python.types.Int) next.__int__()).value;
                                    if ((value < 0) || (value > 255)) {
                                        throw new org.python.exceptions.ValueError("byte must be in range(0, 256)");
                                    } else {
                                        generated.add(new Byte((byte) value));
                                    }
                                } else if (next instanceof org.python.types.Str) {
                                    // TODO: Can take ASCII single-character strings
                                    throw new org.python.exceptions.NotImplementedError("Builtin function 'bytearray' with strings not implemented");
                                }
                            }
                        } catch (org.python.exceptions.StopIteration si) {
                        }
                        byte[] primative_bytes = new byte[generated.size()];
                        for (int i = 0; i < primative_bytes.length; i++) {
                            primative_bytes[i] = generated.get(i);
                        }
                        this.value = primative_bytes;
                    } else {
                        // bytearray(bytes_or_buffer)
                        throw new org.python.exceptions.NotImplementedError("Builtin function 'bytearray' with bytes_or_buffer not implemented");
                    }
                }
            } else {
                // bytearray(string, args[1][, errors])
                if (args[2] == null) {
                    // bytearray(string, args[1])
                    throw new org.python.exceptions.NotImplementedError("Builtin function 'bytearray' not implemented");
                } else {
                    // bytearray(string, args[1], errors)
                    throw new org.python.exceptions.NotImplementedError("Builtin function 'bytearray' not implemented");
                }
            }
        }
    }

    // public ByteArray(org.python.types.Bool bool) {
    //     this.value = new byte [(bool.value == true) ? 1 : 0];
    // }

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
        sb.append("bytearray(b'");
        for (int c : this.value) {
            if (c >= 32 && c < 128) {
                sb.append((char) c);
            } else {
                sb.append(String.format("\\x%02d", c));
            }
        }
        sb.append("')");
        return new org.python.types.Str(sb.toString());
    }

/*
    public org.python.types.Str __repr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("bytearray.__repr__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        try {
            return new org.python.types.Str("bytearray(b'" + new java.lang.String(this.value, "UTF-8") + "')");
        } catch (java.io.UnsupportedEncodingException e) {
            throw new org.python.exceptions.UnicodeDecodeError();
        }
    }

    public org.python.types.Str __str__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("bytearray.__str__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        try {
            return new org.python.types.Str(new java.lang.String(this.value, "UTF-8"));
        } catch (java.io.UnsupportedEncodingException e) {
            throw new org.python.exceptions.UnicodeDecodeError();
        }
    }
*/

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __and__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for &: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary +: '" + this.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: '" + this.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: '" + this.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __bool__() {
        return new org.python.types.Bool(this.value.length > 0);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_value = ((org.python.types.Bytes) other).value;
            return new org.python.types.Bool(Arrays.equals(this.value, other_value));
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_value = ((org.python.types.ByteArray) other).value;
            return new org.python.types.Bool(Arrays.equals(this.value, other_value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __add__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_bytes = (byte[]) ((org.python.types.Bytes) other).value;
            byte[] new_bytes = new byte[this.value.length + other_bytes.length];
            System.arraycopy(this.value, 0, new_bytes, 0, this.value.length);
            System.arraycopy(other_bytes, 0, new_bytes, this.value.length, other_bytes.length);
            return new ByteArray(new_bytes);
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_bytes = (byte[]) ((org.python.types.ByteArray) other).value;
            if (other_bytes == null) {
                return this;
            }
            byte[] new_bytes = new byte[this.value.length + other_bytes.length];
            System.arraycopy(this.value, 0, new_bytes, 0, this.value.length);
            System.arraycopy(other_bytes, 0, new_bytes, this.value.length, other_bytes.length);
            return new ByteArray(new_bytes);
        }
        throw new org.python.exceptions.TypeError("can't concat " + this.typeName() + " to " + other.typeName());
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __iadd__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes || other instanceof org.python.types.ByteArray) {
            return this.__add__(other);
        }
        throw new org.python.exceptions.TypeError("can't concat " + other.typeName() + " to " + this.typeName());
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            boolean other_bool = ((org.python.types.Bool) other).value;
            if (other_bool) {
                return this;
            } else {
                return new ByteArray();
            }
        }
        if (other instanceof org.python.types.Int) {
            int other_value = Math.max(0, (int) ((org.python.types.Int) other).value);
            int len = this.value.length;
            byte[] bytes = new byte[other_value * len];
            for (int i = 0; i < other_value; i++) {
                System.arraycopy(this.value, 0, bytes, i * len, len);
            }
            return new ByteArray(bytes);
        } else {
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
    public org.python.Object __getitem__(org.python.Object index) {
        if (index instanceof org.python.types.Slice) {
            org.python.types.Slice slice = (org.python.types.Slice) index;
            byte[] sliced;

            // if (slice.start == null && slice.stop == null && slice.step == null) {
            int start;
            if (slice.start != null) {
                start = (int) slice.start.value;
            } else {
                start = 0;
            }

            int stop;
            if (slice.stop != null) {
                stop = (int) slice.stop.value;
            } else {
                stop = this.value.length;
            }
            if (stop > this.value.length) {
                stop = this.value.length;
            }

            int step;
            if (slice.step != null) {
                step = (int) slice.step.value;
            } else {
                step = 1;
            }

            if (step > 0) {
                if (start >= this.value.length || start > stop) {
                    return new ByteArray();
                }

                int len = (int) Math.ceil((float) (stop - start) / step);
                sliced = new byte[len];

                for (int i = 0, j = start; j < stop; i++, j += step) {
                    sliced[i] = this.value[j];
                }
            } else { // step < 0
                if (Math.abs(start) >= this.value.length || stop > start) {
                    return new ByteArray();
                }

                int len = (int) Math.ceil((float) (stop - start) / step);
                sliced = new byte[len];

                for (int i = 0, j = start; j > stop; i++, j += step) {
                    sliced[i] = this.value[j];
                }
            }
            return new ByteArray(sliced);
        } else if (index instanceof org.python.types.Bool || index instanceof org.python.types.Int) {
            int idx;
            if (index instanceof org.python.types.Bool) {
                boolean index_bool = ((org.python.types.Bool) index).value;
                if (index_bool) {
                    idx = 1;
                } else {
                    idx = 0;
                }
            } else {
                idx = (int) ((org.python.types.Int) index).value;
            }

            if (idx < 0) {
                if (-idx > this.value.length) {
                    throw new org.python.exceptions.IndexError("bytearray index out of range");
                } else {
                    idx = this.value.length + idx;
                    // return new Bytes(java.util.Arrays.copyOfRange(this.value, idx, idx));
                    return new org.python.types.Int(this.value[idx]);
                }
            } else {
                if (idx >= this.value.length) {
                    throw new org.python.exceptions.IndexError("bytearray index out of range");
                } else {
                    // return new Bytes(java.util.Arrays.copyOfRange(this.value, idx, idx));
                    return new org.python.types.Int(this.value[idx]);
                }
            }
        } else {
            if (org.Python.VERSION < 0x03050000) {
                throw new org.python.exceptions.TypeError("bytearray indices must be integers");
            } else {
                throw new org.python.exceptions.TypeError(
                        "bytearray indices must be integers or slices, not " + index.typeName()
                );
            }
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_bytes = (byte[]) ((org.python.types.Bytes) other).value;
            for (int i = 0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] > other_bytes[i]) {
                    return new org.python.types.Bool(1);
                }
                if (this.value[i] < other_bytes[i]) {
                    return new org.python.types.Bool(0);
                }
            }
            if (this.value.length < other_bytes.length) {
                return new org.python.types.Bool(0);
            }
            return new org.python.types.Bool(1);
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_bytes = (byte[]) ((org.python.types.ByteArray) other).value;
            if (other_bytes == null) {
                return new org.python.types.Bool(1);
            }
            for (int i = 0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] > other_bytes[i]) {
                    return new org.python.types.Bool(1);
                }
                if (this.value[i] < other_bytes[i]) {
                    return new org.python.types.Bool(0);
                }
            }
            if (this.value.length < other_bytes.length) {
                return new org.python.types.Bool(0);
            }
            return new org.python.types.Bool(1);
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_bytes = (byte[]) ((org.python.types.Bytes) other).value;
            for (int i = 0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] > other_bytes[i]) {
                    return new org.python.types.Bool(1);
                }
                if (this.value[i] < other_bytes[i]) {
                    return new org.python.types.Bool(0);
                }
            }
            if (this.value.length <= other_bytes.length) {
                return new org.python.types.Bool(0);
            }
            return new org.python.types.Bool(1);
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_bytes = (byte[]) ((org.python.types.ByteArray) other).value;
            if (other_bytes == null) {
                other_bytes = new byte[0];
            }
            for (int i = 0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] > other_bytes[i]) {
                    return new org.python.types.Bool(1);
                }
                if (this.value[i] < other_bytes[i]) {
                    return new org.python.types.Bool(0);
                }
            }
            if (this.value.length <= other_bytes.length) {
                return new org.python.types.Bool(0);
            }
            return new org.python.types.Bool(1);
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_bytes = (byte[]) ((org.python.types.Bytes) other).value;
            for (int i = 0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] < other_bytes[i]) {
                    return new org.python.types.Bool(1);
                }
                if (this.value[i] > other_bytes[i]) {
                    return new org.python.types.Bool(0);
                }
            }
            if (this.value.length <= other_bytes.length) {
                return new org.python.types.Bool(1);
            }
            return new org.python.types.Bool(0);
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_bytes = (byte[]) ((org.python.types.ByteArray) other).value;
            if (other_bytes == null) {
                other_bytes = new byte[0];
            }
            for (int i = 0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] < other_bytes[i]) {
                    return new org.python.types.Bool(1);
                }
                if (this.value[i] > other_bytes[i]) {
                    return new org.python.types.Bool(0);
                }
            }
            if (this.value.length <= other_bytes.length) {
                return new org.python.types.Bool(1);
            }
            return new org.python.types.Bool(0);
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_bytes = (byte[]) ((org.python.types.Bytes) other).value;
            for (int i = 0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] < other_bytes[i]) {
                    return new org.python.types.Bool(1);
                }
                if (this.value[i] > other_bytes[i]) {
                    return new org.python.types.Bool(0);
                }
            }
            if (this.value.length < other_bytes.length) {
                return new org.python.types.Bool(1);
            }
            return new org.python.types.Bool(0);
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_bytes = (byte[]) ((org.python.types.ByteArray) other).value;
            if (other_bytes == null) {
                return new org.python.types.Bool(0);
            }
            for (int i = 0; i < Math.min(this.value.length, other_bytes.length); i++) {
                if (this.value[i] < other_bytes[i]) {
                    return new org.python.types.Bool(1);
                }
                if (this.value[i] > other_bytes[i]) {
                    return new org.python.types.Bool(0);
                }
            }
            if (this.value.length < other_bytes.length) {
                return new org.python.types.Bool(1);
            }
            return new org.python.types.Bool(0);
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __mod__(org.python.Object other) {
        if (org.Python.VERSION < 0x03050000) {
            throw new org.python.exceptions.TypeError(
                    "unsupported operand type(s) for %: 'bytearray' and '" + other.typeName() + "'"
            );
        } else {
            if (other instanceof org.python.types.List
                    || other instanceof org.python.types.Range
                    || other instanceof org.python.types.Dict) {
                int i, size;
                for (i = 0; i < this.value.length; i++) {
                    if (this.value[0] == 0) {
                        break;
                    }
                }
                if (org.Python.VERSION < 0x03050300) {
                    size = i;
                } else {
                    size = this.value.length;
                }
                byte[] bytes = new byte[size];
                System.arraycopy(this.value, 0, bytes, 0, size);
                return new ByteArray(bytes);
            }
            throw new org.python.exceptions.TypeError("not all arguments converted during bytes formatting");
        }
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __imod__(org.python.Object other) {
        if (org.Python.VERSION < 0x03050000) {
            throw new org.python.exceptions.TypeError(
                    "unsupported operand type(s) for %=: 'bytearray' and '" + other.typeName() + "'"
            );
        } else {
            return this.__mod__(other);
        }
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __contains__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.__contains__ has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.types.Str __format__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.__format__ has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __getnewargs__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.__getnewargs__ has not been implemented.");
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // Builtin types can't have attributes set on them.
        return false;
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __iter__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.__iter__ has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.types.Int __len__() {
        return new org.python.types.Int(this.value.length);
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __reduce__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.__reduce__ has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __reduce_ex__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.__reduce_ex__ has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __rmul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.__rmul__ has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object capitalize(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.capitalize has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object center(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.center has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object count(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.count has not been implemented.");
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
        throw new org.python.exceptions.NotImplementedError("bytearray.endswith has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object expandtabs(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.expandtabs has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object find(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.find has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object fromhex(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.fromhex has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object index(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.index has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object isalnum(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.isalnum has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object isalpha(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.isalpha has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object isdigit(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.isdigit has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object islower(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.islower has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object isspace(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.isspace has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object istitle(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.istitle has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object isupper(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.isupper has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object join(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.join has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object ljust(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.ljust has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object lower(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.lower has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object lstrip(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.lstrip has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object maketrans(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.maketrans has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object partition(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.partition has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object replace(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.replace has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object rfind(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.rfind has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object rindex(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.rindex has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object rjust(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.rjust has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object rpartition(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.rpartition has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object rsplit(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.rsplit has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object rstrip(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.rstrip has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object split(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.split has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object splitlines(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.splitlines has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object startswith(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.startswith has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object strip(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.strip has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object swapcase(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.swapcase has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object title(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.title has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object translate(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.translate has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object upper(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.upper has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object zfill(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytearray.zfill has not been implemented.");
    }
}
