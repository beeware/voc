package python.testdaemon;

import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.nio.ByteBuffer;
import java.util.Collections;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.Map;
import java.util.Vector;

// http://www.source-code.biz/snippets/java/12.htm

/**
 * A class loader that combines multiple class loaders into one.<br>
 * The classes loaded by this class loader are associated with this class loader,
 * i.e. Class.getClassLoader() points to this class loader.
 * <p>
 * Author Christian d'Heureuse, Inventec Informatik AG, Zurich, Switzerland, www.source-code.biz<br>
 * License: LGPL, http://www.gnu.org/licenses/lgpl.html<br>
 * Please contact the author if you need another license.
 */
public class JoinClassLoader extends ClassLoader {
    // made static to be retained between different instances of JoinClassLoader
    private static Map<URL, Class> cache = Collections.synchronizedMap(new HashMap<URL, Class>());
    private ClassLoader[] delegateClassLoaders;
    private ClassLoader cacheableClassLoader;

    public JoinClassLoader(ClassLoader parent, ClassLoader cacheableClassLoader, ClassLoader... delegateClassLoaders) {
        super(parent);
        this.cacheableClassLoader = cacheableClassLoader;
        this.delegateClassLoaders = delegateClassLoaders;
    }

    protected Class<?> findClass(String name) throws ClassNotFoundException {
        String path = name.replace('.', '/') + ".class";

        URL url = cacheableClassLoader.getResource(path);
        if (url != null) {
            // class is found in the cacheable ClassLoader
            // attempt to load from cache
            if (cache.containsKey(url)) {
                return cache.get(url);
            }

            // not in cache, load and retain in cache
            ByteBuffer byteCode;
            try {
                byteCode = loadResource(url);
            } catch (IOException e) {
                throw new ClassNotFoundException(name, e);
            }
            Class klass = defineClass(name, byteCode, null);
            cache.put(url, klass);
            return klass;
        } else {
            // class not found in the cacheable ClassLoader, try and load on the
            // fly from the other ClassLoaders
            url = findResource(path);
            if (url == null) {
                throw new ClassNotFoundException(name);
            }
            ByteBuffer byteCode;
            try {
                byteCode = loadResource(url);
            } catch (IOException e) {
                throw new ClassNotFoundException(name, e);
            }
            return defineClass(name, byteCode, null);
        }
    }

    private ByteBuffer loadResource(URL url) throws IOException {
        InputStream stream = null;
        try {
            stream = url.openStream();
            int initialBufferCapacity = Math.min(0x40000, stream.available() + 1);
            if (initialBufferCapacity <= 2) {
                initialBufferCapacity = 0x10000;
            } else {
                initialBufferCapacity = Math.max(initialBufferCapacity, 0x200);
            }
            ByteBuffer buf = ByteBuffer.allocate(initialBufferCapacity);
            while (true) {
                if (!buf.hasRemaining()) {
                    ByteBuffer newBuf = ByteBuffer.allocate(2 * buf.capacity());
                    buf.flip();
                    newBuf.put(buf);
                    buf = newBuf;
                }
                int len = stream.read(buf.array(), buf.position(), buf.remaining());
                if (len <= 0) {
                    break;
                }
                buf.position(buf.position() + len);
            }
            buf.flip();
            return buf;
        } finally {
            if (stream != null) {
                stream.close();
            }
        }
    }

    protected URL findResource(String name) {
        for (ClassLoader delegate : delegateClassLoaders) {
            URL resource = delegate.getResource(name);
            if (resource != null) {
                return resource;
            }
        }
        return null;
    }

    protected Enumeration<URL> findResources(String name) throws IOException {
        Vector<URL> vector = new Vector<URL>();
        for (ClassLoader delegate : delegateClassLoaders) {
            Enumeration<URL> enumeration = delegate.getResources(name);
            while (enumeration.hasMoreElements()) {
                vector.add(enumeration.nextElement());
            }
        }
        return vector.elements();
    }
}
