========================
Logging
========================

.. contents:: ログ管理

Celery本体
===========

rogloateでcopytruncateを使う単純な例
---------------------------------------------------------------

::

     /var/log/celery/*.log {
             weekly
             missingok
             rotate 52
             compress
             delaycompress
             notifempty
             copytruncate
     }

トランザクションが多いとログがロストするでしょう。

logger経由
------------------------------------

::

    nohup <任意のコマンド> | logger -p local0.err &

.. todo::

    - logger動作確認

Worker
=======

Python の標準ロギング
-----------------------

.. todo::

    - ロギング定義の記述
    - ローテーション可能
