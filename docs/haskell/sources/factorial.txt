===============
階乗:Factorial
===============


.. contents::
    :local:


Python
========

.. code-block:: python

    >>> def factorial(i):
    ...     if i < 2 :
    ...         return 1
    ...     return  i * factorial( i - 1 )
    ... 
    >>> factorial(5)
    120

Haskell
=========

.. code-block:: haskell

    Prelude> let factorial n = if n < 2 then 1 else n * factorial (n-1)
    Prelude> factorial 5
    120



