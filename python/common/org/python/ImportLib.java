package org.python;

public class ImportLib {
    /**
     * Factory method to obtain Python classes from their Java counterparts
     */
    public static org.python.types.Module __import__(java.lang.String python_name, java.lang.String [] from_list, int level) {
        // Create an array containing the module path.
        boolean native_import;
        java.lang.String [] path = python_name.split("\\.");
        java.lang.StringBuilder import_name = new java.lang.StringBuilder();
        // If the package name isn't clearly identifiable as a java package path,
        // put it in the python namespace.
        if (       path[0].equals("java")
                || path[0].equals("javax")
                || path[0].equals("org")
                || path[0].equals("com")
                || path[0].equals("edu")
                || path[0].equals("net")
                || path[0].equals("android")) {
            native_import = true;
        } else {
            native_import = false;
        }

        org.python.types.Module python_module = null;
        org.python.types.Module parent_module = null;
        org.python.types.Module return_module = null;

        // Iterate down the full dotted path, making sure that each module
        // along the way has been imported.
        for (java.lang.String name: path) {
            if (import_name.length() > 0) {
                import_name.append(".");
            }
            import_name.append(name);
            java.lang.String mod_name = import_name.toString();

            try {
                // System.out.println("IMPORT " + mod_name);
                python_module = (org.python.types.Module) python.sys.__init__.modules.__getitem__(new org.python.types.Str(mod_name));
            } catch (org.python.exceptions.KeyError ke) {
                try {
                    // System.out.println("handle IMPORT " + mod_name);
                    if (native_import) {
                        python_module = importNativeModule(mod_name);
                    } else {
                        python_module = importPythonModule(mod_name);
                    }
                } catch (java.lang.ClassNotFoundException e) {
                    throw new org.python.exceptions.ImportError("No module named '" + python_name + "'");
                }

                // If we are multiple steps into an import chain, tell the
                // parent module of this new module.
                if (parent_module != null) {
                    parent_module.__setattr__(name.toString(), python_module);
                }
            }

            // Remember the very first module we resolve, because this is the one that
            // will be put into the namespace as an import product if there is no from_list.
            if (return_module == null) {
                return_module = python_module;
            }

            // System.out.println("MODULES: " + python.sys.__init__.modules);
            // The module just imported will be the parent of the next import
            // in the chain.
            parent_module = python_module;
        }

        if (from_list != null) {
            // from_list provided; import all the provided symbols,
            // unless the symbol is *, in which case we know it exists.
            return_module = python_module;
            import_name.append(".");
            for (java.lang.String name: from_list) {
                // System.out.println("IMPORT NAME " + name);
                if (!name.equals("*")) {
                    java.lang.String mod_name = import_name.toString() + name;
                    try {
                        if (native_import) {
                            java.lang.Class java_class = java.lang.Thread.currentThread().getContextClassLoader().loadClass(mod_name);
                            parent_module.__setattr__(name, org.python.java.Type.pythonType(java_class));
                        } else {
                            python_module = importPythonModule(mod_name);
                            parent_module.__setattr__(name, python_module);
                        }
                    } catch (java.lang.ClassNotFoundException e) {
                        // `name` doesn't exist as a submodule; it might be
                        // an exportable symbol in the parent module.
                        try {
                            parent_module.__getattribute__(name);
                        } catch (org.python.exceptions.NameError ne) {
                            python_module = new org.python.java.Module(mod_name);
                            parent_module.__setattr__(name, python_module);
                            python.sys.__init__.modules.__setitem__(new org.python.types.Str(mod_name), python_module);
                        }
                    }
                }
            }
        }
        return return_module;
    }

    private static org.python.types.Module importNativeModule(java.lang.String import_name)
            throws java.lang.ClassNotFoundException {
        org.python.types.Module python_module;
        try {
            java.lang.Class java_class = java.lang.Thread.currentThread().getContextClassLoader().loadClass(import_name);
            python_module = null;
        } catch (java.lang.ClassNotFoundException e) {
            python_module = new org.python.java.Module(import_name);
            python.sys.__init__.modules.__setitem__(new org.python.types.Str(import_name), python_module);
        } finally {
        //     System.out.println("CONSTRUCTOR DONE");
        }
        return python_module;
    }

    private static org.python.types.Module importPythonModule(java.lang.String import_name)
            throws java.lang.ClassNotFoundException {
        org.python.types.Module python_module;
        try {
            // Load and construct an instance of the module class.
            java.lang.Class java_class = java.lang.Thread.currentThread().getContextClassLoader().loadClass("python." + import_name + ".__init__");
            java.lang.reflect.Constructor constructor = java_class.getConstructor();
            python_module = (org.python.types.Module) constructor.newInstance();

            // Store module instance at imported name
            java.lang.String python_name = import_name;
            if (import_name.startsWith("python.")) {
                python_name = import_name.substring(7);
            }
            python.sys.__init__.modules.__setitem__(new org.python.types.Str(python_name), python_module);

            // Initialize module
            java.lang.reflect.Method init = java_class.getMethod("module$import");
            init.invoke(python_module);
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to initialization method for module " + import_name);
        } catch (java.lang.NoSuchMethodException e) {
            throw new org.python.exceptions.RuntimeError("Couldn't find initialization method for module " + import_name);
        } catch (java.lang.reflect.InvocationTargetException e) {
            try {
                e.getTargetException().printStackTrace();
                // If the Java method raised an Python exception, re-raise that
                // exception as-is. If it wasn't a Python exception, wrap it
                // as one and continue.
                throw (org.python.exceptions.BaseException) e.getCause();
            } catch (ClassCastException java_e) {
                throw new org.python.exceptions.RuntimeError(e.getCause().getMessage());
            }
        } catch (java.lang.InstantiationException e) {
            // e.printStackTrace();
            throw new org.python.exceptions.RuntimeError(e.getCause().toString());
        } finally {
        //     System.out.println("CONSTRUCTOR DONE");
        }
        return python_module;
    }

    /**
     * Develop a map of exported symbols for a module.
     *
     * Implements the semantics of "from X import *". Honors the "__all__"
     * attribute if it exists; otherwise, exports all symbols that don't start
     * with an underscore (i.e., all public symbols).
     *
     * @param module_instance the *instance* of the module to interrogate.
     *
     * @return A map of attribute names to Python Objects, representing the
     *         symbols to be exported as part of an "import *" from this
     *         module.
     */
    public static java.util.Map importAll(org.python.types.Module module) {
        java.util.Map<java.lang.String, org.python.Object> exports = new java.util.HashMap<java.lang.String, org.python.Object>();
        org.python.Object all_obj = module.__getattribute_null("__all__");
        if (all_obj == null) {
            for (java.lang.String name: module.__dict__.keySet()) {
                if (!name.startsWith("_")) {
                    exports.put(name, module.__dict__.get(name));
                }
            }
        } else {
            org.python.Iterable iter = all_obj.__iter__();
            try {
                while (true) {
                    java.lang.String name = ((org.python.types.Str) iter.__next__()).value;
                    exports.put(name, module.__dict__.get(name));
                }
            } catch (org.python.exceptions.StopIteration e) {}
        }
        return exports;
    }
}