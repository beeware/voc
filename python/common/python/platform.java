package python;

@org.python.Module(
        __doc__ =
                " This module tries to retrieve as much platform-identifying data as\n" +
                        "    possible. It makes this information available via function APIs.\n" +
                        "\n" +
                        "    If called from the command line, it prints the platform\n" +
                        "    information concatenated as single string to stdout. The output\n" +
                        "    format is useable as part of a filename.\n" +
                        "\n" +
                        "\n" +
                        "\n"
)
public class platform extends org.python.types.Module {
    public static python.PlatformInterface impl;

    static {
        java.util.Properties prop = System.getProperties();
        java.lang.String vendor = prop.getProperty("java.vendor");
        java.lang.String platform_class_name;
        java.lang.Class platform_class;

        if (vendor.equals("Oracle Corporation")) {
            platform_class_name = "python._platform.JavaPlatform";
        } else if (vendor.equals("The Android Project")) {
            platform_class_name = "python._platform.AndroidPlatform";
        } else {
            throw new org.python.exceptions.RuntimeError("Unknown platform vendor '" + vendor + "'");
        }

        try {
            platform_class = java.lang.Class.forName(platform_class_name);
            impl = (python.PlatformInterface) platform_class.getConstructor().newInstance();
        } catch (ClassNotFoundException e) {
            throw new org.python.exceptions.RuntimeError("Unable to find platform '" + platform_class_name + "'");
        } catch (NoSuchMethodException e) {
            throw new org.python.exceptions.RuntimeError("Unable to call constructor for plaform '" + platform_class_name + "'");
        } catch (InstantiationException e) {
            throw new org.python.exceptions.RuntimeError("Unable to instantiate platform '" + platform_class_name + "'");
        } catch (IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Unable to access constructor for platform '" + platform_class_name + "'");
        } catch (java.lang.reflect.InvocationTargetException e) {
            throw new org.python.exceptions.RuntimeError("Unable to invoke constructor for platform '" + platform_class_name + "'");
        }
    }

    // DEV_NULL',
    // _UNIXCONFDIR',
    // __builtins__',
    @org.python.Attribute()
    public static org.python.Object __cached__ = org.python.types.NoneType.NONE;  // TODO;

    // __copyright__',
    @org.python.Attribute()
    public static org.python.Object __file__ = new org.python.types.Str("python/common/python/platform.java");
    @org.python.Attribute()
    public static org.python.Object __loader__ = org.python.types.NoneType.NONE;  // TODO
    @org.python.Attribute()
    public static org.python.Object __name__ = new org.python.types.Str("sys");
    @org.python.Attribute()
    public static org.python.Object __package__ = new org.python.types.Str("");
    @org.python.Attribute()
    public static org.python.Object __spec__ = org.python.types.NoneType.NONE;  // TODO

    // __version__',
    // _default_architecture',
    // _dist_try_harder',
    // _follow_symlinks',
    // _ironpython26_sys_version_parser',
    // _ironpython_sys_version_parser',
    // _java_getprop',
    // _libc_search',
    // _lsb_release_version',
    // _mac_ver_xml',
    // _node',
    // _norm_version',
    // _parse_release_file',
    // _platform',
    // _platform_cache',
    // _pypy_sys_version_parser',
    // _release_filename',
    // _release_version',
    // _supported_dists',
    // _sys_version',
    // _sys_version_cache',
    // _sys_version_parser',
    // _syscmd_file',
    // _syscmd_uname',
    // _syscmd_ver',
    // _uname_cache',
    // _ver_output',
    // _win32_getvalue',
    // architecture',
    // collections',
    // dist',
    // java_ver',
    // libc_ver',
    // linux_distribution',
    // mac_ver',
    // machine',
    // node',
    // os',
    // platform',
    // popen',
    // processor',
    // python_branch',
    // python_build',
    // python_compiler',
    // python_implementation',
    // python_revision',
    // python_version',
    // python_version_tuple',
    // re',
    // release',
    // subprocess',
    // sys',
    // system',
    // system_alias',
    // uname',
    // uname_result',
    // version',
    // win32_ver'
}
