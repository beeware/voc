package org;

public class Python {
    public static java.util.Map<java.lang.String, org.python.Object> builtins;
    /**
     * The version of Python that this library implements
     */
    public static int VERSION = 0x3040000;

    static {
        // Load all the builtins into the dictionary as callables
        builtins = new java.util.HashMap<java.lang.String, org.python.Object>();

        // Add the most basic type
        builtins.put("object", org.python.types.Type.pythonType(org.python.types.Object.class));

        // Add the constants
        builtins.put("Ellipsis", org.python.types.Ellipsis.ELLIPSIS);
        builtins.put("None", org.python.types.NoneType.NONE);
        builtins.put("NotImplemented", org.python.types.NotImplementedType.NOT_IMPLEMENTED);
        builtins.put("True", org.python.types.Bool.TRUE);
        builtins.put("False", org.python.types.Bool.FALSE);

        // Primitives, which are both functions and types.
        builtins.put("bool", org.python.types.Type.pythonType(org.python.types.Bool.class));
        builtins.put("bytearray", org.python.types.Type.pythonType(org.python.types.ByteArray.class));
        builtins.put("bytes", org.python.types.Type.pythonType(org.python.types.Bytes.class));
        builtins.put("complex", org.python.types.Type.pythonType(org.python.types.Complex.class));
        builtins.put("dict", org.python.types.Type.pythonType(org.python.types.Dict.class));
        builtins.put("int", org.python.types.Type.pythonType(org.python.types.Int.class));
        builtins.put("float", org.python.types.Type.pythonType(org.python.types.Float.class));
        builtins.put("frozenset", org.python.types.Type.pythonType(org.python.types.FrozenSet.class));
        builtins.put("list", org.python.types.Type.pythonType(org.python.types.List.class));
        builtins.put("memoryview", org.python.types.Type.pythonType(org.python.types.MemoryView.class));
        builtins.put("set", org.python.types.Type.pythonType(org.python.types.Set.class));
        builtins.put("str", org.python.types.Type.pythonType(org.python.types.Str.class));
        builtins.put("tuple", org.python.types.Type.pythonType(org.python.types.Tuple.class));

        // Add all the builtin exceptions
        builtins.put("BaseException", org.python.types.Type.pythonType(org.python.exceptions.BaseException.class));

        builtins.put("SystemExit", org.python.types.Type.pythonType(org.python.exceptions.SystemExit.class));
        builtins.put("KeyboardInterrupt", org.python.types.Type.pythonType(org.python.exceptions.KeyboardInterrupt.class));
        builtins.put("GeneratorExit", org.python.types.Type.pythonType(org.python.exceptions.GeneratorExit.class));
        builtins.put("Exception", org.python.types.Type.pythonType(org.python.exceptions.Exception.class));

        // subclasses of Exception
        builtins.put("StopIteration", org.python.types.Type.pythonType(org.python.exceptions.StopIteration.class));
        // New in Python 3.5: builtins.put("StopAsyncIteration", org.python.types.Type.pythonType(org.python.exceptions.StopAsyncIteration.class));
        builtins.put("ArithmeticError", org.python.types.Type.pythonType(org.python.exceptions.ArithmeticError.class));
        builtins.put("AssertionError", org.python.types.Type.pythonType(org.python.exceptions.AssertionError.class));
        builtins.put("AttributeError", org.python.types.Type.pythonType(org.python.exceptions.AttributeError.class));
        builtins.put("BufferError", org.python.types.Type.pythonType(org.python.exceptions.BufferError.class));
        builtins.put("EOFError", org.python.types.Type.pythonType(org.python.exceptions.EOFError.class));
        builtins.put("ImportError", org.python.types.Type.pythonType(org.python.exceptions.ImportError.class));
        builtins.put("LookupError", org.python.types.Type.pythonType(org.python.exceptions.LookupError.class));
        builtins.put("MemoryError", org.python.types.Type.pythonType(org.python.exceptions.MemoryError.class));
        builtins.put("NameError", org.python.types.Type.pythonType(org.python.exceptions.NameError.class));
        builtins.put("OSError", org.python.types.Type.pythonType(org.python.exceptions.OSError.class));
        builtins.put("ReferenceError", org.python.types.Type.pythonType(org.python.exceptions.ReferenceError.class));
        builtins.put("RuntimeError", org.python.types.Type.pythonType(org.python.exceptions.RuntimeError.class));
        builtins.put("SyntaxError", org.python.types.Type.pythonType(org.python.exceptions.SyntaxError.class));
        builtins.put("SystemError", org.python.types.Type.pythonType(org.python.exceptions.SystemError.class));
        builtins.put("TypeError", org.python.types.Type.pythonType(org.python.exceptions.TypeError.class));
        builtins.put("ValueError", org.python.types.Type.pythonType(org.python.exceptions.ValueError.class));
        builtins.put("Warning", org.python.types.Type.pythonType(org.python.exceptions.Warning.class));

        // subclasses of ArithmeticError
        builtins.put("FloatingPointError", org.python.types.Type.pythonType(org.python.exceptions.FloatingPointError.class));
        builtins.put("OverflowError", org.python.types.Type.pythonType(org.python.exceptions.OverflowError.class));
        builtins.put("ZeroDivisionError", org.python.types.Type.pythonType(org.python.exceptions.ZeroDivisionError.class));

        // subclasses of ImportError
        // New in 3.6: builtins.put("ModuleNotFoundError", org.python.types.Type.pythonType(org.python.exceptions.ModuleNotFoundError.class));

        // subclasses of LookupError
        builtins.put("IndexError", org.python.types.Type.pythonType(org.python.exceptions.IndexError.class));
        builtins.put("KeyError", org.python.types.Type.pythonType(org.python.exceptions.KeyError.class));

        // subclasses of NameError
        builtins.put("UnboundLocalError", org.python.types.Type.pythonType(org.python.exceptions.UnboundLocalError.class));

        // subclasses of OSError
        builtins.put("BlockingIOError", org.python.types.Type.pythonType(org.python.exceptions.BlockingIOError.class));
        builtins.put("ChildProcessError", org.python.types.Type.pythonType(org.python.exceptions.ChildProcessError.class));
        builtins.put("ConnectionError", org.python.types.Type.pythonType(org.python.exceptions.ConnectionError.class));
        builtins.put("FileExistsError", org.python.types.Type.pythonType(org.python.exceptions.FileExistsError.class));
        builtins.put("FileNotFoundError", org.python.types.Type.pythonType(org.python.exceptions.FileNotFoundError.class));
        builtins.put("InterruptedError", org.python.types.Type.pythonType(org.python.exceptions.InterruptedError.class));
        builtins.put("IsADirectoryError", org.python.types.Type.pythonType(org.python.exceptions.IsADirectoryError.class));
        builtins.put("NotADirectoryError", org.python.types.Type.pythonType(org.python.exceptions.NotADirectoryError.class));
        builtins.put("PermissionError", org.python.types.Type.pythonType(org.python.exceptions.PermissionError.class));
        builtins.put("ProcessLookupError", org.python.types.Type.pythonType(org.python.exceptions.ProcessLookupError.class));
        builtins.put("TimeoutError", org.python.types.Type.pythonType(org.python.exceptions.TimeoutError.class));

        builtins.put("IOError", org.python.types.Type.pythonType(org.python.exceptions.OSError.class));
        builtins.put("EnvironmentError", org.python.types.Type.pythonType(org.python.exceptions.OSError.class));

        // subclasses of ConnectionError
        builtins.put("BrokenPipeError", org.python.types.Type.pythonType(org.python.exceptions.BrokenPipeError.class));
        builtins.put("ConnectionAbortedError", org.python.types.Type.pythonType(org.python.exceptions.ConnectionAbortedError.class));
        builtins.put("ConnectionRefusedError", org.python.types.Type.pythonType(org.python.exceptions.ConnectionRefusedError.class));
        builtins.put("ConnectionResetError", org.python.types.Type.pythonType(org.python.exceptions.ConnectionResetError.class));

        // subclasses of RuntimeError
        builtins.put("NotImplementedError", org.python.types.Type.pythonType(org.python.exceptions.NotImplementedError.class));
        // new in Python 3.5: builtins.put("RecursionError", org.python.types.Type.pythonType(org.python.exceptions.RecursionError.class));

        // subclasses of SyntaxError
        builtins.put("IndentationError", org.python.types.Type.pythonType(org.python.exceptions.IndentationError.class));

        // subclasses of IndentationError
        builtins.put("TabError", org.python.types.Type.pythonType(org.python.exceptions.TabError.class));

        // subclasses of ValueError
        builtins.put("UnicodeError", org.python.types.Type.pythonType(org.python.exceptions.UnicodeError.class));

        // subclasses of UnicodeError
        builtins.put("UnicodeDecodeError", org.python.types.Type.pythonType(org.python.exceptions.UnicodeDecodeError.class));
        builtins.put("UnicodeEncodeError", org.python.types.Type.pythonType(org.python.exceptions.UnicodeEncodeError.class));
        builtins.put("UnicodeTranslateError", org.python.types.Type.pythonType(org.python.exceptions.UnicodeTranslateError.class));

        // subclasses of Warning
        builtins.put("DeprecationWarning", org.python.types.Type.pythonType(org.python.exceptions.DeprecationWarning.class));
        builtins.put("PendingDeprecationWarning", org.python.types.Type.pythonType(org.python.exceptions.PendingDeprecationWarning.class));
        builtins.put("RuntimeWarning", org.python.types.Type.pythonType(org.python.exceptions.RuntimeWarning.class));
        builtins.put("SyntaxWarning", org.python.types.Type.pythonType(org.python.exceptions.SyntaxWarning.class));
        builtins.put("UserWarning", org.python.types.Type.pythonType(org.python.exceptions.UserWarning.class));
        builtins.put("FutureWarning", org.python.types.Type.pythonType(org.python.exceptions.FutureWarning.class));
        builtins.put("ImportWarning", org.python.types.Type.pythonType(org.python.exceptions.ImportWarning.class));
        builtins.put("UnicodeWarning", org.python.types.Type.pythonType(org.python.exceptions.UnicodeWarning.class));
        builtins.put("BytesWarning", org.python.types.Type.pythonType(org.python.exceptions.BytesWarning.class));
        builtins.put("ResourceWarning", org.python.types.Type.pythonType(org.python.exceptions.ResourceWarning.class));

        org.Python.initializeModule(org.Python.class, builtins);
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
        // Get the class annotation and add any properties.
        org.python.Module mod_annotation = (org.python.Module) cls.getAnnotation(org.python.Module.class);
        if (mod_annotation != null) {
            java.lang.String __doc__ = mod_annotation.__doc__();
            if (__doc__.equals("[undocumented]")) {
                attrs.put("__doc__", org.python.types.NoneType.NONE);
            } else {
                attrs.put("__doc__", new org.python.types.Str(__doc__));
            }
        }

        // Iterate over every method in the class, and if the
        // method is annotated for inclusion in the Python class,
        // add a function wrapper to the type definition.
        for (java.lang.reflect.Method method : cls.getMethods()) {
            org.python.Method cls_annotation = method.getAnnotation(org.python.Method.class);
            if (cls_annotation != null) {
                java.lang.String method_name;
                java.lang.String varargs_name;
                java.lang.String kwargs_name;

                // Check for any explicitly set names
                if (cls_annotation.name().equals("")) {
                    method_name = method.getName();
                } else {
                    method_name = cls_annotation.name();
                }

                if (cls_annotation.varargs().equals("")) {
                    varargs_name = null;
                } else {
                    varargs_name = cls_annotation.varargs();
                }

                if (cls_annotation.kwargs().equals("")) {
                    kwargs_name = null;
                } else {
                    kwargs_name = cls_annotation.kwargs();
                }

                attrs.put(
                        method_name,
                        new org.python.types.Function(
                                method,
                                cls_annotation.args(),
                                cls_annotation.default_args(),
                                varargs_name,
                                cls_annotation.kwonlyargs(),
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
                    name = cls.getSimpleName();
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

    /**
     * Add the contents of a list to the varargs to be used in a function call.
     */
    public static org.python.Object[] addToArgs(org.python.Object[] args, org.python.Object varargs) {
        java.util.List<org.python.Object> temp_list = new java.util.ArrayList<org.python.Object>();
        try {
            org.python.Iterable iter = varargs.__iter__();
            while (true) {
                org.python.Object item = iter.__next__();
                temp_list.add(item);
            }
        } catch (org.python.exceptions.StopIteration e) {
        }

        java.lang.Object[] va_list = temp_list.toArray();
        org.python.Object[] arg_list = new org.python.Object[args.length + va_list.length];

        System.arraycopy(args, 0, arg_list, 0, args.length);
        System.arraycopy(va_list, 0, arg_list, args.length, va_list.length);

        return arg_list;
    }

    /**
     * Add the contents of a dictionary to the keyword arguments to be used
     * in a function call.
     *
     * Returns the updated kwargs Map.
     *
     * If any of the keys in the varkwargs dictionary aren't strings,
     * a TypeError is raised.
     */
    public static java.util.Map<java.lang.String, org.python.Object> addToKwargs(java.util.Map<java.lang.String, org.python.Object> kwargs, org.python.Object kwvarargs, java.lang.String func_name) {
        // FIXME: Once we have dictionary iterators, we should use an iteration-based
        // rollout, rather than casting to Dict.
        // try {
        //     org.python.Iterable iter = varkwargs.__iter__();
        //     while (true) {
        //         org.python.Object key = iter.__next__()
        //         java.lang.String key_string = ((org.python.types.Str) key).value;
        //         org.python.Object key
        //         kwargs.put(key_string, value);
        //     }
        // } catch (ClassCastException e) {
        //     throw new org.python.exceptions.TypeError(func_name + "() keywords must be strings");
        // } catch (org.python.exceptions.StopIteration e) {}

        for (java.util.Map.Entry<org.python.Object, org.python.Object> entry : ((org.python.types.Dict) kwvarargs).value.entrySet()) {
            try {
                kwargs.put(((org.python.types.Str) entry.getKey()).value, entry.getValue());
            } catch (ClassCastException e) {
                throw new org.python.exceptions.TypeError(func_name + "() keywords must be strings");
            }
        }
        return kwargs;
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
        org.python.Iterable iter = org.Python.iter(iterable);
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
    }

    @org.python.Method(
            __doc__ = "any(iterable) -> bool" +
                    "\n" +
                    "Return True if bool(x) is True for any x in the iterable.\n" +
                    "If the iterable is empty, return False.\n",
            args = {"iterable"}
    )
    public static org.python.types.Bool any(org.python.Object iterable) {
        org.python.Iterable iter = org.Python.iter(iterable);
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

            java.lang.String s = java.lang.Long.toString(((org.python.types.Int) number.__int__()).value, 2);
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
                throw new org.python.exceptions.ValueError("chr() arg not in range(" + String.format("0x%x", (int) ((org.python.types.Int) i.__int__()).value) + ")");
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
                    "``del x.y''.\n",
            args = {"object", "name"}
    )
    public static org.python.Object delattr(org.python.Object object, org.python.Object name) {
        object.__delattr__(name);
        return org.python.types.NoneType.NONE;
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
                    "(0, seq[0]), (1, seq[1]), (2, seq[2]), ...\n",
            default_args = {"items", "start"}
    )
    public static org.python.Iterable enumerate(org.python.Object items, org.python.Object start) {
        if (items == null) {
            throw new org.python.exceptions.TypeError("Required argument 'iterable' (pos 1) not found");
        }
        org.python.Object index = new org.python.types.Int(0);
        if (start != null) {
            try {
                index = (org.python.types.Int) start; // will throw error if start can't be converted to Int
            } catch (ClassCastException te) {
                throw new org.python.exceptions.TypeError("'" + start.typeName() + "' object cannot be interpreted as an integer");
            }
        }
        org.python.Object increment = new org.python.types.Int(1);
        java.util.List enumList = new java.util.ArrayList();
        try {
            org.python.Iterable iter = org.Python.iter(items);
            while (true) {
                try {
                    java.util.List tuple = new java.util.ArrayList();
                    tuple.add(index);
                    tuple.add(iter.__next__());
                    org.python.types.Tuple pythonTuple = new org.python.types.Tuple(tuple);
                    enumList.add(pythonTuple);
                    index = index.__add__(increment);
                } catch (org.python.exceptions.StopIteration e) {
                    break;
                }
            }
            return org.Python.iter(new org.python.types.List(enumList));
        } catch (org.python.exceptions.AttributeError e) {
            throw new org.python.exceptions.TypeError("'" + items.typeName() + "' object is not iterable");
        }
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
            name = "filter",
            __doc__ = "filter(function or None, iterable) --> filter object" +
                    "\n" +
                    "Return an iterator yielding those items of iterable for which function(item)\n" +
                    "is true. If function is None, return the items that are true.\n",
            args = {"function", "iterable"}
    )
    public static org.python.Object filter(org.python.Object function, org.python.Object iterable) {
        org.python.Iterable iterator = org.Python.iter(iterable);
        throw new org.python.exceptions.NotImplementedError("Builtin function 'filter' not implemented");
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
            __doc__ = "getattr(object, name[, default]) -> value" +
                    "\n" +
                    "Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.\n" +
                    "When a default argument is given, it is returned when the attribute doesn't\n" +
                    "exist; without it, an exception is raised in that case.\n",
            args = {"object", "name"},
            default_args = {"default_"}
    )
    public static org.python.Object getattr(org.python.Object object, org.python.Object name, org.python.Object default_) {
        org.python.Object result;
        try {
            result = object.__getattribute__(name);
        } catch (org.python.exceptions.AttributeError ae) {
            if (default_ == null) {
                throw ae;
            }
            result = default_;
        } catch (org.python.exceptions.TypeError te) {
            throw new org.python.exceptions.TypeError(te.getMessage().replace("__getattribute__", "getattr"));
        }
        return result;
    }

    // @org.python.Method(
    //     __doc__ = "globals() -> dictionary" +
    //         "\n" +
    //         "Return the dictionary containing the current scope's global variables.\n"
    // )
    // public static org.python.types.Dict globals() {
    //     Implemented directly at the AST level
    // }

    @org.python.Method(
            __doc__ = "hasattr(object, name) -> bool" +
                    "\n" +
                    "Return whether the object has an attribute with the given name.\n" +
                    "(This is done by calling getattr(object, name) and catching AttributeError.)\n",
            args = {"object", "name"}
    )
    public static org.python.types.Bool hasattr(org.python.Object object, org.python.Object name) {
        if (!(name instanceof org.python.types.Str)) {
            throw new org.python.exceptions.TypeError("hasattr(): attribute name must be string");
        }
        try {
            object.__getattribute__(name);
            return new org.python.types.Bool(true);
        } catch (org.python.exceptions.AttributeError ae) {
            return new org.python.types.Bool(false);
        } catch (org.python.exceptions.TypeError te) {
            throw new org.python.exceptions.TypeError(te.getMessage().replace("__hasattribute__", "hasattr"));
        }
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

            String s = Long.toString(((org.python.types.Int) number.__int__()).value, 16);
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
            __doc__ = "isinstance(object, class-or-type-or-tuple) -> bool" +
                    "\n" +
                    "Return whether an object is an instance of a class or of a subclass thereof.\n" +
                    "With a type as second argument, return whether that is the object's type.\n" +
                    "The form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for\n" +
                    "isinstance(x, A) or isinstance(x, B) or ... (etc.).\n",
            default_args = {"object", "class_or_type_or_tuple"}
    )
    public static org.python.types.Bool isinstance(org.python.Object object, org.python.Object class_or_type_or_tuple) {
        if (object == null) {
            throw new org.python.exceptions.TypeError("isinstance expected 2 arguments, got 0");
        } else if (class_or_type_or_tuple == null) {
            throw new org.python.exceptions.TypeError("isinstance expected 2 arguments, got 1");
        } else if (class_or_type_or_tuple instanceof org.python.types.Tuple) {
            return org.Python.issubclass(org.Python.type(object, null, null), class_or_type_or_tuple);
        } else if (class_or_type_or_tuple instanceof org.python.types.Type) {
            return org.Python.issubclass(org.Python.type(object, null, null), class_or_type_or_tuple);
        } else {
            throw new org.python.exceptions.TypeError("isinstance() arg 2 must be a type or tuple of types");
        }
    }

    @org.python.Method(
            __doc__ = "issubclass(C, B) -> bool" +
                "\n" +
                "Return whether class C is a subclass (i.e., a derived class) of class B.\n" +
                "When using a tuple as the second argument issubclass(X, (A, B, ...)),\n" +
                "is a shortcut for issubclass(X, A) or issubclass(X, B) or ... (etc.).\n",
            default_args = {"class", "classinfo_or_tuple"}
    )
    public static org.python.types.Bool issubclass(org.python.Object klass, org.python.Object classinfo_or_tuple) {
        if (klass == null) {
            throw new org.python.exceptions.TypeError("issubclass expected 2 arguments, got 0");
        } else if (classinfo_or_tuple == null) {
            throw new org.python.exceptions.TypeError("issubclass expected 2 arguments, got 1");
        } else if (!(klass instanceof org.python.types.Type)) {
            throw new org.python.exceptions.TypeError("issubclass() arg 1 must be a class");
        } else if (classinfo_or_tuple instanceof org.python.types.Tuple) {
            java.util.List<org.python.Object> target_classes = ((org.python.types.Tuple) classinfo_or_tuple).value;
            for (org.python.Object target_klass: target_classes) {
                if (((org.python.types.Bool) org.Python.issubclass(klass, target_klass).__bool__()).value) {
                    return new org.python.types.Bool(true);
                }
            }
            return new org.python.types.Bool(false);
        } else if (classinfo_or_tuple instanceof org.python.types.Type) {
            org.python.types.Type klass_obj = (org.python.types.Type) klass;
            if (klass == classinfo_or_tuple) {
                return new org.python.types.Bool(true);
            } else if (klass_obj.__dict__.get("__bases__") != null) {
                for (org.python.Object base: ((org.python.types.Tuple) klass_obj.__dict__.get("__bases__")).value) {
                    if (base == classinfo_or_tuple || org.Python.issubclass(base, classinfo_or_tuple).value) {
                        return new org.python.types.Bool(true);
                    }
                }
            }
            return new org.python.types.Bool(false);
        } else {
            throw new org.python.exceptions.TypeError("issubclass() arg 2 must be a class or tuple of classes");
        }
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
            try {
                return iterable.__iter__();
            } catch (org.python.exceptions.AttributeError e) {
                // No __iter__ == not iterable
                throw new org.python.exceptions.TypeError("'" + iterable.typeName() + "' object is not iterable");
            }
        } else {
            throw new org.python.exceptions.NotImplementedError("Builtin function 'iter' with callable/sentinel not implemented");
        }
    }

    public static org.python.Iterable iter(org.python.Object iterable) {
        return org.Python.iter(iterable, null);
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

    // @org.python.Method(
    //     __doc__ = "locals() -> dictionary" +
    //         "\n" +
    //         "Update and return a dictionary containing the current scope's local variables.\n"
    // )
    // public static org.python.types.Dict locals() {
    //     Implemented directly at the AST level
    // }

    @org.python.Method(
            __doc__ = "map(func, *iterables) --> map object" +
                    "\n" +
                    "Make an iterator that computes the function using arguments from\n" +
                    "each of the iterables.  Stops when the shortest iterable is exhausted.\n",
            args = {"func"},
            varargs = "iterable"
    )
    public static org.python.Object map(org.python.Object func, org.python.types.Tuple iterables) {
        return new org.python.types.Map(func, iterables);
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

            String s = Long.toString(((org.python.types.Int) number.__int__()).value, 8);
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
                return new org.python.types.Int((int) (((org.python.types.Str) c.__str__()).value).charAt(0));
            } else {
                throw new org.python.exceptions.TypeError("ord() expected a character, but string of length " + length + " found");
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
            if (org.Python.VERSION < 0x03050000) {
                throw new org.python.exceptions.TypeError("pow() 2nd argument cannot be negative when 3rd argument specified");
            } else {
                throw new org.python.exceptions.ValueError("pow() 2nd argument cannot be negative when 3rd argument specified");
            }
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
            varargs = "value",
            kwonlyargs = {"file", "sep", "end", "flush"}
    )
    public static void print(org.python.types.Tuple value, org.python.Object file, org.python.Object sep, org.python.Object end, org.python.Object flush) {
        java.util.List<org.python.Object> valueArgs = value.value;
        StringBuilder buffer = new StringBuilder();

        for (int i = 0; i < valueArgs.size(); i++) {
            buffer.append(valueArgs.get(i).__str__());

            if (i != valueArgs.size() - 1) {
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

        if (file == null) {
            file = python.sys.__init__.stdout;
        }

        org.python.Object content = new org.python.types.Str(buffer.toString());
        org.python.Object write_method = file.__getattribute__("write");
        try {
            ((org.python.Callable) write_method).invoke(new org.python.Object[]{content}, null);
        } catch (java.lang.ClassCastException e) {
            throw new org.python.exceptions.TypeError("'" + write_method.typeName() + "' object is not callable");
        }

        if (flush != null && ((org.python.types.Bool) flush.__bool__()).value) {
            org.python.Object flush_method = file.__getattribute__("flush");
            try {
                ((org.python.Callable) flush_method).invoke(null, null);
            } catch (java.lang.ClassCastException e) {
                throw new org.python.exceptions.TypeError("'" + flush_method.typeName() + "' object is not callable");
            }
        }
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
                    "        del self._x\n",
            args = {"fget"},
            default_args = {"fset", "fdel", "doc"}
    )
    public static org.python.Object property(org.python.Object fget, org.python.Object fset, org.python.Object fdel, org.python.Object doc) {
        return new org.python.types.Property(fget, fset, fdel, doc);
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
            __doc__ = "setattr(object, name, value)" +
                    "\n" +
                    "Set a named attribute on an object; setattr(x, 'y', v) is equivalent to\n" +
                    "``x.y = v''.\n",
            args = {"object", "name", "value"}
    )
    public static org.python.Object setattr(org.python.Object object, org.python.Object name, org.python.Object value) {
        try {
            object.__setattr__(name, value);
            return org.python.types.NoneType.NONE;
        } catch (org.python.exceptions.TypeError te) {
            throw new org.python.exceptions.TypeError(te.getMessage().replace("__setattr__", "setattr"));
        }
    }

    @org.python.Method(
            __doc__ = "slice(stop)" +
                    "slice(start, stop[, step])\n" +
                    "\n" +
                    "Create a slice object.  This is used for extended slicing (e.g. a[0:10:2]).\n",
            args = {"start_or_stop"},
            default_args = {"stop", "step"}
    )
    public static org.python.Object slice(org.python.Object start_or_stop, org.python.Object stop, org.python.Object step) {
        if (stop == null && step == null) {
            return new org.python.types.Slice(start_or_stop);
        } else if (step == null) {
            return new org.python.types.Slice(start_or_stop, stop);
        } else {
            return new org.python.types.Slice(start_or_stop, stop, step);
        }
    }

    public static class __SortedObjectComparator implements java.util.Comparator<org.python.Object> {
        private boolean reverse;
        private org.python.Object key;

        public __SortedObjectComparator(boolean reverse, org.python.Object key) {
            this.reverse = reverse;
            this.key = key;
        }

        public __SortedObjectComparator(boolean reverse) {
            this.reverse = reverse;
        }

        public int compare(org.python.Object o1, org.python.Object o2) {
            if (key != null) {
                try {
                    // Replace the two objects by their keys for comparison
                    o1 = ((org.python.Callable) key).invoke(new org.python.Object[]{o1}, null);
                    o2 = ((org.python.Callable) key).invoke(new org.python.Object[]{o2}, null);
                } catch (java.lang.ClassCastException e) {
                    throw new org.python.exceptions.TypeError("'" + key.typeName() + "' object is not callable");
                }
            }
            org.python.Object result = org.python.types.Object.__cmp_bool__(o1, o2, org.python.types.Object.CMP_OP.LT);
            if (((org.python.types.Bool) result.__bool__()).value) {
                return reverse ? 1 : -1;
            }
            result = org.python.types.Object.__cmp_bool__(o2, o1, org.python.types.Object.CMP_OP.LT);
            if (((org.python.types.Bool) result.__bool__()).value) {
                return reverse ? -1 : 1;
            }
            return 0;
        }
    }

    @org.python.Method(
            __doc__ = "sorted(iterable, key=None, reverse=False) --> new sorted list",
            args = {"iterable"},
            default_args = {"key", "reverse"}
    )
    public static org.python.types.List sorted(org.python.Object iterable, org.python.Object key, org.python.types.Bool reverse) {
        if (iterable == null) {
            return new org.python.types.List();
        } else {
            if (reverse == null) {
                reverse = new org.python.types.Bool(false);
            }
            org.python.Iterable iterator = org.Python.iter(iterable);
            java.util.List<org.python.Object> generated = new java.util.ArrayList<org.python.Object>();
            try {
                while (true) {
                    org.python.Object next = iterator.__next__();
                    generated.add(next);
                }
            } catch (org.python.exceptions.StopIteration si) {
            }
            if (key == null || key instanceof org.python.types.NoneType) {
                java.util.Collections.sort(generated, new __SortedObjectComparator(reverse.value));
            } else {
                java.util.Collections.sort(generated, new __SortedObjectComparator(reverse.value, key));
            }
            return new org.python.types.List(generated);
        }
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
            __doc__ = "sum(iterable[, start]) -> value" +
                    "\n" +
                    "Return the sum of an iterable of numbers (NOT strings) plus the value\n" +
                    "of parameter 'start' (which defaults to 0).  When the iterable is\n" +
                    "empty, return start.\n",
            args = {"iterable"},
            default_args = {"start"}
    )
    public static org.python.Object sum(org.python.Object iterable, org.python.Object start) {
        org.python.Object value;
        if (start != null) {
            value = start;
        } else {
            value = new org.python.types.Int(0);
        }

        org.python.Iterable iterator = org.Python.iter(iterable);
        while (true) {
            org.python.Object next;
            try {
                next = iterator.__next__();
            } catch (org.python.exceptions.StopIteration si) {
                break;
            }
            value = value.__add__(next);
        }

        return value;
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
            return org.python.types.Type.declarePythonType(object_or_name, bases, dict);
        }
    }

    // @org.python.Method(
    //     __doc__ = "vars([object]) -> dictionary" +
    //         "\n" +
    //         "Without arguments, equivalent to locals().\n" +
    //         "With an argument, equivalent to object.__dict__.\n"
    // )
    // public static org.python.types.Dict vars() {
    //     Implemented directly at the AST level
    // }

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
