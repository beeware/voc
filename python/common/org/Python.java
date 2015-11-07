package org;


public class Python {
    public static java.util.Map<java.lang.String, org.python.Object> builtins;

    static {
        // Load all the builtins into the dictionary as callables
        builtins = new java.util.HashMap<java.lang.String, org.python.Object>();

        // Iterate over all methods, adding the static ones to builtins
        for (java.lang.reflect.Method method: Python.class.getMethods()) {
            if (java.lang.reflect.Modifier.isStatic(method.getModifiers())) {
                if (method.getName() == "int_cast") {
                    builtins.put("int", new org.python.types.Function(method));
                } else if (method.getName() == "float_cast") {
                    builtins.put("float", new org.python.types.Function(method));
                } else if (!method.getName().startsWith("python")) {
                    builtins.put(method.getName(), new org.python.types.Function(method));
                }
            }
        }
    }

    public static java.lang.String pythonTypeName(java.lang.Class cls) {
        try {
            java.lang.String class_name = cls.getName();
            if (class_name.startsWith("org.python.types.")) {
                return class_name.substring(17).toLowerCase();
            } else if (class_name.startsWith("python.")) {
                return class_name.substring(7);
            }
            return class_name;
        } catch (java.lang.NullPointerException e) {
            return "**unknown**";
        }
    }

    public static java.lang.String pythonTypeName(org.python.Object obj) {
        return pythonTypeName(obj.getClass());
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
    public static org.python.Object __import__(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function '__import__' not implemented");
    }

    @org.python.Method(
        __doc__ = "abs(number) -> number" +
            "\n" +
            "Return the absolute value of the argument.\n"
    )
    public static org.python.Object abs(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("abs() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("abs() takes no keyword arguments");
        }
        return args[0].__abs__();
    }

    @org.python.Method(
        __doc__ = "all(iterable) -> bool" +
            "\n" +
            "Return True if bool(x) is True for all values x in the iterable.\n" +
            "If the iterable is empty, return True.\n"
    )
    public static org.python.types.Bool all(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'all' not implemented");
    }

    @org.python.Method(
        __doc__ = "any(iterable) -> bool" +
            "\n" +
            "Return True if bool(x) is True for any x in the iterable.\n" +
            "If the iterable is empty, return False.\n"
    )
    public static org.python.types.Bool any(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'any' not implemented");
    }

    @org.python.Method(
        __doc__ = "ascii(object) -> string" +
            "\n" +
            "As repr(), return a string containing a printable representation of an\n" +
            "object, but escape the non-ASCII characters in the string returned by\n" +
            "repr() using \\x, \\u or \\U escapes.  This generates a string similar\n" +
            "to that returned by repr() in Python 2.\n"
    )
    public static org.python.types.Str ascii(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'ascii' not implemented");
    }

    @org.python.Method(
        __doc__ = "bin(number) -> string" +
            "\n" +
            "Return the binary representation of an integer.\n" +
            "\n" +
            "  >>> bin(2796202)\n" +
            "  '0b1010101010101010101010'\n"
    )
    public static org.python.types.Str bin(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("bin() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("bin() takes no keyword arguments");
        }
        return new org.python.types.Str(java.lang.String.format("0b%b", int_cast(args, kwargs).value));
    }

    @org.python.Method(
        __doc__ = "bool(x) -> bool" +
            "\n" +
            "Returns True when the argument x is true, False otherwise.\n" +
            "The builtins True and False are the only two instances of the class bool.\n" +
            "The class bool is a subclass of the class int, and cannot be subclassed.\n"
    )
    public static org.python.types.Bool bool(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("bool() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("bool() takes no keyword arguments");
        }
        return args[0].__bool__();
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
    public static org.python.types.ByteArray bytearray(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
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
    public static org.python.types.Bytes bytes(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'bytes' not implemented");
    }

    @org.python.Method(
        __doc__ = "callable(object) -> bool" +
            "\n" +
            "Return whether the object is callable (i.e., some kind of function).\n" +
            "Note that classes are callable, as are instances of classes with a\n" +
            "__call__() method.\n"
    )
    public static org.python.types.Bool callable(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("callable() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("callable() takes no keyword arguments");
        }
        return new org.python.types.Bool(org.python.Callable.class.isAssignableFrom(args[0].getClass()));
    }

    @org.python.Method(
        __doc__ = "chr(i) -> Unicode character" +
            "\n" +
            "Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.\n"
    )
    public static org.python.types.Str chr(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'callable' not implemented");
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
    public static org.python.Object classmethod(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
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
    public static org.python.Object compile(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'compile' not implemented");
    }

    @org.python.Method(
        __doc__ = "complex(real[, imag]) -> complex number" +
            "\n" +
            "Create a complex number from a real part and an optional imaginary part.\n" +
            "This is equivalent to (real + imag*1j) where imag defaults to 0.\n"
    )
    public static org.python.types.Complex complex(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'complex' not implemented");
    }

    @org.python.Method(
        __doc__ = "interactive prompt objects for printing the license text, a list of" +
            "contributors and the copyright notice.\n"
    )
    public static org.python.types.Str copyright(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
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
    public static org.python.Object credits(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
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
    public static org.python.Object delattr(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
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
            "    in the keyword argument list.  For example:  dict(one=1, two=2)\n"
    )
    public static org.python.types.Dict dict(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'dict' not implemented");
    }

    // public static org.python.Object dict(**
    //        org.python.Object [] args,
    //        java.util.Map<java.lang.String, org.python.Object> kwargs) {
    //     throw new org.python.exceptions.NotImplementedError("Builtin function 'dict' not implemented");
    // }

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
            "    recursively the attributes of its class's base classes.\n"
    )
    public static org.python.types.List dir(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("dir() takes no keyword arguments");
        }
        if (args.length == 0) {
            throw new org.python.exceptions.NotImplementedError("builting function 'dir' with no arguments not implemented");
        } else if (args.length == 1) {
            return args[0].__dir__();
        } else {
            throw new org.python.exceptions.TypeError("dir() takes exactly one argument (" + args.length + " given)");
        }
    }

    @org.python.Method(
        __doc__ = "divmod(x, y) -> (div, mod)" +
            "\n" +
            "Return the tuple ((x-x%y)/y, x%y).  Invariant: div*y + mod == x.\n"
    )
    public static org.python.types.Tuple divmod(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'divmod' not implemented");
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
    public static org.python.Iterable enumerate(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
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
    public static org.python.Object eval(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
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
    public static org.python.Object exec(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'exec' not implemented");
    }

    @org.python.Method(
        __doc__ = "filter(function or None, iterable) --> filter object" +
            "\n" +
            "Return an iterator yielding those items of iterable for which function(item)\n" +
            "is true. If function is None, return the items that are true.\n"
    )
    public static org.python.Object filter(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'filter' not implemented");
    }

    @org.python.Method(
        __doc__ = "float(x) -> floating point number" +
            "\n" +
            "Convert a string or number to a floating point number, if possible.\n"
    )
    public static org.python.types.Float float_cast(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("float() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("float() takes no keyword arguments");
        }
        return args[0].__float__();
    }

    @org.python.Method(
        __doc__ = "format(value[, format_spec]) -> string" +
            "\n" +
            "Returns value.__format__(format_spec)\n" +
            "format_spec defaults to ''\n"
    )
    public static org.python.types.Str format(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("format() takes no keyword arguments");
        }
        if (args.length < 1) {
            throw new org.python.exceptions.TypeError("format() takes at least 1 argument (" + args.length + " given)");
        } else if (args.length == 1) {
            return args[0].__str__();
        } else if (args.length == 2) {
            return args[0].__format__(args[1]);
        } else {
            throw new org.python.exceptions.TypeError("format() takes at most 2 arguments (" + args.length + " given)");
        }
    }

    @org.python.Method(
        __doc__ = "frozenset() -> empty frozenset object" +
            "frozenset(iterable) -> frozenset object\n" +
            "\n" +
            "Build an immutable unordered collection of unique elements.\n"
    )
    public static org.python.types.FrozenSet frozenset(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'frozenset' not implemented");
        // if (kwargs.size() != 0) {
        //     throw new org.python.exceptions.TypeError("frozenset() does not take keyword arguments");
        // }
        // if (args.length == 0) {
        //     return new org.python.types.Set();
        // } else if (args.length == 1) {
        //     // return new org.python.types.Set(args[0]);
        //     throw new org.python.exceptions.NotImplementedError("Builtin function 'frozenset' with iterator not implemented");
        // } else {
        //     throw new org.python.exceptions.TypeError("frozenset() expected at most 1 arguments ( got " + args.length + ")");
        // }
    }

    @org.python.Method(
        __doc__ = "getattr(object, name[, default]) -> value" +
            "\n" +
            "Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.\n" +
            "When a default argument is given, it is returned when the attribute doesn't\n" +
            "exist; without it, an exception is raised in that case.\n"
    )
    public static org.python.Object getattr(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'getattr' not implemented");
    }

    @org.python.Method(
        __doc__ = "globals() -> dictionary" +
            "\n" +
            "Return the dictionary containing the current scope's global variables.\n"
    )
    public static org.python.types.Dict globals(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'globals' not implemented");
    }

    @org.python.Method(
        __doc__ = "hasattr(object, name) -> bool" +
            "\n" +
            "Return whether the object has an attribute with the given name.\n" +
            "(This is done by calling getattr(object, name) and catching AttributeError.)\n"
    )
    public static org.python.types.Bool hasattr(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'hasattr' not implemented");
    }

    @org.python.Method(
        __doc__ = "hash(object) -> integer" +
            "\n" +
            "Return a hash value for the object.  Two objects with the same value have\n" +
            "the same hash value.  The reverse is not necessarily true, but likely.\n"
    )
    public static org.python.types.Int hash(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("hash() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("hash() takes no keyword arguments");
        }
        return args[0].__hash__();
    }

    @org.python.Method(
        __doc__ = "Define the built-in 'help'." +
            "This is a wrapper around pydoc.help (with a twist).\n"
    )
    public static org.python.Object help(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'help' not implemented");
    }

    @org.python.Method(
        __doc__ = "hex(number) -> string" +
            "\n" +
            "Return the hexadecimal representation of an integer.\n" +
            "\n" +
            "  >>> hex(3735928559)\n" +
            "  '0xdeadbeef'\n"
    )
    public static org.python.types.Str hex(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("hex() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("hex() takes no keyword arguments");
        }
        return new org.python.types.Str(String.format("0x%x", int_cast(args, kwargs)));
    }

    @org.python.Method(
        __doc__ = "id(object) -> integer" +
            "\n" +
            "Return the identity of an object.  This is guaranteed to be unique among\n" +
            "simultaneously existing objects.\n"
    )
    public static org.python.types.Int id(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("id() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("id() takes no keyword arguments");
        }
        return new org.python.types.Int(System.identityHashCode(args[0]));
    }

    @org.python.Method(
        __doc__ = "input([prompt]) -> string" +
            "\n" +
            "Read a string from standard input.  The trailing newline is stripped.\n" +
            "If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.\n" +
            "The prompt string, if given,\n" +
            "is printed without a trailing newline before reading.\n"
    )
    public static org.python.types.Str input(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length > 1) {
            throw new org.python.exceptions.TypeError("input() expected at most one arguments ( got " + args.length + ")");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("bin() takes no keyword arguments");
        }

        java.io.BufferedReader reader = new java.io.BufferedReader(new java.io.InputStreamReader(System.in));

        if (args.length == 1) {
            System.out.print(args[0]);
            System.out.flush();
        }

        try {
            return new org.python.types.Str(reader.readLine());
        } catch (java.io.IOException e) {
            throw new org.python.exceptions.OSError();
        }
    }

    @org.python.Method(
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
            "  4\n"
    )
    public static org.python.types.Int int_cast(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() == 0) {
            if (args.length == 1) {
                return args[0].__int__();
            } else if (args.length == 2) {
                throw new org.python.exceptions.NotImplementedError("int() with a base is not implemented");
            } else {
                throw new org.python.exceptions.TypeError("int() takes at most 2 arguments, got got " + args.length);
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
    public static org.python.types.Bool isinstance(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'isinstance' not implemented");
    }

    @org.python.Method(
        __doc__ = "issubclass(C, B) -> bool" +
            "\n" +
            "Return whether class C is a subclass (i.e., a derived class) of class B.\n" +
            "When using a tuple as the second argument issubclass(X, (A, B, ...)),\n" +
            "is a shortcut for issubclass(X, A) or issubclass(X, B) or ... (etc.).\n"
    )
    public static org.python.types.Bool issubclass(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'issubclass' not implemented");
    }

    @org.python.Method(
        __doc__ = "iter(iterable) -> iterator" +
            "iter(callable, sentinel) -> iterator\n" +
            "\n" +
            "Get an iterator from an object.  In the first form, the argument must\n" +
            "supply its own iterator, or be a sequence.\n" +
            "In the second form, the callable is called until it returns the sentinel.\n"
    )
    public static org.python.Iterable iter(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("iter() takes no keyword arguments");
        }
        if (args.length < 1) {
            throw new org.python.exceptions.TypeError("iter() expects at least argument, got " + args.length);
        } else if (args.length == 1) {
            return args[0].__iter__();
        } else if (args.length == 2) {
            throw new org.python.exceptions.NotImplementedError("Builtin function 'iter' with callable/sentinel not implemented");
        } else {
            throw new org.python.exceptions.TypeError("iter() takes exactly one argument (" + args.length + " given)");
        }
    }

    @org.python.Method(
        __doc__ = "len(object)" +
            "\n" +
            "Return the number of items of a sequence or collection.\n"
    )
    public static org.python.types.Int len(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("len() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("len() takes no keyword arguments");
        }
        return args[0].__len__();
    }

    @org.python.Method(
        __doc__ = "interactive prompt objects for printing the license text, a list of" +
            "contributors and the copyright notice.\n"
    )
    public static org.python.Object license(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'license' not implemented");
    }

    @org.python.Method(
        __doc__ = "list() -> new empty list" +
            "list(iterable) -> new list initialized from iterable's items\n"
    )
    public static org.python.types.List list(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'list' not implemented");
    }

    @org.python.Method(
        __doc__ = "locals() -> dictionary" +
            "\n" +
            "Update and return a dictionary containing the current scope's local variables.\n"
    )
    public static org.python.types.Dict locals(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'locals' not implemented");
    }

    @org.python.Method(
        __doc__ = "map(func, *iterables) --> map object" +
            "\n" +
            "Make an iterator that computes the function using arguments from\n" +
            "each of the iterables.  Stops when the shortest iterable is exhausted.\n"
    )
    public static org.python.Object map(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
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
    public static org.python.Object max(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'max' not implemented");
    }

    @org.python.Method(
        __doc__ = "memoryview(object)" +
            "\n" +
            "Create a new memoryview object which references the given object.\n"
    )
    public static org.python.types.MemoryView memoryview(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
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
    public static org.python.Object min(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'min' not implemented");
    }

    @org.python.Method(
        __doc__ = "next(iterator[, default])" +
            "\n" +
            "Return the next item from the iterator. If default is given and the iterator\n" +
            "is exhausted, it is returned instead of raising StopIteration.\n"
    )
    public static org.python.Object next(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'next' not implemented");
    }

    @org.python.Method(
        __doc__ = "The most base type"
    )
    public static org.python.types.Object object(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'object' not implemented");
    }

    @org.python.Method(
        __doc__ = "oct(number) -> string" +
            "\n" +
            "Return the octal representation of an integer.\n" +
            "\n" +
            "   >>> oct(342391)\n" +
            "  '0o1234567'\n"
    )
    public static org.python.types.Str oct(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("oct() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("oct() takes no keyword arguments");
        }
        return new org.python.types.Str(String.format("0o%o", int_cast(args, kwargs).value));
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
            "opened in a binary mode.\n"
    )
    public static org.python.Object open(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'open' not implemented");
    }

    @org.python.Method(
        __doc__ = "ord(c) -> integer" +
            "\n" +
            "Return the integer ordinal of a one-character string.\n"
    )
    public static org.python.types.Int ord(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("org() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("ord() takes no keyword arguments");
        }

        try {
            int length = ((org.python.types.Str) args[0]).value.length();
            if (length != 1) {
                return new org.python.types.Int((int) (str(args, kwargs).value).charAt(0));
            } else {
                throw new org.python.exceptions.TypeError("ord() expected string of length 1, but string of length " + length + " found");
            }
        } catch (ClassCastException e) {
            throw new org.python.exceptions.TypeError("ord() expected string of length 1, but " + args[0].getClass().getName() + " found");
        }
    }

    @org.python.Method(
        __doc__ = "pow(x, y[, z]) -> number" +
            "\n" +
            "With two arguments, equivalent to x**y.  With three arguments,\n" +
            "equivalent to (x**y) % z, but may be more efficient (e.g. for ints).\n"
    )
    public static org.python.Object pow(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length < 2) {
            throw new org.python.exceptions.TypeError("pow() expected at least 2 arguments, got " + args.length);
        }
        if (args.length > 3) {
            throw new org.python.exceptions.TypeError("pow() expected at most 3 arguments, got " + args.length);
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("pow() takes no keyword arguments");
        }

        if (args.length == 3) {
            throw new org.python.exceptions.NotImplementedError("pow() with mod not supported");
            // return args[0].__pow__(args[1], args[2]);
        } else {
            return args[0].__pow__(args[1]);
        }
    }

    @org.python.Method(
        __doc__ = "print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)" +
            "\n" +
            "Prints the values to a stream, or to sys.stdout by default.\n" +
            "Optional keyword arguments:\n" +
            "file:  a file-like object (stream); defaults to the current sys.stdout.\n" +
            "sep:   string inserted between values, default a space.\n" +
            "end:   string appended after the last value, default a newline.\n" +
            "flush: whether to forcibly flush the stream.\n"
    )
    public static void print(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        org.python.Object file = kwargs.get("file");
        org.python.Object sep = kwargs.get("sep");
        org.python.Object end = kwargs.get("end");
        org.python.Object flush = kwargs.get("flush");

        StringBuilder buffer = new StringBuilder();
        for (int i = 0; i < args.length; i++) {
            if (args[i] == null) {
                buffer.append("None");
            } else {
                buffer.append(args[i]);
            }
            if (i != args.length - 1) {
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
    public static org.python.Object property(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'property' not implemented");
    }

    @org.python.Method(
        __doc__ = "range(stop) -> range object" +
            "range(start, stop[, step]) -> range object\n" +
            "\n" +
            "Return a virtual sequence of numbers from start to stop by step.\n"
    )
    public static org.python.types.Range range(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length == 1) {
            return new org.python.types.Range(args[0]);
        } else if (args.length == 2) {
            return new org.python.types.Range(args[0], args[1]);
        } else if (args.length == 3) {
            return new org.python.types.Range(args[0], args[1], args[2]);
        } else if (args.length == 0) {
            throw new org.python.exceptions.TypeError("range expected 1 arguments, got " + args.length);
        } else {
            throw new org.python.exceptions.TypeError("range expected at most 3 arguments, got " + args.length);
        }
    }

    @org.python.Method(
        __doc__ = "repr(object) -> string" +
            "\n" +
            "Return the canonical string representation of the object.\n" +
            "For most object types, eval(repr(object)) == object.\n"
    )
    public static org.python.types.Str repr(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("repr() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("repr() takes no keyword arguments");
        }
        return args[0].__repr__();
    }

    @org.python.Method(
        __doc__ = "reversed(sequence) -> reverse iterator over values of the sequence" +
            "\n" +
            "Return a reverse iterator\n"
    )
    public static org.python.Iterable reversed(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("reversed() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("reversed() takes no keyword arguments");
        }
        return args[0].__reversed__();
    }

    @org.python.Method(
        __doc__ = "round(number[, ndigits]) -> number" +
            "\n" +
            "Round a number to a given precision in decimal digits (default 0 digits).\n" +
            "This returns an int when called with one argument, otherwise the\n" +
            "same type as the number. ndigits may be negative.\n"
    )
    public static org.python.Object round(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("round() takes no keyword arguments");
        }
        if (args.length == 0) {
            throw new org.python.exceptions.TypeError("Required argument 'number' (pos 1) not found");
        } else if (args.length == 1) {
            return args[0].__round__();
        } else if (args.length == 2) {
            return args[0].__round__(args[1]);
        } else {
            throw new org.python.exceptions.TypeError("round() takes at most 2 arguments (" + args.length + " given)");
        }
    }

    @org.python.Method(
        __doc__ = "set() -> new empty set object" +
            "set(iterable) -> new set object\n" +
            "\n" +
            "Build an unordered collection of unique elements.\n"
    )
    public static org.python.types.Set set(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("set() does not take keyword arguments");
        }
        if (args.length == 0) {
            return new org.python.types.Set();
        } else if (args.length == 1) {
            // return new org.python.types.Set(args[0]);
            throw new org.python.exceptions.NotImplementedError("Builtin function 'set' with iterator not implemented");
        } else {
            throw new org.python.exceptions.TypeError("set() expected at most 1 arguments ( got " + args.length + ")");
        }
    }

    @org.python.Method(
        __doc__ = "setattr(object, name, value)" +
            "\n" +
            "Set a named attribute on an object; setattr(x, 'y', v) is equivalent to\n" +
            "``x.y = v''.\n"
    )
    public static org.python.Object setattr(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'setattr' not implemented");
    }

    @org.python.Method(
        __doc__ = "slice(stop)" +
            "slice(start, stop[, step])\n" +
            "\n" +
            "Create a slice object.  This is used for extended slicing (e.g. a[0:10:2]).\n"
    )
    public static org.python.Object slice(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'input' not implemented");
    }

    @org.python.Method(
        __doc__ = "sorted(iterable, key=None, reverse=False) --> new sorted list"
    )
    public static org.python.types.List sorted(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
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
    public static org.python.Object staticmethod(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
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
            "errors defaults to 'strict'.\n"
    )
    public static org.python.types.Str str(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args.length != 1) {
            throw new org.python.exceptions.TypeError("len() takes exactly one argument (" + args.length + " given)");
        }
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("len() takes no keyword arguments");
        }
        return args[0].__str__();
    }

    @org.python.Method(
        __doc__ = "sum(iterable[, start]) -> value" +
            "\n" +
            "Return the sum of an iterable of numbers (NOT strings) plus the value\n" +
            "of parameter 'start' (which defaults to 0).  When the iterable is\n" +
            "empty, return start.\n"
    )
    public static org.python.Object sum(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'sum' not implemented");
    }

    @org.python.Method(
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
    public static org.python.Object super_call(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'super' not implemented");
    }

    @org.python.Method(
        __doc__ = "tuple() -> empty tuple" +
            "tuple(iterable) -> tuple initialized from iterable's items\n" +
            "\n" +
            "If the argument is a tuple, the return value is the same object.\n"
    )
    public static org.python.types.Tuple tuple(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'tuple' not implemented");
    }

    @org.python.Method(
        __doc__ = "type(object_or_name, bases, dict)" +
            "type(object) -> the object's type\n" +
            "type(name, bases, dict) -> a new type\n"
    )
    public static org.python.types.Type type(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("type() takes 1 or 3 arguments");
        }
        if (args.length == 1) {
            return org.python.types.Type.pythonType(args[0].getClass());
        } else if (args.length == 3) {
            throw new org.python.exceptions.NotImplementedError("3-argument form of builtin function 'type' not implemented");
        } else {
            throw new org.python.exceptions.TypeError("type() takes 1 or 3 arguments");
        }
    }

    @org.python.Method(
        __doc__ = "vars([object]) -> dictionary" +
            "\n" +
            "Without arguments, equivalent to locals().\n" +
            "With an argument, equivalent to object.__dict__.\n"
    )
    public static org.python.types.Dict vars(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
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
    public static org.python.Object zip(
                org.python.Object [] args,
                java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'zip' not implemented");
    }
}
