package python.importlib;

@org.python.Module(
        __doc__ = "A pure Python implementation of import."
)
public class __init__ extends org.python.types.Module {
    @org.python.Method(
            __doc__ = "Create and return a new object.  See help(type) for accurate signature."
    )
    public org.python.Object __new__(org.python.Object klass) {
        org.python.types.Type cls = (org.python.types.Type) super.__new__(klass);

        return cls;
    }

    @org.python.Attribute()
    public static org.python.Object _RELOADING;
    @org.python.Attribute()
    public static org.python.Object __all__;

    // @org.python.Attribute()
    // public static org.python.Object __builtins__;
    @org.python.Attribute()
    public static org.python.Object __cached__;
    @org.python.Attribute
    public static org.python.Object __file__ = new org.python.types.Str("python/common/python/importlib/__init__.java");

    @org.python.Method(
            __doc__ = "",
            args = {"python_name"},
            default_args = {"globals", "locals", "from_list", "level"}
    )
    public static org.python.Object __import__(org.python.Object python_name, org.python.Object globals, org.python.Object locals, org.python.Object from_list, org.python.Object level) {
        // return org.python.ImportLib.__import__(java.lang.String python_name, java.lang.String [] from_list, int level)
        throw new org.python.exceptions.NotImplementedError("'__import__' has not been implemented");
    }

    @org.python.Attribute
    public static org.python.Object __loader__ = org.python.types.NoneType.NONE;  // TODO
    @org.python.Attribute
    public static org.python.Object __name__ = new org.python.types.Str("importlib");
    @org.python.Attribute
    public static org.python.Object __package__ = new org.python.types.Str("");
    @org.python.Attribute()
    public static org.python.Object __path__;
    @org.python.Attribute
    public static org.python.Object __spec__ = org.python.types.NoneType.NONE;  // TODO
    @org.python.Attribute()
    public static org.python.Object _bootstrap;
    @org.python.Attribute()
    public static org.python.Object _imp;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _r_long() {
        throw new org.python.exceptions.NotImplementedError("'_r_long' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object _w_long() {
        throw new org.python.exceptions.NotImplementedError("'_w_long' has not been implemented");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object find_loader() {
        throw new org.python.exceptions.NotImplementedError("'find_loader' has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Import a module.\n" +
                    "\n" +
                    "The 'pkg' argument is required when performing a relative import. It\n" +
                    "specifies the package to use as the anchor point from which to resolve the\n" +
                    "relative import to an absolute import.\n",
            args = {"name"},
            default_args = {"pkg"}
    )
    public static org.python.Object import_module(org.python.Object name, org.python.Object pkg) {
        if (name == null) {
            throw new org.python.exceptions.TypeError("import_module() missing 1 required positional argument: 'name'");
        }

        if (pkg == null) {
            try {
                return org.python.ImportLib.__import__((java.lang.String) name.toJava(), null, null, null, 0);
            } catch (ClassCastException cce) {
                throw new org.python.exceptions.AttributeError("'" + name.typeName() + "' object has no attribute 'startswith'");
            }
        } else {
            throw new org.python.exceptions.NotImplementedError("import_module() with package has not been implemented");
        }
    }

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object invalidate_caches() {
        throw new org.python.exceptions.NotImplementedError("'invalidate_caches' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object machinery;

    @org.python.Method(
            __doc__ = ""
    )
    public static org.python.Object reload() {
        throw new org.python.exceptions.NotImplementedError("'reload' has not been implemented");
    }

    @org.python.Attribute()
    public static org.python.Object sys;
    @org.python.Attribute()
    public static org.python.Object types;
    @org.python.Attribute()
    public static org.python.Object util;
    @org.python.Attribute()
    public static org.python.Object warnings;
}
