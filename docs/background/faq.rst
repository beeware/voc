Frequently Asked Questions
==========================

Is VOC a source code converter?
-------------------------------

No. VOC operates *at the bytecode level*, rather than the source code level.
In the initial versions, VOC would take CPython bytecode format (the `.pyc` files
generated at runtime by CPython when the code is imported for the first time),
and convert that
bytecode directly into Java bytecode in a `.class` file.

Currently, VOC uses the Python ``ast`` module to parse the Python code,
and generates the Java bytecode from that.

No intermediate Java source file is generated.

Isn't this the same thing as Jython?
------------------------------------

No. Jython is an implementation of a Python interpreter in Java. This means
it provides a REPL (an interactive prompt), and you *run* your Python code
through Jython. VOC converts Python directly to a Java classfile; The VOC
executable isn't needed at runtime (although there is a runtime support
library that *is* needed).

The `clamped` extension to Jython enable you to use Jython as a generator
of class files - this is a closer analogy to what VOC does.

The easiest way to demonstrate the difference between Jython and VOC is
to look at the `eval()` and `exec()` methods. In Jython, these are key
to how the process works, because they're just hooks into the runtime
process of parsing and evaluating Python code. In VOC, these methods would
be difficult to implement because VOC compiles all the class files up
front. To implement `eval()` and `exec()`, you'd need to run VOC through
VOC, and then expose an API that could be used at runtime to generate
new `.class` files.

How fast is VOC?
----------------

Faster than a slow thing; slower than a fast thing :-)

Programming language performance is always nebulous to quantify. As a
rough guide, it's about an order of magnitude slower than CPython on the
same machine.

This means it probably isn't fast enough for an application that is CPU
bound. However, if this is the case, you can always write your CPU bound
parts in *pure* Java, and call those directly from Python, same as you
would for a CPython extension.

It should also be noted that VOC is a very young project, and very little
time has been spent on performance optimization. There are many obvious
low hanging performance optimizations that could be explored as the project
matures.

What can I use VOC for?
-----------------------

You can use VOC anywhere that provides a Java runtime environment, but you
want to write your logic in Python. For example:

* Writing Android applicaitons

* Writing Lucene/ElasticSearch custom functions

* Writing Minecraft plugins

* Writing web applications to deploy in a J2EE container

In each of these cases, the project provides a Java (or Java-like, in the case
of Android) environment. While some bridging might be possible with JNI, or by
writing a thin Java shim that calls out to another language environment, these
approaches mean you're developing a plugin at arms length.

The VOC approach allows you to develop your Python application *as if it were
native*. The class files even have references to the Python source code, so
when a stack trace is generated, it will tell you the line of Python source
that caused the problem.

What version of Python does VOC require?
----------------------------------------

VOC runs under Python 3.4+.

What version of Java does VOC require?
--------------------------------------

VOC runs on:

* Java 6 without any special handling;
* Java 7 by enabling the `-XX:-UseSplitVerifier` flag at runtime;
* Java 8 by enabling the `-noverify` flag at runtime.

The complication with Java 7 and Java 8 is due to a feature of class files
(called a Stack Map Frame) that was introduced as an optional feature in
Java 6, and has been decreasingly optional in each subsequent release.

It would be entirely possible to generate Stack Map Frames for the generated
class files from the information in a Python class file, but the developers
haven't had a chance to get around to that yet.

Why "VOC"?
----------

The `Vereenigde Oostindische Compagnie (VOC)`_, or Dutch East India Company,
is often considered the be the world's first multinational corporation. It was
also the first company to issue shares, and facilitate the trading of those
shares. It was granted a 21 year monopoly to carry out trade activities in
Asia, primarily the Spice Islands - the Dutch East Indies. They established a
major trading port at Batavia - now Jakarta, on the island of Java (now part
of Indonesia). As a result of their monopoly, the VOC became an incredibly
valuable company, issuing an 18% annual dividend for almost 200 years.

VOC was... the worlds first Enterprise site in Java. (rimshot!)

Can I make an Android app already?
----------------------------------

Yes, but currently you have to use Android Java API (you'll be able to use `toga`_
once `toga-android`_ is more mature).

You can see `here an example TicTacToe app that does that <https://github.com/eliasdorneles/tictactoe-voc>`_.


.. _Vereenigde Oostindische Compagnie (VOC): https://en.wikipedia.org/wiki/Dutch_East_India_Company
.. _toga: https://github.com/beeware/toga
.. _toga-android: https://github.com/beeware/toga-android
