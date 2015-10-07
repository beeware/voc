package python;


public class platform extends org.python.types.Module {
    public static PythonPlatform impl;

    static {
        java.util.Properties prop = System.getProperties();
        java.lang.String vendor = prop.getProperty("java.vendor");
        java.lang.String platform_class_name;
        java.lang.Class platform_class;

        if (vendor.equals("Oracle Corporation")) {
            platform_class_name = "python.JavaPlatform";
        } else if (vendor.equals("The Android Project")) {
            platform_class_name = "python.AndroidPlatform";
        } else {
            throw new org.python.exceptions.RuntimeError("Unknown platform vendor '" + vendor + "'");
        }

        try {
            platform_class = Class.forName(platform_class_name);
            impl = (PythonPlatform) platform_class.getConstructor().newInstance();
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
}
