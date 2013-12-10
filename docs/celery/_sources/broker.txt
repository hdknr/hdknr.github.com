==========
Broker
==========


Django
=======

手早く非同期処理が可能です。

.. code-block:: python

    INSTALLED_APPS += ('djcelery','djkombu',)
    BROKER_URL="django://"
    import djcelery
    djcelery.setup_loader()

- `celerycam は動作しないようです <http://stackoverflow.com/questions/5449163/django-celery-admin-interface-showing-zero-tasks-workers>`_ 。

RabbitMQ
==================

- :ref:`celery:broker-rabbitmq`





