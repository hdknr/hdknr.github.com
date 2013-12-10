=====
Case 
=====

.. contents::
    :local:

.. glossary::

    case
        -  :ref:`case.about` 

.. _case.about:

case式
=======

- :term:`式` である。
- 分岐:変数の指定した値に対するコードブロックを評価することができる。(?)
- パターンマッチ:caseによりコード中のどこでも :term:`パターンマッチ` が使えるようになる。

Syntax
=========

.. code-block:: haskell

    case expression of  pattern -> result
                        pattern -> result 
                        pattern -> result 
                        ...

Sytax Sugar
===================

関数パターンマッチ
------------------------------

- 実際、関数のパターンマッチは case式の :term:`構文糖衣` です。

.. code-block:: haskell
    
    Prelude> :{
    Prelude| let
    Prelude| head' :: [a] -> a
    Prelude| head' [] = error "no head for empty lists!"
    Prelude| head' (x:_) = x
    Prelude| :}
    
    Prelude> head' [1..3]
    1


.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude| head' :: [a] -> a
    Prelude| head' xs = case xs of [] -> error "Empty" 
    Prelude|                       (x:_) -> x
    Prelude| :}

    Prelude> head' [1..3]
    1

if
----

- :doc:`if` も case の :term:`構文糖衣`


.. code-block:: haskell

    Prelude> let color a = if a == 1 then "White" else "Black"
    Prelude> color 1
    "White"

.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude| color a = case a of 1 -> "White"
    Prelude|                     _ -> "Black"
    Prelude| :}

    Prelude> color 1
    "White"
    Prelude> color 2
    "Black"

.. code-block:: haskell

    Prelude> let color a = case a of { (1) -> "White" ; (_) ->  "Black"}

    Prelude> color 1
    "White"


ガード
======

- http://d.hatena.ne.jp/kazu-yamamoto/20110826/1314352340

その他
=========

パターンに一致しないとランタイムエラー
------------------------------------------------

.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude| sign a = case a of 1 -> 'A'
    Prelude|                    2 -> 'B'
    Prelude|                    3 -> 'C'
    Prelude| :}
    Prelude> sign 1
    'A'
    Prelude> sign 3
    'C'
    Prelude> sign 4
    *** Exception: <interactive>:(39,10)-(41,27): Non-exhaustive patterns in case



ワイルドカード (_)
--------------------

- 絶対起こりえないパターンはワイルドカードにする

.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude| yesno :: Char -> String
    Prelude| yesno a = case a of 'Y' -> "Yes"
    Prelude|                     'N' -> "No"
    Prelude|                     _   -> "?"
    Prelude| :}

    Prelude> yesno 'Y'
    "Yes"
    Prelude> yesno 'N'
    "No"
    Prelude> yesno 'x'
    "?"

whant & where
----------------


.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude| yesno :: Char -> String
    Prelude| yesno a = "Your anser is " ++ what a
    Prelude|     where  what 'Y' =  "Yes!"
    Prelude|            what 'N' =  "No.."
    Prelude|            what _   =  "?"
    Prelude| :}

    Prelude> yesno 'Y'
    "Your anser is Yes!"
    Prelude> yesno 'N'
    "Your anser is No.."
    Prelude> yesno '*'
    "Your anser is ?"

Others
========

- www.haskell.org/haskellwiki/Case
- http://www.sampou.org/haskell/tutorial-j/patterns.html
- http://zvon.org/other/haskell/Outputsyntax/caseQexpressions_reference.html
- http://www.haskell.org/tutorial/patterns.html#sect4.3

- A case expression must have at least one alternative 
  and each alternative must have at least one body. 

  Each body must have the same type, 
  and the type of the whole expression is that type. 


.. code-block:: haskell

    Prelude> case 2 of { (1) -> "A"; (2) -> "B"; (3) -> "C" }
    "B"
    Prelude> case 1 of { (1) -> "A"; (2) -> "B"; (3) -> "C" }
    "A"
    Prelude> case 3 of { (1) -> "A"; (2) -> "B"; (3) -> "C" }
    "C"
    Prelude> case 4 of { (1) -> "A"; (2) -> "B"; (3) -> "C" }
    "*** Exception: <interactive>:28:1-48: Non-exhaustive patterns in case
    
.. code-block:: haskell

    Prelude> case 4 of { (1) -> "A"; (2) -> "B"; (3) -> "C" ; (a) -> "Other" }
    "Other"
    
    
.. code-block:: haskell
    
    Prelude> let answer a = case a of { (1) -> "A"; (2) -> "B"; (3) -> "C" ; (a) -> "Other"}
    
    Prelude> answer 1
    "A"
    Prelude> answer 2
    "B"
    Prelude> answer 43
    "Other"


Tips
=====

お勧めの書き方
----------------

- http://d.hatena.ne.jp/kazu-yamamoto/20110826/1314352340 

- let はなるべく使わない。where を使う。
- case はなるべく使わない。関数のトップレベル分岐を使う。

    - case を使いたい場合は、
      where の中に、トップレベル分岐を使ってローカル関数を定義すると読みやすくなるかも
