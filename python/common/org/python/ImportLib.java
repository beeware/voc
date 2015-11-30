package org.python;

public class ImportLib {
    public static java.util.Map<java.lang.String, org.python.types.Module> modules = new java.util.HashMap<java.lang.String, org.python.types.Module>();

    /**
     * Factory method to obtain Python classes from their Java counterparts
     */
    public static org.python.types.Module __import__(java.lang.String python_name, int level) {
        // Create an array containing the module path.
        java.lang.String java_name;

        // If the package name isn't clearly identifiable as a java package path,
        // put it in the python namespace.
        if (       python_name.startsWith("java.")
                || python_name.startsWith("org.")
                || python_name.startsWith("com.")
                || python_name.startsWith("edu.")
                || python_name.startsWith("net.")
                || python_name.startsWith("android.")) {
            throw new org.python.exceptions.ImportError("Cannot import native Java classes (yet!)");
        } else {
            java_name = "python." + python_name;
        }

        org.python.types.Module python_module = modules.get(java_name);
        if (python_module == null) {
            try {
                java.lang.Class java_class = java.lang.Class.forName(java_name);
                java.lang.reflect.Constructor constructor = java_class.getConstructor();
                python_module = (org.python.types.Module) constructor.newInstance();
                modules.put(java_name, python_module);
            } catch (java.lang.ClassNotFoundException e) {
                throw new org.python.exceptions.ImportError("No module named '" + python_name + "'");
            } catch (java.lang.IllegalAccessException e) {
                throw new org.python.exceptions.RuntimeError("Illegal access to constructor for module " + python_name);
            } catch (java.lang.NoSuchMethodException e) {
                throw new org.python.exceptions.RuntimeError("Couldn't find constructor for module " + python_name);
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