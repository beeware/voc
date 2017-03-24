package python.testdaemon;

import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;
import java.security.Permission;
import java.util.Arrays;
import java.util.Scanner;

public class TestDaemon {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = "";

        URL voc;
        URL runtime1;
        URL runtime2;
        try {
            // load the voc jar here so that they can see the runtime classes
            voc = new URL("file:" + System.getProperty("user.dir") + "/dist/python-java-support.jar");
            // need the trailing slash so that the ClassLoader knows it's a
            // directory instead of a jar file
            runtime1 = new URL("file:" + System.getProperty("user.dir") + "/temp/");
            runtime2 = new URL("file:" + System.getProperty("user.dir") + "/java/");
        } catch (MalformedURLException e) {
            e.printStackTrace();
            return;
        }
        ClassLoader vocClassLoader = new URLClassLoader(new URL[]{voc});
        URL[] runtimeURLs = new URL[]{runtime1, runtime2};

        System.setSecurityManager(new NoExitSecurityManager());

        input = sc.nextLine();

        while (!input.equals("exit")) {
            // separate out the params
            String[] parts = input.split(" ");
            String className = parts[0];
            String[] inputArgs = Arrays.copyOfRange(parts, 1, parts.length);

            // get a fresh ClassLoader so that we pick up the latest class files
            ClassLoader runtimeClassLoader = new URLClassLoader(runtimeURLs);

            ClassLoader joinedClassLoader = new JoinClassLoader(
                    TestDaemon.class.getClassLoader(),
                    vocClassLoader,
                    runtimeClassLoader);

            Thread.currentThread().setContextClassLoader(joinedClassLoader);

            try {
                // don't leave this as Class type as that's raw and compiler
                // is required to generate a warning. add generic type <?>.
                Class<?> klass = joinedClassLoader.loadClass(className);

                // retrieve the standard main(String[] args)
                Method method = klass.getMethod("main", String[].class);

                // first parameter can be null since method is static
                // cast second parameter to Object to make it a varargs call
                method.invoke(null, (Object) inputArgs);
            } catch (ReflectiveOperationException e) {
                // InvocationTargetException may contain an ExitException
                if (!(e instanceof InvocationTargetException) || e.getCause() == null
                        || !(e.getCause() instanceof ExitException)) {
                    // ClassNotFound, NoSuchMethod, IllegalAccess Exceptions
                    // This was _not_ a case of System.exit() being invoked somewhere
                    // and being caught due to the custom SecurityManager.
                    e.printStackTrace();
                }
            } catch (ExceptionInInitializerError e) {
                if (e.getCause() == null || !(e.getCause() instanceof ExitException)) {
                    // This was _not_ a case of System.exit() being invoked somewhere
                    // and being caught due to the custom SecurityManager.
                    e.printStackTrace();
                }
            } catch (Throwable e) {
                // NoSuchMethodError
                e.printStackTrace();
            } finally {
                // always cleanup the module cache in ImportLib
                try {
                    Class<?> importlib = joinedClassLoader.loadClass("python.sys.__init__");
                    Field importlib_modules = importlib.getDeclaredField("modules");
                    importlib_modules.set(null, new org.python.types.Dict());
                } catch (ReflectiveOperationException e) {
                    // ClassNotFound, NoSuchMethod, IllegalAccess Exceptions
                }

                System.out.println(".");
            }

            input = sc.nextLine();
        }
    }

    private static class NoExitSecurityManager extends SecurityManager {
        @Override
        public void checkPermission(Permission perm) {
        }

        @Override
        public void checkPermission(Permission perm, Object context) {
        }

        // System.exit() checks this
        @Override
        public void checkExit(int status) {
            // super.checkExit(status);
            throw new ExitException(Integer.toString(status));
        }
    }

    // This needs to be RuntimeException as SecurityManager.checkExit() can't
    // throw a checked exception
    private static class ExitException extends RuntimeException {
        public ExitException(String status) {
            super(status);
        }
    }
}
