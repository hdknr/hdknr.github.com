================================================
単項演算子:Unary Operator
================================================

.. contents::
    :local:

.. glossary::

    
    単項演算子
    Unary Operator
        - http://www.haskell.org/haskellwiki/Unary_operator

前置き(Prefix Notation)
========================

- Prefix NotationとPostfix Notationがありえるが、Haskellでは Prefix のマイナスのみ。

マイナス(-)
------------

.. code-block:: haskell

    Prelude> -2
    -2    

    Prelude> :i -
    class Num a where
      ...
      (-) :: a -> a -> a
      ...
            -- Defined in `GHC.Num'
    infixl 6 -

- 単項マイナスは数値演算リテラル(Numeric Literals)であるべきか、オペレータであるべきかの議論があったが、今は後者。
- 実際は Prelude 関数 negate の 糖衣構文(Syntax Sugar)


Sectioning不可
-------------------------

例えば、リストの要素から2を引く時には、

.. code-block:: haskell

    map(-2) 

ではなく、

.. code-block:: haskell

    map(subtract 2) 

とすること。

