====
型
====

.. contents::
    :local:

.. glossary::

    型
    タイプ
    Type
        - http://www.haskell.org/haskellwiki/%E5%9E%8B
        - http://www.haskell.org/tutorial/goodies.html

.. _type.operator:

型指定(::)
==============

- 値 :: A型　で「値はAという型を持つ」

.. code-block:: haskell

    Prelude> let a=1
    Prelude> :info a
    a :: Integer    -- Defined at <interactive>:2:5
    Prelude> let b=1 :: Int
    Prelude> :info b
    b :: Int        -- Defined at <interactive>:4:5

明示的型
===========

- 関数の明示的宣言。
- 矢印の最後はreturnの値の型

.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude| onlyCap :: [Char] -> [Char]
    Prelude| onlyCap s = [ c | c <- s, c `elem` ['A' .. 'Z']]
    Prelude| :}
    Prelude> onlyCap "Hello World!"
    "HW"    



.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude| adds :: Int -> Int -> Int -> Int
    Prelude| adds x y z = x + y + z
    Prelude| :}
    Prelude> adds 1 2 3
    6


Haskellの型
========================


    ================    ============================
    型                  内容
    ================    ============================
    Int                 整数(有界)
    Integer             整数。限度無し。
    Float               単精度浮動小数点数
    Double              倍精度浮動小数点数
    Bool                真理値型(True,False)
    Char                Unicode 文字
    タプル              要素の最大数は62
    ================    ============================


型変数
========


.. code-block:: haskell

    Prelude> :t head
    head :: [a] -> a

- a: Any(?) = 任意の型
- 型変数を使った関数 = 多相的関数 (polymorphic function)


型クラス
===============

Eq型
--------


Ord型
--------

Show型
--------

Read型
--------

Enum型
--------

Bounded型
------------

Num型
------------

Floating型
------------

Integral型
------------

Integral型
------------




