==================
PowerShell
==================

.. contents::
    :local:

設定
=======

シンタックス
----------------

コメント
^^^^^^^^^^

.. code-block:: bash

    # ラインコメント

    <# ブロックコメント開始
       ブロックコメント途中  
       ブロックコメント終了 #>

XML
======

ファイルから読み込んでXPath
--------------------------------

.. code-block:: bash

    foreach($f in ([xml](Get-Content "test.xml")).SelectNodes("//file")  )
    {
        echo $f.id
    }
