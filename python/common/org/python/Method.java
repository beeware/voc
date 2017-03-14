package org.python;

@java.lang.annotation.Retention(java.lang.annotation.RetentionPolicy.RUNTIME)
public @interface Method {
    java.lang.String name() default "";
    java.lang.String __doc__() default "";
    java.lang.String[] args() default {};
    java.lang.String varargs() default "";
    java.lang.String[] default_args() default {};
    java.lang.String[] kwonlyargs() default {};
    java.lang.String kwargs() default "";
}
