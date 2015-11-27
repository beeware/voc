package org.python;

@java.lang.annotation.Retention(java.lang.annotation.RetentionPolicy.RUNTIME)
public @interface Method {
    java.lang.String name() default "*";
    java.lang.String __doc__() default "";
}
