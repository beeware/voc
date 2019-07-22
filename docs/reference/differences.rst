Differences between VOC and CPython
===================================

StopIteration
-------------

A ``StopIteration`` is a signal raised by an iterator to tell whomever is
iterating that there are no more items to be produced. This is used in ``for``
loops, generator functions, etc. The ``org.python.exception.StopIteration``
exception differs from the CPython ``StopIteration`` exception in that it is a
singleton. This was introduced in `PR #811<https://github.com/beeware/voc/pull/881>`_
as part of a performance effort as it yields a non-trivial performance improvement
for nested ``for`` loops. However, it also means that an equality comparison
between two ``StopIteration`` exceptions will always be ``True``, which is not
the case in CPython.
