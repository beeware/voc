package org.python.java;

public class Type extends org.python.types.Type {
    java.util.Map<java.lang.String, java.lang.reflect.Constructor> constructors;

    public java.lang.Object toJava() {
        return this.klass;
    }

    public Type(org.python.types.Type.Origin origin, java.lang.Class klass) {
        super(origin, klass);

        this.constructors = new java.util.HashMap<java.lang.String, java.lang.reflect.Constructor>();
        for (java.lang.reflect.Constructor constructor : klass.getConstructors()) {
            // System.out.println("Found constructor " + constructor);
            java.lang.StringBuilder signature = new java.lang.StringBuilder();

            for (java.lang.Class c : constructor.getParameterTypes()) {
                signature.append(Function.descriptor(c));
            }

            this.constructors.put(
                    signature.toString(),
                    constructor
            );
        }
        // System.out.println("Constructors: " + this.constructors);
    }

    /*
     * Given a list of constructors (with signatures), and a set of args and kwargs, find
     * the method that is the best match for the args and kwargs, following the rules
     * of the Java Language Specification.
     *
     * Returns null if no method match can be found.
     *
     * If multiple matches exist return the most specific match.
     */
    public java.lang.reflect.Constructor selectConstructor(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        // org.Python.debug("Constructor options: ", this.constructors);

        java.lang.reflect.Constructor constructor = null;
        java.lang.StringBuilder signature = new java.lang.StringBuilder();
        java.lang.Class<?>[] arg_types = new java.lang.Class<?>[args.length];
        int n_args = args.length;
        for (int i = 0; i < n_args; i++) {
            if (args[i] == null) {
                arg_types[i] = null;
            } else if (args[i].toJava() == null) {
                arg_types[i] = null;
            } else {
                arg_types[i] = args[i].toJava().getClass();
            }
            signature.append(Function.descriptor(arg_types[i]));
        }
        // org.Python.debug("Argument signature", signature);
        constructor = this.constructors.get(signature.toString());

        // No pre-cached match - need to try alternatives for signature.
        if (constructor == null) {
            java.util.List<java.lang.reflect.Constructor> candidates = new java.util.ArrayList<java.lang.reflect.Constructor>();
            java.lang.Class<?>[] param_types = null;
            Function.MatchType param_match = Function.MatchType.EXACT_MATCH;

            for (java.lang.reflect.Constructor candidate : this.constructors.values()) {
                param_types = candidate.getParameterTypes();

                // Candidate must have the same number of parameters as
                // there are arguments.
                if (param_types.length == n_args) {

                    // Check each parameter; the argument must be a
                    // subclass of the parameter type.
                    boolean match = true;
                    for (int i = 0; i < n_args; i++) {
                        if (Function.parameterMatch(arg_types[i], param_types[i]) == Function.MatchType.NO_MATCH) {
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
            java.lang.Class<?>[] candidate_types;
            Function.MatchType candidate_match = Function.MatchType.EXACT_MATCH;
            // org.Python.debug("Choose best candidate...", candidates);
            for (java.lang.reflect.Constructor candidate : candidates) {
                // org.Python.debug("Evaluate candidate", candidate);
                if (constructor == null) {
                    // org.Python.debug("New best (default) candidate", candidate);
                    constructor = candidate;
                    param_types = candidate.getParameterTypes();
                    for (int i = 0; i < n_args; i++) {
                        candidate_match = Function.parameterMatch(arg_types[i], param_types[i]);
                        // org.Python.debug(java.lang.String.format("Parameter %d has match", i), candidate_match);
                        if (param_match.betterThan(candidate_match)) {
                            param_match = candidate_match;
                        }
                    }
                    // org.Python.debug("Candidate match:", param_match);
                } else {
                    candidate_types = candidate.getParameterTypes();
                    candidate_match = Function.MatchType.EXACT_MATCH;
                    Function.MatchType match;
                    for (int i = 0; i < n_args; i++) {
                        match = Function.parameterMatch(arg_types[i], candidate_types[i]);
                        // org.Python.debug(java.lang.String.format("Parameter %d has match", i), match);
                        if (candidate_match.betterThan(match)) {
                            candidate_match = match;
                        }
                    }
                    // org.Python.debug("Candidate match:", candidate_match);

                    if (candidate_match.betterThan(param_match)) {
                        // org.Python.debug("New best candidate", candidate);
                        constructor = candidate;
                        param_types = candidate_types;
                        param_match = candidate_match;
                    }
                }
            }

            // If there is still no match, raise an error.
            if (constructor == null) {
                throw new org.python.exceptions.RuntimeError(
                        java.lang.String.format(
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

    public java.lang.Object[] adjustArguments(java.lang.reflect.Constructor constructor, org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        java.lang.Object[] adjusted = new java.lang.Object[args.length];
        java.lang.Class<?>[] param_types = constructor.getParameterTypes();
        for (int i = 0; i < args.length; i++) {
            adjusted[i] = org.python.types.Type.toJava(param_types[i], args[i]);
        }
        return adjusted;
    }

    public org.python.Object __getattribute_null(java.lang.String name) {
        // org.Python.debug(String.format("GETATTRIBUTE %s FROM NATIVE TYPE", name), this.klass);
        org.python.Object value = this.__dict__.get(name);

        // On a native type, __dict__ is a cache of lookups on actual functions.
        // If there's no hit, then we need to reflect on the underyling class
        // and populate the cache.
        if (value == null) {
            // java.lang.Map doesn't differentiate between "doesn't exist"
            // and "value is null"; so since we know the value is null, check
            // to see if it is an explicit null (i.e., attribute doesn't exist)
            // org.Python.debug("No class attr");
            if (!this.__dict__.containsKey(name)) {
                // org.Python.debug("doing lookup...");
                try {
                    // org.Python.debug("Declared method", this.klass);
                    // for (java.lang.reflect.Method m: klass.getDeclaredMethods()) {
                    //     org.Python.debug("    ", m);
                    // }
                    value = new org.python.java.Function(this.klass, name);
                } catch (org.python.exceptions.AttributeError ae) {
                    // org.Python.debug("Function not found", ae);
                    // No function; look for an attribute with the same name.
                    try {
                        // org.Python.debug("Declared fields", this.klass);
                        // for (java.lang.reflect.Field f: klass.getDeclaredFields()) {
                        //     org.Python.debug("    ", f);
                        // }
                        value = new org.python.java.Field(klass.getDeclaredField(name));
                    } catch (java.lang.NoSuchFieldException fe) {
                        // org.Python.debug("Field not found", fe);
                        // Field does not exist.
                        try {
                            // org.Python.debug("Look for inner class ", this.klass.getName() + "$" + name);
                            java.lang.Class inner_klass = java.lang.Thread.currentThread().getContextClassLoader().loadClass(this.klass.getName() + "$" + name);
                            value = new org.python.java.Type(org.python.types.Type.Origin.JAVA, inner_klass);
                        } catch (java.lang.ClassNotFoundException ce) {
                            // org.Python.debug("Inner class not found", ce);
                            // Inner class does not exist. Check superclasses

                            if (this.klass.getSuperclass() != null) {
                                // org.Python.debug("Check superclass", this.klass.getSuperclass());
                                org.python.types.Type superclass = org.python.types.Type.pythonType(this.klass.getSuperclass());
                                value = superclass.__getattribute_null(name);
                            } else {
                                // org.Python.debug("No superclass", this.klass);
                                value = null;
                            }
                        }
                    }
                }
                // If the field doesn't exist, store a value of null
                // so that we don't try to look up the field again.
                // If it does, store the field.
                this.__dict__.put(name, value);
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
        // System.out.println("instance __dict__ = " + this.__dict__);
        // System.out.println("class __dict__ = " + cls.__dict__);

        cls.__dict__.put(name, value);
        return true;
    }

    public org.python.Object invoke(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
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

                java.lang.Object instance = constructor.newInstance(args, kwargs);
                try {
                    java.lang.reflect.Field voc_field = instance.getClass().getField("__VOC__");
                    return (org.python.Object) voc_field.get(instance);
                } catch (java.lang.NoSuchFieldException nsf) {
                    throw new org.python.exceptions.RuntimeError("Extension class " + this.klass.getName() + " has no __VOC__ attribute");
                }
            } else {
                constructor = this.selectConstructor(args, kwargs);
                java.lang.Object[] adjusted_args = this.adjustArguments(constructor, args, kwargs);

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
        // } finally {
            //     System.out.println("CONSTRUCTOR DONE");
        }
    }
}
