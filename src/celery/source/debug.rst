==============
Test/Debug
==============

.. contents:: Test/Debug 

非同期コールが起きないようにする
==================================

CELERY_ALWAYS_EAGER
-----------------------------

settings.py で Trueに設定すると :mod:`apply_async() <celery:celery.app.task.Task.apply_async>` 
が強制的に apply()呼び出しを行うようになります。

.. code-block:: python

    CELERY_ALWAYS_EAGER = True


- @task() デコレータされている関数を delay()すると、 Task.apply_async()され、関数の処理が非同期処理メッセージとしてKombuにキューイングされます。
- CELERY_ALWAY_EAGER = Trueになっていると、 Task.apply_async()が apply()をフォワードするようになるので、子供タスクが全て終わるまで同期的に処理されます。

.. autoclass:: celery.app.task.Task
    :members: apply_async


Taskのモニター
===================

celerycam
----------

- Task の状況を Django の djcelery.models.TaskState に定期的に記録します。

.. autoclass:: djcelery.models.TaskState
    :members:

- Worker に -E (イベント)オプションを付けて起動します。

:: 

    $ python ../manage.py celeryd -l INFO -E

::

    -------------- celery@Peeko.local v3.0.3 (Chiastic Slide)
    ---- **** ----- 
    --- * ***  * -- [Configuration]
    -- * - **** --- . broker:      django://localhost//
    - ** ---------- . app:         default:0x10bf4d310 (djcelery.loaders.DjangoLoader)
    - ** ---------- . concurrency: 4 (processes)
    - ** ---------- . events:      ON
    - ** ---------- 
    - *** --- * --- [Queues]
    -- ******* ---- . celery:      exchange:celery(direct) binding:celery
    --- ***** ----- 
    

- モニタープロセスを起動します。

::

        $ python ../manage.py celerycam

 
- Brokerが :term:`RabbitMQ`, :term:`redis` の `時だけ動作するようです <http://stackoverflow.com/questions/5449163/django-celery-admin-interface-showing-zero-tasks-workers>`_ 。
