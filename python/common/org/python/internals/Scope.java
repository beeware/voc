package org.python.internals;

public class Scope implements java.util.Map<org.python.Object, org.python.Object> {
    java.util.Map<java.lang.String, org.python.Object> value;

    final class ScopeEntry<K, V> implements java.util.Map.Entry<K, V> {
        private final K key;
        private V value;

        public ScopeEntry(K key, V value) {
            this.key = key;
            this.value = value;
        }

        @Override
        public K getKey() {
            return key;
        }

        @Override
        public V getValue() {
            return value;
        }

        @Override
        public V setValue(V value) {
            V old = this.value;
            this.value = value;
            return old;
        }
    }

    public Scope(java.util.Map<java.lang.String, org.python.Object> scope) {
        this.value = scope;
    }

    /**
     * Removes all of the mappings from this map (optional operation).
     */
    public void clear() {
        this.value.clear();
    }

    /**
     * Returns true if this map contains a mapping for the specified key.
     */
    public boolean containsKey(java.lang.Object key) {
        return this.value.containsKey(((org.python.types.Str) key).value);
    }

    /**
     * Returns true if this map maps one or more keys to the specified value.
     */
    public boolean containsValue(java.lang.Object value) {
        return this.value.containsValue(value);
    }

    /**
     * Returns a Set view of the mappings contained in this map.
     */
    public java.util.Set<java.util.Map.Entry<org.python.Object, org.python.Object>> entrySet() {
        java.util.Set<java.util.Map.Entry<org.python.Object, org.python.Object>> entries =
                new java.util.HashSet<java.util.Map.Entry<org.python.Object, org.python.Object>>();

        for (java.util.Map.Entry<java.lang.String, org.python.Object> entry : this.value.entrySet()) {
            entries.add(
                    new ScopeEntry(
                            new org.python.types.Str(entry.getKey()),
                            entry.getValue()
                    )
            );
        }
        return null;
    }

    /**
     * Compares the specified object with this map for equality.
     */
    public boolean equals(java.lang.Object o) {
        return false;
    }

    /**
     * Returns the value to which the specified key is mapped, or null if this map contains no mapping for the key.
     */
    public org.python.Object get(java.lang.Object key) {
        return this.value.get(((org.python.types.Str) key).value);
    }

    /**
     * Returns the hash code value for this map.
     */
    public int hashCode() {
        return this.value.hashCode();
    }

    /**
     * Returns true if this map contains no key-value mappings.
     */
    public boolean isEmpty() {
        return this.value.isEmpty();
    }

    /**
     * Returns a Set view of the keys contained in this map.
     */
    public java.util.Set<org.python.Object> keySet() {
        java.util.Set<org.python.Object> keys = new java.util.HashSet<org.python.Object>();

        for (java.lang.String key : this.value.keySet()) {
            keys.add(new org.python.types.Str(key));
        }
        return keys;
    }

    /**
     * Associates the specified value with the specified key in this map (optional operation).
     */
    public org.python.Object put(org.python.Object key, org.python.Object value) {
        return this.value.put(((org.python.types.Str) key).value, value);
    }

    /**
     * Copies all of the mappings from the specified map to this map (optional operation).
     */
    public void putAll(java.util.Map<? extends org.python.Object, ? extends org.python.Object> map) {
        for (java.util.Map.Entry<? extends org.python.Object, ? extends org.python.Object> entry : map.entrySet()) {
            this.value.put(
                    ((org.python.types.Str) entry.getKey()).value,
                    entry.getValue()
            );
        }
    }

    /**
     * Removes the mapping for a key from this map if it is present (optional operation).
     */
    public org.python.Object remove(java.lang.Object key) {
        return this.value.remove(((org.python.types.Str) key).value);
    }

    /**
     * Returns the number of key-value mappings in this map.
     */
    public int size() {
        return this.value.size();
    }

    /**
     * Returns a Collection view of the values contained in this map.
     */
    public java.util.Collection<org.python.Object> values() {
        return this.value.values();
    }
}
