package org;


public class Python {
    public static java.util.Map<java.lang.String, org.python.Object> builtins;

    static {
        // Load all the builtins into the dictionary as callables
        builtins = new java.util.HashMap<java.lang.String, org.python.Object>();
        org.Python.initializeModule(org.Python.class, builtins);

        // Add all the builtin exceptions
        builtins.put("ArithmeticError", org.python.types.Type.pythonType(org.python.exceptions.ArithmeticError.class));
        builtins.put("AssertionError", org.python.types.Type.pythonType(org.python.exceptions.AssertionError.class));
        builtins.put("AttributeError", org.python.types.Type.pythonType(org.python.exceptions.AttributeError.class));
        builtins.put("BaseException", org.python.types.Type.pythonType(org.python.exceptions.BaseException.class));
        builtins.put("BlockingIOError", org.python.types.Type.pythonType(org.python.exceptions.BlockingIOError.class));
        builtins.put("BrokenPipeError", org.python.types.Type.pythonType(org.python.exceptions.BrokenPipeError.class));
        builtins.put("BufferError", org.python.types.Type.pythonType(org.python.exceptions.BufferError.class));
        builtins.put("BytesWarning", org.python.types.Type.pythonType(org.python.exceptions.BytesWarning.class));
        builtins.put("ChildProcessError", org.python.types.Type.pythonType(org.python.exceptions.ChildProcessError.class));
        builtins.put("ConnectionAbortedError", org.python.types.Type.pythonType(org.python.exceptions.ConnectionAbortedError.class));
        builtins.put("ConnectionError", org.python.types.Type.pythonType(org.python.exceptions.ConnectionError.class));
        builtins.put("ConnectionRefusedError", org.python.types.Type.pythonType(org.python.exceptions.ConnectionRefusedError.class));
        builtins.put("ConnectionResetError", org.python.types.Type.pythonType(org.python.exceptions.ConnectionResetError.class));
        builtins.put("DeprecationWarning", org.python.types.Type.pythonType(org.python.exceptions.DeprecationWarning.class));
        builtins.put("EOFError", org.python.types.Type.pythonType(org.python.exceptions.EOFError.class));
        builtins.put("EnvironmentError", org.python.types.Type.pythonType(org.python.exceptions.EnvironmentError.class));
        builtins.put("Exception", org.python.types.Type.pythonType(org.python.exceptions.Exception.class));
        builtins.put("FileExistsError", org.python.types.Type.pythonType(org.python.exceptions.FileExistsError.class));
        builtins.put("FileNotFoundError", org.python.types.Type.pythonType(org.python.exceptions.FileNotFoundError.class));
        builtins.put("FloatingPointError", org.python.types.Type.pythonType(org.python.exceptions.FloatingPointError.class));
        builtins.put("FutureWarning", org.python.types.Type.pythonType(org.python.exceptions.FutureWarning.class));
        builtins.put("GeneratorExit", org.python.types.Type.pythonType(org.python.exceptions.GeneratorExit.class));
        builtins.put("IOError", org.python.types.Type.pythonType(org.python.exceptions.IOError.class));
        builtins.put("ImportError", org.python.types.Type.pythonType(org.python.exceptions.ImportError.class));
        builtins.put("ImportWarning", org.python.types.Type.pythonType(org.python.exceptions.ImportWarning.class));
        builtins.put("IndentationError", org.python.types.Type.pythonType(org.python.exceptions.IndentationError.class));
        builtins.put("IndexError", org.python.types.Type.pythonType(org.python.exceptions.IndexError.class));
        builtins.put("InterruptedError", org.python.types.Type.pythonType(org.python.exceptions.InterruptedError.class));
        builtins.put("IsADirectoryError", org.python.types.Type.pythonType(org.python.exceptions.IsADirectoryError.class));
        builtins.put("KeyError", org.python.types.Type.pythonType(org.python.exceptions.KeyError.class));
        builtins.put("KeyboardInterrupt", org.python.types.Type.pythonType(org.python.exceptions.KeyboardInterrupt.class));
        builtins.put("LookupError", org.python.types.Type.pythonType(org.python.exceptions.LookupError.class));
        builtins.put("MemoryError", org.python.types.Type.pythonType(org.python.exceptions.MemoryError.class));
        builtins.put("NameError", org.python.types.Type.pythonType(org.python.exceptions.NameError.class));
        builtins.put("NotADirectoryError", org.python.types.Type.pythonType(org.python.exceptions.NotADirectoryError.class));
        builtins.put("NotImplementedError", org.python.types.Type.pythonType(org.python.exceptions.NotImplementedError.class));
        builtins.put("OSError", org.python.types.Type.pythonType(org.python.exceptions.OSError.class));
        builtins.put("OverflowError", org.python.types.Type.pythonType(org.python.exceptions.OverflowError.class));
        builtins.put("PendingDeprecationWarning", org.python.types.Type.pythonType(org.python.exceptions.PendingDeprecationWarning.class));
        builtins.put("PermissionError", org.python.types.Type.pythonType(org.python.exceptions.PermissionError.class));
        builtins.put("ProcessLookupError", org.python.types.Type.pythonType(org.python.exceptions.ProcessLookupError.class));
        builtins.put("ReferenceError", org.python.types.Type.pythonType(org.python.exceptions.ReferenceError.class));
        builtins.put("ResourceWarning", org.python.types.Type.pythonType(org.python.exceptions.ResourceWarning.class));
        builtins.put("RuntimeError", org.python.types.Type.pythonType(org.python.exceptions.RuntimeError.class));
        builtins.put("RuntimeWarning", org.python.types.Type.pythonType(org.python.exceptions.RuntimeWarning.class));
        builtins.put("StopIteration", org.python.types.Type.pythonType(org.python.exceptions.StopIteration.class));
        builtins.put("SyntaxError", org.python.types.Type.pythonType(org.python.exceptions.SyntaxError.class));
        builtins.put("SyntaxWarning", org.python.types.Type.pythonType(org.python.exceptions.SyntaxWarning.class));
        builtins.put("SystemError", org.python.types.Type.pythonType(org.python.exceptions.SystemError.class));
        builtins.put("SystemExit", org.python.types.Type.pythonType(org.python.exceptions.SystemExit.class));
        builtins.put("TabError", org.python.types.Type.pythonType(org.python.exceptions.TabError.class));
        builtins.put("TimeoutError", org.python.types.Type.pythonType(org.python.exceptions.TimeoutError.class));
        builtins.put("TypeError", org.python.types.Type.pythonType(org.python.exceptions.TypeError.class));
        builtins.put("UnboundLocalError", org.python.types.Type.pythonType(org.python.exceptions.UnboundLocalError.class));
        builtins.put("UnicodeDecodeError", org.python.types.Type.pythonType(org.python.exceptions.UnicodeDecodeError.class));
        builtins.put("UnicodeEncodeError", org.python.types.Type.pythonType(org.python.exceptions.UnicodeEncodeError.class));
        builtins.put("UnicodeError", org.python.types.Type.pythonType(org.python.exceptions.UnicodeError.class));
        builtins.put("UnicodeTranslateError", org.python.types.Type.pythonType(org.python.exceptions.UnicodeTranslateError.class));
        builtins.put("UnicodeWarning", org.python.types.Type.pythonType(org.python.exceptions.UnicodeWarning.class));
        builtins.put("UserWarning", org.python.types.Type.pythonType(org.python.exceptions.UserWarning.class));
        builtins.put("ValueError", org.python.types.Type.pythonType(org.python.exceptions.ValueError.class));
        builtins.put("Warning", org.python.types.Type.pythonType(org.python.exceptions.Warning.class));
        builtins.put("ZeroDivisionError", org.python.types.Type.pythonType(org.python.exceptions.ZeroDivisionError.class));

        builtins.put("NotImplemented", org.python.types.NotImplementedType.NOT_IMPLEMENTED);
    }

    public static void debug(java.lang.String msg) {
        python.platform.__init__.impl.debug(msg);
    }

    public static void debug(java.lang.String msg, java.lang.Object obj) {
        if (obj == null) {
            python.platform.__init__.impl.debug(msg, "NULL");
        } else {
            python.platform.__init__.impl.debug(msg, obj);
        }
    }

    public static void initializeModule(java.lang.Class cls, java.util.Map<java.lang.String, org.python.Object> attrs) {
        // Iterate over every method in the class, and if the
        // method is annotated for inclusion in the Python class,
        // add a function wrapper to the type definition.
        for (java.lang.reflect.Method method: cls.getMethods()) {
            org.python.Method annotation = method.getAnnotation(org.python.Method.class);
            if (annotation != null) {
                java.lang.String method_name;
                java.lang.String varargs_name;
                java.lang.String kwargs_name;

                // Check for any explicitly set names
                if (annotation.name().equals("")) {
                    method_name = method.getName();
                } else {
                    method_name = annotation.name();
                }

                if (annotation.varargs().equals("")) {
                    varargs_name = null;
                } else {
                    varargs_name = annotation.varargs();
                }

                if (annotation.kwargs().equals("")) {
                    kwargs_name = null;
                } else {
                    kwargs_name = annotation.kwargs();
                }

                attrs.put(
                    method_name,
                    new org.python.types.Function(
                        method,
                        annotation.args(),
                        annotation.default_args(),
                        varargs_name,
                        annotation.kwonlyargs(),
                        kwargs_name
                    )
                );
            }
        }
    }

    public static java.lang.String typeName(java.lang.Class cls) {
        org.python.types.Type klass = org.python.types.Type.pythonType(cls);
        java.lang.String name = null;

        // First look to the Type for an instance variable holding a
        // cached version of the type name.
        if (klass.PYTHON_TYPE_NAME == null) {
            try {
                // If there's no pre-cached version, warm the cache.

                // Look to the class itself for a static field describing
                // the type name.
                java.lang.reflect.Field field = cls.getField("PYTHON_TYPE_NAME");

                // If a field exists, but it's not static, treat it as if
                // the field didn't exist.
                if ((field.getModifiers() & java.lang.reflect.Modifier.STATIC) != 0) {
                    name = (java.lang.String) field.get(cls);
                } else {
                    throw new java.lang.NoSuchFieldException();
                }
            } catch (java.lang.NoSuchFieldException e) {
                // No PYTHON_TYPE_NAME field found. Fall back to the default
                // behaviour for Python type naming, stripping python-specific
                // namespace prefixes.
                name = cls.getName();
                if (name.startsWith("org.python.types.")) {
                    name = name.substring(17).toLowerCase();
                } else if (name.startsWith("org.python.exceptions.")) {
                    name = name.substring(22);
                } else if (name.startsWith("python.")) {
                    name = name.substring(7);
                }
            } catch (java.lang.IllegalAccessException e) {
                return "**UNKNOWABLE**";
            } catch (java.lang.SecurityException e) {
                return "**UNKNOWABLE**";
            } catch (java.lang.NullPointerException e) {
                return "**UNKNOWN**";
            }

            // Cache the name for next time.
            klass.PYTHON_TYPE_NAME = name;
        } else {
            // Use the cached version.
            name = klass.PYTHON_TYPE_NAME;
        }

        return name;
    }

    @org.python.Method(
        __doc__ = "__import__(name, globals=None, locals=None, fromlist=(), level=0) -> module" +
            "\n" +
            "Import a module. Because this function is meant for use by the Python\n" +
            "interpreter and not for general use it is better to use\n" +
            "importlib.import_module() to programmatically import a module.\n" +
            "\n" +
            "The globals argument is only used to determine the context;\n" +
            "they are not modified.  The locals argument is unused.  The fromlist\n" +
            "should be a list of names to emulate ``from name import ...'', or an\n" +
            "empty list to emulate ``import name''.\n" +
            "When importing a module from a package, note that __import__('A.B', ...)\n" +
            "returns package A when fromlist is empty, but its submodule B when\n" +
            "fromlist is not empty.  Level is used to determine whether to perform\n" +
            "absolute or relative imports. 0 is absolute while a positive number\n" +
            "is the number of parent directories to search relative to the current module.\n"
    )
    public static org.python.Object __import__() {
        throw new org.python.exceptions.NotImplementedError("Builtin function '__import__' not implemented");
    }

    @org.python.Method(
        __doc__ = "abs(number) -> number" +
            "\n" +
            "Return the absolute value of the argument.\n",
        args = {"number"}
    )
    public static org.python.Object abs(org.python.Object number) {
        try {
            return number.__abs__();
        } catch (org.python.exceptions.AttributeError ae) {
            throw new org.python.exceptions.TypeError("bad operand type for abs(): '" + number.typeName() + "'");
        }
    }

    @org.python.Method(
        __doc__ = "all(iterable) -> bool" +
            "\n" +
            "Return True if bool(x) is True for all values x in the iterable.\n" +
            "If the iterable is empty, return True.\n",
        args = {"iterable"}
    )
    public static org.python.types.Bool all(org.python.Object iterable) {
        try {
            org.python.Iterable iter = iterable.__iter__();
            try {
                while (true) {
                    org.python.Object next = iter.__next__();
                    if (!((org.python.types.Bool) next.__bool__()).value) {
                        return new org.python.types.Bool(false);
                    }
                }
            } catch (org.python.exceptions.StopIteration si) {
            }
            return new org.python.types.Bool(true);
        } catch (org.python.exceptions.AttributeError ae) {
            throw new org.python.exceptions.TypeError("'" + iterable.typeName() + "' object is not iterable");
        }
    }

    @org.python.Method(
        __doc__ = "any(iterable) -> bool" +
            "\n" +
            "Return True if bool(x) is True for any x in the iterable.\n" +
            "If the iterable is empty, return False.\n",
        args = {"iterable"}
    )
    public static org.python.types.Bool any(org.python.Object iterable) {
        try {
            org.python.Iterable iter = iterable.__iter__();
            try {
                while (true) {
                    org.python.Object next = iter.__next__();
                    if (((org.python.types.Bool) next.__bool__()).value) {
                        return new org.python.types.Bool(true);
                    }
                }
            } catch (org.python.exceptions.StopIteration si) {
            }
            return new org.python.types.Bool(false);
        } catch (org.python.exceptions.AttributeError ae) {
            throw new org.python.exceptions.TypeError("'" + iterable.typeName() + "' object is not iterable");
        }
    }

    @org.python.Method(
        __doc__ = "ascii(object) -> string" +
            "\n" +
            "As repr(), return a string containing a printable representation of an\n" +
            "object, but escape the non-ASCII characters in the string returned by\n" +
            "repr() using \\x, \\u or \\U escapes.  This generates a string similar\n" +
            "to that returned by repr() in Python 2.\n"
    )
    public static org.python.types.Str ascii() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'ascii' not implemented");
    }

    @org.python.Method(
        __doc__ = "bin(number) -> string" +
            "\n" +
            "Return the binary representation of an integer.\n" +
            "\n" +
            "  >>> bin(2796202)\n" +
            "  '0b1010101010101010101010'\n",
        args = {"number"}
    )
    public static org.python.types.Str bin(org.python.Object number) {
        try {
            if (!(number instanceof org.python.types.Int)) {
                number.__index__();
            }

            String s = Long.toString(int_cast(number, null).value, 2);
            if (s.charAt(0) == '-') {
                s = "-0b" + s.substring(1);
            } else {
                s = "0b" + s;
            }
            return new org.python.types.Str(s);
        } catch (org.python.exceptions.AttributeError ae) {
            throw new org.python.exceptions.TypeError("'" + number.typeName() + "' object cannot be interpreted as an integer");
        }
    }

    @org.python.Method(
        __doc__ = "bool(x) -> bool" +
            "\n" +
            "Returns True when the argument x is true, False otherwise.\n" +
            "The builtins True and False are the only two instances of the class bool.\n" +
            "The class bool is a subclass of the class int, and cannot be subclassed.\n",
        default_args = {"x"}
    )
    public static org.python.types.Bool bool(org.python.Object x) {
        if (x == null) {
            return new org.python.types.Bool(false);
        }
        try {
            return (org.python.types.Bool) x.__bool__();
        } catch (org.python.exceptions.AttributeError ae) {
            try {
                return new org.python.types.Bool(((org.python.types.Int) x.__len__()).value != 0);
            } catch (org.python.exceptions.AttributeError ae2) {
                return new org.python.types.Bool(true);
            }
        }
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
            " - an integer\n"
    )
    public static org.python.types.ByteArray bytearray() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'bytearray' not implemented");
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
            " - an integer\n"
    )
    public static org.python.types.Bytes bytes() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'bytes' not implemented");
    }

    @org.python.Method(
        __doc__ = "callable(object) -> bool" +
            "\n" +
            "Return whether the object is callable (i.e., some kind of function).\n" +
            "Note that classes are callable, as are instances of classes with a\n" +
            "__call__() method.\n",
        args = {"object"}
    )
    public static org.python.types.Bool callable(org.python.Object object) {
        return new org.python.types.Bool(org.python.Callable.class.isAssignableFrom(object.getClass()));
    }

    @org.python.Method(
        __doc__ = "chr(i) -> Unicode character" +
            "\n" +
            "Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.\n",
        args = {"i"}
    )
    public static org.python.types.Str chr(org.python.Object i) {
        if (i instanceof org.python.types.Float) {
            throw new org.python.exceptions.TypeError("integer argument expected, got " + i.typeName() + "");
        }

        try {
            if (!(i instanceof org.python.types.Int)) {
                i.__index__();
            }

            long value = ((org.python.types.Int) i.__int__()).value;
            if (value < 0) {
                throw new org.python.exceptions.ValueError("chr() arg not in range(" + String.format("0x%x", (int) int_cast(i, null).value) + ")");
            }

            return new org.python.types.Str(Character.toChars((int) value)[0]);
        } catch (org.python.exceptions.AttributeError ae) {
            throw new org.python.exceptions.TypeError("an integer is required (got type " + i.typeName() + ")");
        }
    }

    @org.python.Method(
        __doc__ = "classmethod(function) -> method" +
            "\n" +
            "Convert a function to be a class method.\n" +
            "\n" +
            "A class method receives the class as implicit first argument,\n" +
            "just like an instance method receives the instance.\n" +
            "To declare a class method, use this idiom:\n" +
            "\n" +
            " class C:\n" +
            "     def f(cls, arg1, arg2, ...): ...\n" +
            "     f = classmethod(f)\n" +
            "\n" +
            "It can be called either on the class (e.g. C.f()) or on an instance\n" +
            "(e.g. C().f()).  The instance is ignored except for its class.\n" +
            "If a class method is called for a derived class, the derived class\n" +
            "object is passed as the implied first argument.\n" +
            "\n" +
            "Class methods are different than C++ or Java static methods.\n" +
            "If you want those, see the staticmethod builtin.\n"
    )
    public static org.python.Object classmethod() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'classmethod' not implemented");
    }

    @org.python.Method(
        __doc__ = "compile(source, filename, mode[, flags[, dont_inherit]]) -> code object" +
            "\n" +
            "Compile the source (a Python module, statement or expression)\n" +
            "into a code object that can be executed by exec() or eval().\n" +
            "The filename will be used for run-time error messages.\n" +
            "The mode must be 'exec' to compile a module, 'single' to compile a\n" +
            "single (interactive) statement, or 'eval' to compile an expression.\n" +
            "The flags argument, if present, controls which future statements influence\n" +
            "the compilation of the code.\n" +
            "The dont_inherit argument, if non-zero, stops the compilation inheriting\n" +
            "the effects of any future statements in effect in the code calling\n" +
            "compile; if absent or zero these statements do influence the compilation,\n" +
            "in addition to any features explicitly specified.\n"
    )
    public static org.python.Object compile() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'compile' not implemented");
    }

    @org.python.Method(
        __doc__ = "complex(real[, imag]) -> complex number" +
            "\n" +
            "Create a complex number from a real part and an optional imaginary part.\n" +
            "This is equivalent to (real + imag*1j) where imag defaults to 0.\n"
    )
    public static org.python.types.Complex complex() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'complex' not implemented");
    }

    @org.python.Method(
        __doc__ = "interactive prompt objects for printing the license text, a list of" +
            "contributors and the copyright notice.\n"
    )
    public static org.python.types.Str copyright() {
        return new org.python.types.Str(
            "Copyright (c) 2015 Russell Keith-Magee.\n" +
            "All Rights Reserved.\n" +
            "\n" +
            "Copyright (c) 2001-2014 Python Software Foundation.\n" +
            "All Rights Reserved.\n" +
            "\n" +
            "Copyright (c) 2000 BeOpen.com.\n" +
            "All Rights Reserved.\n" +
            "\n" +
            "Copyright (c) 1995-2001 Corporation for National Research Initiatives.\n" +
            "All Rights Reserved.\n" +
            "\n" +
            "Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\n" +
            "All Rights Reserved.\n"
        );
    }

    @org.python.Method(
        __doc__ = "interactive prompt objects for printing the license text, a list of" +
            "contributors and the copyright notice.\n"
    )
    public static org.python.Object credits() {
        return new org.python.types.Str(
            "voc is a BeeWare project. See pybee.org/voc for more information.\n" +
            "\n" +
            "Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands\n" +
            "for supporting Python development.  See www.python.org for more information.\n"
        );
    }

    @org.python.Method(
        __doc__ = "delattr(object, name)" +
            "\n" +
            "Delete a named attribute on an object; delattr(x, 'y') is equivalent to\n" +
            "``del x.y''.\n"
    )
    public static org.python.Object delattr() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'delattr' not implemented");
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
    public static org.python.types.Dict dict(org.python.Object iterable) {
        if (iterable == null) {
            return new org.python.types.Dict();
        } else {
            if (iterable instanceof org.python.types.Dict) {
                return new org.python.types.Dict(
                    new java.util.HashMap<org.python.Object, org.python.Object>(
                        ((org.python.types.Dict) iterable).value
                    )
                );
            } else {
                try {
                    org.python.Iterable iterator = iterable.__iter__();
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
                    return new org.python.types.Dict(generated);
                } catch (org.python.exceptions.AttributeError ae) {
                    throw new org.python.exceptions.TypeError("'" + iterable.typeName() + "' object is not iterable");
                }
            }
        }
    }

    @org.python.Method(
        __doc__ = "dir([object]) -> list of strings" +
            "\n" +
            "If called without an argument, return the names in the current scope.\n" +
            "Else, return an alphabetized list of names comprising (some of) the attributes\n" +
            "of the given object, and of attributes reachable from it.\n" +
            "If the object supplies a method named __dir__, it will be used; otherwise\n" +
            "the default dir() logic is used and returns:\n" +
            "  for a module object: the module's attributes.\n" +
            "  for a class object:  its attributes, and recursively the attributes\n" +
            "    of its bases.\n" +
            "    for any other object: its attributes, its class's attributes, and\n" +
            "    recursively the attributes of its class's base classes.\n",
        default_args = {"object"}
    )
    public static org.python.types.List dir(org.python.Object object) {
        if (object == null) {
            throw new org.python.exceptions.NotImplementedError("builting function 'dir' with no arguments not implemented");
        } else {
            return (org.python.types.List) object.__dir__();
        }
    }

    @org.python.Method(
        __doc__ = "divmod(x, y) -> (div, mod)" +
            "\n" +
            "Return the tuple ((x-x%y)/y, x%y).  Invariant: div*y + mod == x.\n",
        args = {"a", "b"}
    )
    public static org.python.types.Tuple divmod(org.python.Object a, org.python.Object b) {
        try {
            return (org.python.types.Tuple) a.__divmod__(b);
        } catch (org.python.exceptions.AttributeError ae) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for divmod(): '" + a.typeName() + "' and '" + b.typeName() + "'");
        }
    }

    @org.python.Method(
        __doc__ = "enumerate(iterable[, start]) -> iterator for index, value of iterable" +
            "\n" +
            "Return an enumerate object.  iterable must be another object that supports\n" +
            "iteration.  The enumerate object yields pairs containing a count (from\n" +
            "start, which defaults to zero) and a value yielded by the iterable argument.\n" +
            "enumerate is useful for obtaining an indexed list:\n" +
            "       (0, seq[0]), (1, seq[1]), (2, seq[2]), ...\n"
    )
    public static org.python.Iterable enumerate() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'enumerate' not implemented");
    }

    @org.python.Method(
        __doc__ = "eval(source[, globals[, locals]]) -> value" +
            "\n" +
            "Evaluate the source in the context of globals and locals.\n" +
            "The source may be a string representing a Python expression\n" +
            "or a code object as returned by compile().\n" +
            "The globals must be a dictionary and locals can be any mapping,\n" +
            "defaulting to the current globals and locals.\n" +
            "If only globals is given, locals defaults to it.\n"
    )
    public static org.python.Object eval() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'eval' not implemented");
    }

    @org.python.Method(
        __doc__ = "exec(object[, globals[, locals]])" +
            "\n" +
            "Read and execute code from an object, which can be a string or a code\n" +
            "object.\n" +
            "The globals and locals are dictionaries, defaulting to the current\n" +
            "globals and locals.  If only globals is given, locals defaults to it.\n"
    )
    public static org.python.Object exec() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'exec' not implemented");
    }

    @org.python.Method(
        __doc__ = "filter(function or None, iterable) --> filter object" +
            "\n" +
            "Return an iterator yielding those items of iterable for which function(item)\n" +
            "is true. If function is None, return the items that are true.\n"
    )
    public static org.python.Object filter() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'filter' not implemented");
    }

    @org.python.Method(
        name = "float",
        __doc__ = "float(x) -> floating point number" +
            "\n" +
            "Convert a string or number to a floating point number, if possible.\n",
        args = {"x"}
    )
    public static org.python.types.Float float_cast(org.python.Object x) {
        try {
            return (org.python.types.Float) x.__float__();
        } catch (org.python.exceptions.AttributeError ae) {
            throw new org.python.exceptions.TypeError("float() argument must be a string or a number, not '" + x.typeName() + "'");
        }
    }

    @org.python.Method(
        __doc__ = "format(value[, format_spec]) -> string" +
            "\n" +
            "Returns value.__format__(format_spec)\n" +
            "format_spec defaults to ''\n",
        args = {"value"},
        default_args = {"format_spec"}
    )
    public static org.python.types.Str format(org.python.Object value, org.python.Object format_spec) {
        if (format_spec == null) {
            return (org.python.types.Str) value.__str__();
        } else {
            return (org.python.types.Str) value.__format__(format_spec);
        }
    }

    @org.python.Method(
        __doc__ = "frozenset() -> empty frozenset object" +
            "frozenset(iterable) -> frozenset object\n" +
            "\n" +
            "Build an immutable unordered collection of unique elements.\n"
    )
    public static org.python.types.FrozenSet frozenset() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'frozenset' not implemented");
    }

    @org.python.Method(
        __doc__ = "getattr(object, name[, default]) -> value" +
            "\n" +
            "Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.\n" +
            "When a default argument is given, it is returned when the attribute doesn't\n" +
            "exist; without it, an exception is raised in that case.\n"
    )
    public static org.python.Object getattr() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'getattr' not implemented");
    }

    @org.python.Method(
        __doc__ = "globals() -> dictionary" +
            "\n" +
            "Return the dictionary containing the current scope's global variables.\n"
    )
    public static org.python.types.Dict globals() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'globals' not implemented");
    }

    @org.python.Method(
        __doc__ = "hasattr(object, name) -> bool" +
            "\n" +
            "Return whether the object has an attribute with the given name.\n" +
            "(This is done by calling getattr(object, name) and catching AttributeError.)\n"
    )
    public static org.python.types.Bool hasattr() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'hasattr' not implemented");
    }

    @org.python.Method(
        __doc__ = "hash(object) -> integer" +
            "\n" +
            "Return a hash value for the object.  Two objects with the same value have\n" +
            "the same hash value.  The reverse is not necessarily true, but likely.\n",
        args = {"object"}
    )
    public static org.python.types.Int hash(org.python.Object object) {
        return (org.python.types.Int) object.__hash__();
    }

    @org.python.Method(
        __doc__ = "Define the built-in 'help'." +
            "This is a wrapper around pydoc.help (with a twist).\n"
    )
    public static org.python.Object help() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'help' not implemented");
    }

    @org.python.Method(
        __doc__ = "hex(number) -> string" +
            "\n" +
            "Return the hexadecimal representation of an integer.\n" +
            "\n" +
            "  >>> hex(3735928559)\n" +
            "  '0xdeadbeef'\n",
        args = {"number"}
    )
    public static org.python.types.Str hex(org.python.Object number) {
        try {
            if (!(number instanceof org.python.types.Int)) {
                number.__index__();
            }

            String s = Long.toString(int_cast(number, null).value, 16);
            if (s.charAt(0) == '-') {
                s = "-0x" + s.substring(1);
            } else {
                s = "0x" + s;
            }
            return new org.python.types.Str(s);
        } catch (org.python.exceptions.AttributeError ae) {
            throw new org.python.exceptions.TypeError("'" + number.typeName() + "' object cannot be interpreted as an integer");
        }
    }

    @org.python.Method(
        __doc__ = "id(object) -> integer" +
            "\n" +
            "Return the identity of an object.  This is guaranteed to be unique among\n" +
            "simultaneously existing objects.\n",
        args = {"object"}
    )
    public static org.python.types.Int id(org.python.Object object) {
        return new org.python.types.Int(System.identityHashCode(object));
    }

    @org.python.Method(
        __doc__ = "input([prompt]) -> string" +
            "\n" +
            "Read a string from standard input.  The trailing newline is stripped.\n" +
            "If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.\n" +
            "The prompt string, if given,\n" +
            "is printed without a trailing newline before reading.\n",
        default_args = {"prompt"}
    )
    public static org.python.types.Str input(org.python.Object prompt) {
        java.io.BufferedReader reader = new java.io.BufferedReader(new java.io.InputStreamReader(System.in));

        if (prompt != null) {
            System.out.print(prompt);
            System.out.flush();
        }

        try {
            return new org.python.types.Str(reader.readLine());
        } catch (java.io.IOException e) {
            throw new org.python.exceptions.OSError();
        }
    }

    @org.python.Method(
        name = "int",
        __doc__ = "int(x=0) -> integer" +
            "int(x, base=10) -> integer\n" +
            "\n" +
            "Convert a number or string to an integer, or return 0 if no arguments\n" +
            "are given.  If x is a number, return x.__int__().  For floating point\n" +
            "numbers, this truncates towards zero.\n" +
            "\n" +
            "If x is not a number or if base is given, then x must be a string,\n" +
            "bytes, or bytearray instance representing an integer literal in the\n" +
            "given base.  The literal can be preceded by '+' or '-' and be surrounded\n" +
            "by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\n" +
            "Base 0 means to interpret the base from the string as an integer literal.\n" +
            "\n" +
            "  >>> int('0b100', base=0)\n" +
            "  4\n",
        default_args = {"x", "base"}
    )
    public static org.python.types.Int int_cast(org.python.Object x, org.python.Object base) {
        if (x == null) {
            return new org.python.types.Int(0);
        } else if (base == null) {
            try {
                return (org.python.types.Int) x.__int__();
            } catch (org.python.exceptions.AttributeError ae) {
                throw new org.python.exceptions.TypeError("int() argument must be a string, a bytes-like object or a number, not '" + x.typeName() + "'");
            }
        } else {
            throw new org.python.exceptions.NotImplementedError("int() with a base is not implemented");
        }
    }

    @org.python.Method(
        __doc__ = "isinstance(object, class-or-type-or-tuple) -> bool" +
            "\n" +
            "Return whether an object is an instance of a class or of a subclass thereof.\n" +
            "With a type as second argument, return whether that is the object's type.\n" +
            "The form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for\n" +
            "isinstance(x, A) or isinstance(x, B) or ... (etc.).\n"
    )
    public static org.python.types.Bool isinstance() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'isinstance' not implemented");
    }

    @org.python.Method(
        __doc__ = "issubclass(C, B) -> bool" +
            "\n" +
            "Return whether class C is a subclass (i.e., a derived class) of class B.\n" +
            "When using a tuple as the second argument issubclass(X, (A, B, ...)),\n" +
            "is a shortcut for issubclass(X, A) or issubclass(X, B) or ... (etc.).\n"
    )
    public static org.python.types.Bool issubclass() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'issubclass' not implemented");
    }

    @org.python.Method(
        __doc__ = "iter(iterable) -> iterator" +
            "iter(callable, sentinel) -> iterator\n" +
            "\n" +
            "Get an iterator from an object.  In the first form, the argument must\n" +
            "supply its own iterator, or be a sequence.\n" +
            "In the second form, the callable is called until it returns the sentinel.\n",
        args = {"iterable"},
        default_args = {"sentinel"}
    )
    public static org.python.Iterable iter(org.python.Object iterable, org.python.Object sentinel) {
        if (sentinel == null) {
            return iterable.__iter__();
        } else {
            throw new org.python.exceptions.NotImplementedError("Builtin function 'iter' with callable/sentinel not implemented");
        }
    }

    @org.python.Method(
        __doc__ = "len(object)" +
            "\n" +
            "Return the number of items of a sequence or collection.\n",
        args = {"object"}
    )
    public static org.python.types.Int len(org.python.Object object) {
        try {
            return (org.python.types.Int) object.__len__();
        } catch (org.python.exceptions.AttributeError ae) {
            throw new org.python.exceptions.TypeError("object of type '" + object.typeName() + "' has no len()");
        }
    }

    @org.python.Method(
        __doc__ = "interactive prompt objects for printing the license text, a list of" +
            "contributors and the copyright notice.\n"
    )
    public static org.python.Object license() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'license' not implemented");
    }

    @org.python.Method(
        __doc__ = "list() -> new empty list" +
            "list(iterable) -> new list initialized from iterable's items\n",
        default_args = {"iterable"}
    )
    public static org.python.types.List list(org.python.Object iterable) {
        if (iterable == null) {
            return new org.python.types.List();
        } else {
            if (iterable instanceof org.python.types.List) {
                return new org.python.types.List(
                    new java.util.ArrayList<org.python.Object>(
                        ((org.python.types.List) iterable).value
                    )
                );
            } else if (iterable instanceof org.python.types.Set) {
                return new org.python.types.List(
                    new java.util.ArrayList<org.python.Object>(
                        ((org.python.types.Set) iterable).value
                    )
                );
            } else if (iterable instanceof org.python.types.Tuple) {
                return new org.python.types.List(
                    new java.util.ArrayList<org.python.Object>(
                        ((org.python.types.Tuple) iterable).value
                    )
                );
            } else {
                try {
                    org.python.Iterable iterator = iterable.__iter__();
                    java.util.List<org.python.Object> generated = new java.util.ArrayList<org.python.Object>();
                    try {
                        while (true) {
                            org.python.Object next = iterator.__next__();
                            generated.add(next);
                        }
                    } catch (org.python.exceptions.StopIteration si) {
                    }
                    return new org.python.types.List(generated);
                } catch (org.python.exceptions.AttributeError ae) {
                    throw new org.python.exceptions.TypeError("'" + iterable.typeName() + "' object is not iterable");
                }
            }
        }
    }

    @org.python.Method(
        __doc__ = "locals() -> dictionary" +
            "\n" +
            "Update and return a dictionary containing the current scope's local variables.\n"
    )
    public static org.python.types.Dict locals() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'locals' not implemented");
    }

    @org.python.Method(
        __doc__ = "map(func, *iterables) --> map object" +
            "\n" +
            "Make an iterator that computes the function using arguments from\n" +
            "each of the iterables.  Stops when the shortest iterable is exhausted.\n"
    )
    public static org.python.Object map() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'input' not implemented");
    }

    @org.python.Method(
        __doc__ = "max(iterable, *[, default=obj, key=func]) -> value" +
            "max(arg1, arg2, *args, *[, key=func]) -> value\n" +
            "\n" +
            "With a single iterable argument, return its biggest item. The\n" +
            "default keyword-only argument specifies an object to return if\n" +
            "the provided iterable is empty.\n" +
            "With two or more arguments, return the largest argument.\n"
    )
    public static org.python.Object max() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'max' not implemented");
    }

    @org.python.Method(
        __doc__ = "memoryview(object)" +
            "\n" +
            "Create a new memoryview object which references the given object.\n"
    )
    public static org.python.types.MemoryView memoryview() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'memoryview' not implemented");
    }

    @org.python.Method(
        __doc__ = "min(iterable, *[, default=obj, key=func]) -> value" +
            "min(arg1, arg2, *args, *[, key=func]) -> value\n" +
            "\n" +
            "With a single iterable argument, return its smallest item. The\n" +
            "default keyword-only argument specifies an object to return if\n" +
            "the provided iterable is empty.\n" +
            "With two or more arguments, return the smallest argument.\n"
    )
    public static org.python.Object min() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'min' not implemented");
    }

    @org.python.Method(
        __doc__ = "next(iterator[, default])" +
            "\n" +
            "Return the next item from the iterator. If default is given and the iterator\n" +
            "is exhausted, it is returned instead of raising StopIteration.\n",
        args = {"iterator"},
        default_args = {"_default"}
    )
    public static org.python.Object next(org.python.Object iterator, org.python.Object _default) {
        if (iterator instanceof org.python.Iterable) {
            try {
                return ((org.python.Iterable) iterator).__next__();
            } catch (org.python.exceptions.StopIteration si) {
                if (_default != null) {
                    return _default;
                } else {
                    throw si;
                }
            }
        } else {
            throw new org.python.exceptions.TypeError("'" + iterator.typeName() + "' object is not an iterator");
        }
    }

    @org.python.Method(
        __doc__ = "The most base type"
    )
    public static org.python.types.Object object() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'object' not implemented");
    }

    @org.python.Method(
        __doc__ = "oct(number) -> string" +
            "\n" +
            "Return the octal representation of an integer.\n" +
            "\n" +
            "   >>> oct(342391)\n" +
            "  '0o1234567'\n",
        args = {"number"}
    )
    public static org.python.types.Str oct(org.python.Object number) {
        try {
            if (!(number instanceof org.python.types.Int)) {
                number.__index__();
            }

            String s = Long.toString(int_cast(number, null).value, 8);
            if (s.charAt(0) == '-') {
                s = "-0o" + s.substring(1);
            } else {
                s = "0o" + s;
            }
            return new org.python.types.Str(s);
        } catch (org.python.exceptions.AttributeError ae) {
            throw new org.python.exceptions.TypeError("'" + number.typeName() + "' object cannot be interpreted as an integer");
        }
    }

    @org.python.Method(
        __doc__ = "open(file, mode='r', buffering=-1, encoding=None," +
            "     errors=None, newline=None, closefd=True, opener=None) -> file object\n" +
            "\n" +
            "Open file and return a stream.  Raise IOError upon failure.\n" +
            "\n" +
            "file is either a text or byte string giving the name (and the path\n" +
            "if the file isn't in the current working directory) of the file to\n" +
            "be opened or an integer file descriptor of the file to be\n" +
            "wrapped. (If a file descriptor is given, it is closed when the\n" +
            "returned I/O object is closed, unless closefd is set to False.)\n" +
            "\n" +
            "mode is an optional string that specifies the mode in which the file\n" +
            "is opened. It defaults to 'r' which means open for reading in text\n" +
            "mode.  Other common values are 'w' for writing (truncating the file if\n" +
            "it already exists), 'x' for creating and writing to a new file, and\n" +
            "'a' for appending (which on some Unix systems, means that all writes\n" +
            "append to the end of the file regardless of the current seek position).\n" +
            "In text mode, if encoding is not specified the encoding used is platform\n" +
            "dependent: locale.getpreferredencoding(False) is called to get the\n" +
            "current locale encoding. (For reading and writing raw bytes use binary\n" +
            "mode and leave encoding unspecified.) The available modes are:\n" +
            "\n" +
            "========= ===============================================================\n" +
            "Character Meaning\n" +
            "--------- ---------------------------------------------------------------\n" +
            "'r'       open for reading (default)\n" +
            "'w'       open for writing, truncating the file first\n" +
            "'x'       create a new file and open it for writing\n" +
            "'a'       open for writing, appending to the end of the file if it exists\n" +
            "'b'       binary mode\n" +
            "'t'       text mode (default)\n" +
            "'+'       open a disk file for updating (reading and writing)\n" +
            "'U'       universal newline mode (deprecated)\n" +
            "========= ===============================================================\n" +
            "\n" +
            "The default mode is 'rt' (open for reading text). For binary random\n" +
            "access, the mode 'w+b' opens and truncates the file to 0 bytes, while\n" +
            "'r+b' opens the file without truncation. The 'x' mode implies 'w' and\n" +
            "raises an `FileExistsError` if the file already exists.\n" +
            "\n" +
            "Python distinguishes between files opened in binary and text modes,\n" +
            "even when the underlying operating system doesn't. Files opened in\n" +
            "binary mode (appending 'b' to the mode argument) return contents as\n" +
            "bytes objects without any decoding. In text mode (the default, or when\n" +
            "'t' is appended to the mode argument), the contents of the file are\n" +
            "returned as strings, the bytes having been first decoded using a\n" +
            "platform-dependent encoding or using the specified encoding if given.\n" +
            "\n" +
            "'U' mode is deprecated and will raise an exception in future versions\n" +
            "of Python.  It has no effect in Python 3.  Use newline to control\n" +
            "universal newlines mode.\n" +
            "\n" +
            "buffering is an optional integer used to set the buffering policy.\n" +
            "Pass 0 to switch buffering off (only allowed in binary mode), 1 to select\n" +
            "line buffering (only usable in text mode), and an integer > 1 to indicate\n" +
            "the size of a fixed-size chunk buffer.  When no buffering argument is\n" +
            "given, the default buffering policy works as follows:\n" +
            "\n" +
            "* Binary files are buffered in fixed-size chunks; the size of the buffer\n" +
            "  is chosen using a heuristic trying to determine the underlying device's\n" +
            "  'block size' and falling back on `io.DEFAULT_BUFFER_SIZE`.\n" +
            "  On many systems, the buffer will typically be 4096 or 8192 bytes long.\n" +
            "\n" +
            "* 'Interactive' text files (files for which isatty() returns True)\n" +
            "  use line buffering.  Other text files use the policy described above\n" +
            "  for binary files.\n" +
            "\n" +
            "encoding is the name of the encoding used to decode or encode the\n" +
            "file. This should only be used in text mode. The default encoding is\n" +
            "platform dependent, but any encoding supported by Python can be\n" +
            "passed.  See the codecs module for the list of supported encodings.\n" +
            "\n" +
            "errors is an optional string that specifies how encoding errors are to\n" +
            "be handled---this argument should not be used in binary mode. Pass\n" +
            "'strict' to raise a ValueError exception if there is an encoding error\n" +
            "(the default of None has the same effect), or pass 'ignore' to ignore\n" +
            "errors. (Note that ignoring encoding errors can lead to data loss.)\n" +
            "See the documentation for codecs.register or run 'help(codecs.Codec)'\n" +
            "for a list of the permitted encoding error strings.\n" +
            "\n" +
            "newline controls how universal newlines works (it only applies to text\n" +
            "mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as\n" +
            "follows:\n" +
            "\n" +
            "* On input, if newline is None, universal newlines mode is\n" +
            "  enabled. Lines in the input can end in '\n', '\r', or '\r\n', and\n" +
            "  these are translated into '\n' before being returned to the\n" +
            "  caller. If it is '', universal newline mode is enabled, but line\n" +
            "  endings are returned to the caller untranslated. If it has any of\n" +
            "  the other legal values, input lines are only terminated by the given\n" +
            "  string, and the line ending is returned to the caller untranslated.\n" +
            "\n" +
            "* On output, if newline is None, any '\n' characters written are\n" +
            "  translated to the system default line separator, os.linesep. If\n" +
            "  newline is '' or '\n', no translation takes place. If newline is any\n" +
            "  of the other legal values, any '\n' characters written are translated\n" +
            "  to the given string.\n" +
            "\n" +
            "If closefd is False, the underlying file descriptor will be kept open\n" +
            "when the file is closed. This does not work when a file name is given\n" +
            "and must be True in that case.\n" +
            "\n" +
            "A custom opener can be used by passing a callable as *opener*. The\n" +
            "underlying file descriptor for the file object is then obtained by\n" +
            "calling *opener* with (*file*, *flags*). *opener* must return an open\n" +
            "file descriptor (passing os.open as *opener* results in functionality\n" +
            "similar to passing None).\n" +
            "\n" +
            "open() returns a file object whose type depends on the mode, and\n" +
            "through which the standard file operations such as reading and writing\n" +
            "are performed. When open() is used to open a file in a text mode ('w',\n" +
            "'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open\n" +
            "a file in a binary mode, the returned class varies: in read binary\n" +
            "mode, it returns a BufferedReader; in write binary and append binary\n" +
            "modes, it returns a BufferedWriter, and in read/write mode, it returns\n" +
            "a BufferedRandom.\n" +
            "\n" +
            "It is also possible to use a string or bytearray as a file for both\n" +
            "reading and writing. For strings StringIO can be used like a file\n" +
            "opened in a text mode, and for bytes a BytesIO can be used like a file\n" +
            "opened in a binary mode.\n",
        args = {"file"},
        default_args = {"mode", "buffering", "encoding", "errors", "newline", "closefd", "opener"}
    )
    public static org.python.Object open(
                org.python.Object file,
                org.python.Object mode,
                org.python.Object buffering,
                org.python.Object encoding,
                org.python.Object errors,
                org.python.Object newline,
                org.python.Object closefd,
                org.python.Object opener) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'open' not implemented");
    }

    @org.python.Method(
        __doc__ = "ord(c) -> integer" +
            "\n" +
            "Return the integer ordinal of a one-character string.\n",
        args = {"c"}
    )
    public static org.python.types.Int ord(org.python.Object c) {
        try {
            int length = ((org.python.types.Str) c).value.length();
            if (length == 1) {
                return new org.python.types.Int((int) (org.Python.str(c).value).charAt(0));
            } else {
                throw new org.python.exceptions.TypeError("ord() expected string of length 1, but string of length " + length + " found");
            }
        } catch (ClassCastException e) {
            throw new org.python.exceptions.TypeError("ord() expected string of length 1, but " + c.typeName() + " found");
        }
    }

    @org.python.Method(
        __doc__ = "pow(x, y[, z]) -> number" +
            "\n" +
            "With two arguments, equivalent to x**y.  With three arguments,\n" +
            "equivalent to (x**y) % z, but may be more efficient (e.g. for ints).\n",
        args = {"x", "y"},
        default_args = {"z"}
    )
    public static org.python.Object pow(org.python.Object x, org.python.Object y, org.python.Object z) {
        if (z != null && !((x instanceof org.python.types.Int) && (y instanceof org.python.types.Int))) {
            throw new org.python.exceptions.TypeError("pow() 3rd argument not allowed unless all arguments are integers");
        }
        if (z != null && ((org.python.types.Int) y).value < 0) {
            throw new org.python.exceptions.TypeError("pow() 2nd argument cannot be negative when 3rd argument specified");
        }
        return x.__pow__(y, z);
    }

    @org.python.Method(
        __doc__ = "print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)" +
            "\n" +
            "Prints the values to a stream, or to sys.stdout by default.\n" +
            "Optional keyword arguments:\n" +
            "file:  a file-like object (stream); defaults to the current sys.stdout.\n" +
            "sep:   string inserted between values, default a space.\n" +
            "end:   string appended after the last value, default a newline.\n" +
            "flush: whether to forcibly flush the stream.\n",
        varargs="value",
        kwonlyargs={"file", "sep", "end", "flush"}
    )
    public static void print(org.python.Object [] value, org.python.Object file, org.python.Object sep, org.python.Object end, org.python.Object flush) {
        if (file == null) {
            // file = System.out;
        }

        StringBuilder buffer = new StringBuilder();

        for (int i = 0; i < value.length; i++) {
            buffer.append(value[i]);

            if (i != value.length - 1) {
                if (sep == null) {
                    buffer.append(" ");
                } else {
                    buffer.append(sep);
                }
            }
        }
        if (end == null) {
            buffer.append("\n");
        } else {
            buffer.append(end);
        }
        System.out.print(buffer.toString());
        // file.write(buffer.toString());
    }

    @org.python.Method(
        __doc__ = "property(fget=None, fset=None, fdel=None, doc=None) -> property attribute" +
            "\n" +
            "fget is a function to be used for getting an attribute value, and likewise\n" +
            "fset is a function for setting, and fdel a function for del'ing, an\n" +
            "attribute.  Typical use is to define a managed attribute x:\n" +
            "\n" +
            "class C(object):\n" +
            "    def getx(self): return self._x\n" +
            "    def setx(self, value): self._x = value\n" +
            "    def delx(self): del self._x\n" +
            "    x = property(getx, setx, delx, \"I'm the 'x' property.\")\n" +
            "\n" +
            "Decorators make defining new properties or modifying existing ones easy:\n" +
            "\n" +
            "class C(object):\n" +
            "    @property\n" +
            "    def x(self):\n" +
            "        \"I am the 'x' property.\"\n" +
            "        return self._x\n" +
            "    @x.setter\n" +
            "    def x(self, value):\n" +
            "        self._x = value\n" +
            "    @x.deleter\n" +
            "    def x(self):\n" +
            "        del self._x\n"
    )
    public static org.python.Object property() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'property' not implemented");
    }

    @org.python.Method(
        __doc__ = "range(stop) -> range object" +
            "range(start, stop[, step]) -> range object\n" +
            "\n" +
            "Return a virtual sequence of numbers from start to stop by step.\n",
        args = {"start_or_stop"},
        default_args = {"stop", "step"}
    )
    public static org.python.types.Range range(org.python.Object start_or_stop, org.python.Object stop, org.python.Object step) {
        if (stop == null && step == null) {
            return new org.python.types.Range(start_or_stop);
        } else if (step == null) {
            return new org.python.types.Range(start_or_stop, stop);
        } else {
            return new org.python.types.Range(start_or_stop, stop, step);
        }
    }

    @org.python.Method(
        __doc__ = "repr(object) -> string" +
            "\n" +
            "Return the canonical string representation of the object.\n" +
            "For most object types, eval(repr(object)) == object.\n",
        args = {"object"}
    )
    public static org.python.types.Str repr(org.python.Object object) {
        return (org.python.types.Str) object.__repr__();
    }

    @org.python.Method(
        __doc__ = "reversed(sequence) -> reverse iterator over values of the sequence" +
            "\n" +
            "Return a reverse iterator\n"
    )
    public static org.python.Iterable reversed(
                java.util.List<org.python.Object> args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("reversed() takes no keyword arguments");
        }
        if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("reversed() takes exactly one argument (" + args.size() + " given)");
        }
        return args.get(0).__reversed__();
    }

    @org.python.Method(
        __doc__ = "round(number[, ndigits]) -> number" +
            "\n" +
            "Round a number to a given precision in decimal digits (default 0 digits).\n" +
            "This returns an int when called with one argument, otherwise the\n" +
            "same type as the number. ndigits may be negative.\n",
        args = {"number"},
        default_args = {"ndigits"}
    )
    public static org.python.Object round(org.python.Object number, org.python.Object ndigits) {
        if (ndigits == null) {
            return number.__round__(new org.python.types.Int(0));
        }
        return number.__round__(ndigits);
    }

    @org.python.Method(
        __doc__ = "set() -> new empty set object" +
            "set(iterable) -> new set object\n" +
            "\n" +
            "Build an unordered collection of unique elements.\n",
        default_args = {"iterable"}
    )
    public static org.python.types.Set set(org.python.Object iterable) {
        if (iterable == null) {
            return new org.python.types.Set();
        } else {
            if (iterable instanceof org.python.types.Set) {
                return new org.python.types.Set(
                    new java.util.HashSet<org.python.Object>(
                        ((org.python.types.Set) iterable).value
                    )
                );
            } else if (iterable instanceof org.python.types.List) {
                return new org.python.types.Set(
                    new java.util.HashSet<org.python.Object>(
                        ((org.python.types.List) iterable).value
                    )
                );
            } else if (iterable instanceof org.python.types.Tuple) {
                return new org.python.types.Set(
                    new java.util.HashSet<org.python.Object>(
                        ((org.python.types.Tuple) iterable).value
                    )
                );
            } else {
                try {
                    org.python.Iterable iterator = iterable.__iter__();
                    java.util.Set<org.python.Object> generated = new java.util.HashSet<org.python.Object>();
                    try {
                        while (true) {
                            org.python.Object next = iterator.__next__();
                            generated.add(next);
                        }
                    } catch (org.python.exceptions.StopIteration si) {
                    }
                    return new org.python.types.Set(generated);
                } catch (org.python.exceptions.AttributeError ae) {
                    throw new org.python.exceptions.TypeError("'" + iterable.typeName() + "' object is not iterable");
                }
            }
        }
    }



    @org.python.Method(
        __doc__ = "setattr(object, name, value)" +
            "\n" +
            "Set a named attribute on an object; setattr(x, 'y', v) is equivalent to\n" +
            "``x.y = v''.\n"
    )
    public static org.python.Object setattr() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'setattr' not implemented");
    }

    @org.python.Method(
        __doc__ = "slice(stop)" +
            "slice(start, stop[, step])\n" +
            "\n" +
            "Create a slice object.  This is used for extended slicing (e.g. a[0:10:2]).\n"
    )
    public static org.python.Object slice() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'input' not implemented");
    }

    @org.python.Method(
        __doc__ = "sorted(iterable, key=None, reverse=False) --> new sorted list"
    )
    public static org.python.types.List sorted() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'sorted' not implemented");
    }

    @org.python.Method(
        __doc__ = "staticmethod(function) -> method" +
            "\n" +
            "Convert a function to be a static method.\n" +
            "\n" +
            "A static method does not receive an implicit first argument.\n" +
            "To declare a static method, use this idiom:\n" +
            "\n" +
            "     class C:\n" +
            "     def f(arg1, arg2, ...): ...\n" +
            "     f = staticmethod(f)\n" +
            "\n" +
            "It can be called either on the class (e.g. C.f()) or on an instance\n" +
            "(e.g. C().f()).  The instance is ignored except for its class.\n" +
            "\n" +
            "Static methods in Python are similar to those found in Java or C++.\n" +
            "For a more advanced concept, see the classmethod builtin.\n"
    )
    public static org.python.Object staticmethod() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'staticmethod' not implemented");
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
    public static org.python.types.Str str(org.python.Object object) {
        if (object == null) {
            return new org.python.types.Str("");
        }
        return (org.python.types.Str) object.__str__();
    }

    @org.python.Method(
        __doc__ = "sum(iterable[, start]) -> value" +
            "\n" +
            "Return the sum of an iterable of numbers (NOT strings) plus the value\n" +
            "of parameter 'start' (which defaults to 0).  When the iterable is\n" +
            "empty, return start.\n"
    )
    public static org.python.Object sum() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'sum' not implemented");
    }

    @org.python.Method(
        name = "super",
        __doc__ = "super() -> same as super(__class__, <first argument>)" +
            "super(type) -> unbound super object\n" +
            "super(type, obj) -> bound super object; requires isinstance(obj, type)\n" +
            "super(type, type2) -> bound super object; requires issubclass(type2, type)\n" +
            "Typical use to call a cooperative superclass method:\n" +
            "class C(B):\n" +
            "def meth(self, arg):\n" +
            "   super().meth(arg)\n" +
            "This works for class methods too:\n" +
            "class C(B):\n" +
            "@classmethod\n" +
            "def cmeth(cls, arg):\n" +
            "   super().cmeth(arg)\n"
    )
    public static org.python.Object super_call() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'super' not implemented");
    }

    @org.python.Method(
        __doc__ = "tuple() -> empty tuple" +
            "tuple(iterable) -> tuple initialized from iterable's items\n" +
            "\n" +
            "If the argument is a tuple, the return value is the same object.\n"
    )
    public static org.python.types.Tuple tuple() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'tuple' not implemented");
    }

    @org.python.Method(
        __doc__ = "type(object_or_name, bases, dict)" +
            "type(object) -> the object's type\n" +
            "type(name, bases, dict) -> a new type\n",
        args = {"object_or_name"},
        default_args = {"bases", "dict"}
    )
    public static org.python.types.Type type(org.python.Object object_or_name, org.python.Object bases, org.python.Object dict) {
        if (bases == null && dict != null) {
            throw new org.python.exceptions.TypeError("type() takes 1 or 3 arguments");
        }

        if (bases == null && dict == null) {
            return org.python.types.Type.pythonType(object_or_name.getClass());
        } else {
            throw new org.python.exceptions.NotImplementedError("3-argument form of builtin function 'type' not implemented");
        }
    }

    @org.python.Method(
        __doc__ = "vars([object]) -> dictionary" +
            "\n" +
            "Without arguments, equivalent to locals().\n" +
            "With an argument, equivalent to object.__dict__.\n"
    )
    public static org.python.types.Dict vars() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'vars' not implemented");
    }

    @org.python.Method(
        __doc__ = "zip(iter1 [,iter2 [...]]) --> zip object" +
            "\n" +
            "Return a zip object whose .__next__() method returns a tuple where\n" +
            "the i-th element comes from the i-th iterable argument.  The .__next__()\n" +
            "method continues until the shortest iterable in the argument sequence\n" +
            "is exhausted and then it raises StopIteration.\n"
    )
    public static org.python.Object zip() {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'zip' not implemented");
    }
}
