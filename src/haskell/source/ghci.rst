==============================
ghci
==============================

.. contents::
    :local:

.. glossary::

    ghci
        - http://www.haskell.org/ghc/docs/7.4.2/html/users_guide/ghci.html

    it
        - :ref:`ghci.it`

ghci
=========

プロセス
------------


::

    26915 pts/23   Sl+    0:06 /usr/lib/ghc/lib/ghc -B/usr/lib/ghc --interactive

.. _ghci.it:

it変数
---------

- http://www.haskell.org/ghc/docs/7.4.2/html/users_guide/interactive-evaluation.html#id549402
- expression(正確に言うと、non-binding statement )が入力されると、自動的に it に束縛(bind)されます。
- IOタイプが必用で、IOタイプがなければexpressionであるeを次のように変換して、IO-actionとして動作させます。

    .. code-block:: haskell

        let it = e;
        print it

- :ref:`Show` クラスのインスタンスで無ければ、エラーになります。

    .. code-block:: haskell

        Prelude> id
        
        <interactive>:30:1:
            No instance for (Show (a0 -> a0))
              arising from a use of `print'
            Possible fix: add an instance declaration for (Show (a0 -> a0))
            In a stmt of an interactive GHCi command: print it

- If the expression was instead of type IO a for some a, then it will be bound to the result of the IO computation, which is of type a. eg.:

    .. code-block:: haskell

        Prelude> import System.Time
        Prelude System.Time> getClockTime
        Loading package old-locale-1.0.0.4 ... linking ... done.
        Loading package old-time-1.1.0.0 ... linking ... done.
        Fri Oct  5 02:29:15 JST 2012
        
        Prelude System.Time> :info it
        it :: ClockTime         -- Defined at <interactive>:39:1

        Prelude System.Time> print it
        Fri Oct  5 02:29:15 JST 2012
        Prelude System.Time> :info it
        it :: ()        -- Defined at <interactive>:45:1

 


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

プロンプト
^^^^^^^^^^^^^^^^

.. code-block:: haskell

    Prelude> :set prompt katsu-curry>
    katsu-curry>
