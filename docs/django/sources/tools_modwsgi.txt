======================
apache:mod_wsgi
======================


Install 
=========

Debian (Squeeze):

::

    $sudo aptitude install libapache2-mod-wsgi 


::

    $ dpkg -L libapache2-mod-wsgi
    /.
    /usr
    /usr/lib
    /usr/lib/apache2
    /usr/lib/apache2/modules
    /usr/lib/apache2/modules/mod_wsgi.so-2.5
    /usr/lib/apache2/modules/mod_wsgi.so-2.6
    /usr/share
    /usr/share/python
    /usr/share/python/runtime.d
    /usr/share/python/runtime.d/libapache2-mod-wsgi.rtupdate
    /usr/share/doc
    /usr/share/doc/libapache2-mod-wsgi
    /usr/share/doc/libapache2-mod-wsgi/copyright
    /usr/share/doc/libapache2-mod-wsgi/README.gz
    /usr/share/doc/libapache2-mod-wsgi/changelog.Debian.gz
    /etc
    /etc/apache2
    /etc/apache2/mods-available
    /etc/apache2/mods-available/wsgi.load
    /etc/apache2/mods-available/wsgi.conf
    /usr/lib/apache2/modules/mod_wsgi.so

Virtual Directory
=====================

sample::

    WSGIDaemonProcess ve_desk user=www-data group=www-data threads=25 python-path=/home/hdknr/ve/docs/lib/python2.6/site-packages:/home/hdknr/ve/docs/bin
    WSGIScriptAlias /desk /home/hdknr/ve/docs/src/multi/app/wsgi.desk.py
    
    Alias /desk/media /home/hdknr/ve/docs/lib/python2.6/site-packages/django/contrib/admin/media
    
    <Location /desk >
        WSGIProcessGroup ve_desk
        WSGIApplicationGroup %{SERVER}
        Options All
    </Location>

WSGI Script
==============

sample::

    import sys
    sys.stdout = sys.stderr
    
    import os
    
    # put the Django project on sys.path
    PROJECT_DIR = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
    
    # BOTH of the  following sys.path.insert MUST be specified.
    sys.path.insert(0,PROJECT_DIR)
    sys.path.insert(0,os.path.dirname(PROJECT_DIR))
    
    os.environ["DJANGO_SETTINGS_MODULE"] = "app.settings"
    
    # WSGI
    from django.core.handlers.wsgi import WSGIHandler
    application = WSGIHandler()


Media Path
=============

- web server(apache) で環境編集をセットするか、あるいは wsgi.py で直接 os.environ に変数をセットする

sample::

    #: - wsgi.py

    os.environ['VDIR'] = '/desk'


settings.py::


    import os
    VDIR=os.environ.get('VDIR','')

    STATIC_URL = '%s/static/' % VDIR
    ADMIN_MEDIA_PREFIX = '%s/static/admin/'%VDIR

