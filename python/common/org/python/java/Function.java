package org.python.java;

public class Function extends org.python.types.Object implements org.python.Callable {
    java.lang.Class klass;
    java.lang.String name;
    java.util.Map<java.lang.String, java.lang.reflect.Method> methods;

    /**
     * Convert a Java klass into a string-based descriptor of the type.
     * For example:
     *  - an argument of type int -> I
     *  - an argument of type java.lang.Integer -> I
     *  - an argument of type foo.bar.Whiz -> Lfoor/bar/whiz;
     *
     * This method makes one extension to the standard definition, and
     * converts a klass of null into "0". This is required so that
     * it is possible to map a list of actual arguments to a signature.
     */
    public static java.lang.String descriptor(java.lang.Class klass) {
        if (klass == null) {
            return "0";
        } else if (klass.getName().startsWith("[")) {
            return klass.getName();
        } else if (klass == java.lang.Boolean.TYPE
                || klass == java.lang.Boolean.class) {
            return "Z";
        } else if (klass == java.lang.Byte.TYPE
                || klass == java.lang.Byte.class) {
            return "B";
        } else if (klass == java.lang.Character.TYPE
                || klass == java.lang.Character.class) {
            return "C";
        } else if (klass == java.lang.Short.TYPE
                || klass == java.lang.Short.class) {
            return "S";
        } else if (klass == java.lang.Integer.TYPE
                || klass == java.lang.Integer.class) {
            return "I";
        } else if (klass == java.lang.Long.TYPE
                || klass == java.lang.Long.class) {
            return "J";
        } else if (klass == java.lang.Float.TYPE
                || klass == java.lang.Float.class) {
            return "F";
        } else if (klass == java.lang.Double.TYPE
                || klass == java.lang.Double.class) {
            return "D";
        } else {
            return "L" + klass.getName().replace('.', '/') + ";";
        }
    }

    /* Arguments and parameters can match with different levels of compatibility. */
    public enum MatchType {
        /* No match - types are incompatible */
        NO_MATCH,

        /* Loose cast match - Types can be cast into each other, but there will
         * likely be a loss of precision.
         * e.g., passing a float to foo(int x)
         */
        LOOSE_CAST_MATCH,

        /* Range match - Types are compatible, but differ in range; the argument
         * has a smaller range than the parameter. No cast is required.
         * e.g., passing a float to foo(double x)
         *       passing an int to foo(float x)
         *       passing an int to foo(long x)
         */
        RANGE_MATCH,

        /* Cast Range match - Types are closely compatible, but the argument
         * has a much bigger range than the parameter. A cast is necessary to
         * make the argument fit into the value. This is needed because Python's
         * internal types use the largest available range types, but Java APIs
         * will internally tend to int/float.
         * e.g., passing a double to foo(float x)
         *       passing a long to foo(int x)
         */
        CAST_RANGE_MATCH,

        /* Subtype match - Argument is a subtype of the parameter type. No cast
         * is required, but an exact match would be preferred.
         * e.g., passing a java.lang.String to foo(java.lang.CharSequence x)
         */
        SUBTYPE_MATCH,

        /* Exact match - types are identical */
        EXACT_MATCH;

        public boolean betterThan(MatchType other) {
            return this.compareTo(other) > 0;
        }
    }

    /**
     * Determine if a variable of one type can assigned to another type, using
     * the definition provided by the Java Language Specification (plus some
     * light interpretation from Python usage)
     *
     * Returns a boolean describing if a variable of type `from_type` can be
     * assigned to `to_type`. This will return true if:
     *  - `from_type` and `to_type` are the same type
     *  - `from_type` is more specific than `to_type`
     *  - `from_type and `to_type` are primitives, and `from_type` can be cast to
     *    `to_type`, and the `allow_cast` argument is set to true.
     */
    public static MatchType parameterMatch(java.lang.Class<?> from_type, java.lang.Class<?> to_type) {
        // org.Python.debug("param match: From", from_type);
        // org.Python.debug("               To", to_type);

        if (from_type == null) {
            if (to_type == java.lang.Double.TYPE
                    || to_type == java.lang.Float.TYPE
                    || to_type == java.lang.Long.TYPE
                    || to_type == java.lang.Integer.TYPE
                    || to_type == java.lang.Short.TYPE
                    || to_type == java.lang.Byte.TYPE
                    || to_type == java.lang.Character.TYPE) {
                // org.Python.debug("null cannot be assigned to a primitive");
                return MatchType.NO_MATCH;
            } else {
                // org.Python.debug("null can be assigned to any non-primitive");
                return MatchType.EXACT_MATCH;
            }
        }

        // Check if the two types are the same
        if (to_type.equals(from_type)) {
            // org.Python.debug("from and to are same type");
            return MatchType.EXACT_MATCH;
        }

        // Check basic subtyping and assignability
        if (to_type.isAssignableFrom(from_type)) {
            // org.Python.debug(java.lang.String.format("%s arg can be assigned directly", from_type), to_type);
            return MatchType.SUBTYPE_MATCH;
        }

        // Then check all the upcasting possible with primitive types
        if (to_type == java.lang.Double.TYPE || to_type == java.lang.Double.class) {
            // org.Python.debug("Parameter needs a double");
            if (from_type == java.lang.Double.TYPE || from_type == java.lang.Double.class) {
                // org.Python.debug("Got a double");
                return MatchType.EXACT_MATCH;
            } else if ((from_type == java.lang.Float.TYPE || from_type == java.lang.Float.class)
                    || (from_type == java.lang.Long.TYPE || from_type == java.lang.Long.class)
                    || (from_type == java.lang.Integer.TYPE || from_type == java.lang.Integer.class)
                    || (from_type == java.lang.Short.TYPE || from_type == java.lang.Short.class)
                    || (from_type == java.lang.Byte.TYPE || from_type == java.lang.Byte.class)
                    || (from_type == java.lang.Character.TYPE || from_type == java.lang.Character.class)) {
                // Any number can be assigned to a double.
                // org.Python.debug("Can be assigned directly");
                return MatchType.RANGE_MATCH;
            }
        } else if (to_type == java.lang.Float.TYPE || to_type == java.lang.Float.class) {
            // org.Python.debug("Parameter needs a float");
            if (from_type == java.lang.Float.TYPE || from_type == java.lang.Float.class) {
                // org.Python.debug("Got a float");
                return MatchType.EXACT_MATCH;
            } else if (from_type == java.lang.Double.TYPE || from_type == java.lang.Double.class) {
                // org.Python.debug("Got a double");
                return MatchType.CAST_RANGE_MATCH;
            } else if ((from_type == java.lang.Long.TYPE || from_type == java.lang.Long.class)
                    || (from_type == java.lang.Integer.TYPE || from_type == java.lang.Integer.class)
                    || (from_type == java.lang.Short.TYPE || from_type == java.lang.Short.class)
                    || (from_type == java.lang.Byte.TYPE || from_type == java.lang.Byte.class)
                    || (from_type == java.lang.Character.TYPE || from_type == java.lang.Character.class)) {
                // org.Python.debug("Can be assigned directly");
                return MatchType.RANGE_MATCH;
            }
        } else if (to_type == java.lang.Long.TYPE || to_type == java.lang.Long.class) {
            // org.Python.debug("Parameter needs a long");
            if (from_type == java.lang.Long.TYPE || from_type == java.lang.Long.class) {
                // org.Python.debug("Got a long");
                return MatchType.EXACT_MATCH;
            } else if ((from_type == java.lang.Double.TYPE || from_type == java.lang.Double.class)
                    || (from_type == java.lang.Float.TYPE || from_type == java.lang.Float.class)) {
                // org.Python.debug("Got a double/float");
                return MatchType.LOOSE_CAST_MATCH;
            } else if ((from_type == java.lang.Integer.TYPE || from_type == java.lang.Integer.class)
                    || (from_type == java.lang.Short.TYPE || from_type == java.lang.Short.class)
                    || (from_type == java.lang.Byte.TYPE || from_type == java.lang.Byte.class)
                    || (from_type == java.lang.Character.TYPE || from_type == java.lang.Character.class)) {
                // org.Python.debug("Can be assigned directly");
                return MatchType.RANGE_MATCH;
            }
        } else if (to_type == java.lang.Integer.TYPE || to_type == java.lang.Integer.class) {
            // org.Python.debug("Parameter needs a integer");
            if (from_type == java.lang.Integer.TYPE || from_type == java.lang.Integer.class) {
                // org.Python.debug("Got an int");
                return MatchType.EXACT_MATCH;
            } else if ((from_type == java.lang.Double.TYPE || from_type == java.lang.Double.class)
                    || (from_type == java.lang.Float.TYPE || from_type == java.lang.Float.class)) {
                // org.Python.debug("Got a double/float");
                return MatchType.LOOSE_CAST_MATCH;
            } else if (from_type == java.lang.Long.TYPE || from_type == java.lang.Long.class) {
                // org.Python.debug("Got a long");
                return MatchType.CAST_RANGE_MATCH;
            } else if ((from_type == java.lang.Short.TYPE || from_type == java.lang.Short.class)
                    || (from_type == java.lang.Byte.TYPE || from_type == java.lang.Byte.class)
                    || (from_type == java.lang.Character.TYPE || from_type == java.lang.Character.class)) {
                // org.Python.debug("Can be assigned directly");
                return MatchType.RANGE_MATCH;
            }
        } else if (to_type == java.lang.Short.TYPE || to_type == java.lang.Short.class) {
            // org.Python.debug("Parameter needs a short");
            if (from_type == java.lang.Short.TYPE || from_type == java.lang.Short.class) {
                // org.Python.debug("Got a short");
                return MatchType.EXACT_MATCH;
            } else if ((from_type == java.lang.Double.TYPE || from_type == java.lang.Double.class)
                    || (from_type == java.lang.Float.TYPE || from_type == java.lang.Float.class)) {
                // org.Python.debug("Got a double/float");
                return MatchType.LOOSE_CAST_MATCH;
            } else if ((from_type == java.lang.Long.TYPE || from_type == java.lang.Long.class)
                    || (from_type == java.lang.Integer.TYPE || from_type == java.lang.Integer.class)) {
                // org.Python.debug("Got a long/int");
                return MatchType.CAST_RANGE_MATCH;
            } else if ((from_type == java.lang.Byte.TYPE || from_type == java.lang.Byte.class)
                    || (from_type == java.lang.Character.TYPE || from_type == java.lang.Character.class)) {
                // org.Python.debug("Can be assigned directly");
                return MatchType.RANGE_MATCH;
            }
        } else if (to_type == java.lang.Character.TYPE || to_type == java.lang.Character.class) {
            // org.Python.debug("Parameter needs a char");
            if (from_type == java.lang.Character.TYPE || from_type == java.lang.Character.class) {
                // org.Python.debug("Got a char");
                return MatchType.EXACT_MATCH;
            } else if ((from_type == java.lang.Long.TYPE || from_type == java.lang.Long.class)
                    || (from_type == java.lang.Integer.TYPE || from_type == java.lang.Integer.class)
                    || (from_type == java.lang.Short.TYPE || from_type == java.lang.Short.class)) {
                // org.Python.debug("Got a long/int/short");
                return MatchType.CAST_RANGE_MATCH;
            } else if (from_type == java.lang.Byte.TYPE || from_type == java.lang.Byte.class) {
                // org.Python.debug("Can be assigned directly");
                return MatchType.RANGE_MATCH;
            }
        } else if (to_type == java.lang.Byte.TYPE || to_type == java.lang.Byte.class) {
            // org.Python.debug("Parameter needs a byte");
            if (from_type == java.lang.Byte.TYPE || from_type == java.lang.Byte.class) {
                // org.Python.debug("Got a byte");
                return MatchType.EXACT_MATCH;
            } else if ((from_type == java.lang.Long.TYPE || from_type == java.lang.Long.class)
                    || (from_type == java.lang.Integer.TYPE || from_type == java.lang.Integer.class)
                    || (from_type == java.lang.Short.TYPE || from_type == java.lang.Short.class)
                    || (from_type == java.lang.Character.TYPE || from_type == java.lang.Character.class)) {
                // org.Python.debug("Got a long/int/short/char");
                return MatchType.CAST_RANGE_MATCH;
            }
            // } else {
            //     org.Python.debug("Don't know what to do with to-type", to_type);
        }

        // org.Python.debug("Can't be assigned");
        return MatchType.NO_MATCH;
    }

    /**
     * Given a list of methods (with signatures), and a set of args and kwargs, find
     * the method that is the best match for the args and kwargs, following the rules
     * of the Java Language Specification.
     *
     * Returns null if no method match can be found.
     *
     * If multiple matches exist return the most specific match.
     */
    public java.lang.reflect.Method selectMethod(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        // org.Python.debug("Method options: ", this.methods);

        java.lang.reflect.Method method = null;
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
        method = this.methods.get(signature.toString());

        // No pre-cached match - need to try alternatives for signature.
        if (method == null) {
            java.util.List<java.lang.reflect.Method> candidates = new java.util.ArrayList<java.lang.reflect.Method>();
            java.lang.Class<?>[] param_types = null;
            Function.MatchType param_match = Function.MatchType.EXACT_MATCH;

            for (java.lang.reflect.Method candidate : this.methods.values()) {
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
            Function.MatchType candidate_match;
            // org.Python.debug("Choose best candidate...", candidates);
            for (java.lang.reflect.Method candidate : candidates) {
                // org.Python.debug("Evaluate candidate", candidate);
                if (method == null) {
                    // org.Python.debug("New best (default) candidate", candidate);
                    method = candidate;
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
                        method = candidate;
                        param_types = candidate_types;
                        param_match = candidate_match;
                    }
                }
            }

            // If there is still no match, raise an error.
            if (method == null) {
                throw new org.python.exceptions.RuntimeError(
                        java.lang.String.format(
                                "No candidate method found for signature %s(%s); tried %s",
                                this.name,
                                signature.toString(),
                                candidates
                        )
                );
            }

            // We have a match that wasn't previously in the this.methods dictionary;
            // Cache it for later use.
            this.methods.put(signature.toString(), method);
        }

        return method;
    }

    public java.lang.Object[] adjustArguments(java.lang.reflect.Method method, org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        java.lang.Object[] adjusted = new java.lang.Object[args.length];
        java.lang.Class<?>[] param_types = method.getParameterTypes();
        for (int i = 0; i < args.length; i++) {
            adjusted[i] = org.python.types.Type.toJava(param_types[i], args[i]);
        }
        return adjusted;
    }

    public Function(java.lang.Class klass, java.lang.String name) {
        super();
        this.klass = klass;
        this.name = name;
        // org.Python.debug("FUNCTION ", this.name);
        this.methods = new java.util.HashMap<java.lang.String, java.lang.reflect.Method>();

        // When searching for a function, we search *declared* fields -
        // that's all fields that are acutally defined directly on this
        // class. However, having found a match on this class, we then
        // search all subclasses as well, in case there is a method
        // with the same name, but a different prototype. This simplifies
        // the lookup process when the function is invoked.
        java.lang.Class<?> clazz = klass;
        while (clazz != null) {
            // org.Python.debug("CLAZZ:", clazz);
            for (java.lang.reflect.Method method : clazz.getDeclaredMethods()) {
                // org.Python.debug("METHOD:", method.getName());
                if (method.getName().equals(name)) {
                    java.lang.StringBuilder signature = new java.lang.StringBuilder();

                    for (java.lang.Class c : method.getParameterTypes()) {
                        signature.append(org.python.java.Function.descriptor(c));
                    }

                    // org.Python.debug("  match: ", signature.toString());
                    // org.Python.debug("    known: ", this.methods.containsKey(signature.toString()));
                    // org.Python.debug("    abstract: ", java.lang.reflect.Modifier.isAbstract(method.getModifiers()));

                    java.lang.String sig = signature.toString();
                    boolean is_abstract = java.lang.reflect.Modifier.isAbstract(method.getModifiers());
                    if (!this.methods.containsKey(sig) && !is_abstract) {
                        this.methods.put(sig, method);
                    }
                }
            }

            // If we've searched for the name, and and we haven't found
            // any matches, throw an attribute error.
            if (this.methods.size() == 0) {
                throw new org.python.exceptions.AttributeError(klass, name);
            }

            clazz = clazz.getSuperclass();
        }
        // org.Python.debug("methods: ", this.methods);
        this.__dict__.put("__name__", new org.python.types.Str(this.name));
        this.__dict__.put("__qualname__", new org.python.types.Str(this.name));
    }

    @org.python.Method(
            __doc__ = "Implement repr(self)."
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str(
                java.lang.String.format("<native function %s.%s>",
                        this.klass.getName(),
                        this.name)
        );
    }

    @org.python.Method(
            __doc__ = "Implement __get__(self)."
    )
    public org.python.Object __get__(org.python.Object instance, org.python.Object klass) {
        if (instance == klass) {
            return this;
        } else {
            return new org.python.java.Method(instance, this);
        }
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __bool__() {
        return new org.python.types.Bool(true);
    }

    public org.python.Object invoke(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        return this.invoke(null, args, kwargs);
    }

    public org.python.Object invoke(org.python.Object instance, org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            java.lang.Object target = null;
            // org.Python.debug("Native Function:", this.name);
            // org.Python.debug("       instance: ", instance);
            if (instance != null) {
                target = instance.toObject();
                // org.Python.debug("         target: ", target);
            }
            // for (org.python.Object arg: args) {
            //     org.Python.debug("            arg: ", arg);
            //     if (arg != null) {
            //         org.Python.debug("           type: ", arg.getClass());
            //     }
            // }
            // org.Python.debug("         kwargs: ", kwargs);

            if (kwargs.size() > 0) {
                // TODO: This doesn't have to be so - we *could* introspect argument names.
                throw new org.python.exceptions.RuntimeError("Cannot use kwargs to invoke a native Java method.");
            }

            java.lang.reflect.Method method = this.selectMethod(args, kwargs);

            // org.Python.debug("  Native method: ", method);

            java.lang.Object[] adjusted_args = this.adjustArguments(method, args, kwargs);

            // if (adjusted_args != null) {
            //     for (java.lang.Object arg: adjusted_args) {
            //         org.Python.debug("   Adjusted arg: ", arg);
            //         if (arg != null) {
            //             org.Python.debug("           type: ", arg.getClass());
            //         }
            //     }
            // } else {
            //     org.Python.debug("No adjusted args");
            // }

            java.lang.Object result = method.invoke(target, adjusted_args);
            // org.Python.debug("NATIVE RESULT", result);

            org.python.Object pyresult = org.python.types.Type.toPython(result);
            // org.Python.debug("PYTHON RESULT", pyresult);
            // if (pyresult != null) {
            //     org.Python.debug("PYTHON RESULT CLASS", pyresult.getClass());
            //     org.Python.debug("PYTHON RESULT TOJAVA", pyresult.toJava());
            //     if (pyresult.toJava() != null) {
            //         org.Python.debug("PYTHON RESULT TOJAVA", pyresult.toJava().getClass());
            //     }
            // }
            return pyresult;
        } catch (java.lang.IllegalAccessException e) {
            // e.printStackTrace();
            throw new org.python.exceptions.RuntimeError("Illegal access to Java function");
        } catch (java.lang.reflect.InvocationTargetException e) {
            try {
                // e.getTargetException().printStackTrace();
                // If the Java method raised an Python exception, re-raise that
                // exception as-is. If it wasn"t a Python exception, wrap it
                // as one and continue.
                throw (org.python.exceptions.BaseException) e.getCause();
            } catch (ClassCastException java_e) {
                java.lang.String message = e.getCause().getMessage();
                if (message == null) {
                    throw new org.python.exceptions.RuntimeError(
                            e.getCause().getClass().getName()
                    );
                } else {
                    throw new org.python.exceptions.RuntimeError(
                            e.getCause().getClass().getName() + ": " + message
                    );
                }
            }
        // } finally {
            //     org.Python.debug("INVOKE METHOD DONE");
        }
    }
}
