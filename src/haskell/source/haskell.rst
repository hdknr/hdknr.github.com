==============================
Haskell:ノート
==============================

.. contents::
    :local:


.. _haskell.install:

Install
================

Debian
--------------------

haskel-platform を入れる
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ sudo aptitide install haskel-platform

ghci
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    hdknr@wzy:~$ ghci
   
    GHCi, version 7.4.1: http://www.haskell.org/ghc/  :? for help
    Loading package ghc-prim ... linking ... done.
    Loading package integer-gmp ... linking ... done.
    Loading package base ... linking ... done.
    Prelude> ^D
    Leaving GHCi.



cabal パッケージマネージャ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    hdknr@wzy:~$ cabal --version

    cabal-install version 0.14.0
    using version 1.14.0 of the Cabal library 


virthualenv
---------------

ディレクトリ用意
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    hdknr@wzy:~$ mkdir -p hve/sandbox
    hdknr@wzy:~$ cd hve/sandbox/


作成
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    hdknr@wzy:~/hve/sandbox$ virthualenv

    Creating Virtual Haskell directory structure
    Installing GHC
    Initializing GHC Package database at /home/hdknr/hve/sandbox/.virthualenv/ghc_pkg_db
    Copying necessary packages from original GHC package database
      Failed to copy optional package ghc-binary from system's GHC:
        ghc-pkg process failed with status 1
    Installing cabal config at /home/hdknr/hve/sandbox/.virthualenv/cabal/config
    Installing activate script
    Installing cabal wrapper using /home/hdknr/hve/sandbox/.virthualenv/cabal/config at /home/hdknr/hve/sandbox/.virthualenv/bin/cabal
    Updating cabal package database inside Virtual Haskell Environment.
    
    To activate the new environment use 'source .virthualenv/bin/activate'

アクティベート
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    hdknr@wzy:~/hve/sandbox$ source .virthualenv/bin/activate
    Activating sandbox Virtual Haskell Environment (at /home/hdknr/hve/sandbox).
    
    Use regular Haskell tools (ghc, ghci, ghc-pkg, cabal) to manage your Haskell environment.
    
    To exit from this virtual environment, enter command 'deactivate'.

Cabal
======

- 一覧

.. code-block:: bash

    $ cabal list --installed 


cabal-dev
------------

- `cabal-dev インストール   <_static/haskell/cabal-dev.install.txt>`_

    .. code-block:: bash

        $ cabal install cabal-dev --force-reinstalls

.. _haskell.hackage:

Hackage(HackageDB)
====================

- http://hackage.haskell.org/packages/hackage.html

Yesod
=======

- Web Framework for Haskell : http://www.yesodweb.com/

プロジェクト生成
-----------------

生成:

.. code-block:: bash

    (sandbox)hdknr@wzy:~/hve/sandbox/tutor$ yesod init

実行:

.. code-block:: bash

    (sandbox)hdknr@wzy:~/hve/sandbox/tutor/tutor$ yesod --dev devel


Language
=====================

予約語(Keywords)
--------------------

- http://www.haskell.org/haskellwiki/Keywords

Prelude
---------

- http://www.haskell.org/ghc/docs/latest/html/libraries/base/Prelude.html
- http://www.haskell.org/onlinereport/standard-prelude.html

Template Haskell
------------------------

- コンパイル時のメタプログラミング

- http://www.haskell.org/haskellwiki/Template_Haskell


コメント
---------

行:

.. code-block:: haskell

    -- comment line like as  "#" in Python or "//" in C++

ブロック:

.. code-block:: haskell

    {-  
        Here is a blocked commentsas like as  "/*blocked comments*/"  in C++
    -}

論理演算
---------

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
---------

- http://jutememo.blogspot.jp/2008/06/haskell-foldl-foldr.html


ghci
=========

:{ ブロック :}
---------------------

.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude|    add a b 
    Prelude|       = a + b
    Prelude| :}
    Prelude> add 8 3
    11

ロード ( :l, :load )
-------------------------

.. code-block:: haskell


    (sandbox)hdknr@wzy:~/hve/sandbox/tutor/sample$ more add.hs 

    add a b = a + b


.. code-block:: haskell

    (sandbox)hdknr@wzy:~/hve/sandbox/tutor/sample$ ghci
    GHCi, version 7.4.1: http://www.haskell.org/ghc/  :? for help
    Loading package ghc-prim ... linking ... done.
    Loading package integer-gmp ... linking ... done.
    Loading package base ... linking ... done.
    Prelude> :l add.hs
    [1 of 1] Compiling Main             ( add.hs, interpreted )
    Ok, modules loaded: Main.
    \*Main> add 7 3
    10

設定 (:set)
---------------

プンプト
^^^^^^^^^^

.. code-block:: haskell

    Prelude> :set prompt katsu-curry>
    katsu-curry>

Resource
=========

API
------

- Hoogle : http://www.haskell.org/hoogle/

Terms
--------

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

    純粋関数型プログラミング言語
        - http://ja.wikipedia.org/wiki/関数型言語
        - 「コンピュータに何であるか、を伝える。」 

    モナド
    Monads
    Monad
        - http://ja.wikipedia.org/wiki/%E3%83%A2%E3%83%8A%E3%83%89_(%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0)
        - モナドは三つの条件を満たす抽象的なデータ型である。(http://d.hatena.ne.jp/anatoo/20100305/1267801847)

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
