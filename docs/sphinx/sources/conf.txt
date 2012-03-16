==========
conf.py
==========


.. contents:: Configuration(conf.py)

Django のdocstringを参照したい
==============================

appの用意
---------

以下のようにDjangoのアプリケーションを用意します。

::

    (docs)hdknr@sqg:~/ve/docs/src/hdknr.github.com/src/sphinx$ django-admin.py startproject app

    (docs)hdknr@sqg:~/ve/docs/src/hdknr.github.com/src/sphinx$ tree app

    app
    ├── __init__.py
    ├── manage.py
    ├── settings.py
    └── urls.py

    (docs)hdknr@sqg:~/ve/docs/src/hdknr.github.com/src/sphinx$ ls -l
    合計 28
    -rw-r--r-- 1 hdknr hdknr 5593 2012-01-04 10:44 Makefile
    drwxr-xr-x 2 hdknr hdknr 4096 2012-01-18 17:33 app
    drwxr-xr-x 4 hdknr hdknr 4096 2012-01-04 13:40 build
    -rw-r--r-- 1 hdknr hdknr 5115 2012-01-04 10:44 make.bat
    drwxr-xr-x 5 hdknr hdknr 4096 2012-01-18 17:29 source
   
conf.pyにDjanogのsysパスを設定します。

::

    (docs)hdknr@sqg:~/ve/docs/src/hdknr.github.com/src/sphinx$ vi source/conf.py

    RJ_PATH= os.path.dirname( os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(PRJ_PATH ))
    sys.path.insert(0, os.path.join(os.path.dirname(PRJ_PATH ),'app'))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
         

これでDjangoのライブラリのdocstringを参照することができます。

例えば、

.. code-block:: rst

    .. automodule:: django.conf
        :members:
    
とやると以下のようにDjangoのdjang.conf モジュールのメンバーのdocstringを見る事ができます。
    
.. automodule:: django.conf
    :members:


intersphinx_mapping
=====================

    - :mod:`sphinx:sphinx.ext.intersphinx`



マッピングの定義

::

    intersphinx_mapping = {'http://docs.python.org/': None,
                        'sphinx': ('http://sphinx.pocoo.org/',None),
                      }

参照

.. code-block:: rst

     :ref:`comparison manual <python:comparisons>`

とか。


