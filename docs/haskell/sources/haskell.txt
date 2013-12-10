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


Haskellの実行
===============

1.  対話式インタプリタ(ghci)
------------------------------

- :doc:`ghci` で対話実行できます。

.. code-block:: haskell

    (sandbox)hdknr@wzy:~/hve/sandbox/tutor$ ghci
    GHCi, version 7.4.1: http://www.haskell.org/ghc/  :? for help
    Loading package ghc-prim ... linking ... done.
    Loading package integer-gmp ... linking ... done.
    Loading package base ... linking ... done.

    Prelude> putStrLn "Hey Joe"
    Hey Joe

2.  スクリプトランナー(runghc)
----------------------------------

.. code-block:: haskell

    (tact)hdknr@wzy:~/ve/tact/src$ cat hello.hs 
    main = putStrLn "Hey Joe"

    (tact)hdknr@wzy:~/ve/tact/src$ runghc hello.hs 
    Hey Joe

3.  コンパイラ(ghc)
----------------------

.. code-block:: bash

    (tact)hdknr@wzy:~/ve/tact/src$ ghc hello.hs 
    [1 of 1] Compiling Main             ( hello.hs, hello.o )
    Linking hello ...

    (tact)hdknr@wzy:~/ve/tact/src$ ls hell*
    hello  hello.hi  hello.hs  hello.o

    (tact)hdknr@wzy:~/ve/tact/src$ ./hello 
    Hey Joe

    (tact)hdknr@wzy:~/ve/tact/src$ file hello
    hello: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), 
    dynamically linked (uses shared libs), 
    for GNU/Linux 2.6.26, BuildID[sha1]=0x0fd60bbab2809046d0d303ea555e99984f331dc4, not stripped


ドキュメント
============

- http://www.haskell.org/haddock/
- http://www.haskell.org/haddock/doc/html/index.html

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


Resource
=========

Haskell Hierarchical Libraries
------------------------------------------

- http://www.haskell.org/ghc/docs/latest/html/libraries/index.html

API
------

- Hoogle : http://www.haskell.org/hoogle/


