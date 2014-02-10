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
