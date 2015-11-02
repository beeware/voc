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

    public static org.python.types.Module getModule(java.lang.String java_name) {
        return modules.get(java_name);
    }

}