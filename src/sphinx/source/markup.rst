============
マークアップ
============

.. contents::
    :local:

コード
============

- :ref:`sphinx:code-examples`

\.\. literalinclude\:\: フィル名
-----------------------------------

- 「ファイル名」のファイルを読み込みます
- \:language\: で **言語** を指定できます
- \:emphasize-lines\: で指定行を **強調** できます
- \:linenos\: で **行番号** を付与します

.. code-block:: rst

    .. literalinclude:: example.rb
       :language: ruby
       :emphasize-lines: 12,15-18
       :linenos:

\.\. include\:\: フィル名
-----------------------------------

- ファイルをrstのまま読み込みます
- :ref:`markup.orphan` 使った方がいいかと 


ファイルレベルメタデータ
==========================

- :ref:`sphinx:metadata`

ファイル
------------------


.. _markup.orphan:

\:orphan\:
^^^^^^^^^^^^^^^

.. code-block:: rst

    :orphan:

- toctreeから参照されていない時に出力される警告が抑制されます
- includeされる rst の先頭に入れるとか


メタ情報
-----------


タグベースインクルード
------------------------

テーブル
------------------------


