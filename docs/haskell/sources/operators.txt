==============================
演算子: Operators
==============================

.. contents::
    :local:


.. glossary::

    関数適用演算子
    Function Application Operator
        - :ref:`ドル($)記号 <operator.dollar>`


演算子
===========

Comments
----------

    ==========  ========================
    演算子      内容
    ==========  ========================
    --          Start of comment line
    {-          Start of short comment
    -}          End of short comment
    ==========  ========================

Math&Boolean
--------------

    ==========  ========================
    演算子      内容
    ==========  ========================
    +           Add operator
    -           Subtract/negate operator
    *           Multiply operator
    /           Division operator
                Substitution operator, as in e{f/x}
    ^, ^^, **   Raise-to-the-power operators
    &&          And operator
    ||          Or operator
    ==========  ========================


Relational
--------------

    ==========  ========================
    演算子      内容
    ==========  ========================
    <           Less-than operator
    <=          Less-than-or-equal operator
    ==          Equal operator
    /=          Not-equal operator
    >=          Greater-than-or-equal operator
    >           Greater-than operator
    ==========  ========================

Lambda/Function
----------------------

    ==========  ================================================
    演算子      内容
    ==========  ================================================
    \\          Lambda operator
    .           Function composition operator
                Name qualifeer
    |           Guard and case specifier
                Separator in list comprehension
                Alternative in data denition (enum type)
    ==========  ================================================

List
------

    ==========  =====================================================================
    演算子      内容
    ==========  =====================================================================
    ++          :ref:`List concatenation operator <list.concat>`
    :           :ref:`Append-head operator ("cons") <list.cons>`
    !!          :ref:`Indexing operator <list.index>`
    ..          Range-specifier for lists
    \\          List-difference operator
    <-          List comprehension generator
                Single assignment operator in do-constr.
    ==========  =====================================================================


Type
-------

    ==========  =====================================================================
    演算子      内容
    ==========  =====================================================================
    ;           Definition separator
    ->          Function type-mapping operator.
                Lambda definition operator
                Separator in case construction
    =           Type- or value-naming operator
    \:\:        :ref:`Type specification operator, has type <type.operator>`
    =>          Context inheritance from class
    ()          Empty value in IO () type
    >>          Monad sequencing operator
    >>=         Monad sequencing operator with value passing
    >@>         Object composition operator (monads)
    (..)        Constructor for export operator (postfix)
    ==========  =====================================================================

Constructor
---------------------


    ==========  ================================================
    演算子      内容
    ==========  ================================================
    [ and ]     List constructors, "," as separator
    ( and )     Tuple constructors, "," as separator
                Infxx-to-prefix constructors
    ` and `     Prefix-to-infix constructors
    ' and '     Literal char constructors
    " and "     String constructors
    _           Wildcard in pattern
    ~           Irrefutable pattern
    !           Force evaluation (strictness flag)
    @           "Read As" in pattern matching
    ==========  ================================================

.. _operator.dollar:

関数適用演算子
==================

.. code-block:: haskell

    Prelude> :i $
    ($) :: (a -> b) -> a -> b       -- Defined in `GHC.Base'
    infixr 0 $



- 右結合。 (スペースを使った関数適用は左結合)
- 優先順位が低いので、$より右側の式を$に与えてくれる。つまり $(右側の式の結果)

.. code-block:: haskell

    Prelude> sqrt (3+4+9)
    4.0
    Prelude> sqrt $ 3+4+9
    4.0

print 2^2 は (print 2) ^ 2 なので、エラーになる。よって

.. code-block:: haskell

    Prelude> print 2^2

    <interactive>:11:8:
        No instance for (Num (IO ()))
          arising from a use of `^'
        Possible fix: add an instance declaration for (Num (IO ()))
        In the expression: print 2 ^ 2
        In an equation for `it': it = print 2 ^ 2

    Prelude> print $ 2^2
    4

ながいカッコで式を簡潔に

.. code-block:: haskell

    Prelude> sum (filter (>10) (map (*2) [2..10]))
    80
    Prelude> sum $ filter (>10) $ map (*2) [2..10]
    80
    
    Prelude> --** 


関数適用の受け皿として$を使えるので

.. code-block:: haskell

    Prelude> map($ 3)[ (4+),(10*),(^2),sqrt]
    [7.0,30.0,9.0,1.7320508075688772]


Pythonだと

.. code-block:: python

    >>> from math import sqrt
    >>> map(lambda x:x(3),[ lambda x:x+4, lambda x:x*10, lambda x:x**2, lambda x:sqrt(x)])
    [7, 30, 9, 1.7320508075688772]
