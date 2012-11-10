========
文字列
========


.. contents::
    :local:


標準出力
===========

putStr,putStrLn
------------------------

.. code-block:: haskell

    (sandbox)hdknr@wzy:~/hve/sandbox$ ghci
    GHCi, version 7.4.1: http://www.haskell.org/ghc/  :? for help
    Loading package ghc-prim ... linking ... done.
    Loading package integer-gmp ... linking ... done.
    Loading package base ... linking ... done.
    Prelude> putStr "abc"
    abcPrelude> 
    Prelude> putStrLn "efg"
    efg
    Prelude> 

.. code-block:: haskell

    Prelude> :i putStrLn
    putStrLn :: String -> IO ()     -- Defined in `System.IO'


System.IO.UTF8 : print 関数はユニコード値を出力する
------------------------------------------------------------

.. code-block:: haskell

    Prelude System.IO.UTF8 System.IO> System.IO.putStrLn  "ああああ"
    ああああ
    Prelude System.IO.UTF8 System.IO> System.IO.UTF8.putStrLn  "ああああ"
    ãã



ファイル
=========

書き込む
---------


.. code-block:: haskell

    import System.IO
    
    main = do
        h <- openFile "test.txt" WriteMode
        hSetEncoding h utf8
        hPutStrLn h "テスト"
        hClose h


Codec.Text.IConv
=================

- http://hackage.haskell.org/packages/archive/iconv/0.4.0.2/doc/html/Codec-Text-IConv.html
