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

    public org.python.Object byValue() {
        return new org.python.types.Str(this.value);
    }

    public int hashCode() {
        return this.value.hashCode();
    }

    public Str() {
        this.value = "";
    }

    public Str(java.lang.String str) {
        this.value = str;
    }

    public Str(char chr) {
        this.value = new java.lang.String(new char[]{chr});
    }

    @org.python.Method(
            __doc__ = "str(object='') -> str" +
                    "str(bytes_or_buffer[, encoding[, errors]]) -> str\n" +
                    "\n" +
                    "Create a new string object from the given object. If encoding or\n" +
                    "errors is specified, then the object must expose a data buffer\n" +
                    "that will be decoded using the given encoding and error handler.\n" +
                    "Otherwise, returns the result of object.__str__() (if defined)\n" +
                    "or repr(object).\n" +
                    "encoding defaults to sys.getdefaultencoding().\n" +
                    "errors defaults to 'strict'.\n",
            default_args = {"object"}
    )
    public Str(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args[0] == null) {
            this.value = "";
        } else {
            this.value = ((org.python.types.Str) args[0].__str__()).value;
        }
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("__new__() has not been implemented.");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("__init__() has not been implemented.");
    // }

    private static boolean isCharPrintable(char c) {
        // ASCII non-printable
        if ((int) c <= 0x1f || (int) c >= 0x7f && (int) c <= 0xa0 || (int) c == 0xad) {
            return false;
        }
        if ((int) c == 0x2029) {
            return false;
        }
        if (Character.isISOControl(c)) {
            return false;
        }
        return true;
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __repr__() {
    /*
    * Reference: https://www.python.org/dev/peps/pep-3138/#id7
    * TODO: Need to treat the leading surrogate pair characters
    */
        StringBuilder sb = new StringBuilder();
        boolean hasDoubleQuote = false;
        boolean hasSingleQuote = false;

        for (char c : this.value.toCharArray()) {
            if (c == '\'') {
                hasSingleQuote = true;
            } else if (c == '"') {
                hasDoubleQuote = true;
            }

            if (c == '\n') {
                sb.append("\\n");
            } else if (c == '\t') {
                sb.append("\\t");
            } else if (c == '\r') {
                sb.append("\\r");
            } else if (c == '\\') {
                sb.append("\\\\");
            // ASCII Non-Printable
            } else if (c <= 0x1f || c >= 0x7f && c <= 0xa0 || c == 0xad) {
                sb.append(String.format("\\x%02x", (int) c));
            } else if (!this.isCharPrintable(c)) {
                sb.append(String.format("\\u%04x", (int) c));
            } else {
                sb.append((char) c);
            }
        }

        // Decide if we wanna wrap the result with single or double quotes
        String quote;
        String repr = sb.toString();

        if (hasSingleQuote) {
            if (hasDoubleQuote) {
                quote = "'";
                repr = repr.replaceAll("'", "\\\\'");
            } else {
                quote = "\"";
            }
        } else {
            quote = "'";
        }

        return new org.python.types.Str(quote + repr + quote);
    }


    @org.python.Method(
            __doc__ = "Return str(self)."
    )
    public org.python.Object __str__() {
        return new org.python.types.Str(this.value);
    }

    @org.python.Method(
            __doc__ = "S.__format__(format_spec) -> str\n\nReturn a formatted version of S as described by format_spec."
    )
    public org.python.Object __format__(org.python.Object format_string) {
        throw new org.python.exceptions.NotImplementedError("__format__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __int__() {
        try {
            return new org.python.types.Int(Long.parseLong(this.value));
        } catch (NumberFormatException e) {
            throw new org.python.exceptions.ValueError("invalid literal for int() with base 10: '" + this.value + "'");
        }
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __float__() {
        double result;
        try {
            result = java.lang.Double.parseDouble(this.value);
        } catch (NumberFormatException e) {
            java.lang.String trimmed = this.value.trim();
            if (trimmed == "inf") {
                result = java.lang.Double.POSITIVE_INFINITY;
            } else if (trimmed == "-inf") {
                result = java.lang.Double.NEGATIVE_INFINITY;
            } else if (trimmed == "nan") {
                result = java.lang.Double.NaN;
            } else {
                java.lang.String value = this.value;
                if (value.length() > 0) {
                    value = "'" + value + "'";
                }
                throw new org.python.exceptions.ValueError(
                        "could not convert string to float: " + value);
            }
        }
        return new org.python.types.Float(result);
    }

    @org.python.Method(
            __doc__ = "Return self<value.",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        if (other instanceof org.python.types.Str) {
            java.lang.String value = ((org.python.types.Str) other).value;
            return new org.python.types.Bool(this.value.compareTo(value) < 0);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }

    @org.python.Method(
            __doc__ = "Return self<=value.",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        if (other instanceof org.python.types.Str) {
            java.lang.String value = ((org.python.types.Str) other).value;
            return new org.python.types.Bool(this.value.compareTo(value) <= 0);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }

    @org.python.Method(
            __doc__ = "Return self==value.",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.Str) {
            java.lang.String value = ((org.python.types.Str) other).value;
            return new org.python.types.Bool(this.value.equals(value));
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }

    @org.python.Method(
            __doc__ = "Return self>value.",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        if (other instanceof org.python.types.Str) {
            java.lang.String value = ((org.python.types.Str) other).value;
            return new org.python.types.Bool(this.value.compareTo(value) > 0);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }

    @org.python.Method(
            __doc__ = "Return self>=value.",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        if (other instanceof org.python.types.Str) {
            java.lang.String value = ((org.python.types.Str) other).value;
            return new org.python.types.Bool(this.value.compareTo(value) >= 0);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // Builtin types can't have attributes set on them.
        return false;
    }

    @org.python.Method(
            __doc__ = "__dir__() -> list\ndefault dir() implementation"
    )
    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("__dir__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "len(object)\n\nReturn the number of items of a sequence or collection."
    )
    public org.python.types.Int __len__() {
        return new org.python.types.Int(this.value.length());
    }

    @org.python.Method(
            __doc__ = "Return self[key].",
            args = {"index"}
    )
    public org.python.Object __getitem__(org.python.Object index) {
        try {
            if (index instanceof org.python.types.Slice) {
                org.python.types.Slice.ValidatedValue slice = ((org.python.types.Slice) index).validateValueTypes();
                java.lang.String sliced;

                if (slice.start == null && slice.stop == null && slice.step == null) {
                    sliced = this.value;
                } else {
                    long start;
                    if (slice.start != null) {
                        start = toPositiveIndex(slice.start.value);
                    } else {
                        start = 0;
                    }

                    long stop;
                    if (slice.stop != null) {
                        stop = toPositiveIndex(slice.stop.value);
                    } else {
                        stop = this.value.length();
                    }
                    stop = Math.max(start, stop);

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
                            buffer.append(this.value.charAt((int) i));
                        }
                        sliced = buffer.toString();
                    }
                }
                return new org.python.types.Str(sliced);
            } else if (index instanceof org.python.types.Bool) {
                boolean slice = ((org.python.types.Bool) index).value;
                java.lang.String sliced;

                if (this.value.length() == 0) {
                    throw new org.python.exceptions.IndexError("string index out of range");
                } else {
                    if (slice) {
                        sliced = this.value.substring(1, 2);
                    } else {
                        sliced = this.value.substring(0, 1);
                    }
                    return new org.python.types.Str(sliced);
                }
            } else {
                int idx = (int) ((org.python.types.Int) index).value;
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
            throw new org.python.exceptions.TypeError("string indices must be integers");
        }
    }

    @org.python.Method(
            __doc__ = "Implement iter(self)."
    )
    public org.python.Object __iter__() {
        java.util.List<org.python.Object> listOfStrs = new java.util.ArrayList<org.python.Object>();
        for (int i = 0; i < this.value.length(); i++) {
            listOfStrs.add(new org.python.types.Str(this.value.substring(i, i + 1)));
        }
        return new org.python.types.List(listOfStrs).__iter__();
    }

    @org.python.Method(
            __doc__ = "Return key in self.",
            args = {"item"}
    )
    public org.python.types.Int __contains__(org.python.Object item) {
        if (item instanceof org.python.types.Str) {

            int substr_exists = 0;
            org.python.types.Str item_str = (org.python.types.Str) item;

            if (this.value.length() == 0 && item_str.value.length() == 0) {
                substr_exists = 1;
            } else {
                for (int i = 0; i < this.value.length() - item_str.value.length(); i++) {
                    boolean mismatch = false;
                    for (int j = 0; j < item_str.value.length(); j++) {
                        if (this.value.charAt(i + j) != item_str.value.charAt(j)) {
                            mismatch = true;
                            break;
                        }
                    }
                    if (!mismatch) {
                        substr_exists = 1;
                    }
                }
            }
            return new org.python.types.Int(substr_exists);
        }
        if (org.Python.VERSION < 0x03060000) {
            throw new org.python.exceptions.TypeError("Can't convert '" + item.typeName() + "' object to str implicitly");
        } else {
            throw new org.python.exceptions.TypeError("must be str, not " + item.typeName());
        }
        // throw new org.python.exceptions.NotImplementedError("__contains__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return self+value.",
            args = {"other"}
    )
    public org.python.Object __add__(org.python.Object other) {
        if (other instanceof org.python.types.Str) {
            org.python.types.Str other_str = (org.python.types.Str) other;
            if (0 == other_str.value.length()) {
                return this;
            }
            java.lang.StringBuffer sb = new java.lang.StringBuffer(value);
            sb.append(other_str.value);
            return new org.python.types.Str(sb.toString());
        }
        if (org.Python.VERSION < 0x03060000) {
            throw new org.python.exceptions.TypeError("Can't convert '" + other.typeName() + "' object to str implicitly");
        } else {
            throw new org.python.exceptions.TypeError("must be str, not " + other.typeName());
        }
    }

    @org.python.Method(
            __doc__ = "Return self*value.n",
            args = {"other"}
    )
    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            long other_int = ((org.python.types.Int) other).value;
            if (other_int < 1) {
                return new org.python.types.Str("");
            }
            java.lang.StringBuffer res = new java.lang.StringBuffer(value.length() * (int) other_int);
            for (int i = 0; i < other_int; i++) {
                res.append(value);
            }
            return new org.python.types.Str(res.toString());
        } else if (other instanceof org.python.types.Bool) {
            boolean other_bool = ((org.python.types.Bool) other).value;
            if (other_bool) {
                return new org.python.types.Str(value);
            } else {
                return new org.python.types.Str("");
            }
        }
        throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self%value.",
            args = {"other"}
    )
    public org.python.Object __mod__(org.python.Object other) {
        return org.python.types.PythonFormatter.format(this, other);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ipow__(org.python.Object other) {
        this.setValue(this.__pow__(other, null));
        return this;
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary +: 'str'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: 'str'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'str'");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __bool__() {
        return new org.python.types.Bool(this.value.length() > 0);
    }

    @org.python.Method(
            __doc__ = "Return self*value.",
            args = {"other"}
    )
    public org.python.Object __rmul__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("__rmul__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value%self.",
            args = {"other"}
    )
    public org.python.Object __rmod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("__rmod__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __imul__(org.python.Object other) {
        this.setValue(this.__mul__(other));
        return this;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __imod__(org.python.Object other) {
        this.setValue(this.__mod__(other));
        return this;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"ndigits"}
    )
    public org.python.Object __round__(org.python.Object ndigits) {

        throw new org.python.exceptions.TypeError("type str doesn't define __round__ method");
    }

    @org.python.Method(
            __doc__ = "S.capitalize() -> str\n" +
                    "\n" +
                    "Return a capitalized version of S, i.e. make the first character\n" +
                    "have upper case and the rest lower case.\n"
    )
    public org.python.Object capitalize() {
        if (this.value.length() > 0) {
            java.lang.String newval = this.value.substring(0, 1).toUpperCase() + this.value.substring(1).toLowerCase();
            return new org.python.types.Str(newval);
        }
        return this;
    }

    @org.python.Method(
            __doc__ = "S.casefold() -> str\n" +
                    "\n" +
                    "Return a version of S suitable for caseless comparisons.\n"
    )
    public org.python.Object casefold() {
        return new org.python.types.Str(this.value.toUpperCase().toLowerCase());
    }

    @org.python.Method(
            __doc__ = "S.center(width[, fillchar]) -> str\n" +
                    "\n" +
                    "Return S centered in a string of length width. Padding is\n" +
                    "done using the specified fill character (default is a space)\n",
            args = {"width"},
            default_args = {"charToFill"}
    )
    public org.python.Object center(org.python.Object width, org.python.Object charToFill) {
        java.lang.String fillChar = new java.lang.String();
        if (charToFill instanceof org.python.types.Str) {
            // fillChar has right type
            if (((org.python.types.Str) charToFill).value.length() != 1) {
                throw new org.python.exceptions.TypeError("The fill character must be exactly one character long");
            }
            fillChar = ((org.python.types.Str) charToFill).value;
        } else if (charToFill == null) {
            fillChar = " ";
        } else {
            throw new org.python.exceptions.TypeError("Fill char must of type String");
        }

        if (width instanceof org.python.types.Int) {
            java.lang.String str = this.value;
            int widthVal = (int) ((org.python.types.Int) width).value;
            int strLen = str.length();
            if (strLen >= widthVal) {
                return new org.python.types.Str(str);
            } else {
                int diff = widthVal - strLen;
                int lenFirst = (diff) / 2;
                int lenSecond = diff - lenFirst;

                java.lang.StringBuffer returnString = new java.lang.StringBuffer(widthVal);

                for (int i = 0; i < lenFirst; i++) {
                    returnString.append(fillChar);
                }
                returnString.append(str);
                for (int i = 0; i < lenSecond; i++) {
                    returnString.append(fillChar);
                }
                return new org.python.types.Str(returnString.toString());
            }
        } else if (width instanceof org.python.types.Bool) {
            return new org.python.types.Str(this.value);
        }

        throw new org.python.exceptions.TypeError("Length must be of type Integer or Bool");
    }

    @org.python.Method(
            __doc__ = "S.count(sub[, start[, end]]) -> int\n" +
                    "\n" +
                    "Return the number of non-overlapping occurrences of substring sub in\n" +
                    "string S[start:end].  Optional arguments start and end are\n" +
                    "interpreted as in slice notation.\n",
            args = {"item"},
            default_args = {"start", "end"}
    )
    public org.python.Object count(org.python.Object sub, org.python.Object start, org.python.Object end) {
        java.lang.String sub_str = ((org.python.types.Str) sub).value;
        if (start == null) {
            start = new org.python.types.Int(0);
        }
        if (end == null) {
            end = new org.python.types.Int(this.value.length());
        }
        java.lang.String original = this.__getitem__(new org.python.types.Slice(start, end)).toString();
        return new org.python.types.Int((original.length() - original.replace(sub_str, "").length()) / sub_str.length());
    }

    @org.python.Method(
            __doc__ = "S.encode(encoding='utf-8', errors='strict') -> bytes\n" +
                    "\n" +
                    "Encode S using the codec registered for encoding. Default encoding\n" +
                    "is 'utf-8'. errors may be given to set a different error\n" +
                    "handling scheme. Default is 'strict' meaning that encoding errors raise\n" +
                    "a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and\n" +
                    "'xmlcharrefreplace' as well as any other name registered with\n" +
                    "codecs.register_error that can handle UnicodeEncodeErrors.\n"
    )
    public org.python.Object encode() {
        throw new org.python.exceptions.NotImplementedError("encode() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "S.endswith(suffix[, start[, end]]) -> bool\n" +
                    "\n" +
                    "Return True if S ends with the specified suffix, False otherwise.\n" +
                    "With optional start, test S beginning at that position.\n" +
                    "With optional end, stop comparing S at that position.\n" +
                    "suffix can also be a tuple of strings to try.\n",
            args = {"suffix"},
            default_args = {"start", "end"}
    )
    public org.python.Object endswith(org.python.Object suffix, org.python.Object start, org.python.Object end) {
        if (suffix instanceof org.python.types.Str) {
            if (start == null) {
                start = new org.python.types.Int(0);
            }
            if (end == null) {
                end = new org.python.types.Int(this.value.length());
            }
            java.lang.String original = this.__getitem__(new org.python.types.Slice(start, end)).toString();
            boolean result = original.endsWith(((org.python.types.Str) suffix).toString());
            return new org.python.types.Bool(result);
        }
        throw new org.python.exceptions.TypeError("endswith first arg must be str, not " + suffix.typeName());
    }

    @org.python.Method(
            __doc__ = "S.expandtabs(tabsize=8) -> str\n" +
                    "\n" +
                    "Return a copy of S where all tab characters are expanded using spaces.\n" +
                    "If tabsize is not given, a tab size of 8 characters is assumed.\n",
            default_args = {"tabsize"}
    )
    public org.python.Object expandtabs(org.python.Object tabsize) {
        int tabsize_int = 8;
        if (tabsize != null) {
            tabsize_int = (int) ((org.python.types.Int) tabsize).value;
        }
        if (this.value == null) {
            return null;
        }
        java.lang.StringBuilder buf = new java.lang.StringBuilder();
        int col = 0;
        for (int i = 0; i < this.value.length(); i++) {
            char c = this.value.charAt(i);
            switch (c) {
                case '\n':
                    col = 0;
                    buf.append(c);
                    break;
                case '\t':
                    buf.append(this.spaces(tabsize_int - col % tabsize_int));
                    col += tabsize_int - col % tabsize_int;
                    break;
                default:
                    col++;
                    buf.append(c);
                    break;
            }
        }
        return new org.python.types.Str(buf.toString());
    }

    private static String spaces(int n) {
        java.lang.StringBuilder buf = new java.lang.StringBuilder();
        for (int sp = 0; sp < n; sp++) {
            buf.append(" ");
        }
        return buf.toString();
    }

    @org.python.Method(
            __doc__ = "S.find(sub[, start[, end]]) -> int\n" +
                    "\n" +
                    "Return the lowest index in S where substring sub is found,\n" +
                    "such that sub is contained within S[start:end].  Optional\n" +
                    "arguments start and end are interpreted as in slice notation.\n",
            args = {"item"},
            default_args = {"start", "end"}
    )
    public org.python.Object find(org.python.Object item, org.python.Object start, org.python.Object end) {
        if (start == null) {
            start = new org.python.types.Int(0);
        }
        if (end == null) {
            end = new org.python.types.Int(this.value.length());
        }
        int foundAt = this.__getitem__(new Slice(start, end)).toString().indexOf(item.toString());
        if (foundAt >= 0) {
            return new org.python.types.Int(foundAt + toPositiveIndex(((Int) start).value));
        }
        return new org.python.types.Int(foundAt);
    }

    @org.python.Method(
            __doc__ = "S.format(*args, **kwargs) -> str\n" +
                    "\n" +
                    "Return a formatted version of S, using substitutions from args and kwargs.\n" +
                    "The substitutions are identified by braces ('{' and '}').\n"
    )
    public org.python.Object format() {
        throw new org.python.exceptions.NotImplementedError("format() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "S.format_map(mapping) -> str\n" +
                    "\n" +
                    "Return a formatted version of S, using substitutions from mapping.\n" +
                    "The substitutions are identified by braces ('{' and '}').\n"
    )
    public org.python.Object format_map() {
        throw new org.python.exceptions.NotImplementedError("format_map() has not been implemented.");
    }

    /** Normalize index into an index in the range [0, this.value.length()] */
    private long toPositiveIndex(long index) {
        if (index < 0) {
            if (-index > this.value.length()) {
                return 0;
            } else {
                return index + this.value.length();
            }
        } else {
            if (index > this.value.length()) {
                return this.value.length();
            } else {
                return index;
            }
        }
    }

    @org.python.Method(
            __doc__ = "S.index(sub[, start[, end]]) -> int\n" +
                    "\n" +
                    "Like S.find() but raise ValueError when the substring is not found.\n",
            args = {"item"},
            default_args = {"start", "end"}
    )
    public org.python.Object index(org.python.Object item, org.python.Object start, org.python.Object end) {
        org.python.Object foundAt = this.find(item, start, end);
        if (((Int) foundAt).value < 0) {
            throw new org.python.exceptions.ValueError("substring not found");
        } else {
            return foundAt;
        }
    }

    @org.python.Method(
            __doc__ = "S.isalnum() -> bool\n" +
                    "\n" +
                    "Return True if all characters in S are alphanumeric\n" +
                    "and there is at least one character in S, False otherwise.\n"
    )
    public org.python.Object isalnum() {
        if (this.value.isEmpty()) {
            return new org.python.types.Bool(false);
        }
        for (char c : this.value.toCharArray()) {
            if (!java.lang.Character.isLetter(c) && !java.lang.Character.isDigit(c)) {
                return new org.python.types.Bool(false);
            }
        }
        return new org.python.types.Bool(true);
    }

    @org.python.Method(
            __doc__ = "S.isalpha() -> bool\n" +
                    "\n" +
                    "Return True if all characters in S are alphabetic\n" +
                    "and there is at least one character in S, False otherwise.\n"
    )
    public org.python.Object isalpha() {
        if (this.value.isEmpty()) {
            return new org.python.types.Bool(false);
        }
        for (char ch : this.value.toCharArray()) {
            if (!(Character.isLetter(ch))) {
                return new org.python.types.Bool(false);
            }
        }
        return new org.python.types.Bool(true);
    }

    @org.python.Method(
            __doc__ = "S.isdecimal() -> bool\n" +
                    "\n" +
                    "Return True if there are only decimal characters in S,\n" +
                    "False otherwise.\n"
    )
    public org.python.Object isdecimal() {
        if (this.value.isEmpty()) {
            return new org.python.types.Bool(false);
        }
        for (char c : this.value.toCharArray()) {
            if (!java.lang.Character.isDigit(c)) {
                return new org.python.types.Bool(false);
            }
        }
        return new org.python.types.Bool(true);
    }

    @org.python.Method(
            __doc__ = "S.isdigit() -> bool\n" +
                    "\n" +
                    "Return True if all characters in S are digits\n" +
                    "and there is at least one character in S, False otherwise.\n"
    )
    public org.python.Object isdigit() {
        if (this.value.isEmpty()) {
            return new org.python.types.Bool(false);
        }
        for (char ch : this.value.toCharArray()) {
            if (!(Character.isDigit(ch))) {
                return new org.python.types.Bool(false);
            }
        }
        return new org.python.types.Bool(true);
    }

    @org.python.Method(
            __doc__ = "S.isidentifier() -> bool\n" +
                    "\n" +
                    "Return True if S is a valid identifier according\n" +
                    "to the language definition.\n" +
                    "\n" +
                    "Use keyword.iskeyword() to test for reserved identifiers\n" +
                    "such as \"def\" and \"class\".\n"
    )
    public org.python.Object isidentifier() {
        if (this.value.isEmpty()) {
            return new org.python.types.Bool(false);
        }
        boolean firstCheck = true;
        for (char ch : this.value.toCharArray()) {
            // Beginning with underscores seems to blow up on isUnicodeIdentifierStart
            if (ch == '_') {
                continue;
            }
            if (firstCheck) {
                if (!(Character.isUnicodeIdentifierStart(ch))) {
                    return new org.python.types.Bool(false);
                }
                firstCheck = false;
            } else {
                if (!(Character.isUnicodeIdentifierPart(ch))) {
                    return new org.python.types.Bool(false);
                }
            }
        }
        return new org.python.types.Bool(true);
    }

    @org.python.Method(
            __doc__ = "S.islower() -> bool\n" +
                    "\n" +
                    "Return True if all cased characters in S are lowercase and there is\n" +
                    "at least one cased character in S, False otherwise.\n"
    )
    public org.python.Object islower() {
        if (!this.value.isEmpty() && this.value.toLowerCase().equals(this.value)) {
            return new org.python.types.Bool(true);
        }
        return new org.python.types.Bool(false);
    }

    @org.python.Method(
            __doc__ = "S.isnumeric() -> bool\n" +
                    "\n" +
                    "Return True if there are only numeric characters in S,\n" +
                    "False otherwise.\n"
    )
    public org.python.Object isnumeric() {
        if (this.value.isEmpty()) {
            return new org.python.types.Bool(false);
        }
        for (char ch : this.value.toCharArray()) {
            if (!(Character.isDigit(ch))) {
                return new org.python.types.Bool(false);
            }
        }
        return new org.python.types.Bool(true);
    }

    @org.python.Method(
            __doc__ = "S.isprintable() -> bool\n" +
                    "\n" +
                    "Return True if all characters in S are considered\n" +
                    "printable in repr() or S is empty, False otherwise.\n"
    )
    public org.python.Object isprintable() {
        for (char ch : this.value.toCharArray()) {
            if (!this.isCharPrintable(ch)) {
                return new org.python.types.Bool(false);
            }
        }
        return new org.python.types.Bool(true);
    }

    @org.python.Method(
            __doc__ = "S.isspace() -> bool\n" +
                    "\n" +
                    "Return True if all characters in S are whitespace\n" +
                    "and there is at least one character in S, False otherwise.\n"
    )
    public org.python.Object isspace() {
        if (this.value.isEmpty()) {
            return new org.python.types.Bool(false);
        }
        for (char ch : this.value.toCharArray()) {
            if (!isWhitespace(ch)) {
                return new org.python.types.Bool(false);
            }
        }
        return new org.python.types.Bool(true);
    }

    @org.python.Method(
            __doc__ = "S.istitle() -> bool\n" +
                    "\n" +
                    "Return True if S is a titlecased string and there is at least one\n" +
                    "character in S, i.e. upper- and titlecase characters may only\n" +
                    "follow uncased characters and lowercase characters only cased ones.\n" +
                    "Return False otherwise.\n"
    )
    public org.python.Object istitle() {
        if (this.value.isEmpty()) {
            return new org.python.types.Bool(false);
        }

        if (this.value.equals(_title(this.value))) {
            for (int idx = 0; idx < this.value.length(); idx++) {
                if (Character.isLetter(this.value.charAt(idx))) {
                    return new org.python.types.Bool(true);
                }
            }
        }

        return new org.python.types.Bool(false);
    }

    @org.python.Method(
            __doc__ = "S.isupper() -> bool\n" +
                    "\n" +
                    "Return True if all cased characters in S are uppercase and there is\n" +
                    "at least one cased character in S, False otherwise.\n"
    )
    public org.python.Object isupper() {
        if (!this.value.isEmpty() && this.value.toUpperCase().equals(this.value)) {
            return new org.python.types.Bool(true);
        }
        return new org.python.types.Bool(false);
    }

    @org.python.Method(
            __doc__ = "S.join(iterable) -> str\n" +
                    "\n" +
                    "Return a string which is the concatenation of the strings in the\n" +
                    "iterable.  The separator between elements is S.\n",
            args = {"iterable"}
    )
    public org.python.Object join(org.python.Object iterable) {
        java.util.List<org.python.Object> temp_list = new java.util.ArrayList<org.python.Object>();
        org.python.Object iter = null;
        try {
            iter = org.Python.iter(iterable);
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("can only join an iterable");
        }
        try {
            while (true) {
                org.python.Object item = iter.__next__();
                temp_list.add(item);
            }
        } catch (org.python.exceptions.StopIteration e) {
        }
        java.lang.StringBuilder buf = new java.lang.StringBuilder();
        boolean firstTime = true;
        for (org.python.Object each : temp_list) {
            if (firstTime) {
                buf.append(each.toString());
                firstTime = false;
            } else {
                buf.append(this.value).append(each.toString());
            }
        }
        return new org.python.types.Str(buf.toString());
    }

    @org.python.Method(
            __doc__ = "S.ljust(width[, fillchar]) -> str\n" +
                    "\n" +
                    "Return S left-justified in a Unicode string of length width. Padding is\n" +
                    "done using the specified fill character (default is a space).\n",
            args = {"width"},
            default_args = {"fillChar"}
    )
    public org.python.Object ljust(org.python.Object width, org.python.Object fillChar) {
        java.lang.String ch = "";
        if (fillChar instanceof org.python.types.Str) {
            if (((org.python.types.Str) fillChar).value.length() != 1) {
                throw new org.python.exceptions.TypeError("The fill character must be exactly one character long");
            }
            ch = ((org.python.types.Str) fillChar).value;
        } else if (fillChar == null) {
            ch = " ";
        } else {
            throw new org.python.exceptions.TypeError("The fill character cannot be converted to Unicode");
        }

        if (!(width instanceof org.python.types.Int)) {
            throw new org.python.exceptions.TypeError("integer argument expected, got " + org.Python.typeName(width.getClass()));
        }

        int w = (int) ((org.python.types.Int) width).value;
        if (w < this.value.length()) {
            return new org.python.types.Str(this.value);
        }
        java.lang.StringBuffer str = new java.lang.StringBuffer(w);
        str.append(this.value);
        int balance = w - this.value.length();
        for (int i = 0; i < balance; i++) {
            str.append(ch);
        }
        return new org.python.types.Str(str.toString());
    }

    @org.python.Method(
            __doc__ = "S.lower() -> str\n" +
                    "\n" +
                    "Return a copy of the string S converted to lowercase.\n"
    )
    public org.python.Object lower() {
        return new org.python.types.Str(this.value.toLowerCase());
    }

    @org.python.Method(
            __doc__ = "S.lstrip([chars]) -> str\n" +
                    "\n" +
                    "Return a copy of the string S with leading whitespace removed.\n" +
                    "If chars is given and not None, remove characters in chars instead.\n",
            default_args = {"chars"}
    )
    public org.python.Object lstrip(org.python.Object chars) {
        int start = 0;
        int end = this.value.length();
        if (chars == null || chars instanceof org.python.types.NoneType) {
            while (start < end && isWhitespace(this.value.charAt(start))) {
                start++;
            }
        } else if (chars instanceof org.python.types.Str) {
            org.python.types.Str chars_str = (org.python.types.Str) chars;
            while (start < end && chars_str.value.indexOf(this.value.charAt(start)) != -1) {
                start++;
            }
        } else {
            throw new org.python.exceptions.TypeError("lstrip arg must be None or str");
        }
        return new org.python.types.Str(this.value.substring(start, end));
    }

    @org.python.Method(
             __doc__ = "Return a translation table usable for str.translate().\n" +
                    "\n" +
                    "If there is only one argument, it must be a dictionary mapping Unicode\n" +
                    "ordinals (integers) or characters to Unicode ordinals, strings or None.\n" +
                    "Character keys will be then converted to ordinals.\n" +
                    "If there are two arguments, they must be strings of equal length, and\n" +
                    "in the resulting dictionary, each character in x will be mapped to the\n" +
                    "character at the same position in y. If there is a third argument, it\n" +
                    "must be a string, whose characters will be mapped to None in the result.\n"
    )
    public org.python.Object maketrans() {
        throw new org.python.exceptions.NotImplementedError("maketrans() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "S.partition(sep) -> (head, sep, tail)\n" +
                    "\n" +
                    "Search for the separator sep in S, and return the part before it,\n" +
                    "the separator itself, and the part after it.  If the separator is not\n" +
                    "found, return S and two empty strings.\n",
            args = {"sep"}
    )
    public org.python.Object partition(org.python.Object sep) {
        java.lang.String sepStr = ((org.python.types.Str) sep).value;
        if (sepStr.equals("")) {
            throw new org.python.exceptions.ValueError("empty separator");
        }
        java.lang.String[] split = this.value.split(sepStr, 2);
        java.util.List<org.python.Object> tuple = new java.util.ArrayList<org.python.Object>();
        tuple.add(new org.python.types.Str(split[0]));
        if (split.length != 1) {
            tuple.add(sep);
            tuple.add(new org.python.types.Str(split[1]));
        } else {
            tuple.add(new org.python.types.Str(""));
            tuple.add(new org.python.types.Str(""));
        }
        return new org.python.types.Tuple(tuple);
    }

    @org.python.Method(
            __doc__ = "S.replace(old, new[, count]) -> str\n" +
                    "\n" +
                    "Return a copy of S with all occurrences of substring\n" +
                    "old replaced by new.  If the optional argument count is\n" +
                    "given, only the first count occurrences are replaced.\n",
            default_args = {"repChars", "repWith", "num"}
    )
    public org.python.Object replace(org.python.Object repChars, org.python.Object repWith, org.python.Object num) {

        if (repWith == null && repChars == null) {
            throw new org.python.exceptions.TypeError("replace() takes at least 2 arguments (0 given)");
        } else if (repWith == null || repChars == null) {
            throw new org.python.exceptions.TypeError("replace() takes at least 2 arguments (1 given)");
        } else if (!(repChars instanceof org.python.types.Str)) {
            if (org.Python.VERSION < 0x03060000) {
                throw new org.python.exceptions.TypeError("Can't convert '" + repChars.typeName() + "' object to str implicitly");
            } else {
                throw new org.python.exceptions.TypeError("replace() argument 1 must be str, not " + repChars.typeName());
            }
        } else if (!(repWith instanceof org.python.types.Str)) {
            if (org.Python.VERSION < 0x03060000) {
                throw new org.python.exceptions.TypeError("Can't convert '" + repWith.typeName() + "' object to str implicitly");
            } else {
                throw new org.python.exceptions.TypeError("replace() argument 2 must be str, not " + repWith.typeName());
            }
        }
        int no;
        if (num == null) {
            no = this.value.length();
        } else {
            no = Integer.parseInt(num.toString());
        }
        java.lang.String replace = ((org.python.types.Str) repChars).value;
        java.lang.String replaceWith = ((org.python.types.Str) repWith).value;
        java.lang.String str = this.value;
        java.lang.String ret_str = str;
        if (replace == "") {
            ret_str = replaceWith;
            for (int i = 0; i < str.length(); i++) {
                char c = str.charAt(i);
                ret_str += c;
                ret_str += replaceWith;
            } //  ^^^^  to cover the border case of replacing an empty string with something
        } else {
            for (int i = 0; i < no && i < str.length(); i++) {
                ret_str = ret_str.replaceFirst(replace, replaceWith);
            }
        }
        return new org.python.types.Str(ret_str);
    }

    @org.python.Method(
            __doc__ = "S.rfind(sub[, start[, end]]) -> int\n" +
                    "\n" +
                    "Return the highest index in S where substring sub is found,\n" +
                    "such that sub is contained within S[start:end].  Optional\n" +
                    "arguments start and end are interpreted as in slice notation.\n" +
                    "\n" +
                    "Return -1 on failure.\n",
            default_args = {"item", "start", "end"}
    )
    public org.python.Object rfind(org.python.Object item, org.python.Object start, org.python.Object end) {
        if (item == null) {
            throw new org.python.exceptions.TypeError("rfind() takes at least 1 argument (0 given)");
        }
        try {
            org.python.Object st = (org.python.types.Str) item;
        } catch (ClassCastException te) {
            throw new org.python.exceptions.TypeError("Can't convert '" + item.typeName() + "' object to str implicitly");
        }
        if (start == null) {
            start = new org.python.types.Int(0);
        }
        if (end == null) {
            end = new org.python.types.Int(this.value.length());
        }
        org.python.Object index = new org.python.types.Int(-1);
        org.python.Object temp = (org.python.types.Int) index;
        while (((org.python.types.Bool) (temp.__lt__(end))).value) {
            temp = this.find(item, start, end);
            if (((org.python.types.Int) temp).value < 0) {
                break;
            }
            index = temp;
            start = temp.__add__(new org.python.types.Int(1));
        }
        return index;
    }

    @org.python.Method(
            __doc__ = "S.rindex(sub[, start[, end]]) -> int\n" +
                    "\n" +
                    "Like S.rfind() but raise ValueError when the substring is not found.\n",
            default_args = {"items", "start", "end"}
    )
    public org.python.Object rindex(org.python.Object item, org.python.Object start, org.python.Object end) {
        if (item == null) {
            throw new org.python.exceptions.TypeError("rindex() takes at least 1 argument (0 given)");
        }
        org.python.Object index = this.rfind(item, start, end);
        if (((org.python.types.Int) index).value < 0) {
            throw new org.python.exceptions.ValueError("substring not found");
        } else {
            return index;
        }
    }

    @org.python.Method(
            __doc__ = "S.rjust(width[, fillchar]) -> str\n" +
                    "\n" +
                    "Return S right-justified in a string of length width. Padding is\n" +
                    "done using the specified fill character (default is a space).\n",
            default_args = {"width", "fillChar"}
    )
    public org.python.Object rjust(org.python.Object width, org.python.Object fillChar) {
        if (width == null) {
            throw new org.python.exceptions.TypeError("rjust() takes at least 1 argument (0 given)");
        } else if (!(width instanceof org.python.types.Int)) {
            throw new org.python.exceptions.TypeError("integer argument expected, got " + width.typeName());
        } else {
            java.lang.String ch = new java.lang.String();
            if (fillChar instanceof org.python.types.Str) {
                if (((org.python.types.Str) fillChar).value.length() != 1) {
                    throw new org.python.exceptions.TypeError("The fill character must be exactly one character long");
                }
                ch = ((org.python.types.Str) fillChar).value;
            } else if (fillChar == null) {
                ch = " ";
            } else {
                throw new org.python.exceptions.TypeError("The fill character cannot be converted to Unicode");
            }
            int w = (int) ((org.python.types.Int) width).value;
            if (w < this.value.length()) {
                return new org.python.types.Str(this.value);
            }
            java.lang.StringBuffer str = new java.lang.StringBuffer(w);
            int balance = w - this.value.length();
            for (int i = 0; i < balance; i++) {
                str.append(ch);
            }
            str.append(this.value);
            return new org.python.types.Str(str.toString());
        }
    }

    @org.python.Method(
            __doc__ = "S.rpartition(sep) -> (head, sep, tail)\n" +
                    "\n" +
                    "Search for the separator sep in S, starting at the end of S, and return\n" +
                    "the part before it, the separator itself, and the part after it.  If the\n" +
                    "separator is not found, return two empty strings and S.\n",
            default_args = {"sep"}
    )
    public org.python.Object rpartition(org.python.types.Object sep) {
        java.util.List<org.python.Object> tuple = new java.util.ArrayList<org.python.Object>();
        if (sep == null) {
            throw new org.python.exceptions.TypeError("rpartition() takes exactly one argument (0 given)");
        }
        if (!(sep instanceof org.python.types.Str)) {
            if (org.Python.VERSION < 0x03060000) {
                throw new org.python.exceptions.TypeError("Can't convert '" + org.Python.typeName(sep.getClass()) + "' object to str implicitly");
            }
            return new org.python.exceptions.TypeError("must be str, not " + org.Python.typeName(sep.getClass()));
        }
        java.lang.String sepStr = ((org.python.types.Str) sep).value;
        if (sepStr.equals("")) {
            throw new org.python.exceptions.ValueError("empty separator");
        }
        if (this.value.equals("")) {
            tuple.add(new org.python.types.Str(""));
            tuple.add(new org.python.types.Str(""));
            tuple.add(new org.python.types.Str(""));
            return new org.python.types.Tuple(tuple);
        }
        int i = this.value.lastIndexOf(sepStr);
        if (i != -1) {
            tuple.add(new org.python.types.Str(this.value.substring(0, i)));
            tuple.add(new org.python.types.Str(sepStr));
            tuple.add(new org.python.types.Str(this.value.substring(i + sepStr.length())));
            return new org.python.types.Tuple(tuple);
        }
        tuple.add(new org.python.types.Str(""));
        tuple.add(new org.python.types.Str(""));
        tuple.add(new org.python.types.Str(this.value));
        return new org.python.types.Tuple(tuple);
    }

    @org.python.Method(
            __doc__ = "S.rsplit(sep=None, maxsplit=-1) -> list of strings\n" +
                    "\n" +
                    "Return a list of the words in S, using sep as the\n" +
                    "delimiter string, starting at the end of the string and\n" +
                    "working to the front.  If maxsplit is given, at most maxsplit\n" +
                    "splits are done. If sep is not specified, any whitespace string\n" +
                    "is a separator.\n"
    )
    public org.python.Object rsplit() {
        throw new org.python.exceptions.NotImplementedError("rsplit() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "S.rstrip([chars]) -> str\n" +
                    "\n" +
                    "Return a copy of the string S with trailing whitespace removed.\n" +
                    "If chars is given and not None, remove characters in chars instead.\n",
            default_args = "chars"
    )
    public org.python.Object rstrip(org.python.Object chars) {
        int start = 0;
        int end = this.value.length();
        if (chars == null || chars instanceof org.python.types.NoneType) {
            while (end > start && isWhitespace(this.value.charAt(end - 1))) {
                end--;
            }
        } else if (chars instanceof org.python.types.Str) {
            org.python.types.Str chars_str = (org.python.types.Str) chars;
            while (end > start && chars_str.value.indexOf(this.value.charAt(end - 1)) != -1) {
                end--;
            }
        } else {
            throw new org.python.exceptions.TypeError("rstrip arg must be None or str");
        }
        return new org.python.types.Str(this.value.substring(start, end));
    }

    @org.python.Method(
            __doc__ = "S.split(sep=None, maxsplit=-1) -> list of strings\n" +
                    "\n" +
                    "Return a list of the words in S, using sep as the\n" +
                    "delimiter string.  If maxsplit is given, at most maxsplit\n" +
                    "splits are done. If sep is not specified or is None, any\n" +
                    "whitespace string is a separator and empty strings are\n" +
                    "removed from the result.\n",
            default_args = {"sep", "maxsplit"}
    )
    public org.python.Object split(org.python.Object sep, org.python.Object maxsplit) {
        if (this.value.isEmpty()) {
            if (sep == null) {
                if (maxsplit == null || maxsplit instanceof org.python.types.Int) {
                    return new org.python.types.List();
                }
                throw new org.python.exceptions.TypeError("'" + maxsplit.typeName() + "' cannot be interpreted as an integer");
            } else if (sep instanceof org.python.types.Str) {
                if (maxsplit == null || maxsplit instanceof org.python.types.Int) {
                    org.python.types.List result_list = new org.python.types.List();
                    result_list.append(new org.python.types.Str(""));
                    return result_list;
                }
                throw new org.python.exceptions.TypeError("'" + maxsplit.typeName() + "' cannot be interpreted as an integer");
            }
        }

        java.lang.String value = this.value.toString();
        if (sep == null) {
            value = value.trim();
            sep = new org.python.types.Str("\\s+");
        } else if (!(sep instanceof org.python.types.Str)) {
            if (org.Python.VERSION < 0x03060000) {
                throw new org.python.exceptions.TypeError("Can't convert '" + sep.typeName() + "' object to str implicitly");
            } else {
                throw new org.python.exceptions.TypeError("must be str or None, not " + sep.typeName());
            }
        }

        java.lang.String[] result;
        if (maxsplit == null) {
            result = value.split(((org.python.types.Str) sep).toString());
        } else {
            int number = java.lang.Integer.parseInt(maxsplit.toString());
            result = value.split(((org.python.types.Str) sep).toString(), number + 1);
        }
        org.python.types.List result_list = new org.python.types.List();
        for (java.lang.String w : result) {
            result_list.append(new org.python.types.Str(w));
        }
        if (this.value.endsWith(sep.toString())) {
            result_list.append(new org.python.types.Str(""));
        }
        return result_list;
    }

    private static boolean isLineBreak(char character) {
        // List of line boundaries from https://docs.python.org/3.4/library/stdtypes.html#str.splitlines
        switch (character) {
            case '\n':
            case '\r':
            case '\u000B':
            case '\u000C':
            case '\u001C':
            case '\u001D':
            case '\u001E':
            case '\u0085':
            case '\u2028':
            case '\u2029':
                return true;
            default:
                return false;
        }
    }

    private static boolean isWhitespace(char character) {
        // Compared to Java, Python does not consider U+180E as whitespace,
        // but it does U+0085, U+00A0, U+2007, and U+202F.
        if (character == '\u180E') {
            return false;
        }
        if (Character.isWhitespace(character)) {
            return true;
        }
        switch (character) {
            case '\u0085':
            case '\u00A0':
            case '\u2007':
            case '\u202F':
                return true;
            default:
                return false;
        }
    }

    @org.python.Method(
            __doc__ = "S.splitlines([keepends]) -> list of strings\n" +
                    "\n" +
                    "Return a list of the lines in S, breaking at line boundaries.\n" +
                    "Line breaks are not included in the resulting list unless keepends\n" +
                    "is given and true.\n",
            default_args = {"keepends"}
    )
    public org.python.Object splitlines(org.python.Object keepends) {
        if (keepends == null) {
            keepends = new org.python.types.Bool(false);
        }

        org.python.types.List result = new org.python.types.List();
        char current;

        int start = 0;
        int end;
        int start_extra;
        boolean skip = false;

        for (int i = 0; i < this.value.length(); i++) {
            current = this.value.charAt(i);
            char next = current;

            if (i < this.value.length() - 1) {
                next = this.value.charAt(i + 1);
            }

            if (this.isLineBreak(current)) {
                end = i;
                if (current == '\r' && next == '\n') {
                    skip = true;
                    start_extra = 1;
                    if (keepends.toBoolean()) {
                        end++;
                    }
                } else {
                    start_extra = 0;
                }
                if (keepends.toBoolean()) {
                    end++;
                }
                result.append(this.__getitem__(new org.python.types.Slice(new org.python.types.Int(start), new org.python.types.Int(end))));
                start = i + 1 + start_extra;
                if (skip) {
                    skip = false;
                    i++;
                }
            }
        }
        org.python.types.Str last = (org.python.types.Str) this.__getitem__(new org.python.types.Slice(new org.python.types.Int(start), org.python.types.NoneType.NONE));
        if (last.value.length() > 0) {
            result.append(last);
        }
        return result;

    }

    @org.python.Method(
            __doc__ = "S.startswith(prefix[, start[, end]]) -> bool\n" +
                    "\n" +
                    "Return True if S starts with the specified prefix, False otherwise.\n" +
                    "With optional start, test S beginning at that position.\n" +
                    "With optional end, stop comparing S at that position.\n" +
                    "prefix can also be a tuple of strings to try.\n",
            args = {"suffix"},
            default_args = {"start", "end"}
    )
    public org.python.Object startswith(org.python.Object suffix, org.python.Object start, org.python.Object end) {
        if (suffix instanceof org.python.types.Str) {
            if (start == null) {
                start = new org.python.types.Int(0);
            }
            if (end == null) {
                end = new org.python.types.Int(this.value.length());
            }
            java.lang.String original = this.__getitem__(new org.python.types.Slice(start, end)).toString();
            boolean result = original.startsWith(((org.python.types.Str) suffix).toString());
            return new org.python.types.Bool(result);
        }
        throw new org.python.exceptions.TypeError("startswith first arg must be str, not " + suffix.typeName());
    }

    @org.python.Method(
            __doc__ = "S.strip([chars]) -> str\n" +
                    "\n" +
                    "Return a copy of the string S with leading and trailing\n" +
                    "whitespace removed.\n" +
                    "If chars is given and not None, remove characters in chars instead.\n",
            default_args = {"chars"}
    )
    public org.python.Object strip(org.python.Object chars) {
        if (chars == null || chars instanceof org.python.types.NoneType) {
            return new org.python.types.Str(this.value.trim());
        } else if (chars instanceof org.python.types.Str) {
            return ((org.python.types.Str) this.lstrip(chars)).rstrip(chars);
        } else {
            throw new org.python.exceptions.TypeError("strip arg must be None or str");
        }
    }

    @org.python.Method(
            __doc__ = "S.swapcase() -> str\n" +
                    "\n" +
                    "Return a copy of S with uppercase characters converted to lowercase\n" +
                    "and vice versa.\n"
    )
    public org.python.Object swapcase() {
        if (this.value.isEmpty()) {
            return new org.python.types.Str(this.value);
        }
        java.lang.StringBuffer swapcase = new java.lang.StringBuffer();
        for (int c = 0; c < this.value.length(); c++) {
            if (Character.isUpperCase(this.value.charAt(c))) {
                swapcase.append(Character.toLowerCase(this.value.charAt(c)));
            } else {
                swapcase.append(Character.toUpperCase(this.value.charAt(c)));
            }
        }
        return new org.python.types.Str(swapcase.toString());
    }

    public static String _title(String input) {
        if (input.isEmpty()) {
            return input;
        }

        java.lang.StringBuffer title = new java.lang.StringBuffer();
        title.append(Character.toUpperCase(input.charAt(0)));
        for (int c = 1; c < input.length(); c++) {
            if (!(Character.isLetter(title.charAt(c - 1)))) {
                title.append(Character.toUpperCase(input.charAt(c)));
            } else if (Character.isUpperCase(input.charAt(c))) {
                title.append(Character.toLowerCase(input.charAt(c)));
            } else {
                title.append(input.charAt(c));
            }
        }

        return title.toString();
    }


    @org.python.Method(
            __doc__ = "S.title() -> str\n" +
                    "\n" +
                    "Return a titlecased version of S, i.e. words start with title case\n" +
                    "characters, all remaining cased characters have lower case.\n"
    )
    public org.python.Object title() {
        return new org.python.types.Str(_title(this.value));
    }

    @org.python.Method(
            __doc__ = "S.translate(table) -> str\n" +
                    "\n" +
                    "Return a copy of the string S in which each character has been mapped\n" +
                    "through the given translation table. The table must implement\n" +
                    "lookup/indexing via __getitem__, for instance a dictionary or list,\n" +
                    "mapping Unicode ordinals to Unicode ordinals, strings, or None. If\n" +
                    "this operation raises LookupError, the character is left untouched.\n" +
                    "Characters mapped to None are deleted.\n"
    )
    public org.python.Object translate() {
        throw new org.python.exceptions.NotImplementedError("translate() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "S.upper() -> str\n" +
                    "\n" +
                    "Return a copy of S converted to uppercase.\n"
    )
    public org.python.Object upper() {
        return new org.python.types.Str(this.value.toUpperCase());
    }
}


final class PythonFormatter {

    /*############################# =- Public -= #############################*/
    /*--- Public class methods  ---------------=------------------------------*/

    /**
     * This is the main interface that enables that basically any Python object
     * to be parsed into a given format String. If a Tuple is passed it serves
     * as argument list for format specifiers in the String. A dict requires
     * <b>all</b> format specifier to be mapped to a Key. The dict can only
     * make use if values that have a key of String type since no type cast
     * is performed with the key obtained from the format String.
     *
     * @param  formatString                        Any Python String.
     * @param  arg                                 Any Python objct. Passing
     *                                             {@link org.python.types.Dict Dict} or
     *                                             {@link org.python.types.Tuple Tuple}
     *                                             has special meaning.
     *
     * @return                                      A new String that where any specifier in the format
     *                                                string has been replaced by a corresponding value
     *                                                in args.
     *
     * @throws org.python.exceptions.TypeError     Various errors. Seriously, almost anything that could go wrong throws TypeError.
     * @throws org.python.exceptions.KeyError      if a predicted key could not be found in the given kwargs dict.
     * @throws org.python.exceptions.OverflowError if a character conversion exceeds unicode range.
     * @throws org.python.exceptions.ValueError    if a conversion character is unknown. See Python's documentation.
     * @throws java.lang.NullPointerException      if null passed to method in any argument.
     */
    public static org.python.types.Str format(
            org.python.types.Str formatString, org.python.Object arg)
            throws
                org.python.exceptions.TypeError, org.python.exceptions.KeyError,
                org.python.exceptions.OverflowError, org.python.exceptions.ValueError,
                java.lang.NullPointerException {
        if (formatString == null || arg == null) {
            throw new java.lang.NullPointerException("Cannot pass any null reference to this method.");
        }

        if (arg instanceof org.python.types.Tuple) {
            return new PythonFormatter(formatString.value, ((org.python.types.Tuple) arg).value)._format();
        } else if (arg instanceof org.python.types.Dict) {
            return new PythonFormatter(formatString.value, ((org.python.types.Dict) arg).value)._format();
        } else {
            return new PythonFormatter(formatString.value, arg)._format();
        }
    }

    /**
     * For testing purposes.
     * @param  str The format String.
     * @param  arg Any Python object.
     * @return     The formatted string.
     */
    protected static java.lang.String format(java.lang.String str, org.python.Object arg) {
        return format(new org.python.types.Str(str), arg).value;
    }

    /*############################# =- Private -= ############################*/
    /*--- Private constructor  -----------------------------------------------*/
    private PythonFormatter(java.lang.String formatString, java.util.List<org.python.Object> args) {
        this.formatString = formatString;
        this.args = args;
        this.kwargs = null;

        fillCharacterQueue();
    }

    private PythonFormatter(java.lang.String formatString, java.util.Map<org.python.Object, org.python.Object> kwargs) {
        this.formatString = formatString;
        this.args = new java.util.LinkedList<>();
        this.kwargs = kwargs;

        // necessary for certain edge cases
        this.args.add(new org.python.types.Dict(kwargs));
        fillCharacterQueue();
    }

    private PythonFormatter(java.lang.String formatString, org.python.Object arg) {
        this.formatString = formatString;
        this.args = new java.util.LinkedList<>();
        this.kwargs = null;

        this.singleValueIsAllowed = arg instanceof org.python.types.Bytes
                                 || arg instanceof org.python.types.ByteArray
                                 || arg instanceof org.python.types.Range
                                 || arg instanceof org.python.types.List;

        this.args.add(arg);
        fillCharacterQueue();
    }

    /*--- Private object methods  --------------------------------------------*/

    /**
     * Parses a key if the % char is immediately followed by an opening bracket.
     * It then parses that key with regard to correct bracket count (the key ist
     * always of type string, nothing will be cast and '(' and ')' can be part
     * of it).
     *
     * If a key could be parsed it is looked up in a dictionary that was provided
     * and inserted into the arg list so the following code will not be able to
     * tell the difference.
     */
    private void insertValueOfKeyAsArgIntoArgs() {
        if (!isHeadOfQueueAndIfSoRemove('(')) {
            return;
        }

        handleMappingExceptions();

        java.lang.StringBuilder keyBuilder = new java.lang.StringBuilder();
        for (int openBrackets = 1; openBrackets > 0;) {
            if (characterQueue.isEmpty()) {
                throw new org.python.exceptions.ValueError("incomplete format key");
            }

            if (isHeadOfQueueAndIfSoRemove('(')) {
                openBrackets++;
            } else if (isHeadOfQueueAndIfSoRemove(')') && openBrackets == 1) {
                openBrackets--;
            } else {
                keyBuilder.append(pollNextCharacter());
            }
        }

        org.python.types.Str key = new org.python.types.Str(keyBuilder.toString());

        if (!kwargs.containsKey(key)) {
            throw new org.python.exceptions.KeyError(key);
        }

        // This is really not intuitive. But apparently Python behaves
        // similar. Consider the following valid python code:
        //
        //      %(C)*%s" % {'C': 234, 'D': 2}
        //
        // The * is evaluated as we know it. eval() of the expression
        // yields "%s" instead of raising an error due to the missing
        // arglist as one would expect. Instead if the value for key 'C'
        // is of type str "TypeError: * wants int" will be raised.
        // Anyway, this works.
        args.add(currentArgumentIndex, kwargs.get(key));
    }

    private java.util.Map<java.lang.Character, java.lang.Boolean> parseConversionFlags() {

        java.util.Map<java.lang.Character, java.lang.Boolean> flags = getInitialConversionFlags();

        while (flags.containsKey(peekCharacterQueue())) {
            switch (pollNextCharacter()) {
                case '#':
                    flags.put('#', true);
                    break;

                case '0':
                    // '-' overrides '0'.
                    if (!flags.get('-')) {
                        flags.put('0', true);
                    }
                    break;

                case '-':
                    flags.put('-', true);
                    flags.put('0', false);
                    break;

                case ' ':
                    // '+' overrides ' '
                    if (!flags.get('+')) {
                        flags.put(' ', true);
                    }
                    break;

                case '+':
                    flags.put('+', true);
                    flags.put(' ', false);
                    break;

                default:
                    /* this isn't a python error. I'm just throwing an exception to the
                    caller that the conversion flag isn't legal. */
                    throw new org.python.exceptions.TypeError("illegal character");
            }
        }

        return flags;
    }

    /**
     * The minimum width the arg to be formatted should fill out.
     * @return the minimum width.
     */
    private java.lang.Long parseMinimumWidth() {
        if (isHeadOfQueueAndIfSoRemove('*')) {
            return getIntValueForStarInFormatSpecification();
        }

        java.lang.Long minimumWidth = DEFAULT_MINIMUM_WIDTH; /* == 0 */
        while (java.lang.Character.isDigit(peekCharacterQueue())) {
            minimumWidth = (10 * minimumWidth) + pollNextCharacter() - '0';
        }

        return minimumWidth;
    }

    /**
     * Determine the precision of the arg. In Python this means truncating
     * for a string, precision as usual for floats and missing digits of int
     * values will be filled with zeros.
     *
     * @return The correct precision of a default value.
     */
    private java.lang.Long parsePrecision() {
        java.lang.Long precision = PRECSION_NOT_SET;

        if (isHeadOfQueueAndIfSoRemove('.')) {
            if (isHeadOfQueueAndIfSoRemove('*')) {
                return getIntValueForStarInFormatSpecification();
            }

            /* Python accepts the precision to be omitted and just assumes
            it to be 0. Java would throw UnknownFormatConversionException.*/
            precision = 0L;
            while (java.lang.Character.isDigit(peekCharacterQueue())) {
                precision = (10 * precision) + pollNextCharacter() - '0';
            }
        }

        return precision;
    }


    /**
     * How may character of the format String have already been processed.
     * @return Number of processed characters.
     */
    private int getCurrentCharacterIndex() {
        return formatString.length() - characterQueue.size() - 1;
    }


    /**
     * Determine the conversion. It is important to note here
     * that the wanted conversion type and the object's type do not have to
     * match. In most cases that is not a problem (e.g. if conversion char
     * is d and value has float type it's just type casted). In some cases
     * it leads to certain errors (e.g. d and "zany" even Python won't
     * handle). Furthermore does Java behave very differently from Python,
     * therefore two things are due here:
     *
     *     1. throw errors as needed for Python.
     *     2. then convert most types so Java won't throw errors at us.
     *
     * The general pattern with Java and Python regarding Exceptions is
     * that while Python either ignores options that make no sense with
     * some conversion, Java throws an Exception for everything that does
     * not match.
     *
     *
     * @param conversionFlags The flags '#', '-', '+', ' ', '0',
     * @param minimumWidth    The minimum width of the formatted string
     * @param precision       Precision for float and int values. Can truncate
     *                        strings.
     */
    private void parseConversionChar(
            java.util.Map<java.lang.Character, java.lang.Boolean> conversionFlags,
            java.lang.Long minimumWidth, java.lang.Long precision) {

        char conversionChar = pollNextCharacter();

        /*  We just ignore everything in between %...% just
        like Python does it. No kidding. */
        if (conversionChar == '%') {
            buffer.append('%');
            return;
        }

        org.python.Object fmtObjectPython = popNextArg();
        pythonObjectMatchesConversionOrDie(fmtObjectPython, conversionChar);

        // Choose the Java Object representation and remove and store the
        // sign if the Object represents a number.
        java.lang.Object fmtObjectJava;
        char sign = SIGN_UNDEFINED;
        if (conversionChar == 's') {
            fmtObjectJava = fmtObjectPython.__str__().toJava();
        } else if (conversionChar == 'r') {
            fmtObjectJava = fmtObjectPython.__repr__().toJava();
        } else if (fmtObjectPython instanceof org.python.types.Int) {
            sign = 0 < (java.lang.Long) fmtObjectPython.toJava() ? SIGN_POSITIV : SIGN_NEGATIV;
            fmtObjectJava = java.lang.Math.abs((java.lang.Long) fmtObjectPython.toJava());
        } else if (fmtObjectPython instanceof org.python.types.Float) {
            sign = 0 < (java.lang.Double) fmtObjectPython.toJava() ? SIGN_POSITIV : SIGN_NEGATIV;
            fmtObjectJava = java.lang.Math.abs((java.lang.Double) fmtObjectPython.toJava());
        } else if (fmtObjectPython instanceof org.python.types.Bool /* && not conv == s or r */) {
            fmtObjectJava = ((org.python.types.Bool) fmtObjectPython).value ? 1 : 0;
        } else {
            /* Again not a Python error. */
            throw new org.python.exceptions.TypeError("Conversion impossible");
        }

        java.lang.String preFormattedObject;
        if ("gGfFeE".indexOf(conversionChar) != -1) {
            java.lang.Double value = ((java.lang.Number) fmtObjectJava).doubleValue();
            java.lang.Boolean isVeryLargeOrVerySmall = value >= java.lang.Math.pow(10, precision) || value < .0001;

            if ("gGeE".indexOf(conversionChar) != -1 && isVeryLargeOrVerySmall) {
                preFormattedObject = toExp(value, precision, conversionChar, conversionFlags.get('#'));
            } else {
                preFormattedObject = toFixed(value, precision, conversionFlags.get('#'));
            }

        } else if (conversionChar == 'c') {
            preFormattedObject = java.lang.String.format(
                "%" + conversionChar, (java.lang.Character) fmtObjectJava);

        } else if ("iudoxX".indexOf(conversionChar) != -1) {
            // resolve alias
            if ("iu".indexOf(conversionChar) != -1) {
                conversionChar = 'd';
            }

            preFormattedObject = toInteger(fmtObjectJava, precision, conversionChar);

        } else if ("sr".indexOf(conversionChar) != -1) {
            preFormattedObject = java.lang.String.format(
                "%"
                + (precision != PRECSION_NOT_SET ? "." + precision : "")
                + conversionChar,
                fmtObjectJava
            );

        } else {
            throw new org.python.exceptions.ValueError(
                String.format("unsupported format character '%c' (%#x) at index %d",
                    conversionChar, (int) conversionChar, getCurrentCharacterIndex()));
        }

        java.lang.String signToUse = determineSignToUse(sign, conversionFlags);

        java.lang.String alternateIntegerFormPrefix;
        if (conversionFlags.get('#') && "oxX".indexOf(conversionChar) != -1) {
            alternateIntegerFormPrefix = "0" + conversionChar;
        } else {
            alternateIntegerFormPrefix = "";
        }

        char paddingChar = conversionFlags.get('0') ? '0' : ' ';
        long missingStringLength = java.lang.Math.max(0L, minimumWidth - preFormattedObject.length() - signToUse.length());
        java.lang.String padding = getPaddingOfLength(paddingChar, missingStringLength);

        if (conversionFlags.get('-')) {
            buffer.append(signToUse);
            buffer.append(alternateIntegerFormPrefix);
            buffer.append(preFormattedObject);
            buffer.append(padding);
        } else {
            buffer.append(padding);
            buffer.append(signToUse);
            buffer.append(alternateIntegerFormPrefix);
            buffer.append(preFormattedObject);
        }
    }

    /**
     * The beginning of a formatting specification. Everything is processed as
     * the steps below suggest.
     */
    private void processConversion() {
        insertValueOfKeyAsArgIntoArgs();
        java.util.Map<java.lang.Character, java.lang.Boolean> conversionFlags = parseConversionFlags();

        long minimumWidth = parseMinimumWidth();
        long precision = parsePrecision();

        // Java does not know these and Python does not care.
        if ("hlL".indexOf(peekCharacterQueue()) != -1) {
            pollNextCharacter();
        }

        parseConversionChar(conversionFlags, minimumWidth, precision);
    }


    /**
     * Iterates the format string exactly once without looking ahead. The
     * implementation loosely follows the original CPython format string
     * implementation. Instead of a buffer the implementation uses a
     * {@link java.lang.StringBuilder StringBuilder} to concatenate the string.
     * There is room for optimization though since some Strings are allocated
     * nonetheless. StringBuilder dynamically expanded it's buffer
     * automatically.
     *
     * The detection of errors is lazy, meaning that no a priori checks are
     * preformed (e.g. looking for '%(' and assert a map is given). A string may
     * be parsed almost until the end until an error is thrown. This implements
     * Python behaviour.
     *
     * @return The Python printf style formatted string.
     */
    private org.python.types.Str _format() {
        while (!characterQueue.isEmpty()) {
            if (peekCharacterQueue() != '%') {
                buffer.append(pollNextCharacter());
            } else {
                pollNextCharacter();
                processConversion();
            }
        }

        ensureNoArgumentsAreLeft();
        return new org.python.types.Str(buffer.toString());
    }

    /**
     * Pops and casts the next value for the argument list for a starred
     * expression.
     *
     * @return The Integer value for the next argument of the arg list.
     */
    private java.lang.Long getIntValueForStarInFormatSpecification() {
        if (peekNextArg() instanceof org.python.types.Int) {
            return ((org.python.types.Int) popNextArg()).value;
        } else if (peekNextArg() instanceof org.python.types.Bool) {
            return ((org.python.types.Bool) popNextArg()).value ? 1L : 0L;
        } else {
            throw new org.python.exceptions.TypeError("* wants int");
        }
    }

    /**
     * Fills the character Queue with the current format String.
     */
    private void fillCharacterQueue() {
        for (char c : formatString.toCharArray()) {
            characterQueue.add(c);
        }
    }

    /**
     * Wrapper around peeking at the Character Queue.
     * @return [description]
     */
    private java.lang.Character peekCharacterQueue() {
        if (characterQueue.isEmpty()) {
            throw new org.python.exceptions.ValueError("incomplete format");
        }

        return characterQueue.peek();
    }

    /**
     * Some character only have control function so once it was parsed at the
     * right place it can be disposed. This serves a simple wrapper for that
     * functionality.
     *
     * @param  character The character for which is checked if it is head of queue.
     * @return           True if it was the head and has been removed false otherwise.
     */
    private java.lang.Boolean isHeadOfQueueAndIfSoRemove(java.lang.Character character) {
        if (characterQueue.isEmpty()) {
            throw new org.python.exceptions.ValueError("incomplete format");
        }

        if (characterQueue.peek() == character) {
            characterQueue.remove();
            return true;
        }

        return false;
    }

    /**
     * Wrapper to get the next character. It is checked that the queue is not
     * empty.
     * @return the head of {@link org.python.types.PythonFormatter#characterQueue the queue}.
     */
    private java.lang.Character pollNextCharacter() {
        characterQueue.peek();
        return characterQueue.poll();
    }

    /**
     * A short wrapper for {@link java.util.LinkedList#peek() peek()} on
     * {@link PythonFormatter#args the argument list} method so an error can be
     * thrown, if the list is empty.
     *
     * @return The first value of {@link PythonFormatter#args the argument list}
     * @throws org.python.exceptions.TypeError If the list is empty there have
     *                                         not been enough values.
     */
    private org.python.Object peekNextArg() throws org.python.exceptions.TypeError {
        if (currentArgumentIndex < args.size()) {
            return args.get(currentArgumentIndex);
        }

        throw new org.python.exceptions.TypeError("not enough arguments for format string");
    }

    /**
     * A short wrapper for {@link java.util.LinkedList#peek() pop()} on
     * {@link PythonFormatter#args the argument list} method so an error can be
     * thrown, if the list is empty.
     *
     * @return The first argument of {@link PythonFormatter#args the argument list}
     * @throws org.python.exceptions.TypeError If the list is empty there have
     *                                         not been enough values.
     */
    private org.python.Object popNextArg() throws org.python.exceptions.TypeError {
        peekNextArg();
        return args.get(currentArgumentIndex++);
    }

    /**
     * If there are arguments left that have not been processed throw an Exception
     * otherwise do nothing;
     * @throws org.python.exceptions.TypeError if not all arguments were converted during string formatting
     */
    private void ensureNoArgumentsAreLeft() throws org.python.exceptions.TypeError {
        if (!singleValueIsAllowed && kwargs == null && currentArgumentIndex < args.size()) {
            throw new org.python.exceptions.TypeError(
                "not all arguments converted during string formatting");
        }
    }

    /**
     * Some special cases were no dict is passed to the formatting string
     * but keys are used in the strings. Has no side effects just throws exceptions.
     */
    private void handleMappingExceptions() {

        if (singleValueIsAllowed) {
            org.python.Object arg = peekNextArg();
            if (arg instanceof org.python.types.Range) {
                throw new org.python.exceptions.TypeError("range indices must be integers or slices, not str");
            } else if (arg instanceof org.python.types.Bytes) {
                throw new org.python.exceptions.TypeError("byte indices must be integers, not str");
            } else if (arg instanceof org.python.types.ByteArray) {
                throw new org.python.exceptions.TypeError(arg.typeName() + " indices must be integers");
            } else {
                throw new org.python.exceptions.TypeError(arg.typeName() + " indices must be integers, not str");
            }
        }

        if (kwargs == null) {
            throw new org.python.exceptions.TypeError("format requires a mapping");
        }
    }

    /*############################## =- Class -= #############################*/
    /*--- Private class methods  ---------------------------------------------*/
    /**
     * Given a Python object and a conversion char we can determine if the
     * conversion can be applied. If not a TypeError is thrown. The errors
     * message is identical to the punctuation with Python's error message.
     * Python is very forgiving if the conversion is not intuitive (e.g. %d with
     * a float value) and in that case casts the type to whatever makes sense.
     *
     * In the case of a character conversion an OverflowError error can occur.
     * The current limit is 0x110000 since that is what Java offers.
     *
     * @param pythonObject A Python object that should be inserted into the
     *                     String after conversion.
     * @param conversion   The type of conversion that should be performed.
     *
     * @throws org.python.exceptions.TypeError     If conversion and Object does
     *                                             not match and there is not
     *                                             type case possible.
     * @throws org.python.exceptions.OverflowError In case the objects integer
     *                                             value is not in Unicode range
     */
    private static void pythonObjectMatchesConversionOrDie(org.python.Object pythonObject, char conversion)
        throws org.python.exceptions.TypeError, org.python.exceptions.OverflowError {
        java.lang.Object javaObject = pythonObject.toJava();

        if (conversion == 'c') {
            if (pythonObject instanceof org.python.types.Int || pythonObject instanceof org.python.types.Float) {
                if ((java.lang.Long) javaObject >= 0x110000) { // Unicode max => same as in Java.
                    throw new org.python.exceptions.OverflowError("%c arg not in range(0x110000)");
                }
            } else if (pythonObject instanceof org.python.types.Str && ((java.lang.String) pythonObject.toJava()).length() == 1) {
                javaObject = ((java.lang.String) javaObject).charAt(0);
            } else {
                throw new org.python.exceptions.TypeError("%c requires int or char");
            }
        } else if ("fFgGeE".indexOf(conversion) != -1) {
            if (pythonObject instanceof org.python.types.Complex) {
                throw new org.python.exceptions.TypeError("can't convert complex to float");
            } else if (!(pythonObject instanceof org.python.types.Int
                    || pythonObject instanceof org.python.types.Float
                    || pythonObject instanceof org.python.types.Bool)) {
                throw new org.python.exceptions.TypeError("a float is required");
            }
        } else if ("diouxX".indexOf(conversion) != -1) {
            if (!(pythonObject instanceof org.python.types.Int
                    || pythonObject instanceof org.python.types.Float
                    || pythonObject instanceof org.python.types.Bool)) {
                throw new org.python.exceptions.TypeError("%" + conversion + " format: a number is required, not " + pythonObject.typeName());
            }
        }
    }


    /**
     * Given the formatter has to convert a Number (Float or Int). Various
     * options determine how the formatter handles signed numbers. All options
     * are considered here and a String that should be perpended to a Number is
     * returned.
     * @param  sign The sign as a character. '\0' is the value for no sign
     *              specified.
     *
     * @param flags The conversion flag map
     * @return      Whatever should be appended to the String.
     */
    private static String determineSignToUse(char sign,
            java.util.Map<java.lang.Character, java.lang.Boolean> flags) {

        if (sign == SIGN_POSITIV) {
            if (flags.get(' ')) {
                return " ";
            } else if (flags.get('+')) {
                return "+";
            } else {
                return "";
            }
        } else if (sign == SIGN_UNDEFINED) {
            return "";
        } else {
            return "-";
        }
    }

    /**
     * A wrapper around {@link java.lang.String#format Java's string formatter}
     * for Float values.
     * @param  num             The floating point number to be formatted.
     * @param  precision       The precision, applied as one would expect.
     * @param  conversionChar  The conversion char passed to Java.
     * @param  isAlternateForm Decide if # should be included aka always include
     *                         a dot in floating point numbers.
     * @return                 The desired String correctly formatted by Java.
     */
    private static java.lang.String convertFloatingPointTypeByJavaFormatter(
            java.lang.Double num, long precision, char conversionChar, boolean isAlternateForm) {
        return java.lang.String.format(
            "%" + (isAlternateForm ? "#" : "")
                + (precision == PRECSION_NOT_SET ? "" : "." + precision)
                + conversionChar,
                    ((java.lang.Number) num).doubleValue());
    }

    /**
     * Specifies floating point formatting into fixed decimal format by Java.
     * @param  num              The floating point number to be formatted.
     * @param  precision        The precision, applied as one would expect.
     * @param  isAlternateForm  Decide if # should be included aka always include
     *                          a dot in floating point numbers.
     *
     * @return                  The desired String correctly formatted by Java.
     */
    private static java.lang.String toFixed(java.lang.Double num, long precision, boolean isAlternateForm) {
        return convertFloatingPointTypeByJavaFormatter(num, precision, 'f', isAlternateForm);
    }

    /**
     * Wraps integer formatting by Java.
     * @param  num              The floating point number to be formatted.
     * @param  precision        The precision, applied as one would expect.
     * @param conversionChar    Either e or E.
     * @param  isAlternateForm  Decide if # should be included aka always include
     *                          a dot in floating point numbers.
     *
     * @return                  The desired String correctly formatted by Java.
     */
    private static java.lang.String toExp(java.lang.Double num, long precision, char conversionChar, boolean isAlternateForm) {
        return convertFloatingPointTypeByJavaFormatter(num, precision, conversionChar, isAlternateForm);
    }

    /**
     * A wrapper around {@link java.lang.String#format Java's string formatter}
     * for Integer values.
     *
     * @param  num            Integer or Double that should be converted with
     *                        the given arguments by {@link java.lang.String#format Java's string formatter}
     *
     * @param  precision      The precision for Python's integer conversion
     *                        determines with minimum width of the outputted
     *                        number. Missing digits are padded with zeros. This
     *                        happens regardless of minimum width, padding
     *                        character flag ('0' or ' ') and adjustment.
     *
     * @param  conversionChar Conversion char is passed to Java untouched.
     * @return                The desired String correctly formatted by Java.
     */
    private static java.lang.String toInteger(java.lang.Object num, long precision, char conversionChar) {
        return java.lang.String.format("%"
            + (precision == PRECSION_NOT_SET ? 1 : "0" + precision)
            + conversionChar,
                ((java.lang.Number) num).intValue());
    }

    /**
     * Sets and resets all conversion flags. Must be called for each format
     * specifier in a format string.
     *
     * @return A new HashMap with all flags set false.
     */
    private static java.util.Map<java.lang.Character, java.lang.Boolean> getInitialConversionFlags() {
        java.util.Map<java.lang.Character, java.lang.Boolean> flags = new java.util.HashMap<>();

        flags.put('#', false);
        flags.put('0', false);
        flags.put('+', false);
        flags.put('-', false);
        flags.put(' ', false);

        return flags;
    }

    /**
     * Builds a new String of specified length filled with a given character.
     * @param  filling A char that the string should consist of.
     * @param  length  The length of the returned string.
     * @return         A string of length length which's only character is
     *                   filling.
     */
    private static String getPaddingOfLength(char filling, long length) {
        java.lang.StringBuilder buffer = new StringBuilder();
        while (length-- > 0) {
            buffer.append(filling);
        }

        return new java.lang.String(buffer);
    }

    /*############################# =- Fields -= #############################*/
    /*--- Private object variables -------------------------------------------*/
    // set by Constructor
    private final java.lang.String formatString;
    private final java.util.List<org.python.Object> args;
    private final java.util.Map<org.python.Object, org.python.Object> kwargs;

    // have default values
    private final java.lang.StringBuilder buffer = new StringBuilder();
    private final java.util.Deque<java.lang.Character> characterQueue = new java.util.LinkedList<>();;
    private java.lang.Integer currentArgumentIndex = 0;
    private boolean singleValueIsAllowed = false;

    /*############################ =- Constants -= ###########################*/
    public static final java.lang.Long DEFAULT_MINIMUM_WIDTH = 0L;
    public static final java.lang.Long DEFAULT_PRECSION = 6L;
    public static final java.lang.Long PRECSION_NOT_SET = -1L;

    public static final char SIGN_POSITIV = '-';
    public static final char SIGN_NEGATIV = '+';
    public static final char SIGN_UNDEFINED = '\0';
}
