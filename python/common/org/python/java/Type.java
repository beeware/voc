package org.python.java;

public class Type extends org.python.types.Type {
    java.util.Map<java.lang.String, java.lang.reflect.Constructor> constructors;

    public Type(org.python.types.Type.Origin origin, java.lang.Class klass) {
        super(origin, klass);

        this.constructors = new java.util.HashMap<java.lang.String, java.lang.reflect.Constructor>();
        for (java.lang.reflect.Constructor constructor: klass.getConstructors()) {
            // System.out.println("Found constructor " + constructor);
            java.lang.StringBuilder signature = new java.lang.StringBuilder();

            for (java.lang.Class c: constructor.getParameterTypes()) {
                signature.append(org.python.java.Function.descriptor(c));
            }

            this.constructors.put(
                signature.toString(),
                constructor
            );
        }
        // System.out.println("Constructors: " + this.constructors);
    }

    public java.lang.reflect.Constructor selectConstructor(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        // org.Python.debug("Constructor options: ", this.constructors);

        java.lang.reflect.Constructor constructor = null;
        java.lang.StringBuilder signature = new java.lang.StringBuilder();
        java.lang.Class<?> [] arg_types = new java.lang.Class<?> [args.length];
        int n_args = args.length;
        for (int i = 0; i < n_args; i++) {
            if (args[i] == null) {
                arg_types[i] = null;
            } else if (args[i].toJava() == null) {
                arg_types[i] = null;
            } else {
                arg_types[i] = args[i].toJava().getClass();
            }
            signature.append(org.python.java.Function.descriptor(arg_types[i]));
        }
        // System.out.println("Argument signature " + signature.toString());
        constructor = this.constructors.get(signature.toString());

        // No pre-cached match - need to try alternatives for signature.
        if (constructor == null) {
            java.util.List<java.lang.reflect.Constructor> candidates = new java.util.ArrayList<java.lang.reflect.Constructor>();
            Class<?> [] param_types = null;

            for (java.lang.reflect.Constructor candidate: this.constructors.values()) {
                param_types = candidate.getParameterTypes();

                // Candidate must have the same number of parameters as
                // there are arguments.
                if (param_types.length == n_args) {

                    // Check each parameter; the argument must be a
                    // subclass of the paramteter type.
                    boolean match = true;
                    for (int i = 0; i < n_args; i++) {
                        if (arg_types[i] != null && !param_types[i].isAssignableFrom(arg_types[i])) {
                            match = false;
                        }
                    }

                    if (match) {
                        // org.Python.debug("New candidate", candidate);
                        candidates.add(candidate);
                    // } else {
                    //     org.Python.debug("Ignore candidate; non-matching signature", candidate);
                    }
                // } else {
                //     org.Python.debug("Ignore candidate; wrong number of parameters", candidate);
                }
            }

            // Now work out *which* candidate is the most specific match.
            java.lang.Class<?> [] candidate_types;
            // org.Python.debug("Choose best candidate...", candidates);
            for (java.lang.reflect.Constructor candidate: candidates) {
                // org.Python.debug("Evaluate candidate", candidate);
                if (constructor == null) {
                    // org.Python.debug("New best candidate", candidate);
                    constructor = candidate;
                    param_types = candidate.getParameterTypes();
                } else {
                    candidate_types = candidate.getParameterTypes();
                    java.lang.Boolean more_specific = null;
                    java.lang.Boolean less_specific = null;
                    for (int i = 0; i < n_args; i++) {
                        if (param_types[i] != candidate_types[i]) {
                            if (param_types[i].isAssignableFrom(candidate_types[i])) {
                                // org.Python.debug("More specific type on parameter", i);
                                more_specific = true;
                            } else if (candidate_types[i].isAssignableFrom(param_types[i])) {
                                // org.Python.debug("Less specific type on parameter", i);
                                less_specific = true;
                            }
                        // } else {
                        //     org.Python.debug("Same type on parameter", i);
                        }
                    }

                    if (more_specific && (less_specific == null || !less_specific)) {
                        // org.Python.debug("New best candidate", candidate);
                        constructor = candidate;
                        param_types = candidate_types;
                    }
                }
            }

            // If there is still no match, raise an error.
            if (constructor == null) {
                throw new org.python.exceptions.RuntimeError(
                    String.format(
                        "No candidate constructor found for signature (%s); tried %s",
                        signature.toString(),
                        candidates
                    )
                );
            }

            // We have a match that wasn't previously in the this.constructors dictionary;
            // Cache it for later use.
            this.constructors.put(signature.toString(), constructor);
        }

        return constructor;
    }

    public java.lang.Object [] adjustArguments(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        java.lang.Object [] adjusted = new java.lang.Object [args.length];
        for (int i = 0; i < args.length; i++) {
            if (args[i] == null) {
                adjusted[i] = null;
            } else {
                adjusted[i] = args[i].toJava();
            }
        }
        return adjusted;
    }

    public org.python.Object __getattribute_null(java.lang.String name) {
        // org.Python.debug(String.format("GETATTRIBUTE %s FROM NATIVE TYPE", name), this.klass);
        org.python.Object value = this.attrs.get(name);

        // On a native type, attrs is a cache of lookups on actual functions.
        // If there's no hit, then we need to reflect on the underyling class
        // and populate the cache.
        if (value == null) {
            // java.lang.Map doesn't differentiate between "doesn't exist"
            // and "value is null"; so since we know the value is null, check
            // to see if it is an explicit null (i.e., attribute doesn't exist)
            // org.Python.debug("No class attr");
            if (!this.attrs.containsKey(name)) {
                // org.Python.debug("doing lookup...");
                try {
                    value = new org.python.java.Function(this.klass, name);
                } catch (org.python.exceptions.AttributeError ae) {
                    // No function; look for an attribute with the same name.
                    try {
                        value = new org.python.java.Field(klass.getDeclaredField(name));
                    } catch (java.lang.NoSuchFieldException fe) {
                        // Field does not exist.
                        try {
                            // org.Python.debug("Look for inner class ", this.klass.getName() + "$" + name);
                            java.lang.Class inner_klass = java.lang.Class.forName(this.klass.getName() + "$" + name);
                            value = new org.python.java.Type(org.python.types.Type.Origin.JAVA, inner_klass);
                        } catch (java.lang.ClassNotFoundException ce) {
                            // org.Python.debug("Inner class not found", ce);
                            // Inner class does not exist.
                            value = null;
                        }
                    }
                }
                // If the field doesn't exist, store a value of null
                // so that we don't try to look up the field again.
                // If it does, store the field.
                this.attrs.put(name, value);
            }
        }

        // org.Python.debug(String.format("GETATTRIBUTE %s NATIVE value ", name), value);
        // If there's still no value, return that as an indicator of no attribute.
        if (value == null) {
            return null;
        }

        // Post-process the attribute, passing the class as the instance.
        return value.__get__(this, this);
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // System.out.println("SETATTRIBUTE NATIVE TYPE " + this + " " + name + " = " + value);
        org.python.types.Type cls = org.python.types.Type.pythonType(this.klass);
        // System.out.println("instance attrs = " + this.attrs);
        // System.out.println("class attrs = " + cls.attrs);

        cls.attrs.put(name, value);
        return true;
    }

    public org.python.Object invoke(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            // org.Python.debug("Native Constructor:", this.constructor);
            // org.Python.debug("            Origin:", this.origin);
            // org.Python.debug("              Type:", this);
            // for (org.python.Object arg: args) {
            //     org.Python.debug("            arg: ", arg);
            // }
            // org.Python.debug("         kwargs: ", kwargs);

            java.lang.reflect.Constructor constructor;
            if (this.origin == org.python.types.Type.Origin.EXTENSION) {
                constructor = this.constructor;

                return new org.python.java.Object(constructor.newInstance(args, kwargs));
            } else {
                constructor = this.selectConstructor(args, kwargs);
                java.lang.Object [] adjusted_args = this.adjustArguments(args, kwargs);

                return new org.python.java.Object(constructor.newInstance(adjusted_args));
            }
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to native Java constructor for " + this.klass);
        } catch (java.lang.reflect.InvocationTargetException e) {
            try {
                // e.getTargetException().printStackTrace();
                // If the Java constructor raised an Python exception, re-raise that
                // exception as-is. If it wasn't a Python exception, wrap it
                // as one and continue.
                throw (org.python.exceptions.BaseException) e.getCause();
            } catch (ClassCastException java_e) {
                throw new org.python.exceptions.RuntimeError(e.getCause().toString());
            }
        } catch (java.lang.InstantiationException e) {
            throw new org.python.exceptions.RuntimeError(e.getCause().toString());
        } finally {
        //     System.out.println("CONSTRUCTOR DONE");
        }
    }
}
