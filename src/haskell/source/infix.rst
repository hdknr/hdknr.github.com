===================================================
infix operator:中置演算子
===================================================

.. contents::
    :local:

.. glossary::

    中置関数
    中置演算子
    Infix Operator
    中置記法
    Infix Notation
        - http://www.haskell.org/haskellwiki/Infix_operator
        - http://hdknr.posterous.com/32-a-gentle-introduction-to-haskell-functions
        - 「Haskell の場合，任意の関数 f に対し， `f` のように `（バッククオート）で囲むことにより
          中置演算子（infix operator）として用いることができる．」 
          `λx.x K S K ＠ はてな　: ■[OCaml] #004 中置演算子化 <http://d.hatena.ne.jp/KeisukeNakano/20060810/1155347324>`_


    前置記法 
    Prefix Notation
    ポーランド記法
    Polish Notation 
        - http://ja.wikipedia.org/wiki/ポーランド記法

概要
=====

- http://www.haskell.org/haskellwiki/Infix_operator
- Haskellの関数は基本的に :term:`前置記法`
- + 見たいに :term:`Infix Notation` も可能。 


InfixをPrefixで使う
===================

括弧(parenthesis) で囲むと :term:`Prefix Notation` できる。

.. code-block:: haskell

    Prelude> + 3 3
    
    <interactive>:2:1: parse error on input `+'
    Prelude> (+) 3 3
    6


PrefixをInfixで使う
=======================

バッククオート(`)で囲むと、 :term:`Infix Notaion` できる。

.. code-block:: haskell


    Prelude> let add x y = x + y
    Prelude> add 9 3
    12
    Prelude> 8 `add` 4
    12

ただし、引数が２個の時

.. code-block:: haskell


    Prelude> let square x = x * x
    Prelude> square 2
    4
    Prelude> 2 `square`
    
    <interactive>:7:11: parse error (possibly incorrect indentation)


3対上の場合も基本はダメ

.. code-block:: haskell

    Prelude> let sum a b c = a + b  + c
    Prelude> sum 1 2 3
    6
    Prelude> 1 `sum` 2 3
    
    <interactive>:10:9:
        No instance for (Num (a1 -> a0))
          arising from the literal `2'
        Possible fix: add an instance declaration for (Num (a1 -> a0))
        In the expression: 2
        In the second argument of `sum', namely `2 3'
        In the expression: 1 `sum` 2 3


ただし、

.. code-block:: haskell

    Prelude> (1 `sum` 2  ) 3
    6


.. code-block:: haskell

    Prelude> let sum a b c d = a + b + c + d
    
    Prelude> (1 `sum` 2 ) 3 4
    10

