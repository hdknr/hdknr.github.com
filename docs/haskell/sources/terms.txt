==============================
用語
==============================

.. contents::
    :local:

用語
========

.. glossary::

    参照透過性
    参照透明性
    Referential Transparency
        - http://ja.wikipedia.org/wiki/%E5%8F%82%E7%85%A7%E9%80%8F%E9%81%8E%E6%80%A7
        - 関数に与えられる入力が同じであれば、いつでも同じ結果を返す。 (後でやっても良い -> :term:`遅延評価` )
        - べきとうせい ( http://ja.wikipedia.org/wiki/冪等 )

    Side Effect
    副作用
        - http://en.wikipedia.org/wiki/Side_effect_(computer_science)
        - 作用:算数の動作結果。 副作用:作用以外で何かが変更されること。(グローバルステート、ローカルスタティックなど)

    命令型プログラミング言語
        - http://ja.wikipedia.org/wiki/命令型プログラミング
        - 手続き型プログラミングと同義 
        - 「コンピュータに何をするかを伝える。」

    関数型言語
    Functional Language
        - 関数型プログラミングに向いた特徴を持つプログラミング言語、関数型プログラミング言語である。
          引数に関数を作用（applicate）させて計算をおこなうことから、
          作用型言語（applicational language）ともいう。
          データフロープログラミング言語も関数型言語の一種である。 
          ( `関数型言語(Wikipedia) <http://ja.wikipedia.org/wiki/%E9%96%A2%E6%95%B0%E5%9E%8B%E8%A8%80%E8%AA%9E>`_ )

        - 分類

            +---------------+---------------+---------------+
            |  関数型言語   | 型            | 言語          |
            +===============+===============+===============+
            |  純粋         | 強い静的      | Clean         |
            |               |               +---------------+
            |               |               | Haskell       |
            |               |               +---------------+
            |               |               | Miranda       |  
            |               +---------------+---------------+
            |               | 型無し        | Lazy K        |
            +---------------+---------------+---------------+
            | 非純粋        | 静的          | ML            |
            |               |               +---------------+
            |               |               | OCaml         |
            |               |               +---------------+
            |               |               | Scala         |
            |               |               +---------------+
            |               |               | F#            |
            |               +---------------+---------------+
            |               | 動的          | Erlang        |
            |               |               +---------------+
            |               |               | Lisp          |
            |               |               +---------------+
            |               |               | Scheme        | 
            |               +---------------+---------------+
            |               | 型無し        | Unlambda      |
            +---------------+---------------+---------------+
            

    純粋関数型プログラミング言語
        - http://ja.wikipedia.org/wiki/関数型言語
        - 「コンピュータに何であるか、を伝える。」 
        - :term:`参照透過性` が常に保たれるという意味において、
          全ての式や関数は :term:`副作用` を持たない。

    モナド
    Monads
    Monad
        - `Monad(Wikpedia) <http://ja.wikipedia.org/wiki/%E3%83%A2%E3%83%8A%E3%83%89_%28%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%29>`_ 
        - `モナドは三つの条件を満たす抽象的なデータ型である <http://d.hatena.ne.jp/anatoo/20100305/1267801847>`_ 。

            - モナドは他のデータ型を包み込む
            - モナドは前述したような包み込みを行う操作を持つ。紛らわしいことにこれはreturnと呼ばれる
            - モナドはモナドを返すある関数に対してモナド内部の値を提供することを許可するbindと呼ばれる操作を持つ

    darcs
        - http://darcs.net
        - Haskellで書かれたDVCS


    遅延評価
    Lazy Evaluation
    Delayed Evaluation
        - http://ja.wikipedia.org/wiki/遅延評価
        

    Haskel Platform
        - :ref:`haskell.install`

    中置関数
    中置演算子
        - http://www.haskell.org/haskellwiki/Infix_operator
        - http://hdknr.posterous.com/32-a-gentle-introduction-to-haskell-functions
        - 「Haskell の場合，任意の関数 f に対し， `f` のように `（バッククオート）で囲むことにより
          中置演算子（infix operator）として用いることができる．」 
          `λx.x K S K ＠ はてな　: ■[OCaml] #004 中置演算子化 <http://d.hatena.ne.jp/KeisukeNakano/20060810/1155347324>`_

    総称性
    Generics
        - さまざまな型に対応するために、型をパラメータとして与えて、その型に対応したクラスや関数を生成するもの機能
        
            - Generic Class, Generic Method, Generic Function

        - Haskell : 引数の型によって動作を変えるような関数を総称関数と言う。 
          例えば (==), (>), (<), ...は引数によって比較の方法を変化させています。

    総称関数
    総称的関数
    Generic Function
        - 「Haskell では総称関数の組のことを class と呼びます」  
            

    型推論
    Type Inference 
        - 型を明示的に書かなくても適切な型（できるだけ広く適用できる型）を自動的に付けてくれます

    型変数
    Type Variable
        - 任意の型に置き換えることができる変数。


    代数的データ型
    Agebraic Data Type
        - (TBD)

    型構成子
    型構築子
    Type Constructor
        - (TBD)

    データ構成子
    データ構築子
    Data Constructor
        - (TBD)


    部分型多相
    Subtype Polymorphism
        - (TBD)

    ランクN多相性
    Rank-N Polymorphism
        - (TBD)

    高階関数
    HigherjOrder Function
    Higher-Order Function
        - :doc:`higer_order_function`

    型構成子クラス
    型構築子クラス
    type constructor class
        - Functorクラスのように
          型構成子に対して関数のインタフェース（関数名と関数の型）を定義したもの

        
    圏論
    カテゴリー論
    Category Theory
        - (TBD)
 

    構文糖衣
    Syntax Sugar
        - (TBD)


    パターンマッチ
    Pattern Match
        - (TBD)

    式
        - (TBD)
    
