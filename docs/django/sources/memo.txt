======
メモ
======

テストランナーでEncoding エラー
------------------------------------

settings.py のDATABASEの設定に TEST_* を入れる。

.. code-block:: python

    DATABASES = { 
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'paloma',                      # Or path to database file if using sqlite3.
            'USER': 'paloma',                      # Not used with sqlite3.
            'PASSWORD': 'paloma',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
            'TEST_CHARSET': 'utf8',
            'TEST_DATABASE_COLLATION': 'utf8_general_ci',
        } 


モデルを辞書に変更
----------------------------

- :py:func:django.forms.models.model_to_dict

    - doc:`django.forms.models`


URLのフルパス
-------------

.. eodo-block:: python
    
    def enroll(request,command,secret):
        ''' :param request: django.core.handlers.wsgi.WSGIRequest
        '''
        from django import template
        from django.http import HttpResponse
    
        print type(request)
        return HttpResponse(
            template.Template("""
            <html><head><title>Paloma Enroll</title></head> <body> <h1> Paloma Enroll</h1>
                {{ url     }} <br/>
                {{ command }} <br/>
                {{ secret  }} <br/>
            """
            ).render( template.RequestContext(request,
                    {'command':command,'secret':secret,
                     'url' : request.build_absolute_uri('/o/my/god'),
                    }) )
        )   

::

     http://wzy:9000/o/my/god 

