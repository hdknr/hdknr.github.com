========================
Celeryとは？
========================


分散タスクキュー
===================

- http://celeryproject.org/

::

    Celery is an asynchronous task queue/job queue based on distributed message passing. 
    It is focused on real-time operation, but supports scheduling as well.

    The execution units, called tasks, are executed concurrently 
    on a single or more worker servers using multiprocessing, 
    Eventlet, or gevent. 

    Tasks can execute asynchronously (in the background) or synchronously (wait until ready).

    Celery is used in production systems to process millions of tasks a day.


非同期キュー
------------

- taskキュー
- jobキュー

- 非同期実行 ( your_task.apply_async() / your_task.delay() )
- 同期実行 ( your_task() )

分散メッセージング
------------------------

- 分散ブローカー

リアルタイムオペレーション
------------------------------

- リアルタイムオペレーション
- スケジューリングオペレーション

スケーラブル
-------------

- タスクの同時実行性
- １つ以上のワーカーサーバー
- 非同期I/O ( :term:`eventlet` , :term:`gevent` )


非同期処理
====================

- :ref:`celery:faq-when-to-use`

業務上必要なケース
------------------------------------

- 間にオフライン業務が入るとか 
- 定期的にバックグラウンド処理を行う

スループット
------------------------------------

- リソースのレイテンシが高い(処理能力の非対称性)

    - 零細サーバーへの要求
    - こちらの性能が良すぎる

- キューの登録があふれる

    - メールサーバー
    - クライアントソケット 

- 処理を分散させる

    - プロセス/スレッド
    - コンピュータ 

プログラミングモデル
------------------------

- システム基盤の要求に対するプログラミングの振れ幅を小さくする
