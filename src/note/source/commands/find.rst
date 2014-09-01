=====================
find コマンド
=====================

.. contents::
    :local:

.svn ディレクトリを除外する
============================

'-prune' を使う

.. code-block:: bash

    $ find -type d -name ".svn" -prune -o -type f "jquery*" -print

サイズで探す
===============

20Mバイト以上のファイル
----------------------------

単純:

.. code-block:: bash

    $ find /home -size +20M

サイズを表示して大きい順にソート:

.. code-block:: bash

    $ find /home -type f -size +20000k -exec ls -lh {} \; 2> /dev/null | awk '{ print $NF ": " $5 }' | sort -nrk 2,2
