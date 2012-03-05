=========================
その他ツール
=========================


django-globals
===============

- Django-globals, is a very simple application, that allow to define a thread specific global variables.
- https://github.com/svetlyak40wt/django-globals

settings.py 

::

    MIDDLEWARE_CLASSES = (
        #....
        'django_globals.middleware.Global',                    #django-globals
    )


you_module.py

::

    from django_globals import globals
    def async_call(async=None):
    
        if async != None:
            globals.async=async 
        elif hasattr(globals,'async') ==False:
            globals.async=True
    
        return globals.async




