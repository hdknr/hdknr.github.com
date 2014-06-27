=====================
gunicorn
=====================

.. contents::
    :local:

インストール設定
==================

::
    
    $ pip install gunicorn

Django 
---------------------

settings.py
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    INSTALLED_APPS += ('gunicorn', )

    # least logging settings
    LOGGING = {'version': 1, }

manage.py
^^^^^^^^^^^^^^

::

    $ python manage.py run_gunicorn
    2014-05-28 15:43:10 [20351] [INFO] Starting gunicorn 18.0
    2014-05-28 15:43:10 [20351] [INFO] Listening at: http://127.0.0.1:8000 (20351)
    2014-05-28 15:43:10 [20351] [INFO] Using worker: sync
    2014-05-28 15:43:10 [20356] [INFO] Booting worker with pid: 20356



