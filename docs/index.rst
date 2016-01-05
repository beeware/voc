VOC
===

.. image:: _static/logo.png
    :target: https://pybee.org/voc

**VOC is an early alpha project. If it breaks, you get to keep all the shiny pieces.**

VOC is a transpiler that takes Python 3.4 source code, and compile it into a Java
class file that can then be executed on a JVM, or run through a DEX tool to
run on Android. It does this *at the bytecode level*, rather than the source code level.

It honors Python 3.4 syntax and conventions, but also provides the ability to
reference objects and classes defined in Java code, and implement interfaces
defined in Java code.

.. toctree::
   :maxdepth: 2
   :glob:

   intro/index
   tutorials/index
   howto/index
   topics/index
   reference/index
   internals/index
