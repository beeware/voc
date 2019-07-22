.. raw:: html

    <style>
        .row {clear: both}

        .column img {border: 1px solid black;}

        @media only screen and (min-width: 1000px),
               only screen and (min-width: 500px) and (max-width: 768px){

            .column {
                padding-left: 5px;
                padding-right: 5px;
                float: left;
            }

            .column3  {
                width: 33.3%;
            }

            .column2  {
                width: 50%;
            }
        }
    </style>


===
VOC
===

VOC is a transpiler that takes Python 3.4+ source code, and compiles it into a Java
class file that can then be executed on a JVM, or run through a DEX tool to
run on Android. It does this *at the bytecode level*, rather than the source code level.

It honors Python 3.4+ syntax and conventions, but also provides the ability to
reference objects and classes defined in Java code, and implement interfaces
defined in Java code.

.. rst-class::  row

Table of contents
=================

.. rst-class:: clearfix row

.. rst-class:: column column2


:ref:`Tutorial <tutorial>`
--------------------------

Get started with a hands-on introduction for beginners


.. rst-class:: column column2

:ref:`How-to guides <how-to>`
-----------------------------

Guides and recipes for common problems and tasks, including how to contribute


.. rst-class:: column column2

:ref:`Background <background>`
------------------------------

Explanation and discussion of key topics and concepts


.. rst-class:: column column2

:ref:`Reference <reference>`
----------------------------

Technical reference - commands, modules, classes, methods


.. rst-class:: clearfix row

Community
=========

VOC is part of the `BeeWare suite`_. You can talk to the community through:

 * `@pybeeware on Twitter`_

 * `beeware/general on Gitter`_

.. _BeeWare suite: https://beeware.org
.. _Read The Docs: https://voc.readthedocs.io
.. _@pybeeware on Twitter: https://twitter.com/pybeeware
.. _beeware/general on Gitter: https://gitter.im/beeware/general


.. toctree::
   :maxdepth: 2
   :hidden:
   :titlesonly:

   tutorial/index
   how-to/index
   background/index
   reference/index
