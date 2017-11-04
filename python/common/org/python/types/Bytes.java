package org.python.types;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Bytes extends org.python.types.Object {
    public byte[] value;

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

    public Bytes(byte[] value) {
        this.value = Arrays.copyOf(value, value.length);
    }

    public Bytes(java.lang.String value) {
        try {
            this.value = value.getBytes("ISO-8859-1");
        } catch (java.io.UnsupportedEncodingException e) {
            throw new org.python.exceptions.UnicodeDecodeError();
        }
    }

    @org.python.Method(
            __doc__ = "bytes(iterable_of_ints) -> bytes" +
                    "bytes(string, encoding[, errors]) -> bytes\n" +
                    "bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer\n" +
                    "bytes(int) -> bytes object of size given by the parameter initialized with null bytes\n" +
                    "bytes() -> empty bytes object\n" +
                    "\n" +
                    "Construct an immutable array of bytes from:\n" +
                    " - an iterable yielding integers in range(256)\n" +
                    " - a text string encoded using the specified encoding\n" +
                    " - any object implementing the buffer API.\n" +
                    " - an integer\n",
            default_args = {"source", "encoding", "errors"}
    )
    public Bytes(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'bytes' not implemented");
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("str.__new__() has not been implemented.");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("str.__init__() has not been implemented.");
    // }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.types.Str __repr__() {
        return this.__str__();
    }

    @org.python.Method(
            __doc__ = "Return str(self)."
    )
    public org.python.types.Str __str__() {
        StringBuilder sb = new StringBuilder();
        sb.append("b'");
        for (byte c : this.value) {
            if (c == '\n') {
                sb.append("\\n");
            } else if (c == '\t') {
                sb.append("\\t");
            } else if (c == '\r') {
                sb.append("\\r");
            } else if (c >= 32 && c < 127) {
                sb.append((char) c);
            } else {
                sb.append(String.format("\\x%02x", c));
            }
        }
        sb.append("'");
        return new org.python.types.Str(sb.toString());
    }

    @org.python.Method(
            __doc__ = "Return self==value.",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_value = ((org.python.types.Bytes) other).value;
            return new org.python.types.Bool(Arrays.equals(this.value, other_value));
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_value = ((org.python.types.ByteArray) other).value;
            if (other_value == null) {
                other_value = new byte[0];
            }
            return new org.python.types.Bool(Arrays.equals(this.value, other_value));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self+value.",
            args = {"other"}
    )
    public org.python.Object __add__(org.python.Object other) {
        if (other instanceof org.python.types.Bytes) {
            byte[] other_bytes = (byte[]) ((org.python.types.Bytes) other).value;
            byte[] new_bytes = new byte[this.value.length + other_bytes.length];
            System.arraycopy(this.value, 0, new_bytes, 0, this.value.length);
            System.arraycopy(other_bytes, 0, new_bytes, this.value.length, other_bytes.length);
            return new Bytes(new_bytes);
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_bytes = (byte[]) ((org.python.types.ByteArray) other).value;
            if (other_bytes == null) {
                return this;
            }
            byte[] new_bytes = new byte[this.value.length + other_bytes.length];
            System.arraycopy(this.value, 0, new_bytes, 0, this.value.length);
            System.arraycopy(other_bytes, 0, new_bytes, this.value.length, other_bytes.length);
            return new Bytes(new_bytes);
        }
        if (org.Python.VERSION < 0x03050400 || (org.Python.VERSION >= 0x03060000 && org.Python.VERSION < 0x03060200)) {
            throw new org.python.exceptions.TypeError("can't concat bytes to " + other.typeName());
        } else {
            throw new org.python.exceptions.TypeError("can't concat " + other.typeName() + " to bytes");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __and__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for &: 'bytes' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary +: 'bytes'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: 'bytes'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'bytes'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __bool__() {
        return new org.python.types.Bool(this.value.length > 0);
    }

    @org.python.Method(
            __doc__ = "Return true if contains the arg",
            args = {"slice"}
    )
    public org.python.Object __contains__(org.python.Object slice) {
        byte[] bslice;
        if (slice instanceof org.python.types.Int) {
            int islice = (int) ((org.python.types.Int) slice).value;
            if (islice < 0 || islice > 255) {
                throw new org.python.exceptions.ValueError("byte must be in range(0, 256)\n");
            }
            bslice = new byte[1];
            bslice[0] = (byte) islice;
        } else if (slice instanceof org.python.types.Bytes) {
            bslice = ((org.python.types.Bytes) slice).value;
        } else if (slice instanceof org.python.types.ByteArray) {
            bslice = ((org.python.types.ByteArray) slice).value;
        } else {
            String error_message = "a bytes-like object is required, not '" + slice.typeName() + "'\n";
            if (org.Python.VERSION < 0x03050000) {
                error_message = "'" + slice.typeName() + "' does not support the buffer interface\n";
            }
            throw new org.python.exceptions.TypeError(error_message);
        }
        int counter_slice = 0;
        for (int i = 0; i < this.value.length + 1; i++) {
            if (counter_slice == bslice.length) {
                return new org.python.types.Bool(true);
            } else if (i == this.value.length) {
                break;
            } else if (bslice[counter_slice] == this.value[i]) {
                counter_slice++;
            } else {
                counter_slice = 0;
            }
        }
        return new org.python.types.Bool(false);
    }

    @org.python.Method(
            __doc__ = "default object formatter"
    )
    public org.python.types.Str __format__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.__format__ has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return self>=value.",
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
            __doc__ = "Return self>value.",
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
            __doc__ = "Return self<=value.",
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
            __doc__ = "Return self<value.",
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
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __mod__(org.python.Object other) {
        if (org.Python.VERSION < 0x03050000) {
            if (other instanceof org.python.types.Dict) {
                return this;
            }
            throw new org.python.exceptions.TypeError(
                    "unsupported operand type(s) for %: 'bytes' and '" + other.typeName() + "'"
            );
        } else {
            if (other instanceof org.python.types.List || other instanceof org.python.types.Range) {
                return this;
            }
            throw new org.python.exceptions.TypeError("not all arguments converted during bytes formatting");
        }
    }

    private org.python.Object __getitem__slice(org.python.Object index) {
        org.python.types.Slice.ValidatedValue slice = ((org.python.types.Slice) index).validateValueTypes();
        byte[] sliced;
        if (slice.start == null && slice.stop == null && slice.step == null) {
            sliced = this.value;
        } else {
            int step;
            if (slice.step != null) {
                step = (int) slice.step.value;
            } else {
                step = 1;
            }
            int start;
            if (slice.start == null) {
                if (step > 0) {
                    start = 0;
                } else {
                    start = this.value.length - 1;
                }
            } else {
                start = (int) slice.start.value;
                //Clamp value to negative positive range of indices
                int length = this.value.length;
                start = Math.max(-length, Math.min(length, start));
                //Compute wrapped index for negative values
                if (start < 0) {
                    start = start + length;
                }
                //Modify the start location for stepping backwaards
                if ((int) slice.start.value >= this.value.length && step < 0) {
                    start = this.value.length - 1;
                }
                //If stepping backwards modify start location to be outside the range
                if ((int) slice.start.value < -this.value.length && step < 0) {
                    start = -1;
                }
            }
            int stop;
            if (slice.stop == null) {
                if (step > 0) {
                    stop = this.value.length;
                } else {
                    stop = -1;
                }
            } else {
                stop = (int) slice.stop.value;
                //Clamp value to negative positive range of indices
                int length = this.value.length;
                stop = Math.max(-length, Math.min(length, stop));
                //Compute wrapped index for negative values
                if (stop < 0) {
                    stop = stop + length;
                }
                //Check for the case where stop was clipped and needs to be inclusive
                if ((int) slice.stop.value < -this.value.length && step < 0) {
                    stop = -1;
                }
            }
            if (step > 0) {
                int sliced_length = (int) Math.ceil((stop - start) / (float) step);
                if (sliced_length <= 0) {
                    return new Bytes(new byte[0]);
                }
                sliced = new byte[sliced_length];
                for (int i = 0, j = start; j < stop; i++, j += step) {
                    sliced[i] = this.value[j];
                }
            } else {
                int sliced_length = (int) Math.ceil((start - stop) / (float) -step);
                if (sliced_length <= 0) {
                    return new Bytes(new byte[0]);
                }
                sliced = new byte[sliced_length];
                for (int i = 0, j = start; j > stop; i++, j += step) {
                    sliced[i] = this.value[j];
                }
            }
        }
        return new Bytes(sliced);
    }

    private org.python.Object __getitem__index(org.python.Object index) {
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
    }

    @org.python.Method(
            __doc__ = "Return self[key].",
            args = {"index"}
    )
    public org.python.Object __getitem__(org.python.Object index) {
        if (index instanceof org.python.types.Slice) {
            return this.__getitem__slice(index);
        } else if (index instanceof org.python.types.Bool || index instanceof org.python.types.Int) {
            return this.__getitem__index(index);
        } else {
            org.python.Object index_object = null;
            boolean error_caught = false;
            try {
                index_object = index.__index__();
            } catch (org.python.exceptions.TypeError error) {
                error_caught = true;
            } catch (org.python.exceptions.AttributeError error) {
                error_caught = true;
            }
            if (error_caught) {
                String message = "byte indices must be integers or slices, not " + index.typeName();
                if (org.Python.VERSION < 0x03050000) {
                    throw new org.python.exceptions.TypeError("byte indices must be integers, not " + index.typeName());
                }
                throw new org.python.exceptions.TypeError(message);
            }
            if (index_object instanceof org.python.types.Int) {
                return this.__getitem__index(index);
            } else {
                throw new org.python.exceptions.TypeError("TypeError: __index__ returned non-int (type " + index_object.typeName() + ")");
            }
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
            __doc__ = "Implement iter(self)."
    )
    public org.python.Object __iter__() {
        java.util.List<org.python.Object> listOfBytes = new java.util.ArrayList<org.python.Object>();
        for (byte b: this.value) {
            listOfBytes.add(new org.python.types.Int(b));
        }
        return new org.python.types.List(listOfBytes).__iter__();
    }

    @org.python.Method(
            __doc__ = "Return len(self)."
    )
    public org.python.types.Int __len__() {
        return new org.python.types.Int(this.value.length);
    }

    @org.python.Method(
            __doc__ = "Return self*value.n",
            args = {"other"}
    )
    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            boolean other_bool = ((org.python.types.Bool) other).value;
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
            for (int i = 0; i < other_value; i++) {
                System.arraycopy(this.value, 0, bytes, i * len, len);
            }
            return new Bytes(bytes);
        } else {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __imul__(org.python.Object other) {
        return this.__mul__(other);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __imod__(org.python.Object other) {
        if (org.Python.VERSION < 0x03050000) {
            throw new org.python.exceptions.TypeError(
                    "unsupported operand type(s) for %=: 'bytes' and '" + other.typeName() + "'"
            );
        } else {
            if (other instanceof org.python.types.List || other instanceof org.python.types.Range) {
                return this.__mod__(other);
            }
            throw new org.python.exceptions.TypeError("not all arguments converted during bytes formatting");
        }
    }

    @org.python.Method(
            __doc__ = "helper for pickle"
    )
    public org.python.Object __reduce__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.__reduce__ has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "helper for pickle"
    )
    public org.python.Object __reduce_ex__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.__reduce_ex__ has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return self*value."
    )
    public org.python.Object __rmul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.__rmul__ has not been implemented.");
    }

    public static byte[] _capitalize(byte[] input) {
        byte[] value = new byte[input.length];
        for (int i = 0; i < input.length; i++) {
            byte b = input[i];
            if (b < 127 && b > 32) {
                char c = (char) b;
                if (i == 0) {
                    c = Character.toUpperCase(c);
                } else {
                    c = Character.toLowerCase(c);
                }
                value[i] = (byte) c;
            } else {
                value[i] = b;
            }
        }
        return value;
    }

    @org.python.Method(
            __doc__ = "B.capitalize() -> copy of B\n\nReturn a copy of B with only its first character capitalized (ASCII)\nand the rest lower-cased."
    )

    public org.python.Object capitalize() {
        return new Bytes(_capitalize(this.value));
    }

    @org.python.Method(
            __doc__ = "B.center(width[, fillbyte]) -> bytes\n" +
                    "\n" +
                    "Return S centered in a bytes of length width. Padding is\n" +
                    "done using the specified fill character (default is a space)\n",
            args = {"width"},
            default_args = {"byteToFill"}
    )
    public org.python.Object center(org.python.Object width, org.python.Object byteToFill) {
        return new org.python.types.Bytes(_center(this.value, width, byteToFill));
    }
    public static byte[] _center(byte[] input, org.python.Object width, org.python.Object byteToFill) {
        byte[] fillByte;
        if (byteToFill instanceof org.python.types.Bytes || byteToFill instanceof org.python.types.ByteArray) {
            if (byteToFill instanceof org.python.types.ByteArray) {
                fillByte = ((org.python.types.ByteArray) byteToFill).value;
            } else {
                fillByte = ((org.python.types.Bytes) byteToFill).value;
            }
            if (fillByte.length != 1) {
                if (org.Python.VERSION < 0x030502F0) {
                    throw new org.python.exceptions.TypeError("must be a byte string of length 1, not bytes");
                } else {
                    throw new org.python.exceptions.TypeError("center() argument 2 must be a byte string of length 1, not bytes");
                }
            }
        } else if (byteToFill == null) {
            fillByte = " ".getBytes();
        } else {
            if (org.Python.VERSION < 0x030502F0) {
                throw new org.python.exceptions.TypeError("must be a byte string of length 1, not " + byteToFill.typeName());
            } else {
                throw new org.python.exceptions.TypeError("center() argument 2 must be a byte string of length 1, not " + byteToFill.typeName());
            }
        }

        if (width instanceof org.python.types.Int) {
            int iwidth = (int) ((org.python.types.Int) width).value;
            if (input.length >= iwidth) {
                return input;
            } else {
                int diff = iwidth - input.length;
                int lenfirst = (diff) / 2;
                int lensecond = diff - lenfirst;

                byte[] returnBytes;
                returnBytes = new byte[iwidth];

                for (int i = 0; i < lenfirst; i++) {
                    returnBytes[i] = fillByte[0];
                }
                for (int i = lenfirst; i < (iwidth - lensecond); i++) {
                    returnBytes[i] = input[i - lenfirst];
                }
                for (int i = (iwidth - lensecond); i < iwidth; i++) {
                    returnBytes[i] = fillByte[0];
                }
                return returnBytes;
            }
        } else if (width instanceof org.python.types.Bool) {
            return input;
        } else {
            throw new org.python.exceptions.TypeError("'" + width.typeName() +
              "'" + " object cannot be interpreted as an integer\n");
        }
    }

    @org.python.Method(
            __doc__ = "B.count(sub[, start[, end]]) -> int\n" +
                "\n" +
                "Return the number of non-overlapping occurrences of " +
                "subsequence sub in the range [start, end]. Optional " +
                "arguments start and end are interpreted as in slice" +
                "notation.\n" +
                "The subsequence to search for may be any bytes-like object" +
                "or an integer in the range 0 to 255.\n",
            args = {"sub"},
            default_args = {"start", "end"}
    )
    public org.python.Object count(org.python.Object sub, org.python.Object start, org.python.Object end) {
        byte[] sub_array;
        if (sub instanceof org.python.types.Int) {
            int isub = (int) (((org.python.types.Int) sub).value);
            if (isub < 0 || isub > 255) {
                throw new org.python.exceptions.ValueError("byte must be in range(0, 256)");
            }
            sub_array = new byte[1];
            sub_array[0] = (byte) isub;
        } else if (sub instanceof org.python.types.Bytes) {
            sub_array = ((org.python.types.Bytes) sub).value;
        } else {
            String error_message = "a bytes-like object is required, not '" + sub.typeName() + "'\n";
            if (org.Python.VERSION < 0x03050000) {
                error_message = "'" + sub.typeName() + "' does not support the buffer interface\n";
            }
            throw new org.python.exceptions.TypeError(error_message);
        }
        //If the sub string is longer than the value string a match cannot exist
        if (sub_array.length > this.value.length) {
            return new org.python.types.Int(0);
        }
        int istart = 0;
        int iend = this.value.length;
        //todo: Error if end is not slice type
        if (start != null) {
            if (start instanceof org.python.types.Int) {
                istart = (int) (((org.python.types.Int) start).value);
                //Clamp value to negative positive range of indices
                int length = this.value.length;
                istart = Math.max(-length, Math.min(length, istart));
                //Compute wrapped index for negative values(Python modulo operation)
                if (istart < 0) {
                    istart = ((istart % length) + length) % length;
                }
            } else {
                //todo: how is this suppose to be handled? slice doesn't even provide this?
                throw new org.python.exceptions.TypeError("slice indices must be integers or None or have an __index__ method");
            }
        }
        //todo: Error if end is not slice type
        if (end != null) {
            if (end instanceof org.python.types.Int) {
                iend = (int) (((org.python.types.Int) end).value);
                //Clamp value to negative positive range of indices
                int length = this.value.length;
                iend = Math.max(-length, Math.min(length, iend));
                //Compute wrapped index for negative values(Python modulo operation)
                if (iend < 0) {
                    iend = ((iend % length) + length) % length;
                }
            } else {
                //todo: how is this suppose to be handled? slice doesn't even provide this?
                throw new org.python.exceptions.TypeError("slice indices must be integers or None or have an __index__ method");
            }
        }
        int count = 0;
        boolean found_match = true;
        //iend-sub_array.length+1 accounts for the inner loop comparison to
        //  end comparisons at (i+j)==iend
        for (int i = istart; i < iend - sub_array.length + 1; i++) {
            found_match = true;
            for (int j = 0; j < sub_array.length; j++) {
                if (this.value[i + j] != sub_array[j]) {
                    found_match = false;
                    break;
                }
            }
            if (found_match) {
                count++;
                //skip ahead by the length of the sub_array (-1 to account for i++ in outer loop)
                //this consumes the match from the value array
                i += sub_array.length - 1;
            }
        }
        return new org.python.types.Int(count);
    }

    @org.python.Method(
            __doc__ = "B.decode(encoding='utf-8', errors='strict') -> str\n\nDecode B using the codec registered for encoding. Default encoding\nis 'utf-8'. errors may be given to set a different error\nhandling scheme.  Default is 'strict' meaning that encoding errors raise\na UnicodeDecodeError.  Other possible values are 'ignore' and 'replace'\nas well as any other name registerd with codecs.register_error that is\nable to handle UnicodeDecodeErrors."
    )
    public org.python.Object decode(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        try {
            return new org.python.types.Str(new java.lang.String(this.value, "UTF-8"));
            // return new org.python.types.Str(new java.lang.String(this.value, encoding));
        } catch (java.io.UnsupportedEncodingException e) {
            throw new org.python.exceptions.UnicodeDecodeError();
        }
    }

    private org.python.Object endsOrStartsWith(org.python.Object substring, org.python.Object start, org.python.Object end, int direction) {
        if (start != null || end != null) {
            Bytes sliced = (Bytes) this.__getitem__(new org.python.types.Slice(start, end));
            return sliced.endsOrStartsWith(substring, null, null, direction);
        }

        if (substring instanceof org.python.types.Tuple) {
            org.python.types.Tuple tuple = (org.python.types.Tuple) substring;
            int length = (int) tuple.__len__().value;
            for (int i = 0; i < length; i++) {
                org.python.Object item = tuple.__getitem__(new org.python.types.Int(i));
                if (item instanceof org.python.types.Tuple) {
                    throw new org.python.exceptions.TypeError("a bytes-like object is required, not '" + item.typeName() + "'");
                }
                boolean ok = ((org.python.types.Bool) this.endsOrStartsWith(item, null, null, direction)).value;
                if (ok) {
                    return new org.python.types.Bool(true);
                }
            }
            return new org.python.types.Bool(false);

        } else if (substring instanceof Bytes) {
            byte[] substringValue = ((Bytes) substring).value;
            if (substringValue.length > this.value.length) {
                return new org.python.types.Bool(false);
            }

            int startIndex;
            int endIndex;

            if (direction < 0) {
                startIndex = 0;
                endIndex = substringValue.length;
            } else {
                startIndex = this.value.length - substringValue.length;
                endIndex = this.value.length;
            }

            byte[] thisValuePart = Arrays.copyOfRange(this.value, startIndex, endIndex);
            boolean ok = Arrays.equals(thisValuePart, substringValue);
            return new org.python.types.Bool(ok);
        } else {
            String methodName;
            if (direction < 0) {
                methodName = "startswith";
            } else {
                methodName = "endswith";
            }
            throw new org.python.exceptions.TypeError(methodName + " first arg must be bytes or a tuple of bytes, not " + substring.typeName());
        }
    }

    @org.python.Method(
            __doc__ = "B.endswith(suffix[, start[, end]]) -> bool\n\nReturn True if B ends with the specified suffix, False otherwise.\nWith optional start, test B beginning at that position.\nWith optional end, stop comparing B at that position.\nsuffix can also be a tuple of bytes to try.",
            args = {"suffix"},
            default_args = {"start", "end"}
    )
    public org.python.Object endswith(org.python.Object suffix, org.python.Object start, org.python.Object end) {
        return endsOrStartsWith(suffix, start, end, 1);
    }

    @org.python.Method(
            __doc__ = "B.expandtabs(tabsize=8) -> copy of B\n\nReturn a copy of B where all tab characters are expanded using spaces.\nIf tabsize is not given, a tab size of 8 characters is assumed."
    )
    public org.python.Object expandtabs(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.expandtabs has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "B.find(sub[, start[, end]]) -> int" +
            "\n\nReturn the lowest index in B where substring sub is found,\nsuch that sub is contained within B[start:end].  Optional" +
            "\narguments start and end are interpreted as in slice notation.\n\nReturn -1 on failure.",
            args = {"sub"},
            default_args = {"start", "end"}
    )
    public org.python.types.Int find(org.python.Object sub, org.python.Object start, org.python.Object end) {
        int _start = 0;
        int _end = 0;
        if (start != null && !(start instanceof org.python.types.NoneType)) {
            _start = (int) ((Int) start).value;
        }
        if (end == null || end instanceof org.python.types.NoneType) {
            _end = this.value.length;
        }
        byte[] _sub;
        if (sub instanceof org.python.types.ByteArray) {
            _sub = ((org.python.types.ByteArray) sub).value;
        } else {
            _sub = ((org.python.types.Bytes) sub).value;
        }
        if (_sub.length <= 0) {
            return new Int(0);
        }
        int pos = -1;
        for (int i = 0; _start < _end; _start++) {
            byte b1 = this.value[_start];
            byte b2 = _sub[i];
            if (b1 == b2) {
                i++;
                if (pos == -1) {
                    pos = _start;
                }
            }
            if (i == _sub.length) {
                break;
            }
            if (b1 != b2) {
                i = 0;
                pos = -1;
            }
        }
        return new Int(pos);
    }

    @org.python.Method(
            __doc__ = "bytes.fromhex(string) -> bytes\n\nCreate a bytes object from a string of hexadecimal numbers.\nSpaces between two numbers are accepted.\nExample: bytes.fromhex('B9 01EF') -> b'\\xb9\\x01\\xef'."
    )
    public org.python.Object fromhex(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.fromhex has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "get an index of any byte from bytes",
            args = {"sub"},
            default_args = {"start", "end"}
    )
    public org.python.types.Int index(org.python.Object sub, org.python.Object start, org.python.Object end) {
        Int pos = this.find(sub, start, end);
        if (pos.equals(new Int(-1))) {
            String message = "subsection not found";
            if (org.Python.VERSION < 0x03060000) {
                message = "substring not found";
            }
            throw new org.python.exceptions.ValueError(message);
        }
        return pos;
    }

    @org.python.Method(
            __doc__ = "B.isalnum() -> bool\n\nReturn True if all characters in B are alphanumeric\nand there is at least one character in B, False otherwise."
    )
    public org.python.Object isalnum() {
        if (this.value.length == 0) {
            return new org.python.types.Bool(false);
        }
        for (byte ch: this.value) {
            if (!(ch >= 'A' && ch <= 'Z') && !(ch >= 'a' && ch <= 'z') &&
                        !(ch >= '0' && ch <= '9')) {
                return new org.python.types.Bool(false);
            }
        }
        return new org.python.types.Bool(true);
    }

    public static boolean _isalpha(byte[] input) {
        if (input.length == 0) {
            return false;
        }
        for (byte ch : input) {
            if (!_isalpha(ch)) {
                return false;
            }
        }
        return true;
    }

    public static boolean _isalpha(byte ch) {
        return (ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z');
    }

    @org.python.Method(
            __doc__ = "B.isalpha() -> bool\n\nReturn True if all characters in B are alphabetic\nand there is at least one character in B, False otherwise."
    )
    public org.python.Object isalpha() {
        return new Bool(_isalpha(this.value));
    }

    @org.python.Method(
            __doc__ = "B.isdigit() -> bool\n\nReturn True if all characters in B are digits\nand there is at least one character in B, False otherwise."
    )
    public org.python.Object isdigit() {
        if (this.value.length == 0) {
            return new org.python.types.Bool(false);
        }
        for (byte ch : this.value) {
            if (!(ch >= '0' && ch <= '9')) {
                return new org.python.types.Bool(false);
            }
        }
        return new org.python.types.Bool(true);
    }

    public static boolean _islower(byte[] input) {
        if (input.length == 0) {
            return false;
        }
        byte[] value = new byte[input.length];
        for (int i = 0; i < input.length; i++) {
            byte b = input[i];
            if ((b < 97 || b > 122) && b != ' ') {
                return false;
            }
        }
        return true;
    }

    @org.python.Method(
            __doc__ = "B.islower() -> bool\n\nReturn True if all cased characters in B are lowercase and there is\nat least one cased character in B, False otherwise."
    )
    public org.python.Object islower() {
        return new Bool(_islower(this.value));
    }

    public static boolean _isspace(byte[] input) {
        if (input.length == 0) {
            return false;
        }
        for (byte ch : input) {
            // VT \x0b = 11
            if (ch != ' ' && ch != '\t' && ch != '\n' && ch != '\r' && ch != 11 && ch != '\f') {
                return false;
            }
        }
        return true;
    }

    @org.python.Method(
            __doc__ = "B.isspace() -> bool\n\nReturn True if all characters in B are whitespace\nand there is at least one character in B, False otherwise."
    )
    public org.python.Object isspace() {
        return new Bool(_isspace(this.value));
    }

    public static boolean _istitle(byte[] input) {
        if (input.length == 0) {
            return false;
        }

        if (Arrays.equals(input, _title(input))) {
            for (int idx = 0; idx < input.length; ++idx) {
                if (_isalpha(input[idx])) {
                    return true;
                }
            }
        }

        return false;
    }

    @org.python.Method(
            __doc__ = "B.istitle() -> bool\n\nReturn True if B is a titlecased string and there is at least one\ncharacter in B, i.e. uppercase characters may only follow uncased\ncharacters and lowercase characters only cased ones. Return False\notherwise."
    )
    public org.python.Object istitle() {
        return new org.python.types.Bool(_istitle(this.value));
    }

    public static boolean _isupper(byte[] input) {
        if (input.length == 0) {
            return false;
        }
        byte[] value = new byte[input.length];
        for (int i = 0; i < input.length; i++) {
            byte b = input[i];
            if ((b < 65 || b > 90) && b != ' ') {
                return false;
            }
        }
        return true;
    }

    @org.python.Method(
            __doc__ = "B.isupper() -> bool\n\nReturn True if all cased characters in B are uppercase and there is\nat least one cased character in B, False otherwise."
    )
    public org.python.Object isupper() {
        return new Bool(_isupper(this.value));
    }

    @org.python.Method(
            __doc__ = "B.join(iterable_of_bytes) -> bytes\n\nConcatenate any number of bytes objects, with B in between each pair.\nExample: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'."
    )
    public org.python.Object join(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.join has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "B.ljust(width[, fillchar]) -> copy of B\n\nReturn B left justified in a string of length width. Padding is\ndone using the specified fill character (default is a space)."
    )
    public org.python.Object ljust(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.ljust has not been implemented.");
    }

    public static byte[] _lower(byte[] input) {
        byte[] result = new byte[input.length];
        for (int idx = 0; idx < input.length; ++idx) {
            char lc = (char) input[idx];
            result[idx] = (byte) Character.toLowerCase(lc);
        }
        return result;
    }

    @org.python.Method(
            __doc__ = "B.lower() -> copy of B\n\nReturn a copy of B with all ASCII characters converted to lowercase."
    )
    public org.python.Object lower() {
        return new Bytes(_lower(this.value));
    }

    @org.python.Method(
            __doc__ = "B.lstrip([bytes]) -> bytes\n\nStrip leading bytes contained in the argument.\nIf the argument is omitted, strip leading ASCII whitespace."
    )
    public Bytes lstrip() {
        int start = 0;
        int end = this.value.length;

        while (start < end && Character.isWhitespace(this.value[start])) {
            start++;
        }

        byte[] slice = Arrays.copyOfRange(this.value, start, end);


        return new Bytes(slice);
    }

    @org.python.Method(
            __doc__ = "B.maketrans(frm, to) -> translation table\n\nReturn a translation table (a bytes object of length 256) suitable\nfor use in the bytes or bytearray translate method where each byte\nin frm is mapped to the byte at the same position in to.\nThe bytes objects frm and to must be of the same length."
    )
    public org.python.Object maketrans(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.maketrans has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "B.partition(sep) -> (head, sep, tail)\n\nSearch for the separator sep in B, and return the part before it,\nthe separator itself, and the part after it.  If the separator is not\nfound, returns B and two empty bytes objects.",
            args = {"sep"}
    )
    public org.python.Object partition(org.python.Object sep) {
        Tuple result = new Tuple();
        int pos = (int) this.find(sep, null, null).value;
        if (pos < 0) {
            result.value.add(this);
            result.value.add(new Bytes(""));
            result.value.add(new Bytes(""));
        }
        else {
            result.value.add(new Bytes(Arrays.copyOfRange(this.value, 0, pos)));
            result.value.add(sep);
            result.value.add(new Bytes(Arrays.copyOfRange(this.value, pos + ((Bytes)sep).value.length, this.value.length)));
        }
        return result;
    }

    @org.python.Method(
            __doc__ = "B.replace(old, new[, count]) -> bytes\n\nReturn a copy of B with all occurrences of subsection\nold replaced by new.  If the optional argument count is\ngiven, only first count occurances are replaced."
    )
    public org.python.Object replace(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.replace has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "B.rfind(sub[, start[, end]]) -> int\n\nReturn the highest index in B where substring sub is found,\nsuch that sub is contained within B[start:end].  Optional\narguments start and end are interpreted as in slice notation.\n\nReturn -1 on failure."
    )
    public org.python.Object rfind(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.rfind has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "B.rindex(sub[, start[, end]]) -> int\n\nLike B.rfind() but raise ValueError when the substring is not found."
    )
    public org.python.Object rindex(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.rindex has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "B.rjust(width[, fillchar]) -> copy of B\n\nReturn B right justified in a string of length width. Padding is\ndone using the specified fill character (default is a space)"
    )
    public org.python.Object rjust(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.rjust has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "B.rpartition(sep) -> (head, sep, tail)\n\nSearch for the separator sep in B, starting at the end of B,\nand return the part before it, the separator itself, and the\npart after it.  If the separator is not found, returns two empty\nbytes objects and B."
    )
    public org.python.Object rpartition(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.rpartition has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "B.rsplit(sep=None, maxsplit=-1) -> list of bytes\n\nReturn a list of the sections in B, using sep as the delimiter,\nstarting at the end of B and working to the front.\nIf sep is not given, B is split on ASCII whitespace characters\n(space, tab, return, newline, formfeed, vertical tab).\nIf maxsplit is given, at most maxsplit splits are done."
    )
    public org.python.Object rsplit(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.rsplit has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "B.rstrip([bytes]) -> bytes\n\nStrip trailing bytes contained in the argument.\nIf the argument is omitted, strip trailing ASCII whitespace."
    )
    public Bytes rstrip() {
        int start = 0;
        int end = this.value.length - 1;

        while (end > start && Character.isWhitespace(this.value[end])) {
            end--;
        }

        byte[] slice = Arrays.copyOfRange(this.value, start, end + 1);

        return new Bytes(slice);
    }

    @org.python.Method(
            __doc__ = "B.split(sep=None, maxsplit=-1) -> list of bytes\n\nReturn a list of the sections in B, using sep as the delimiter.\nIf sep is not specified or is None, B is split on ASCII whitespace\ncharacters (space, tab, return, newline, formfeed, vertical tab).\nIf maxsplit is given, at most maxsplit splits are done."
    )
    public org.python.Object split(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.split has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "B.splitlines([keepends]) -> list of lines\n\nReturn a list of the lines in B, breaking at line boundaries.\nLine breaks are not included in the resulting list unless keepends\nis given and true."
    )
    public org.python.Object splitlines(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.splitlines has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "B.startswith(prefix[, start[, end]]) -> bool\n\nReturn True if B starts with the specified prefix, False otherwise.\nWith optional start, test B beginning at that position.\nWith optional end, stop comparing B at that position.\nprefix can also be a tuple of bytes to try.",
            args = {"prefix"},
            default_args = {"start", "end"}
    )
    public org.python.Object startswith(org.python.Object prefix, org.python.Object start, org.python.Object end) {
        return endsOrStartsWith(prefix, start, end, -1);
    }

    @org.python.Method(
            __doc__ = "B.strip([bytes]) -> bytes\n\nStrip leading and trailing bytes contained in the argument.\nIf the argument is omitted, strip leading and trailing ASCII whitespace."
    )
    public org.python.Object strip() {
        return this.lstrip().rstrip();
    }

    public static byte[] _swapcase(byte[] input) {
        byte[] result = new byte[input.length];
        for (int idx = 0; idx < input.length; ++idx) {
            char lc = (char) input[idx];
            if (Character.isUpperCase(lc)) {
                result[idx] = (byte) Character.toLowerCase(lc);
            } else {
                result[idx] = (byte) Character.toUpperCase(lc);
            }
        }
        return result;
    }

    @org.python.Method(
            __doc__ = "B.swapcase() -> copy of B\n\nReturn a copy of B with uppercase ASCII characters converted\nto lowercase ASCII and vice versa."
    )
    public org.python.Object swapcase() {
        return new Bytes(_swapcase(this.value));
    }

    public static byte[] _title(byte[] input) {
        byte[] result = new byte[input.length];
        boolean capitalizeNext = true;

        for (int idx = 0; idx < input.length; ++idx) {
            byte lc = input[idx];
            if (!_isalpha(lc)) {
                result[idx] = lc;
                capitalizeNext = true;
            } else if (capitalizeNext) {
                result[idx] = (byte) Character.toUpperCase((char) lc);
                capitalizeNext = false;
            } else {
                result[idx] = (byte) Character.toLowerCase((char) lc);
            }
        }
        return result;
    }

    @org.python.Method(
            __doc__ = "B.title() -> copy of B\n\nReturn a titlecased version of B, i.e. ASCII words start with uppercase\ncharacters, all remaining cased characters have lowercase."
    )
    public org.python.Object title() {
        return new Bytes(_title(this.value));
    }

    @org.python.Method(
            __doc__ = "B.translate(table[, deletechars]) -> bytes\n\nReturn a copy of B, where all characters occurring in the\noptional argument deletechars are removed, and the remaining\ncharacters have been mapped through the given translation\ntable, which must be a bytes object of length 256."
    )
    public org.python.Object translate(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.translate has not been implemented.");
    }

    public static byte[] _upper(byte[] input) {
        byte[] result = new byte[input.length];
        for (int idx = 0; idx < input.length; ++idx) {
            char lc = (char) input[idx];
            result[idx] = (byte) Character.toUpperCase(lc);
        }
        return result;
    }

    @org.python.Method(
            __doc__ = "B.upper() -> copy of B\n\nReturn a copy of B with all ASCII characters converted to uppercase."
    )
    public org.python.Object upper() {
        return new Bytes(_upper(this.value));
    }

    @org.python.Method(
            __doc__ = "B.zfill(width) -> copy of B\n\nPad a numeric string B with zeros on the left, to fill a field\nof the specified width.  B is never truncated."
    )
    public org.python.Object zfill(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("bytes.zfill has not been implemented.");
    }
}
