==============
コンポーネント
==============


Applciation
==============

.. code-block:: python

    (tact)hdknr@wzy:~/ve/tact/src/paloma/example/app$ python ../manage.py shell
    Python 2.7.3rc2 (default, Apr 22 2012, 22:30:17) 
    [GCC 4.6.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> from celery import app
    >>> app.current_app()
    <Celery default:0x1dbcd50>
    >>> type(_)
    <class 'celery.app.base.Celery'>

Configuration
---------------

.. code-block:: python

    >>> a=app.current_app()
    >>> type(a.conf)
    <class 'celery.app.utils.Settings'>
    

CELERY_TASK_SERIALIZER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

デフォルト(settings.pyで何も指定しないと)で pickle

.. code-block:: python

    >>> app.current_app().conf.CELERY_TASK_SERIALIZER
    'pickle'
    
