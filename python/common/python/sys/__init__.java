package python.sys;


public class __init__ extends org.python.types.Module {
    @org.python.Method(
        __doc__ = "Create and return a new object.  See help(type) for accurate signature."
    )
    public org.python.Object __new__(org.python.Object klass) {
        org.python.types.Type cls = (org.python.types.Type) super.__new__(klass);

        // Initialize sys.argv using command line arguments from environment
        // java.util.regex.Pattern cmdline_pattern = java.util.regex.Pattern.compile("(\"[^\"]*\"|[^\"]+)(\\s+|$)");
        java.util.regex.Pattern cmdline_pattern = java.util.regex.Pattern.compile("\\s+");
        java.lang.String [] cmdline_args = cmdline_pattern.split(System.getProperty("sun.java.command"));
        java.util.List<org.python.Object> arg_list = new java.util.ArrayList<org.python.Object>();
        for (String arg: cmdline_args) {
            arg_list.add(new org.python.types.Str(arg));
        }

        cls.__dict__.put("argv", new org.python.types.List(arg_list));
        return cls;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object __displayhook__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.__displayhook__() has not been implemented.");
    }

    public static org.python.types.Str __doc__;

    public static org.python.types.Int __egginsert;

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object __excepthook__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.__excepthook__() has not been implemented.");
    }

    // __loader__ <class 'type'>

    public static org.python.types.Str __name__;

    public static org.python.types.Str __package__;

    public static org.python.types.Int __plen;

    // __spec__ <class '_frozen_importlib.ModuleSpec'>

    // __stderr__ <class '_io.TextIOWrapper'>

    // __stdin__ <class '_io.TextIOWrapper'>

    // __stdout__ <class '_io.TextIOWrapper'>

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

    public static org.python.types.Str abiflags;

    public static org.python.types.Int api_version;

    @org.python.Attribute()
    public static org.python.types.List argv;

    public static org.python.types.Str base_exec_prefix;

    public static org.python.types.Str base_prefix;

    public static org.python.types.Tuple builtin_module_names;

    public static org.python.types.Str byteorder;

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

    public static org.python.types.Str copyright;

    // displayhook <class 'IPython.core.displayhook.DisplayHook'>

    // dont_write_bytecode <class 'bool'>

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object exc_info(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("sys.exc_info() has not been implemented.");
    }

    // excepthook <class 'method'>

    public static org.python.types.Str exec_prefix;

    public static org.python.types.Str executable;

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

    public static org.python.types.Str float_repr_style;

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

    public static org.python.types.Str platform;

    public static org.python.types.Str prefix;

    public static org.python.types.Str ps1;

    public static org.python.types.Str ps2;

    public static org.python.types.Str ps3;

    public static org.python.types.Str real_prefix;

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

    public static org.python.types.Str version;

    // version_info <class 'sys.version_info'>

    public static org.python.types.List warnoptions;

}