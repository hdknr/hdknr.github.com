=========
Debug
=========


非同期コールが起きないようにする
==================================

CELERY_ALWAYS_EAGER
-----------------------------

settings.py で Trueに設定すると apply_async()が強制的に apply()呼び出しを行うようになる。

.. code-block:: python

    CELERY_ALWAYS_EAGER = True


@task() デコレータされている関数を delay()すると、 Task.apply_async()され、関数の処理が非同期処理メッセージとしてKombuにキューイングされます。
CELERY_ALWAY_EAGER = Trueになっていると、 Task.apply_async()が apply()をフォワードするようになるので、子供タスクが全て終わるまで同期的に処理されます。
