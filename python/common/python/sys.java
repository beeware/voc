package python;

@org.python.Module(
        __doc__ =
                "This module provides access to some objects used or maintained by the\n" +
                        "interpreter and to functions that interact strongly with the interpreter.\n" +
                        "\n" +
                        "Dynamic objects:\n" +
                        "\n" +
                        "argv -- command line arguments; argv[0] is the script pathname if known\n" +
                        "path -- module search path; path[0] is the script directory, else ''\n" +
                        "modules -- dictionary of loaded modules\n" +
                        "\n" +
                        "displayhook -- called to show results in an interactive session\n" +
                        "excepthook -- called to handle any uncaught exception other than SystemExit\n" +
                        "  To customize printing in an interactive session or to install a custom\n" +
                        "  top-level exception handler, assign other functions to replace these.\n" +
                        "\n" +
                        "stdin -- standard input file object; used by input()\n" +
                        "stdout -- standard output file object; used by print()\n" +
                        "stderr -- standard error object; used for error messages\n" +
                        "  By assigning other file objects (or objects that behave like files)\n" +
                        "  to these, it is possible to redirect all of the interpreter's I/O.\n" +
                        "\n" +
                        "last_type -- type of last uncaught exception\n" +
                        "last_value -- value of last uncaught exception\n" +
                        "last_traceback -- traceback of last uncaught exception\n" +
                        "  These three are only available in an interactive session after a\n" +
                        "  traceback has been printed.\n" +
                        "\n" +
                        "Static objects:\n" +
                        "\n" +
                        "builtin_module_names -- tuple of module names built into this interpreter\n" +
                        "copyright -- copyright notice pertaining to this interpreter\n" +
                        "exec_prefix -- prefix used to find the machine-specific Python library\n" +
                        "executable -- absolute path of the executable binary of the Python interpreter\n" +
                        "float_info -- a struct sequence with information about the float implementation.\n" +
                        "float_repr_style -- string indicating the style of repr() output for floats\n" +
                        "hash_info -- a struct sequence with information about the hash algorithm.\n" +
                        "hexversion -- version information encoded as a single integer\n" +
                        "implementation -- Python implementation information.\n" +
                        "int_info -- a struct sequence with information about the int implementation.\n" +
                        "maxsize -- the largest supported length of containers.\n" +
                        "maxunicode -- the value of the largest Unicode code point\n" +
                        "platform -- platform identifier\n" +
                        "prefix -- prefix used to find the Python library\n" +
                        "thread_info -- a struct sequence with information about the thread implementation.\n" +
                        "version -- the version of this interpreter as a string\n" +
                        "version_info -- version information as a named tuple\n" +
                        "__stdin__ -- the original stdin; don't touch!\n" +
                        "__stdout__ -- the original stdout; don't touch!\n" +
                        "__stderr__ -- the original stderr; don't touch!\n" +
                        "__displayhook__ -- the original displayhook; don't touch!\n" +
                        "__excepthook__ -- the original excepthook; don't touch!\n" +
                        "\n" +
                        "Functions:\n" +
                        "\n" +
                        "displayhook() -- print an object to the screen, and save it in builtins._\n" +
                        "excepthook() -- print an exception and its traceback to sys.stderr\n" +
                        "exc_info() -- return thread-safe information about the current exception\n" +
                        "exit() -- exit the interpreter by raising SystemExit\n" +
                        "getdlopenflags() -- returns flags to be used for dlopen() calls\n" +
                        "getprofile() -- get the global profiling function\n" +
                        "getrefcount() -- return the reference count for an object (plus one :-)\n" +
                        "getrecursionlimit() -- return the max recursion depth for the interpreter\n" +
                        "getsizeof() -- return the size of an object in bytes\n" +
                        "gettrace() -- get the global debug tracing function\n" +
                        "setcheckinterval() -- control how often the interpreter checks for events\n" +
                        "setdlopenflags() -- set the flags to be used for dlopen() calls\n" +
                        "setprofile() -- set the global profiling function\n" +
                        "setrecursionlimit() -- set the max recursion depth for the interpreter\n" +
                        "settrace() -- set the global debug tracing function\n"
)
public class sys extends org.python.types.Module {
    static {
        stdout = python.platform.impl.stdout();
        stderr = python.platform.impl.stderr();
        stdin = python.platform.impl.stdin();

        __stdout__ = python.platform.impl.stdout();
        __stderr__ = python.platform.impl.stderr();
        __stdin__ = python.platform.impl.stdin();

        platform = python.platform.impl.getPlatform();

        hexversion = new org.python.types.Int(org.Python.VERSION);

        int major = org.Python.VERSION >> 24;
        int minor = (org.Python.VERSION >> 16) % 0x10;
        int micro = (org.Python.VERSION >> 8) % 0x10;
        int releaselevel = (org.Python.VERSION >> 4) % 0x10;
        int serial = org.Python.VERSION % 0x10;

        version_info = new org.python.stdlib.sys.VersionInfo(major, minor, micro, releaselevel, serial);
        version = new org.python.types.Str(
                java.lang.String.format("%x.%x.%x (VOC)\n[Java(TM) SE Runtime Environment (build %s)]",
                        major, minor, micro,
                        System.getProperty("java.version")
                )
        );
    }

    @org.python.Method(
            __doc__ = "Create and return a new object.  See help(type) for accurate signature."
    )
    public org.python.Object __new__(org.python.Object klass) {
        org.python.types.Type cls = (org.python.types.Type) super.__new__(klass);

        // cls.__dict__.put("__spec__", new org.python.types...);
        // cls.__dict__.put("__loader__", new org.python.types...);

        cls.__dict__.put("argv", python.platform.impl.args());
        return cls;
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object __displayhook__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.__displayhook__() has not been implemented.");
    }

    public static org.python.types.Int __egginsert;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object __excepthook__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.__excepthook__() has not been implemented.");
    }

    @org.python.Attribute()
    public static org.python.Object __loader__ = org.python.types.NoneType.NONE;  // TODO
    @org.python.Attribute()
    public static org.python.Object __name__ = new org.python.types.Str("sys");
    @org.python.Attribute
    public static org.python.Object __file__ = new org.python.types.Str("python/common/python/sys.java");
    @org.python.Attribute()
    public static org.python.Object __package__ = new org.python.types.Str("");
    @org.python.Attribute()
    public static org.python.Object __spec__ = org.python.types.NoneType.NONE;  // TODO

    public static org.python.types.Int __plen;

    @org.python.Attribute()
    public static org.python.Object __stderr__;
    @org.python.Attribute()
    public static org.python.Object __stdin__;
    @org.python.Attribute()
    public static org.python.Object __stdout__;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _clear_type_cache(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys._clear_type_cache() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _current_frames(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys._current_frames() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _debugmallocstats(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys._debugmallocstats() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _getframe(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys._getframe() has not been implemented.");
    }

    public static org.python.types.Tuple _mercurial;
    public static org.python.types.Dict _xoptions;
    public static org.python.Object abiflags;
    public static org.python.types.Int api_version;
    @org.python.Attribute()
    public static org.python.types.List argv;
    public static org.python.Object base_exec_prefix;
    public static org.python.Object base_prefix;
    public static org.python.types.Tuple builtin_module_names;
    public static org.python.Object byteorder;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object call_tracing(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.call_tracing() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object callstats(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.callstats() has not been implemented.");
    }

    public static org.python.Object copyright;

    // displayhook <class 'IPython.core.displayhook.DisplayHook'>

    // dont_write_bytecode <class 'bool'>

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object exc_info(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.exc_info() has not been implemented.");
    }

    // excepthook <class 'method'>
    public static org.python.Object exec_prefix;
    public static org.python.Object executable;

    @org.python.Method(
            __doc__ = "exit([status])\n" +
                    "\n" +
                    "Exit the interpreter by raising SystemExit(status).\n" +
                    "If the status is omitted or None, it defaults to zero (i.e., success).\n" +
                    "If the status is an integer, it will be used as the system exit status.\n" +
                    "If it is another kind of object, it will be printed and the systemn\n" +
                    "exit status will be one (i.e., failure).\n",
            default_args = {"status"}
    )
    public static org.python.Object exit(org.python.Object status) {
        if (status == null) {
            throw new org.python.exceptions.SystemExit();
        } else {
            throw new org.python.exceptions.SystemExit(status);
        }
    }

    // flags <class 'sys.flags'>

    // float_info <class 'sys.float_info'>
    public static org.python.Object float_repr_style;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getallocatedblocks(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.getallocatedblocks() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getcheckinterval(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.getcheckinterval() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getdefaultencoding(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.getdefaultencoding() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getdlopenflags(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.getdlopenflags() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getfilesystemencoding(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.getfilesystemencoding() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getprofile(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.getprofile() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getrecursionlimit(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.getrecursionlimit() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getrefcount(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.getrefcount() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getsizeof(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.getsizeof() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.types.Float getswitchinterval(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        return new org.python.types.Float(0.005);
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object gettrace(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.gettrace() has not been implemented.");
    }

    // hash_info <class 'sys.hash_info'>
    @org.python.Attribute
    public static org.python.types.Int hexversion;

    // implementation <class 'types.SimpleNamespace'>

    // int_info <class 'sys.int_info'>

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object intern(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.intern() has not been implemented.");
    }

    // last_traceback <class 'traceback'>

    // last_type <class 'type'>

    // last_value <class 'SyntaxError'>
    public static org.python.types.Int maxsize;
    public static org.python.types.Int maxunicode;
    public static org.python.types.List meta_path;
    public static org.python.types.Dict modules = new org.python.types.Dict();
    public static org.python.types.List path;
    public static org.python.types.List path_hooks;
    public static org.python.types.Dict path_importer_cache;
    @org.python.Attribute
    public static org.python.Object platform;
    public static org.python.Object prefix;
    public static org.python.Object ps1;
    public static org.python.Object ps2;
    public static org.python.Object ps3;
    public static org.python.Object real_prefix;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setcheckinterval(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.setcheckinterval() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setdlopenflags(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.setdlopenflags() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setprofile(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.setprofile() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setrecursionlimit(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.setrecursionlimit() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setswitchinterval(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.setswitchinterval() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object settrace(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.settrace() has not been implemented.");
    }

    @org.python.Attribute()
    public static org.python.Object stderr;
    @org.python.Attribute()
    public static org.python.Object stdin;
    @org.python.Attribute()
    public static org.python.Object stdout;

    // thread_info <class 'sys.thread_info'>
    @org.python.Attribute
    public static org.python.Object version;
    @org.python.Attribute
    public static org.python.Object version_info;
    public static org.python.Object warnoptions;
}
