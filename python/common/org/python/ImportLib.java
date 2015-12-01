package org.python;

public class ImportLib {
    public static java.util.Map<java.lang.String, org.python.types.Module> modules = new java.util.HashMap<java.lang.String, org.python.types.Module>();

    /**
     * Factory method to obtain Python classes from their Java counterparts
     */
    public static org.python.types.Module __import__(java.lang.String python_name, java.lang.String [] from_list, int level) {
        // Create an array containing the module path.
        boolean native_import;
        java.lang.String [] path = python_name.split("\\.");
        java.lang.StringBuilder java_name = new java.lang.StringBuilder();
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
            throw new org.python.exceptions.ImportError("Cannot import native Java classes (yet!)");
        } else {
            java_name.append("python");
            native_import = false;
        }

        org.python.types.Module python_module = null;
        org.python.types.Module parent_module = null;
        org.python.types.Module return_module = null;

        // Iterate down the full dotted path, making sure that each module
        // along the way has been imported.
        for (java.lang.String name: path) {
            if (java_name.length() > 0) {
                java_name.append("/");
            }
            java_name.append(name);

            python_module = modules.get(java_name.toString());
            if (python_module == null) {
                try {
                    python_module = importModule(java_name.toString());
                } catch (java.lang.ClassNotFoundException e) {
                    throw new org.python.exceptions.ImportError("No module named '" + python_name + "'");
                }

                // If we are multiple steps into an import chain, tell the
                // parent module of this new module.
                if (parent_module != null) {
                    parent_module.__setattr__(name, python_module);
                }
            }

            // Remember the very first module we resolve, because this is the one that
            // will be put into the namespace as an import product if there is no from_list.
            if (return_module == null) {
                return_module = python_module;
            }

            // The module just imported will be the parent of the next import
            // in the chain.
            parent_module = python_module;
        }

        if (from_list != null) {
            // from_list provided; import all the provided symbols,
            // unless the symbol is *, in which case we know it exists.
            return_module = python_module;
            java_name.append("/");
            for (java.lang.String name: from_list) {
                if (!name.equals("*")) {
                    try {
                        python_module = importModule(java_name.toString() + name);
                        parent_module.__setattr__(name, python_module);
                    } catch (java.lang.ClassNotFoundException e) {
                        // `name` doesn't exist as a submodule; it might be
                        // an exportable symbol in the parent module.
                        try {
                            parent_module.__getattribute__(name);
                        } catch (org.python.exceptions.NameError ne) {
                            throw new org.python.exceptions.ImportError("No module named '" + python_name + "'");
                        }
                    }
                }
            }
        }
        return return_module;
    }

    private static org.python.types.Module importModule(java.lang.String java_name)
            throws java.lang.ClassNotFoundException {
        org.python.types.Module python_module;
        try {
            java.lang.Class java_class = java.lang.Class.forName(java_name.toString().replace("/", "."));
            java.lang.reflect.Constructor constructor = java_class.getConstructor();
            python_module = (org.python.types.Module) constructor.newInstance();
            modules.put(java_name.toString(), python_module);
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to constructor for module " + java_name);
        } catch (java.lang.NoSuchMethodException e) {
            throw new org.python.exceptions.RuntimeError("Couldn't find constructor for module " + java_name);
        } catch (java.lang.reflect.InvocationTargetException e) {
            try {
                // If the Java method raised an Python exception, re-raise that
                // exception as-is. If it wasn't a Python exception, wrap it
                // as one and continue.
                throw (org.python.exceptions.BaseException) e.getCause();
            } catch (ClassCastException java_e) {
                throw new org.python.exceptions.RuntimeError(e.getCause().getMessage());
            }
        } catch (java.lang.InstantiationException e) {
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
    public static java.util.Map importAll(org.python.types.Module module_instance) {
        java.util.Map<java.lang.String, org.python.Object> exports = new java.util.HashMap<java.lang.String, org.python.Object>();
        org.python.types.Type module = org.python.types.Type.pythonType(module_instance.getClass());

        org.python.Object all_obj = module.attrs.get("__all__");
        if (all_obj == null) {
            for (java.lang.String name: module.attrs.keySet()) {
                if (!name.startsWith("_")) {
                    exports.put(name, module.attrs.get(name));
                }
            }
        } else {
            java.util.List args = new java.util.ArrayList();
            args.add(all_obj);
            org.python.types.List all = org.Python.list(args, null);

            for (org.python.Object name: all.value) {
                exports.put(name.toString(), module.attrs.get(name.toString()));
            }
        }
        // System.out.println("exports" +  exports);

        return exports;
    }
}