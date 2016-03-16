
package python.testdaemon;

import java.io.File;
import java.lang.reflect.Method;
import java.net.URL;
import java.net.URLClassLoader;
import java.net.MalformedURLException;
import java.util.Arrays;
import java.util.Scanner;

public class TestDaemon {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = "";

        URL url;
        try {
            // need the trailing slash so that the ClassLoader knows it's a
            // directory instead of a jar file
            url = new URL("file:" + System.getProperty("user.dir") + "/temp/");
        } catch (MalformedURLException e) {
            e.printStackTrace();
            return;
        }
        URL[] urls = new URL[] { url };

        input = sc.nextLine();

        while (!input.equals("exit")) {
            // separate out the params
            String[] parts = input.split(" ");
            String className = parts[0];
            String[] inputArgs = Arrays.copyOfRange(parts, 1, parts.length);

            // get a fresh ClassLoader so that we pick up the latest class files
            ClassLoader newClassLoader = new URLClassLoader(urls);

            try {
                // don't leave this as Class type as that's raw and compiler
                // is required to generate a warning. add generic type <?>.
                Class<?> klass = newClassLoader.loadClass(className);

                // retrieve the standard main(String[] args)
                Method method = klass.getMethod("main", String[].class);

                // first parameter can be null since method is static
                // cast second parameter to Object to make it a varargs call
                method.invoke(null, (Object) inputArgs);
            } catch (ReflectiveOperationException e) {
                // ClassNotFound, NoSuchMethod, IllegalAccess Exceptions
                e.printStackTrace();
            } catch (ExceptionInInitializerError e) {
                // unwrap the Error to get the org.python.exceptions.* thing
                System.err.print("Exception in thread \"main\" ");
                e.printStackTrace();
            } catch (Throwable e) {
                // NoSuchMethodError
                e.printStackTrace();
            } finally {
                System.out.println(".");
            }

            input = sc.nextLine();
        }

    }
}
