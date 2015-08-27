package org;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Hashtable;
import java.util.HashSet;

import org.python.PyObject;
import org.python.exceptions.IOError;
import org.python.exceptions.NotImplementedError;
import org.python.exceptions.TypeError;


public class Python {
    public static Hashtable<String, PyObject> globals;

    /**
     * __import__(name, globals=None, locals=None, fromlist=(), level=0) -> module
     *
     * Import a module. Because this function is meant for use by the Python
     * interpreter and not for general use it is better to use
     * importlib.import_module() to programmatically import a module.
     *
     * The globals argument is only used to determine the context;
     * they are not modified.  The locals argument is unused.  The fromlist
     * should be a list of names to emulate ``from name import ...'', or an
     * empty list to emulate ``import name''.
     * When importing a module from a package, note that __import__('A.B', ...)
     * returns package A when fromlist is empty, but its submodule B when
     * fromlist is not empty.  Level is used to determine whether to perform
     * absolute or relative imports. 0 is absolute while a positive number
     * is the number of parent directories to search relative to the current module.
     */
    public static PyObject __import__(PyObject name, PyObject globals, PyObject locals, PyObject fromlist, PyObject level) {
        throw new NotImplementedError("Builtin function '__import__' not implemented");
    }

    /**
     * abs(number) -> number
     *
     * Return the absolute value of the argument.
     */
    public static PyObject abs(PyObject number) {
        throw new NotImplementedError("Builtin function 'abs' not implemented");
    }

    /**
     * all(iterable) -> bool
     *
     * Return True if bool(x) is True for all values x in the iterable.
     * If the iterable is empty, return True.
     */
    public static PyObject all(PyObject iterable) {
        throw new NotImplementedError("Builtin function 'all' not implemented");
    }

    /**
     * any(iterable) -> bool
     *
     * Return True if bool(x) is True for any x in the iterable.
     * If the iterable is empty, return False.
     */
    public static PyObject any(PyObject iterable) {
        throw new NotImplementedError("Builtin function 'any' not implemented");
    }

    /**
     * ascii(object) -> string
     *
     * As repr(), return a string containing a printable representation of an
     * object, but escape the non-ASCII characters in the string returned by
     * repr() using \\x, \\u or \\U escapes.  This generates a string similar
     * to that returned by repr() in Python 2.
     */
    public static PyObject ascii(PyObject obj) {
        throw new NotImplementedError("Builtin function 'ascii' not implemented");
    }

    /**
     * bin(number) -> string
     *
     * Return the binary representation of an integer.
     *
     *   >>> bin(2796202)
     *   '0b1010101010101010101010'
     */
    public static PyObject bin(PyObject obj) {
        return new PyObject(String.format("0b%b", obj.value));
    }

    /**
     * bool(x) -> bool
     *
     * Returns True when the argument x is true, False otherwise.
     * The builtins True and False are the only two instances of the class bool.
     * The class bool is a subclass of the class int, and cannot be subclassed.
     */
    public static PyObject bool(PyObject obj) {
        // bytearray(iterable_of_ints) -> bytearray
        // bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
        // bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
        throw new NotImplementedError("Builtin function 'bool' not implemented");
    }

    /**
     * bytearray(iterable_of_ints) -> bytearray
     * bytearray(string, encoding[, errors]) -> bytearray
     * bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
     * bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
     * bytearray() -> empty bytes array
     *
     * Construct an mutable bytearray object from:
     *  - an iterable yielding integers in range(256)
     *  - a text string encoded using the specified encoding
     *  - a bytes or a buffer object
     *  - any object implementing the buffer API.
     *  - an integer
     */
    public static PyObject bytearray(PyObject obj) {
        // bytearray(iterable_of_ints) -> bytearray
        // bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
        // bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
        throw new NotImplementedError("Builtin function 'bytearray' not implemented");
    }

    public static PyObject bytearray(PyObject string, PyObject encoding, PyObject errors) {
        // bytearray(string, encoding[, errors]) -> bytearray
        throw new NotImplementedError("Builtin function 'bytearray' not implemented");
    }

    public static PyObject bytearray(PyObject string, PyObject encoding) {
        // bytearray(string, encoding) -> bytearray
        return bytearray(string, encoding, null);
    }

    public static PyObject bytearray() {
        // bytearray() -> empty bytes array
        throw new NotImplementedError("Builtin function 'bytearray' not implemented");
    }

    /**
     * bytes(iterable_of_ints) -> bytes
     * bytes(string, encoding[, errors]) -> bytes
     * bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
     * bytes(int) -> bytes object of size given by the parameter initialized with null bytes
     * bytes() -> empty bytes object
     *
     * Construct an immutable array of bytes from:
     *  - an iterable yielding integers in range(256)
     *  - a text string encoded using the specified encoding
     *  - any object implementing the buffer API.
     *  - an integer
     */
    public static PyObject bytes(PyObject obj) {
        // bytes(iterable_of_ints) -> bytes
        // bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
        // bytes(int) -> bytes object of size given by the parameter initialized with null bytes
        throw new NotImplementedError("Builtin function 'bytes' not implemented");
    }

    public static PyObject bytes(PyObject string, PyObject encoding, PyObject errors) {
        // bytes(string, encoding[, errors]) -> bytes
        throw new NotImplementedError("Builtin function 'bytes' not implemented");
    }

    public static PyObject bytes(PyObject string, PyObject encoding) {
        // bytes(string, encoding) -> bytes
        return bytes(string, encoding, null);
    }

    public static PyObject bytes() {
        // bytes() -> empty bytes object
        throw new NotImplementedError("Builtin function 'bytes' not implemented");
    }

    /**
     * callable(object) -> bool
     *
     * Return whether the object is callable (i.e., some kind of function).
     * Note that classes are callable, as are instances of classes with a
     * __call__() method.
     */
    public static PyObject callable(PyObject obj) {
        throw new NotImplementedError("Builtin function 'callable' not implemented");
    }

    /**
     * chr(i) -> Unicode character
     *
     * Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
     */
    public static PyObject chr(PyObject i) {
        throw new NotImplementedError("Builtin function 'callable' not implemented");
    }

    /**
     * classmethod(function) -> method
     *
     * Convert a function to be a class method.
     *
     * A class method receives the class as implicit first argument,
     * just like an instance method receives the instance.
     * To declare a class method, use this idiom:
     *
     *  class C:
     *      def f(cls, arg1, arg2, ...): ...
     *      f = classmethod(f)
     *
     * It can be called either on the class (e.g. C.f()) or on an instance
     * (e.g. C().f()).  The instance is ignored except for its class.
     * If a class method is called for a derived class, the derived class
     * object is passed as the implied first argument.
     *
     * Class methods are different than C++ or Java static methods.
     * If you want those, see the staticmethod builtin.
     */
    public static PyObject classmethod(PyObject function) {
        throw new NotImplementedError("Builtin function 'classmethod' not implemented");
    }

    /**
     * compile(source, filename, mode[, flags[, dont_inherit]]) -> code object
     *
     * Compile the source (a Python module, statement or expression)
     * into a code object that can be executed by exec() or eval().
     * The filename will be used for run-time error messages.
     * The mode must be 'exec' to compile a module, 'single' to compile a
     * single (interactive) statement, or 'eval' to compile an expression.
     * The flags argument, if present, controls which future statements influence
     * the compilation of the code.
     * The dont_inherit argument, if non-zero, stops the compilation inheriting
     * the effects of any future statements in effect in the code calling
     * compile; if absent or zero these statements do influence the compilation,
     * in addition to any features explicitly specified.
     */
    public static PyObject compile(PyObject source, PyObject filename, PyObject mode, PyObject flags, PyObject dont_inherit) {
        throw new NotImplementedError("Builtin function 'compile' not implemented");
    }

    public static PyObject compile(PyObject source, PyObject filename, PyObject mode, PyObject flags) {
        return compile(source, filename, mode, flags, null);
    }

    public static PyObject compile(PyObject source, PyObject filename, PyObject mode) {
        return compile(source, filename, mode, null, null);
    }

    /**
     * complex(real[, imag]) -> complex number
     *
     * Create a complex number from a real part and an optional imaginary part.
     * This is equivalent to (real + imag*1j) where imag defaults to 0.
     */
    public static PyObject complex(PyObject real, PyObject imag) {
        throw new NotImplementedError("Builtin function 'complex' not implemented");
    }

    public static PyObject complex(PyObject real) {
        return complex(real, new PyObject(0));
    }

    /**
     * interactive prompt objects for printing the license text, a list of
     * contributors and the copyright notice.
     */
    public static PyObject copyright() {
        throw new NotImplementedError("Builtin function 'copyright' not implemented");
    }

    /**
     * interactive prompt objects for printing the license text, a list of
     * contributors and the copyright notice.
     */
    public static PyObject credits() {
        throw new NotImplementedError("Builtin function 'credits' not implemented");
    }

    /**
     * delattr(object, name)
     *
     * Delete a named attribute on an object; delattr(x, 'y') is equivalent to
     * ``del x.y''.
    */
    public static PyObject delattr(PyObject object, PyObject name) {
        throw new NotImplementedError("Builtin function 'delattr' not implemented");
    }

    /**
     * dict() -> new empty dictionary
     * dict(mapping) -> new dictionary initialized from a mapping object's
     *     (key, value) pairs
     * dict(iterable) -> new dictionary initialized as if via:
     *     d = {}
     *     for k, v in iterable:
     *         d[k] = v
     * dict(**kwargs) -> new dictionary initialized with the name=value pairs
     *     in the keyword argument list.  For example:  dict(one=1, two=2)
     */
    public static PyObject dict(PyObject obj) {
        throw new NotImplementedError("Builtin function 'dict' not implemented");
    }

    public static PyObject dict() {
        throw new NotImplementedError("Builtin function 'dict' not implemented");
    }

    // public static PyObject dict(**kwargs) {
    //     throw new NotImplementedError("Builtin function 'dict' not implemented");
    // }

    /**
     * dir([object]) -> list of strings
     *
     * If called without an argument, return the names in the current scope.
     * Else, return an alphabetized list of names comprising (some of) the attributes
     * of the given object, and of attributes reachable from it.
     * If the object supplies a method named __dir__, it will be used; otherwise
     * the default dir() logic is used and returns:
     *   for a module object: the module's attributes.
     *   for a class object:  its attributes, and recursively the attributes
     *     of its bases.
     *     for any other object: its attributes, its class's attributes, and
     *     recursively the attributes of its class's base classes.
     */
    public static PyObject dir(PyObject obj) {
        throw new NotImplementedError("Builtin function 'dir' not implemented");
    }

    public static PyObject dir() {
        throw new NotImplementedError("Builtin function 'dir' not implemented");
    }

    /**
     * divmod(x, y) -> (div, mod)
     *
     * Return the tuple ((x-x%y)/y, x%y).  Invariant: div*y + mod == x.
     */
    public static PyObject divmod(PyObject x, PyObject y) {
        throw new NotImplementedError("Builtin function 'divmod' not implemented");
    }

    /**
     * enumerate(iterable[, start]) -> iterator for index, value of iterable
     *
     * Return an enumerate object.  iterable must be another object that supports
     * iteration.  The enumerate object yields pairs containing a count (from
     * start, which defaults to zero) and a value yielded by the iterable argument.
     * enumerate is useful for obtaining an indexed list:
     *        (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
     */
    public static PyObject enumerate(PyObject iterable, PyObject start) {
        throw new NotImplementedError("Builtin function 'enumerate' not implemented");
    }

    public static PyObject enumerate(PyObject iterable) {
        return enumerate(iterable, new PyObject(0));
    }

    /**
     * eval(source[, globals[, locals]]) -> value
     *
     * Evaluate the source in the context of globals and locals.
     * The source may be a string representing a Python expression
     * or a code object as returned by compile().
     * The globals must be a dictionary and locals can be any mapping,
     * defaulting to the current globals and locals.
     * If only globals is given, locals defaults to it.
     */
    public static PyObject eval(PyObject source, PyObject globals, PyObject locals) {
        throw new NotImplementedError("Builtin function 'eval' not implemented");
    }

    public static PyObject eval(PyObject source, PyObject globals) {
        return eval(source, globals, null);
    }

    public static PyObject eval(PyObject source) {
        return eval(source, null, null);
    }

    /**
     * exec(object[, globals[, locals]])
     *
     * Read and execute code from an object, which can be a string or a code
     * object.
     * The globals and locals are dictionaries, defaulting to the current
     * globals and locals.  If only globals is given, locals defaults to it.
    */
    public static PyObject exec(PyObject obj, PyObject globals, PyObject locals) {
        throw new NotImplementedError("Builtin function 'exec' not implemented");
    }

    public static PyObject exec(PyObject obj, PyObject globals) {
        return exec(obj, globals, null);
    }

    public static PyObject exec(PyObject obj) {
        return exec(obj, null, null);
    }

    /**
     * filter(function or None, iterable) --> filter object
     *
     * Return an iterator yielding those items of iterable for which function(item)
     * is true. If function is None, return the items that are true.
     */
    public static PyObject filter(PyObject function, PyObject iterable) {
        throw new NotImplementedError("Builtin function 'filter' not implemented");
    }

    /**
     * float(x) -> floating point number
     *
     * Convert a string or number to a floating point number, if possible.
     */
    public static PyObject float_cast(PyObject obj) {
        return obj.__float__();
    }

    /**
     * format(value[, format_spec]) -> string
     *
     * Returns value.__format__(format_spec)
     * format_spec defaults to ""
    */
    public static PyObject format(PyObject value, PyObject format_spec) {
        throw new NotImplementedError("Builtin function 'format' not implemented");
    }

    public static PyObject format(PyObject value) {
        return format(value, new PyObject(""));
    }

    /**
     * frozenset() -> empty frozenset object
     * frozenset(iterable) -> frozenset object
     *
     * Build an immutable unordered collection of unique elements.
     */
    public static PyObject frozenset(PyObject iterable) {
        throw new NotImplementedError("Builtin function 'frozenset' not implemented");
    }

    public static PyObject frozenset() {
        throw new NotImplementedError("Builtin function 'frozenset' not implemented");
    }

    /**
     * getattr(object, name[, default]) -> value
     *
     * Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
     * When a default argument is given, it is returned when the attribute doesn't
     * exist; without it, an exception is raised in that case.
     */
    public static PyObject getattr(PyObject obj, PyObject name, PyObject def) {
        throw new NotImplementedError("Builtin function 'getattr' not implemented");
    }

    public static PyObject getattr(PyObject obj, PyObject name) {
        return getattr(obj, name, null);
    }

    /**
     * globals() -> dictionary
     *
     * Return the dictionary containing the current scope's global variables.
     */
    public static PyObject globals() {
        return new PyObject(Python.globals);
    }

    /**
     * hasattr(object, name) -> bool
     *
     * Return whether the object has an attribute with the given name.
     * (This is done by calling getattr(object, name) and catching AttributeError.)
     */
    public static PyObject hasattr(PyObject object, PyObject name) {
        throw new NotImplementedError("Builtin function 'hasattr' not implemented");
    }

    /**
     * hash(object) -> integer
     *
     * Return a hash value for the object.  Two objects with the same value have
     * the same hash value.  The reverse is not necessarily true, but likely.
     */
    public static PyObject hash(PyObject obj) {
        return obj.__hash__();
    }

    /**
     * Define the built-in 'help'.
     * This is a wrapper around pydoc.help (with a twist).
     */
    public static PyObject help(PyObject obj) {
        throw new NotImplementedError("Builtin function 'help' not implemented");
    }

    /**
     * hex(number) -> string
     *
     * Return the hexadecimal representation of an integer.
     *
     *   >>> hex(3735928559)
     *   '0xdeadbeef'
     */
    public static PyObject hex(PyObject obj) {
        return new PyObject(String.format("0x%x", obj.value));
    }

    /**
     * id(object) -> integer
     *
     * Return the identity of an object.  This is guaranteed to be unique among
     * simultaneously existing objects.
     */
    public static PyObject id(PyObject obj) {
        return new PyObject(System.identityHashCode(obj));
    }

    /**
     * input([prompt]) -> string
     *
     * Read a string from standard input.  The trailing newline is stripped.
     * If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
     * The prompt string, if given,
     * is printed without a trailing newline before reading.
     */
    public static PyObject input(PyObject prompt) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        if (prompt != null) {
            System.out.print(prompt);
            System.out.flush();
        }

        try {
            return new PyObject(reader.readLine());
        } catch (IOException e) {
            throw new IOError();
        }
    }

    public static PyObject input() {
        return input(null);
    }

    /**
     * int(x=0) -> integer
     * int(x, base=10) -> integer
     *
     * Convert a number or string to an integer, or return 0 if no arguments
     * are given.  If x is a number, return x.__int__().  For floating point
     * numbers, this truncates towards zero.
     *
     * If x is not a number or if base is given, then x must be a string,
     * bytes, or bytearray instance representing an integer literal in the
     * given base.  The literal can be preceded by '+' or '-' and be surrounded
     * by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
     * Base 0 means to interpret the base from the string as an integer literal.
     *
     *   >>> int('0b100', base=0)
     *   4
     */
    public static PyObject int_cast(PyObject obj, PyObject base) {
        throw new NotImplementedError("Builtin function 'int_cast' with base not implemented");
    }

    public static PyObject int_cast(PyObject obj) {
        return obj.__int__();
    }

    public static PyObject int_cast() {
        return new PyObject(0);
    }

    /**
     * isinstance(object, class-or-type-or-tuple) -> bool
     *
     * Return whether an object is an instance of a class or of a subclass thereof.
     * With a type as second argument, return whether that is the object's type.
     * The form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for
     * isinstance(x, A) or isinstance(x, B) or ... (etc.).
     */
    public static PyObject isinstance(PyObject obj, PyObject class_or_type_or_tuple) {
        throw new NotImplementedError("Builtin function 'isinstance' not implemented");
    }

    /**
     * issubclass(C, B) -> bool
     *
     * Return whether class C is a subclass (i.e., a derived class) of class B.
     * When using a tuple as the second argument issubclass(X, (A, B, ...)),
     * is a shortcut for issubclass(X, A) or issubclass(X, B) or ... (etc.).
     */
    public static PyObject issubclass(PyObject C, PyObject B) {
        throw new NotImplementedError("Builtin function 'issubclass' not implemented");
    }

    /**
     * iter(iterable) -> iterator
     * iter(callable, sentinel) -> iterator
     *
     * Get an iterator from an object.  In the first form, the argument must
     * supply its own iterator, or be a sequence.
     * In the second form, the callable is called until it returns the sentinel.
     */
    public static PyObject iter(PyObject iterable) {
        throw new NotImplementedError("Builtin function 'iter' not implemented");
    }

    public static PyObject iter(PyObject callable, PyObject sentinel) {
        throw new NotImplementedError("Builtin function 'iter' not implemented");
    }

    /**
     * len(object)
     *
     * Return the number of items of a sequence or collection.
     */
    public static PyObject len(PyObject obj) {
        return obj.__len__();
    }

    /**
     * interactive prompt objects for printing the license text, a list of
     * contributors and the copyright notice.
     */
    public static PyObject license() {
        throw new NotImplementedError("Builtin function 'license' not implemented");
    }

    /**
     * list() -> new empty list
     * list(iterable) -> new list initialized from iterable's items
     */
    public static PyObject list(PyObject iterable) {
        throw new NotImplementedError("Builtin function 'list' not implemented");
    }

    public static PyObject list() {
        throw new NotImplementedError("Builtin function 'list' not implemented");
    }

    /**
     * locals() -> dictionary
     *
     * Update and return a dictionary containing the current scope's local variables.
     */
    public static PyObject locals() {
        throw new NotImplementedError("Builtin function 'locals' not implemented");
    }

    /**
     * map(func, *iterables) --> map object
     *
     * Make an iterator that computes the function using arguments from
     * each of the iterables.  Stops when the shortest iterable is exhausted.
     */
    public static PyObject map(PyObject func, PyObject iterables) {
        throw new NotImplementedError("Builtin function 'input' not implemented");
    }

    /**
     * max(iterable, *[, default=obj, key=func]) -> value
     * max(arg1, arg2, *args, *[, key=func]) -> value
     *
     * With a single iterable argument, return its biggest item. The
     * default keyword-only argument specifies an object to return if
     * the provided iterable is empty.
     * With two or more arguments, return the largest argument.
     */
    public static PyObject max(PyObject iterable) {
        throw new NotImplementedError("Builtin function 'max' not implemented");
    }

    public static PyObject max(PyObject arg1, PyObject arg2) {
        throw new NotImplementedError("Builtin function 'max' not implemented");
    }

    /**
     * memoryview(object)
     *
     * Create a new memoryview object which references the given object.
     */
    public static PyObject memoryview(PyObject obj) {
        throw new NotImplementedError("Builtin function 'memoryview' not implemented");
    }

    /**
     * min(iterable, *[, default=obj, key=func]) -> value
     * min(arg1, arg2, *args, *[, key=func]) -> value
     *
     * With a single iterable argument, return its smallest item. The
     * default keyword-only argument specifies an object to return if
     * the provided iterable is empty.
     * With two or more arguments, return the smallest argument.
     */
    public static PyObject min(PyObject iterable) {
        throw new NotImplementedError("Builtin function 'min' not implemented");
    }

    public static PyObject min(PyObject arg1, PyObject arg2) {
        throw new NotImplementedError("Builtin function 'min' not implemented");
    }

    /**
     * next(iterator[, default])
     *
     * Return the next item from the iterator. If default is given and the iterator
     * is exhausted, it is returned instead of raising StopIteration.
     */
    public static PyObject next(PyObject iterator, PyObject def) {
        throw new NotImplementedError("Builtin function 'next' not implemented");
    }

    public static PyObject next(PyObject iterator) {
        throw new NotImplementedError("Builtin function 'next' not implemented");
    }

    /**
     * The most base type
     */
    public static PyObject object() {
        throw new NotImplementedError("Builtin function 'object' not implemented");
    }

    /**
     * oct(number) -> string
     *
     * Return the octal representation of an integer.
     *
     *    >>> oct(342391)
     *   '0o1234567'
     */
    public static PyObject oct(PyObject obj) {
        return new PyObject(String.format("0o%o", obj.value));
    }

    /**
     * open(file, mode='r', buffering=-1, encoding=None,
     *      errors=None, newline=None, closefd=True, opener=None) -> file object
     *
     * Open file and return a stream.  Raise IOError upon failure.
     *
     * file is either a text or byte string giving the name (and the path
     * if the file isn't in the current working directory) of the file to
     * be opened or an integer file descriptor of the file to be
     * wrapped. (If a file descriptor is given, it is closed when the
     * returned I/O object is closed, unless closefd is set to False.)
     *
     * mode is an optional string that specifies the mode in which the file
     * is opened. It defaults to 'r' which means open for reading in text
     * mode.  Other common values are 'w' for writing (truncating the file if
     * it already exists), 'x' for creating and writing to a new file, and
     * 'a' for appending (which on some Unix systems, means that all writes
     * append to the end of the file regardless of the current seek position).
     * In text mode, if encoding is not specified the encoding used is platform
     * dependent: locale.getpreferredencoding(False) is called to get the
     * current locale encoding. (For reading and writing raw bytes use binary
     * mode and leave encoding unspecified.) The available modes are:
     *
     * ========= ===============================================================
     * Character Meaning
     * --------- ---------------------------------------------------------------
     * 'r'       open for reading (default)
     * 'w'       open for writing, truncating the file first
     * 'x'       create a new file and open it for writing
     * 'a'       open for writing, appending to the end of the file if it exists
     * 'b'       binary mode
     * 't'       text mode (default)
     * '+'       open a disk file for updating (reading and writing)
     * 'U'       universal newline mode (deprecated)
     * ========= ===============================================================
     *
     * The default mode is 'rt' (open for reading text). For binary random
     * access, the mode 'w+b' opens and truncates the file to 0 bytes, while
     * 'r+b' opens the file without truncation. The 'x' mode implies 'w' and
     * raises an `FileExistsError` if the file already exists.
     *
     * Python distinguishes between files opened in binary and text modes,
     * even when the underlying operating system doesn't. Files opened in
     * binary mode (appending 'b' to the mode argument) return contents as
     * bytes objects without any decoding. In text mode (the default, or when
     * 't' is appended to the mode argument), the contents of the file are
     * returned as strings, the bytes having been first decoded using a
     * platform-dependent encoding or using the specified encoding if given.
     *
     * 'U' mode is deprecated and will raise an exception in future versions
     * of Python.  It has no effect in Python 3.  Use newline to control
     * universal newlines mode.
     *
     * buffering is an optional integer used to set the buffering policy.
     * Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
     * line buffering (only usable in text mode), and an integer > 1 to indicate
     * the size of a fixed-size chunk buffer.  When no buffering argument is
     * given, the default buffering policy works as follows:
     *
     * * Binary files are buffered in fixed-size chunks; the size of the buffer
     *   is chosen using a heuristic trying to determine the underlying device's
     *   "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
     *   On many systems, the buffer will typically be 4096 or 8192 bytes long.
     *
     * * "Interactive" text files (files for which isatty() returns True)
     *   use line buffering.  Other text files use the policy described above
     *   for binary files.
     *
     * encoding is the name of the encoding used to decode or encode the
     * file. This should only be used in text mode. The default encoding is
     * platform dependent, but any encoding supported by Python can be
     * passed.  See the codecs module for the list of supported encodings.
     *
     * errors is an optional string that specifies how encoding errors are to
     * be handled---this argument should not be used in binary mode. Pass
     * 'strict' to raise a ValueError exception if there is an encoding error
     * (the default of None has the same effect), or pass 'ignore' to ignore
     * errors. (Note that ignoring encoding errors can lead to data loss.)
     * See the documentation for codecs.register or run 'help(codecs.Codec)'
     * for a list of the permitted encoding error strings.
     *
     * newline controls how universal newlines works (it only applies to text
     * mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
     * follows:
     *
     * * On input, if newline is None, universal newlines mode is
     *   enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
     *   these are translated into '\n' before being returned to the
     *   caller. If it is '', universal newline mode is enabled, but line
     *   endings are returned to the caller untranslated. If it has any of
     *   the other legal values, input lines are only terminated by the given
     *   string, and the line ending is returned to the caller untranslated.
     *
     * * On output, if newline is None, any '\n' characters written are
     *   translated to the system default line separator, os.linesep. If
     *   newline is '' or '\n', no translation takes place. If newline is any
     *   of the other legal values, any '\n' characters written are translated
     *   to the given string.
     *
     * If closefd is False, the underlying file descriptor will be kept open
     * when the file is closed. This does not work when a file name is given
     * and must be True in that case.
     *
     * A custom opener can be used by passing a callable as *opener*. The
     * underlying file descriptor for the file object is then obtained by
     * calling *opener* with (*file*, *flags*). *opener* must return an open
     * file descriptor (passing os.open as *opener* results in functionality
     * similar to passing None).
     *
     * open() returns a file object whose type depends on the mode, and
     * through which the standard file operations such as reading and writing
     * are performed. When open() is used to open a file in a text mode ('w',
     * 'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
     * a file in a binary mode, the returned class varies: in read binary
     * mode, it returns a BufferedReader; in write binary and append binary
     * modes, it returns a BufferedWriter, and in read/write mode, it returns
     * a BufferedRandom.
     *
     * It is also possible to use a string or bytearray as a file for both
     * reading and writing. For strings StringIO can be used like a file
     * opened in a text mode, and for bytes a BytesIO can be used like a file
     * opened in a binary mode.
     */
    public static PyObject open(PyObject file, PyObject mode, PyObject buffering, PyObject encoding, PyObject errors, PyObject newline, PyObject closefd, PyObject opener) {
        throw new NotImplementedError("Builtin function 'open' not implemented");
    }

    public static PyObject open(PyObject file) {
        return open(file, new PyObject('r'), new PyObject(-1), null, null, null, null, null);
    }

    /**
     * ord(c) -> integer
     *
     * Return the integer ordinal of a one-character string.
     */
    public static PyObject ord(PyObject obj) {
        if (obj.type == String.class) {
            int length = ((String) obj.value).length();
            if (length != 1) {
                return new PyObject((int) ((String) obj.value).charAt(0));
            } else {
                throw new TypeError("ord() expected string of length 1, but string of length " + length + " found");
            }
        } else {
            throw new TypeError("ord() expected string of length 1, but " + obj.type + " found");
        }
    }

    /**
     * pow(x, y[, z]) -> number
     *
     * With two arguments, equivalent to x**y.  With three arguments,
     * equivalent to (x**y) % z, but may be more efficient (e.g. for ints).
     */
    public static PyObject pow(PyObject x, PyObject y) {
        return x.__pow__(y);
    }

    public static PyObject pow(PyObject x, PyObject y, PyObject z) {
        return x.__pow__(y).__mod__(z);
    }

    /**
     * print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
     *
     * Prints the values to a stream, or to sys.stdout by default.
     * Optional keyword arguments:
     * file:  a file-like object (stream); defaults to the current sys.stdout.
     * sep:   string inserted between values, default a space.
     * end:   string appended after the last value, default a newline.
     * flush: whether to forcibly flush the stream.
     */
    public static void print(PyObject... args) {
        StringBuilder buffer = new StringBuilder();
        for (int i = 0; i < args.length; i++) {
            buffer.append(args[i]);
            if (i != args.length - 1) {
                buffer.append(" ");
            }
        }
        System.out.println(buffer.toString());
    }

    /**
     * property(fget=None, fset=None, fdel=None, doc=None) -> property attribute
     *
     * fget is a function to be used for getting an attribute value, and likewise
     * fset is a function for setting, and fdel a function for del'ing, an
     * attribute.  Typical use is to define a managed attribute x:
     *
     * class C(object):
     *     def getx(self): return self._x
     *     def setx(self, value): self._x = value
     *     def delx(self): del self._x
     *     x = property(getx, setx, delx, "I'm the 'x' property.")
     *
     * Decorators make defining new properties or modifying existing ones easy:
     *
     * class C(object):
     *     @property
     *     def x(self):
     *         "I am the 'x' property."
     *         return self._x
     *     @x.setter
     *     def x(self, value):
     *         self._x = value
     *     @x.deleter
     *     def x(self):
     *         del self._x
     */
    public static PyObject property(PyObject fget, PyObject fset, PyObject fdel, PyObject doc) {
        throw new NotImplementedError("Builtin function 'property' not implemented");
    }

    /**
     * range(stop) -> range object
     * range(start, stop[, step]) -> range object
     *
     * Return a virtual sequence of numbers from start to stop by step.
     */
    public static PyObject range(PyObject stop) {
        throw new NotImplementedError("Builtin function 'range' not implemented");
    }

    public static PyObject range(PyObject start, PyObject stop, PyObject step) {
        throw new NotImplementedError("Builtin function 'range' not implemented");
    }


    public static PyObject range(PyObject start, PyObject stop) {
        return range(start, stop, new PyObject(1));
    }

    /**
     * repr(object) -> string
     *
     * Return the canonical string representation of the object.
     * For most object types, eval(repr(object)) == object.
     */
    public static PyObject repr(PyObject obj) {
        return obj.__repr__();
    }

    /**
     * reversed(sequence) -> reverse iterator over values of the sequence
     *
     * Return a reverse iterator
     */
    public static PyObject reversed(PyObject sequence) {
        throw new NotImplementedError("Builtin function 'reversed' not implemented");
    }

    /**
     * round(number[, ndigits]) -> number
     *
     * Round a number to a given precision in decimal digits (default 0 digits).
     * This returns an int when called with one argument, otherwise the
     * same type as the number. ndigits may be negative.
     */
    public static PyObject round(PyObject number, PyObject ndigits) {
        throw new NotImplementedError("Builtin function 'round' not implemented");
    }

    /**
     * round(number) -> number
     *
     * Round a number to a given precision in decimal digits (default 0 digits).
     * This returns an int when called with one argument, otherwise the
     * same type as the number. ndigits may be negative.
     */
    public static PyObject round(PyObject number) {
        return round(number, new PyObject(0));
    }

    /**
     * set() -> new empty set object
     * set(iterable) -> new set object
     *
     * Build an unordered collection of unique elements.
     */
    public static PyObject set(PyObject iterable) {
        throw new NotImplementedError("Builtin function 'set' not implemented");
    }

    public static PyObject set() {
        return new PyObject(new HashSet());
    }

    /**
     * setattr(object, name, value)
     *
     * Set a named attribute on an object; setattr(x, 'y', v) is equivalent to
     * ``x.y = v''.
     */
    public static PyObject setattr(PyObject obj, PyObject name, PyObject value) {
        throw new NotImplementedError("Builtin function 'setattr' not implemented");
    }

    /**
     * slice(stop)
     * slice(start, stop[, step])
     *
     * Create a slice object.  This is used for extended slicing (e.g. a[0:10:2]).
     */
    public static PyObject slice(PyObject stop) {
        throw new NotImplementedError("Builtin function 'input' not implemented");
    }

    public static PyObject slice(PyObject start, PyObject stop, PyObject step) {
        throw new NotImplementedError("Builtin function 'input' not implemented");
    }

    public static PyObject slice(PyObject start, PyObject stop) {
        return slice(start, stop, new PyObject(1));
    }

    /**
     * sorted(iterable, key=None, reverse=False) --> new sorted list
     */
    public static PyObject sorted(PyObject iterable) {
        throw new NotImplementedError("Builtin function 'sorted' not implemented");
    }

    public static PyObject sorted(PyObject iterable, PyObject key, PyObject reverse) {
        throw new NotImplementedError("Builtin function 'sorted' not implemented");
    }

    /**
     * staticmethod(function) -> method
     *
     * Convert a function to be a static method.
     *
     * A static method does not receive an implicit first argument.
     * To declare a static method, use this idiom:
     *
     *      class C:
     *      def f(arg1, arg2, ...): ...
     *      f = staticmethod(f)
     *
     * It can be called either on the class (e.g. C.f()) or on an instance
     * (e.g. C().f()).  The instance is ignored except for its class.
     *
     * Static methods in Python are similar to those found in Java or C++.
     * For a more advanced concept, see the classmethod builtin.
     */
    public static PyObject staticmethod(PyObject function) {
        throw new NotImplementedError("Builtin function 'staticmethod' not implemented");
    }

    /**
     * str(object='') -> str
     * str(bytes_or_buffer[, encoding[, errors]]) -> str
     *
     * Create a new string object from the given object. If encoding or
     * errors is specified, then the object must expose a data buffer
     * that will be decoded using the given encoding and error handler.
     * Otherwise, returns the result of object.__str__() (if defined)
     * or repr(object).
     * encoding defaults to sys.getdefaultencoding().
     * errors defaults to 'strict'.
     */
    public static PyObject str(PyObject obj) {
        return new PyObject((String) obj.value);
    }

    public static PyObject str() {
        return new PyObject("");
    }

    public static PyObject str(PyObject bytes_or_buffer, PyObject encoding, PyObject errors) {
        return new PyObject((String) bytes_or_buffer.value);
    }

    public static PyObject str(PyObject bytes_or_buffer, PyObject encoding) {
        return str(bytes_or_buffer, encoding, null);
    }

    /**
     * sum(iterable[, start]) -> value
     *
     * Return the sum of an iterable of numbers (NOT strings) plus the value
     * of parameter 'start' (which defaults to 0).  When the iterable is
     * empty, return start.
     */
    public static PyObject sum(PyObject iterable, PyObject start) {
        throw new NotImplementedError("Builtin function 'sum' not implemented");
    }

    public static PyObject sum(PyObject iterable) {
        return sum(iterable, new PyObject(0));
    }

    /**
     * super() -> same as super(__class__, <first argument>)
     * super(type) -> unbound super object
     * super(type, obj) -> bound super object; requires isinstance(obj, type)
     * super(type, type2) -> bound super object; requires issubclass(type2, type)
     * Typical use to call a cooperative superclass method:
     * class C(B):
     * def meth(self, arg):
     *    super().meth(arg)
     * This works for class methods too:
     * class C(B):
     * @classmethod
     * def cmeth(cls, arg):
     *    super().cmeth(arg)
     */

    public static PyObject super_call() {
        throw new NotImplementedError("Builtin function 'super' not implemented");
    }

    public static PyObject super_call(PyObject type) {
        throw new NotImplementedError("Builtin function 'super' not implemented");
    }

    public static PyObject super_call(PyObject type, PyObject obj) {
        throw new NotImplementedError("Builtin function 'super' not implemented");
    }

    /**
     * tuple() -> empty tuple
     * tuple(iterable) -> tuple initialized from iterable's items
     *
     * If the argument is a tuple, the return value is the same object.
     */
    public static PyObject tuple(PyObject iterable) {
        throw new NotImplementedError("Builtin function 'tuple' not implemented");
    }

    public static PyObject tuple() {
        throw new NotImplementedError("Builtin function 'tuple' not implemented");
    }

    /**
     * type(object_or_name, bases, dict)
     * type(object) -> the object's type
     * type(name, bases, dict) -> a new type
     */
    public static PyObject type(PyObject object_or_name, PyObject bases, PyObject dict) {
        throw new NotImplementedError("Builtin function 'type' not implemented");
    }

    public static PyObject type(PyObject object) {
        throw new NotImplementedError("Builtin function 'type' not implemented");
    }

    /**
     * vars([object]) -> dictionary
     *
     * Without arguments, equivalent to locals().
     * With an argument, equivalent to object.__dict__.
     */
    public static PyObject vars(PyObject obj) {
        throw new NotImplementedError("Builtin function 'vars' not implemented");
    }

    public static PyObject vars() {
        throw new NotImplementedError("Builtin function 'vars' not implemented");
    }

    /**
     * zip(iter1 [,iter2 [...]]) --> zip object
     *
     * Return a zip object whose .__next__() method returns a tuple where
     * the i-th element comes from the i-th iterable argument.  The .__next__()
     * method continues until the shortest iterable in the argument sequence
     * is exhausted and then it raises StopIteration.
     */
    public static PyObject zip(PyObject... iter) {
        throw new NotImplementedError("Builtin function 'zip' not implemented");
    }
}
