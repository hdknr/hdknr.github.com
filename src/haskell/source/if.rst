===============
if-then-else
===============

.. contents::
    :local:

- http://www.haskell.org/haskellwiki/If-then-else


if .. then .. else .. で1セット
====================================

.. code-block:: haskell

    Prelude Data.Ord> let color a = if a == 1 then "White" else "Black" 
    Prelude Data.Ord> color 1
    "White"
    Prelude Data.Ord> color 0
    "Black"

if-then-else 分岐はパターンマッチでも書く事ができる

.. code-block:: haskell


    Prelude> :{
    Prelude| let
    Prelude|    color 1 = "White"
    Prelude|    color n = "Black"
    Prelude| :}

    Prelude> color 1
    "White"
    Prelude> color 0
    "Black"
    Prelude> color 3
    "Black"



