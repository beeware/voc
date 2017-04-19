package python;

@org.python.Module(
        __doc__ =
                "OS routines for NT or Posix depending on what system we're on.\n" +
                        "\n" +
                        "This exports:\n" +
                        "  - all functions from posix, nt or ce, e.g. unlink, stat, etc.\n" +
                        "  - os.path is either posixpath or ntpath\n" +
                        "  - os.name is either 'posix', 'nt' or 'ce'.\n" +
                        "  - os.curdir is a string representing the current directory ('.' or ':')\n" +
                        "  - os.pardir is a string representing the parent directory ('..' or '::')\n" +
                        "  - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')\n" +
                        "  - os.extsep is the extension separator (always '.')\n" +
                        "  - os.altsep is the alternate pathname separator (None or '/')\n" +
                        "  - os.pathsep is the component separator used in $PATH etc\n" +
                        "  - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')\n" +
                        "  - os.defpath is the default search path for executables\n" +
                        "  - os.devnull is the file path of the null device ('/dev/null', etc.)\n" +
                        "\n" +
                        "Programs that import and use 'os' stand a better chance of being\n" +
                        "portable between different platforms.  Of course, they must then\n" +
                        "only use functions that are defined by all platforms (e.g., unlink\n" +
                        "and opendir), and leave all pathname manipulation to os.path\n" +
                        "(e.g., split and join).\n" +
                        "\n"
)
public class os extends org.python.types.Module {
    static {
        environ = new org.python.types.Dict();
        environb = new org.python.types.Dict();
    }

    @org.python.Method(
            __doc__ = "Create and return a new object.  See help(type) for accurate signature."
    )
    public org.python.Object __new__(org.python.Object klass) {
        org.python.types.Type cls = (org.python.types.Type) super.__new__(klass);

        return cls;
    }

    @org.python.Attribute()
    public static org.python.Object CLD_CONTINUED;
    @org.python.Attribute()
    public static org.python.Object CLD_DUMPED;
    @org.python.Attribute()
    public static org.python.Object CLD_EXITED;
    @org.python.Attribute()
    public static org.python.Object CLD_TRAPPED;
    @org.python.Attribute()
    public static org.python.Object EX_CANTCREAT;
    @org.python.Attribute()
    public static org.python.Object EX_CONFIG;
    @org.python.Attribute()
    public static org.python.Object EX_DATAERR;
    @org.python.Attribute()
    public static org.python.Object EX_IOERR;
    @org.python.Attribute()
    public static org.python.Object EX_NOHOST;
    @org.python.Attribute()
    public static org.python.Object EX_NOINPUT;
    @org.python.Attribute()
    public static org.python.Object EX_NOPERM;
    @org.python.Attribute()
    public static org.python.Object EX_NOUSER;
    @org.python.Attribute()
    public static org.python.Object EX_OK;
    @org.python.Attribute()
    public static org.python.Object EX_OSERR;
    @org.python.Attribute()
    public static org.python.Object EX_OSFILE;
    @org.python.Attribute()
    public static org.python.Object EX_PROTOCOL;
    @org.python.Attribute()
    public static org.python.Object EX_SOFTWARE;
    @org.python.Attribute()
    public static org.python.Object EX_TEMPFAIL;
    @org.python.Attribute()
    public static org.python.Object EX_UNAVAILABLE;
    @org.python.Attribute()
    public static org.python.Object EX_USAGE;
    @org.python.Attribute()
    public static org.python.Object F_LOCK;
    @org.python.Attribute()
    public static org.python.Object F_OK;
    @org.python.Attribute()
    public static org.python.Object F_TEST;
    @org.python.Attribute()
    public static org.python.Object F_TLOCK;
    @org.python.Attribute()
    public static org.python.Object F_ULOCK;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object MutableMapping() {
        throw new org.python.exceptions.NotImplementedError("'MutableMapping' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object NGROUPS_MAX;
    @org.python.Attribute()
    public static org.python.Object O_ACCMODE;
    @org.python.Attribute()
    public static org.python.Object O_APPEND;
    @org.python.Attribute()
    public static org.python.Object O_ASYNC;
    @org.python.Attribute()
    public static org.python.Object O_CLOEXEC;
    @org.python.Attribute()
    public static org.python.Object O_CREAT;
    @org.python.Attribute()
    public static org.python.Object O_DIRECTORY;
    @org.python.Attribute()
    public static org.python.Object O_DSYNC;
    @org.python.Attribute()
    public static org.python.Object O_EXCL;
    @org.python.Attribute()
    public static org.python.Object O_EXLOCK;
    @org.python.Attribute()
    public static org.python.Object O_NDELAY;
    @org.python.Attribute()
    public static org.python.Object O_NOCTTY;
    @org.python.Attribute()
    public static org.python.Object O_NOFOLLOW;
    @org.python.Attribute()
    public static org.python.Object O_NONBLOCK;
    @org.python.Attribute()
    public static org.python.Object O_RDONLY;
    @org.python.Attribute()
    public static org.python.Object O_RDWR;
    @org.python.Attribute()
    public static org.python.Object O_SHLOCK;
    @org.python.Attribute()
    public static org.python.Object O_SYNC;
    @org.python.Attribute()
    public static org.python.Object O_TRUNC;
    @org.python.Attribute()
    public static org.python.Object O_WRONLY;
    @org.python.Attribute()
    public static org.python.Object PRIO_PGRP;
    @org.python.Attribute()
    public static org.python.Object PRIO_PROCESS;
    @org.python.Attribute()
    public static org.python.Object PRIO_USER;
    @org.python.Attribute()
    public static org.python.Object P_ALL;
    @org.python.Attribute()
    public static org.python.Object P_NOWAIT;
    @org.python.Attribute()
    public static org.python.Object P_NOWAITO;
    @org.python.Attribute()
    public static org.python.Object P_PGID;
    @org.python.Attribute()
    public static org.python.Object P_PID;
    @org.python.Attribute()
    public static org.python.Object P_WAIT;
    @org.python.Attribute()
    public static org.python.Object RTLD_GLOBAL;
    @org.python.Attribute()
    public static org.python.Object RTLD_LAZY;
    @org.python.Attribute()
    public static org.python.Object RTLD_LOCAL;
    @org.python.Attribute()
    public static org.python.Object RTLD_NODELETE;
    @org.python.Attribute()
    public static org.python.Object RTLD_NOLOAD;
    @org.python.Attribute()
    public static org.python.Object RTLD_NOW;
    @org.python.Attribute()
    public static org.python.Object R_OK;
    @org.python.Attribute()
    public static org.python.Object SCHED_FIFO;
    @org.python.Attribute()
    public static org.python.Object SCHED_OTHER;
    @org.python.Attribute()
    public static org.python.Object SCHED_RR;
    @org.python.Attribute()
    public static org.python.Object SEEK_CUR;
    @org.python.Attribute()
    public static org.python.Object SEEK_END;
    @org.python.Attribute()
    public static org.python.Object SEEK_SET;
    @org.python.Attribute()
    public static org.python.Object ST_NOSUID;
    @org.python.Attribute()
    public static org.python.Object ST_RDONLY;
    @org.python.Attribute()
    public static org.python.Object TMP_MAX;
    @org.python.Attribute()
    public static org.python.Object WCONTINUED;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object WCOREDUMP() {
        throw new org.python.exceptions.NotImplementedError("'WCOREDUMP' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object WEXITED;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object WEXITSTATUS() {
        throw new org.python.exceptions.NotImplementedError("'WEXITSTATUS' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object WIFCONTINUED() {
        throw new org.python.exceptions.NotImplementedError("'WIFCONTINUED' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object WIFEXITED() {
        throw new org.python.exceptions.NotImplementedError("'WIFEXITED' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object WIFSIGNALED() {
        throw new org.python.exceptions.NotImplementedError("'WIFSIGNALED' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object WIFSTOPPED() {
        throw new org.python.exceptions.NotImplementedError("'WIFSTOPPED' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object WNOHANG;
    @org.python.Attribute()
    public static org.python.Object WNOWAIT;
    @org.python.Attribute()
    public static org.python.Object WSTOPPED;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object WSTOPSIG() {
        throw new org.python.exceptions.NotImplementedError("'WSTOPSIG' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object WTERMSIG() {
        throw new org.python.exceptions.NotImplementedError("'WTERMSIG' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object WUNTRACED;
    @org.python.Attribute()
    public static org.python.Object W_OK;
    @org.python.Attribute()
    public static org.python.Object X_OK;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _Environ() {
        throw new org.python.exceptions.NotImplementedError("'_Environ' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object __all__;

    // @org.python.Attribute()
    // public static org.python.Object __builtins__;
    @org.python.Attribute()
    public static org.python.Object __cached__ = org.python.types.NoneType.NONE;  // TODO;
    @org.python.Attribute()
    public static org.python.Object __file__ = new org.python.types.Str("python/common/python/os.java");
    @org.python.Attribute()
    public static org.python.Object __loader__ = org.python.types.NoneType.NONE;  // TODO
    @org.python.Attribute()
    public static org.python.Object __name__ = new org.python.types.Str("os");
    @org.python.Attribute()
    public static org.python.Object __package__ = new org.python.types.Str("");
    @org.python.Attribute()
    public static org.python.Object __spec__ = org.python.types.NoneType.NONE;  // TODO

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _execvpe() {
        throw new org.python.exceptions.NotImplementedError("'_execvpe' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _exists() {
        throw new org.python.exceptions.NotImplementedError("'_exists' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _exit() {
        throw new org.python.exceptions.NotImplementedError("'_exit' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _get_exports_list() {
        throw new org.python.exceptions.NotImplementedError("'_get_exports_list' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _putenv() {
        throw new org.python.exceptions.NotImplementedError("'_putenv' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _spawnvef() {
        throw new org.python.exceptions.NotImplementedError("'_spawnvef' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _unsetenv() {
        throw new org.python.exceptions.NotImplementedError("'_unsetenv' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _wrap_close() {
        throw new org.python.exceptions.NotImplementedError("'_wrap_close' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object abort() {
        throw new org.python.exceptions.NotImplementedError("'abort' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object access() {
        throw new org.python.exceptions.NotImplementedError("'access' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object altsep;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object chdir() {
        throw new org.python.exceptions.NotImplementedError("'chdir' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object chflags() {
        throw new org.python.exceptions.NotImplementedError("'chflags' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object chmod() {
        throw new org.python.exceptions.NotImplementedError("'chmod' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object chown() {
        throw new org.python.exceptions.NotImplementedError("'chown' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object chroot() {
        throw new org.python.exceptions.NotImplementedError("'chroot' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object close() {
        throw new org.python.exceptions.NotImplementedError("'close' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object closerange() {
        throw new org.python.exceptions.NotImplementedError("'closerange' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object confstr() {
        throw new org.python.exceptions.NotImplementedError("'confstr' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object confstr_names;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object cpu_count() {
        throw new org.python.exceptions.NotImplementedError("'cpu_count' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object ctermid() {
        throw new org.python.exceptions.NotImplementedError("'ctermid' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object curdir;
    @org.python.Attribute()
    public static org.python.Object defpath;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object device_encoding() {
        throw new org.python.exceptions.NotImplementedError("'device_encoding' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object devnull;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object dup() {
        throw new org.python.exceptions.NotImplementedError("'dup' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object dup2() {
        throw new org.python.exceptions.NotImplementedError("'dup2' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object environ;
    @org.python.Attribute()
    public static org.python.Object environb;
    @org.python.Attribute()
    public static org.python.Object errno;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object error() {
        throw new org.python.exceptions.NotImplementedError("'error' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object execl() {
        throw new org.python.exceptions.NotImplementedError("'execl' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object execle() {
        throw new org.python.exceptions.NotImplementedError("'execle' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object execlp() {
        throw new org.python.exceptions.NotImplementedError("'execlp' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object execlpe() {
        throw new org.python.exceptions.NotImplementedError("'execlpe' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object execv() {
        throw new org.python.exceptions.NotImplementedError("'execv' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object execve() {
        throw new org.python.exceptions.NotImplementedError("'execve' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object execvp() {
        throw new org.python.exceptions.NotImplementedError("'execvp' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object execvpe() {
        throw new org.python.exceptions.NotImplementedError("'execvpe' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object extsep;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object fchdir() {
        throw new org.python.exceptions.NotImplementedError("'fchdir' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object fchmod() {
        throw new org.python.exceptions.NotImplementedError("'fchmod' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object fchown() {
        throw new org.python.exceptions.NotImplementedError("'fchown' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object fdopen() {
        throw new org.python.exceptions.NotImplementedError("'fdopen' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object fork() {
        throw new org.python.exceptions.NotImplementedError("'fork' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object forkpty() {
        throw new org.python.exceptions.NotImplementedError("'forkpty' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object fpathconf() {
        throw new org.python.exceptions.NotImplementedError("'fpathconf' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object fsdecode() {
        throw new org.python.exceptions.NotImplementedError("'fsdecode' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object fsencode() {
        throw new org.python.exceptions.NotImplementedError("'fsencode' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object fstat() {
        throw new org.python.exceptions.NotImplementedError("'fstat' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object fstatvfs() {
        throw new org.python.exceptions.NotImplementedError("'fstatvfs' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object fsync() {
        throw new org.python.exceptions.NotImplementedError("'fsync' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object ftruncate() {
        throw new org.python.exceptions.NotImplementedError("'ftruncate' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object get_exec_path() {
        throw new org.python.exceptions.NotImplementedError("'get_exec_path' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object get_inheritable() {
        throw new org.python.exceptions.NotImplementedError("'get_inheritable' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object get_terminal_size() {
        throw new org.python.exceptions.NotImplementedError("'get_terminal_size' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getcwd() {
        throw new org.python.exceptions.NotImplementedError("'getcwd' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getcwdb() {
        throw new org.python.exceptions.NotImplementedError("'getcwdb' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getegid() {
        throw new org.python.exceptions.NotImplementedError("'getegid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Get an environment variable, return None if it doesn't exist.\n" +
                      "The optional second argument can specify an alternate default.\n" +
                      "key, default and the result are str.",
            args = {"key"},
            default_args = {"default"}
    )
    public static org.python.Object getenv(org.python.Object key, org.python.Object defaultVal) {
        if (!(key instanceof org.python.types.Str)) {
            throw new org.python.exceptions.TypeError("str expected, not " + key.typeName());
        }
        if (defaultVal == null) {
            defaultVal = org.python.types.NoneType.NONE;
        }
        String value = System.getenv(((org.python.types.Str) key).value);
        if (value != null) {
            return new org.python.types.Str(value);
        }
        return defaultVal;
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getenvb() {
        throw new org.python.exceptions.NotImplementedError("'getenvb' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object geteuid() {
        throw new org.python.exceptions.NotImplementedError("'geteuid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getgid() {
        throw new org.python.exceptions.NotImplementedError("'getgid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getgrouplist() {
        throw new org.python.exceptions.NotImplementedError("'getgrouplist' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getgroups() {
        throw new org.python.exceptions.NotImplementedError("'getgroups' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getloadavg() {
        throw new org.python.exceptions.NotImplementedError("'getloadavg' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getlogin() {
        throw new org.python.exceptions.NotImplementedError("'getlogin' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getpgid() {
        throw new org.python.exceptions.NotImplementedError("'getpgid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getpgrp() {
        throw new org.python.exceptions.NotImplementedError("'getpgrp' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getpid() {
        throw new org.python.exceptions.NotImplementedError("'getpid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getppid() {
        throw new org.python.exceptions.NotImplementedError("'getppid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getpriority() {
        throw new org.python.exceptions.NotImplementedError("'getpriority' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getsid() {
        throw new org.python.exceptions.NotImplementedError("'getsid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object getuid() {
        throw new org.python.exceptions.NotImplementedError("'getuid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object initgroups() {
        throw new org.python.exceptions.NotImplementedError("'initgroups' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object isatty() {
        throw new org.python.exceptions.NotImplementedError("'isatty' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object kill() {
        throw new org.python.exceptions.NotImplementedError("'kill' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object killpg() {
        throw new org.python.exceptions.NotImplementedError("'killpg' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object lchflags() {
        throw new org.python.exceptions.NotImplementedError("'lchflags' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object lchmod() {
        throw new org.python.exceptions.NotImplementedError("'lchmod' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object lchown() {
        throw new org.python.exceptions.NotImplementedError("'lchown' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object linesep;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object link() {
        throw new org.python.exceptions.NotImplementedError("'link' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object listdir() {
        throw new org.python.exceptions.NotImplementedError("'listdir' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object lockf() {
        throw new org.python.exceptions.NotImplementedError("'lockf' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object lseek() {
        throw new org.python.exceptions.NotImplementedError("'lseek' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object lstat() {
        throw new org.python.exceptions.NotImplementedError("'lstat' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object major() {
        throw new org.python.exceptions.NotImplementedError("'major' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object makedev() {
        throw new org.python.exceptions.NotImplementedError("'makedev' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object makedirs() {
        throw new org.python.exceptions.NotImplementedError("'makedirs' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object minor() {
        throw new org.python.exceptions.NotImplementedError("'minor' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object mkdir() {
        throw new org.python.exceptions.NotImplementedError("'mkdir' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object mkfifo() {
        throw new org.python.exceptions.NotImplementedError("'mkfifo' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object mknod() {
        throw new org.python.exceptions.NotImplementedError("'mknod' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object name;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object nice() {
        throw new org.python.exceptions.NotImplementedError("'nice' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object open() {
        throw new org.python.exceptions.NotImplementedError("'open' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object openpty() {
        throw new org.python.exceptions.NotImplementedError("'openpty' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object pardir;
    @org.python.Attribute()
    public static org.python.Object path;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object pathconf() {
        throw new org.python.exceptions.NotImplementedError("'pathconf' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object pathconf_names;
    @org.python.Attribute()
    public static org.python.Object pathsep;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object pipe() {
        throw new org.python.exceptions.NotImplementedError("'pipe' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object popen() {
        throw new org.python.exceptions.NotImplementedError("'popen' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object pread() {
        throw new org.python.exceptions.NotImplementedError("'pread' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object putenv() {
        throw new org.python.exceptions.NotImplementedError("'putenv' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object pwrite() {
        throw new org.python.exceptions.NotImplementedError("'pwrite' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object read() {
        throw new org.python.exceptions.NotImplementedError("'read' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object readlink() {
        throw new org.python.exceptions.NotImplementedError("'readlink' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object readv() {
        throw new org.python.exceptions.NotImplementedError("'readv' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object remove() {
        throw new org.python.exceptions.NotImplementedError("'remove' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object removedirs() {
        throw new org.python.exceptions.NotImplementedError("'removedirs' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object rename() {
        throw new org.python.exceptions.NotImplementedError("'rename' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object renames() {
        throw new org.python.exceptions.NotImplementedError("'renames' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object replace() {
        throw new org.python.exceptions.NotImplementedError("'replace' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object rmdir() {
        throw new org.python.exceptions.NotImplementedError("'rmdir' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object sched_get_priority_max() {
        throw new org.python.exceptions.NotImplementedError("'sched_get_priority_max' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object sched_get_priority_min() {
        throw new org.python.exceptions.NotImplementedError("'sched_get_priority_min' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object sched_yield() {
        throw new org.python.exceptions.NotImplementedError("'sched_yield' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object sendfile() {
        throw new org.python.exceptions.NotImplementedError("'sendfile' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object sep;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object set_inheritable() {
        throw new org.python.exceptions.NotImplementedError("'set_inheritable' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setegid() {
        throw new org.python.exceptions.NotImplementedError("'setegid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object seteuid() {
        throw new org.python.exceptions.NotImplementedError("'seteuid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setgid() {
        throw new org.python.exceptions.NotImplementedError("'setgid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setgroups() {
        throw new org.python.exceptions.NotImplementedError("'setgroups' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setpgid() {
        throw new org.python.exceptions.NotImplementedError("'setpgid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setpgrp() {
        throw new org.python.exceptions.NotImplementedError("'setpgrp' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setpriority() {
        throw new org.python.exceptions.NotImplementedError("'setpriority' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setregid() {
        throw new org.python.exceptions.NotImplementedError("'setregid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setreuid() {
        throw new org.python.exceptions.NotImplementedError("'setreuid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setsid() {
        throw new org.python.exceptions.NotImplementedError("'setsid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object setuid() {
        throw new org.python.exceptions.NotImplementedError("'setuid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object spawnl() {
        throw new org.python.exceptions.NotImplementedError("'spawnl' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object spawnle() {
        throw new org.python.exceptions.NotImplementedError("'spawnle' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object spawnlp() {
        throw new org.python.exceptions.NotImplementedError("'spawnlp' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object spawnlpe() {
        throw new org.python.exceptions.NotImplementedError("'spawnlpe' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object spawnv() {
        throw new org.python.exceptions.NotImplementedError("'spawnv' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object spawnve() {
        throw new org.python.exceptions.NotImplementedError("'spawnve' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object spawnvp() {
        throw new org.python.exceptions.NotImplementedError("'spawnvp' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object spawnvpe() {
        throw new org.python.exceptions.NotImplementedError("'spawnvpe' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object st;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object stat() {
        throw new org.python.exceptions.NotImplementedError("'stat' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object stat_float_times() {
        throw new org.python.exceptions.NotImplementedError("'stat_float_times' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object stat_result() {
        throw new org.python.exceptions.NotImplementedError("'stat_result' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object statvfs() {
        throw new org.python.exceptions.NotImplementedError("'statvfs' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object statvfs_result() {
        throw new org.python.exceptions.NotImplementedError("'statvfs_result' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object strerror() {
        throw new org.python.exceptions.NotImplementedError("'strerror' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object supports_bytes_environ;
    @org.python.Attribute()
    public static org.python.Object supports_dir_fd;
    @org.python.Attribute()
    public static org.python.Object supports_effective_ids;
    @org.python.Attribute()
    public static org.python.Object supports_fd;
    @org.python.Attribute()
    public static org.python.Object supports_follow_symlinks;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object symlink() {
        throw new org.python.exceptions.NotImplementedError("'symlink' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object sync() {
        throw new org.python.exceptions.NotImplementedError("'sync' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object sys;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object sysconf() {
        throw new org.python.exceptions.NotImplementedError("'sysconf' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object sysconf_names;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object system() {
        throw new org.python.exceptions.NotImplementedError("'system' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object tcgetpgrp() {
        throw new org.python.exceptions.NotImplementedError("'tcgetpgrp' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object tcsetpgrp() {
        throw new org.python.exceptions.NotImplementedError("'tcsetpgrp' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object terminal_size() {
        throw new org.python.exceptions.NotImplementedError("'terminal_size' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object times() {
        throw new org.python.exceptions.NotImplementedError("'times' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object times_result() {
        throw new org.python.exceptions.NotImplementedError("'times_result' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object truncate() {
        throw new org.python.exceptions.NotImplementedError("'truncate' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object ttyname() {
        throw new org.python.exceptions.NotImplementedError("'ttyname' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object umask() {
        throw new org.python.exceptions.NotImplementedError("'umask' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object uname() {
        throw new org.python.exceptions.NotImplementedError("'uname' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object uname_result() {
        throw new org.python.exceptions.NotImplementedError("'uname_result' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object unlink() {
        throw new org.python.exceptions.NotImplementedError("'unlink' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object unsetenv() {
        throw new org.python.exceptions.NotImplementedError("'unsetenv' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object urandom() {
        throw new org.python.exceptions.NotImplementedError("'urandom' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object utime() {
        throw new org.python.exceptions.NotImplementedError("'utime' has not been implemented");
    }

    @org.python.Method(
            __doc__ = "",
            name = "wait"
    )
    public static org.python.Object wait_() {
        throw new org.python.exceptions.NotImplementedError("'wait' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object wait3() {
        throw new org.python.exceptions.NotImplementedError("'wait3' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object wait4() {
        throw new org.python.exceptions.NotImplementedError("'wait4' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object waitpid() {
        throw new org.python.exceptions.NotImplementedError("'waitpid' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object walk() {
        throw new org.python.exceptions.NotImplementedError("'walk' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object write() {
        throw new org.python.exceptions.NotImplementedError("'write' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object writev() {
        throw new org.python.exceptions.NotImplementedError("'writev' has not been implemented");
    }
}
