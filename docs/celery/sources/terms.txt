===============
用語
===============

Celery
==========

.. glossary::

    Celery application
    Celery applications
        Celeryを使ったアプリケーション


    Task
    Tasks
        :term:`Celery application` の構成要素 (「 :ref:`guide-tasks` 」).

    Message
    Messages
        :term:`Broker` に投入されるデータ。(TBD)

    Broker
    Message Broker
        TBD

    Worker
    ワーカー
        (TBD)

    Request
    リクエスト
        - :term:`Task` :term:`messages` は :term:`Worker` によってリクエストに変換されます。
        - リクエストの情報は :term:`Task` の :term:`Context` でも利用可能です。

    Context
    コンテキスト
        - :term:`Task` の **id** や、どの :term:`Queue` が使われるかなどの情報がコンテキストに含まれる。
        - Taskオブジェクトの request 属性で参照可能。
        - :ref:`celery:task-request-info`

    Queue
    キュー
        (TBD)

    Idempotent
        - タスクは結果を変更する事無しに何度も適用可能である、ということ。 ( 冪等性/巾等性 :「 :term:`べきとうせい` 」)
        - :ref:`tasks.acks_late` 参照

    Acknowledged
        :term:`Message` が受領されたこと。「了承済み」


    Eager
        Task呼び出しプロセス内で同期的に実行される。キューイングされないTaskの実行状態。 (TBD)


    Delvier
        TBD

    Exchange
        TBD

    Routing Key
        TBD

    Destination Queue
        TBD

    Task State
        TBD
    
    Result Instance
        TBD

    Result Backend
    Result Backends
        :ref:`task-result-backends` 参照。

Python
=========

.. glossary::

    callable
        -   **__call__** メソッドを持っているオブジェクト。カッコ()を使って、そこにパラメータを渡す事ができる関数のような物。
        -  TBD 

    pickle
        TBD

一般
===============

.. glossary::

.. glossary::

    冪等性
    べきとうせい
        「ある操作を1回行っても複数回行っても結果が同じであることをいう概念である。」
        ( `Wikipedia 冪等性 <http://ja.wikipedia.org/wiki/%E5%86%AA%E7%AD%89>`_ )

    eventlet
        TBD

    gevent
        TBD

    rabbitmq
        TBD

    redis
        TBD

    OpenStack
        OpenStackは、アマゾンクラウドに相当するIaaS（Amazon EC2相当）や
        オブジェクトストレージ（Amazon S3相当）
        を構築できるオープンソースのクラウド基盤ソフトウェアで、
        OpenStack仕様に準拠したIaaSであれば、同じAPIによる管理が可能となります。

        また、Amazon EC2/EBS（Amazon Elastic Block Store）、Amazon S3互換APIを装備しています。

        ( `OpenStackについて <http://technohidelic.posterous.com/openstackcloudstack20itmedia>`_ )


    multiprocessing
        multiprocessing はPythonの標準ライブラリのパッケージで 
        threading とよく似た API を使ってプロセスを生成することができます。 
        multiprocessing パッケージを使用すると、ローカルとリモート両方の並列制御を行うことができます。

        ( :mod:`pythonjp:multiprocessing` )

    python-dateutil
        http://pypi.python.org/pypi/python-dateutil  

        - `relativedeltaが超便利 <http://mitc.xrea.jp/diary/0100>`_

    amqp
        http://www.amqp.org/

    ETA
       Eestimated Time of Arrival
