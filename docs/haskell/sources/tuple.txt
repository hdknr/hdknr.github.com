==================
タプル:Tuple
==================

.. contents::
    :local:

タプルとは？
=============

- 複数の異なる型の要素を格納して１つの値にする
- タプルはサイズが固定 ( リストは拡張できる )

Python
-------

.. code-block:: python

    >>> (1,'A',"Haskell")
    (1, 'A', 'Haskell')    

    >>> (1,2,3)[0]
    1


    >>> (1,2,3)[100]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: tuple index out of range

    >>> (1,2,3)[-1]
    3
    >>> (1,2,3)[-2]
    2
    >>> (1,2,3)[-3]
    1
    >>> (1,2,3)[-4]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: tuple index out of range
    

Haskell
----------

.. code-block:: haskell

    Prelude> (1,'A',"Haskell")
    (1,'A',"Haskell")
    
    
    Prelude> (1,2,3)[0]
    
    <interactive>:3:1:
        The function `(1, 2, 3)' is applied to one argument,
        but its type `(t0, t1, t2)' has none
        In the expression: (1, 2, 3) [0]
        In an equation for `it': it = (1, 2, 3) [0]



ペア
=====

- 2要素のタプル

fst / snd
-----------

.. code-block:: haskell

    Prelude> fst (1,2)
    1
    Prelude> snd (1,2)
    2
    Prelude> fst (1,2,3)
    
    <interactive>:6:5:
        Couldn't match expected type `(a0, b0)'
                    with actual type `(t0, t1, t2)'
        In the first argument of `fst', namely `(1, 2, 3)'
        In the expression: fst (1, 2, 3)
        In an equation for `it': it = fst (1, 2, 3)

zip
------

- ２つのリストからペアを作る

.. code-block:: haskell

    Prelude> zip [1..10] ['a','b','c']
    [(1,'a'),(2,'b'),(3,'c')]


