package org.python.java;

public class Function extends org.python.types.Object implements org.python.Callable {
    java.lang.String name;
    java.util.Map<java.lang.String, java.lang.reflect.Method> methods;

    public static java.lang.String descriptor(java.lang.Class klass) {
        if (klass == null) {
            return "0";
        } else if (klass.getName().startsWith("[")) {
            return klass.getName();
        } else if (   klass == java.lang.Boolean.TYPE
                   || klass == java.lang.Boolean.class) {
            return "Z";
        } else if (   klass == java.lang.Byte.TYPE
                   || klass == java.lang.Byte.class) {
            return "B";
        } else if (   klass == java.lang.Character.TYPE
                   || klass == java.lang.Character.class) {
            return "C";
        } else if (   klass == java.lang.Short.TYPE
                   || klass == java.lang.Short.class) {
            return "S";
        } else if (   klass == java.lang.Integer.TYPE
                   || klass == java.lang.Integer.class) {
            return "I";
        } else if (   klass == java.lang.Long.TYPE
                   || klass == java.lang.Long.class) {
            return "J";
        } else if (   klass == java.lang.Float.TYPE
                   || klass == java.lang.Float.class) {
            return "F";
        } else if (   klass == java.lang.Double.TYPE
                   || klass == java.lang.Double.class) {
            return "D";
        } else {
            return "L" + klass.getName().replace('.', '/') + ";";
        }
    }

    public java.lang.reflect.Method selectMethod(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        // org.Python.debug("Method options: ", this.methods);

        java.lang.reflect.Method method = null;
        java.lang.StringBuilder signature = new java.lang.StringBuilder();
        java.lang.Class [] arg_types = new java.lang.Class [args.length];
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
        // org.Python.debug("Argument signature", signature.toString());
        method = this.methods.get(signature.toString());

        // No pre-cached match - need to try alternatives for signature.
        if (method == null) {
            java.util.List<java.lang.reflect.Method> candidates = new java.util.ArrayList<java.lang.reflect.Method>();
            java.lang.Class<?> [] param_types = null;

            for (java.lang.reflect.Method candidate: this.methods.values()) {
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
            for (java.lang.reflect.Method candidate: candidates) {
                // org.Python.debug("Evaluate candidate", candidate);
                if (method == null) {
                    // org.Python.debug("New best candidate", candidate);
                    method = candidate;
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

                    if (more_specific != null && more_specific && (less_specific == null || !less_specific)) {
                        // org.Python.debug("New best candidate", candidate);
                        method = candidate;
                        param_types = candidate_types;
                    }
                }
            }

            // If there is still no match, raise an error.
            if (method == null) {
                throw new org.python.exceptions.RuntimeError(
                    String.format(
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

    public Function(java.lang.Class klass, java.lang.String name) {
        super();
        this.name = name;
        // org.Python.debug("FUNCTION ", this.name);
        this.methods = new java.util.HashMap<java.lang.String, java.lang.reflect.Method>();

        java.lang.Class<?> clazz = klass;
        while (clazz != null) {
            // org.Python.debug("CLAZZ:", clazz);
            for (java.lang.reflect.Method method: clazz.getDeclaredMethods()) {
                // org.Python.debug("METHOD:", method.getName());
                if (method.getName().equals(name)) {
                    java.lang.StringBuilder signature = new java.lang.StringBuilder();

                    for (java.lang.Class c: method.getParameterTypes()) {
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

            clazz = clazz.getSuperclass();
        }
        // org.Python.debug("methods: ", this.methods);
        if (this.methods.size() == 0) {
            throw new org.python.exceptions.AttributeError(klass, name);
        }
        this.attrs.put("__name__", new org.python.types.Str(this.name));
        this.attrs.put("__qualname__", new org.python.types.Str(this.name));
    }

    @org.python.Method(
        __doc__ = "Implement str(self)."
    )
    public org.python.types.Str __str__() {
        return new org.python.types.Str(this.name + "()");
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

    public org.python.Object invoke(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        return this.invoke(null, args, kwargs);
    }

    public org.python.Object invoke(org.python.Object instance, org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
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

            java.lang.Object [] adjusted_args = this.adjustArguments(args, kwargs);

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
                e.getTargetException().printStackTrace();
                // If the Java method raised an Python exception, re-raise that
                // exception as-is. If it wasn"t a Python exception, wrap it
                // as one and continue.
                throw (org.python.exceptions.BaseException) e.getCause();
            } catch (ClassCastException java_e) {
                java.lang.String message = e.getCause().getMessage();
                if (message == null) {
                    message = e.getCause().getClass().getName();
                }
                throw new org.python.exceptions.RuntimeError(message);
            }
        } finally {
        //     org.Python.debug("INVOKE METHOD DONE");
        }
    }
}
