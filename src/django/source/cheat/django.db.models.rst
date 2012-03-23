.. _cheat.django.db.models:

django.db.models 
-------------------

.. _cheat.django.db.models.list_models:

モデルの一覧
^^^^^^^^^^^^^^^

:py:class:`django.db.modles.loading.AppCache` 参照。

.. code-block:: python

    >>> from django.db import models
    >>> models.get_models()
    [<class 'django.contrib.contenttypes.models.ContentType'>,] 

データベーステーブル名

.. code-block:: python

    >>> print models.get_models()[0]._meta.db_table
    django_content_type


アプリケーション指定

.. code-block:: python

    >>> print models.get_models(models.get_app('django.contrib.auth'))[0]._meta.db_table
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
      File "/home/hdknr/ve/docs/lib/python2.6/site-packages/django/db/models/loading.py", line 140, in get_app
        raise ImproperlyConfigured("App with label %s could not be found" % app_label)
    ImproperlyConfigured: App with label django.contrib.auth could not be found

    >>> print models.get_models(models.get_app('auth'))[0]._meta.db_table
    auth_permission

アプリケーション一覧
^^^^^^^^^^^^^^^^^^^^^^^^^^

:py:class:`django.db.modles.loading.AppCache` 参照。

get_apps()

.. code-block:: python

    >>> from django.db.models import get_apps
    >>> a=get_apps()[0]
    <type 'module'>
    >> [ a.__name__ for a in get_apps() ]
    ['django.contrib.auth.models', 'django.contrib.contenttypes.models', ... 


get_app()

.. code-block:: python

    >>> from django.db.models import get_app
    >>> get_app('south').__name__
    'south.models'


