==============================
Haskell Language
==============================

.. contents::
    :local:


予約語(Keywords)
=====================

- http://www.haskell.org/haskellwiki/Keywords

Prelude
====================

- http://www.haskell.org/ghc/docs/latest/html/libraries/base/Prelude.html
- http://www.haskell.org/onlinereport/standard-prelude.html

Template Haskell
========================

- コンパイル時のメタプログラミング

- http://www.haskell.org/haskellwiki/Template_Haskell

関数
=====

.. glossary::

    関数
    Function
        - http://www.haskell.org/tutorial/functions.html

- 関数名は先頭が小文字でなければならない。
- 記号を含むことはできない。

::

    関数名 引数リスト = 関数定義

.. code-block:: haskell

    myAdd x y = x + y

関数の中から関数を呼ぶ

.. code-block:: haskell

    mySum a b c d = myAdd a b  + myAdd c d 

アポストロフィ
--------------

- 関数名の最後についているアポストロフィ(')は特に文法上は意味がない
- 慣習的には遅延関数じゃない正確版とか、内容が変わった関数をもう一つ定義するとかの時に使う。

.. code-block:: haskell

    Prelude> let add'''''''' a b = a + b
    Prelude> add'''''''' 3 4
    7

コメント
=========

行:

.. code-block:: haskell

    -- comment line like as  "#" in Python or "//" in C++

ブロック:

.. code-block:: haskell

    {-  
        Here is a blocked commentsas like as  "/*blocked comments*/"  in C++
    -}

論理演算
=========

.. code-block:: haskell

    Prelude> True && False
    False
    Prelude> True || False
    True
    Prelude> True && True
    True
    Prelude> not False
    True
    Prelude> not ( True && True )
    False

.. code-block:: haskell

    Prelude> True == True
    True
    Prelude> True /= False
    True


畳み込み
=========

- http://jutememo.blogspot.jp/2008/06/haskell-foldl-foldr.html

