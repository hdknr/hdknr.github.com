=================
Serialization
=================

.. contents:: Serialization

:ref:`celery:calling-serializers`

Djkombu サンプルメッセージ
============================

.. code-block:: javascript

    {
        "body": "KGRwM....(シリアライズされたメッセージ[Base64])....  MnCnA0MgpJMDEKcy4=", 
        "headers": {}, 
        "content-type": "application/x-python-serialize", 
        "properties": {
                "exclusive": false, 
                "name": "celery", 
                "body_encoding": "base64", 
                "delivery_info": {
                    "priority": 0, 
                    "routing_key": "celery", 
                    "exchange": "celery"
                    }, 
                "durable": true, 
                "delivery_mode": 2, 
                "no_ack": false, 
                "alias": null, 
                "queue_arguments": null, 
                "binding_arguments": null, 
                "delivery_tag": 1, 
                "auto_delete": false
            }, 
        "content-encoding": "binary"
    }

Serializer
============

pickle
-------

- デフォルト

JSON
-----

- "content-type": "application/json"

yaml
-----

- "content-type": "application/x-yaml"

msgpack
--------

- "content-type": "application/x-msgpack"  

Serializerの選択オプション
=============================

.. _serializer_in_call:

1. *serializer* 引数
--------------------------------

apply_assync(.. serializer='yaml') とか

.. code-block:: python

    enqueue_schedule.apply_async(options['id'],serializer='yaml')

.. _serializer_in_attr:

2. Task.serializer 属性
------------------------------------

.. code-block:: python

    @task(serializer='json')
    def enqueue_schedule(sender,id=None):
        ''' enqueue specifid mail schedule '''
        Schedule.objects.enqueue_messages(id )


3. settings.CELERY_TASK_SERIALIZER
------------------------------------

- アプリケーションのデフォルトをsettings.pyで設定
- プリミティブタイプ以外のオブジェクトは :term:`pickle` 以外はシリアライズできないので、よっぽどの事のない限り設定しない。
- :ref:`serializer_in_call` か :ref:`serializer_in_attr` で指定する。 
- プリミティブタイプ以外のオブジェクトを引数にタスクはデコレータ @task(serializer="pickle") を指定するのが無難。


serializer='json' の例
----------------------------------------


.. code-block:: javascript 

    {
        "body": "eyJyZXRyaWVzIjogMCwgInRhc2siOiAicGFsb21hLnRhc2tzLmVucXVldWVfc2NoZWR1bGUiLCAiZXJyYmFja3MiOiBudWxsLCAiY2FsbGJhY2tzIjogbnVsbCwgImt3YXJncyI6IHt9LCAiZXRhIjogbnVsbCwgImFyZ3MiOiBbbnVsbF0sICJpZCI6ICJhMWJkMTRhYi1mMjU0LTRkNGUtODYyMS1kNjhiMmM3OTY1YjkiLCAiZXhwaXJlcyI6IG51bGwsICJ1dGMiOiB0cnVlfQ==", 
        "headers": {}, 
        ....
    }

.. code-block:: python

    >>> x="eyJyZXRyaWVzIjogMCwgInRhc2siOiAicGFsb21hLnRhc2tzLmVucXVldWVfc2NoZWR1bGUiLCAiZXJyYmFja3MiOiBudWxsLCAiY2FsbGJhY2tzIjogbnVsbCwgImt3YXJncyI6IHt9LCAiZXRhIjogbnVsbCwgImFyZ3MiOiBbbnVsbF0sICJpZCI6ICJhMWJkMTRhYi1mMjU0LTRkNGUtODYyMS1kNjhiMmM3OTY1YjkiLCAiZXhwaXJlcyI6IG51bGwsICJ1dGMiOiB0cnVlfQ=="
    >>> import base64
    >>> base64.b64decode(x)
    '{"retries": 0, "task": "paloma.tasks.enqueue_schedule", 
    "errbacks": null, "callbacks": null, 
    "kwargs": {}, "eta": null, "args": [null], 
    "id": "a1bd14ab-f254-4d4e-8621-d68b2c7965b9", 
    "expires": null, "utc": true}'


パッケージ
===========

pyYAML
-------

.. include:: misc/pyyaml.rst

