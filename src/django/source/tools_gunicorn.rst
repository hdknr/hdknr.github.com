===========================
Gunicorn
===========================

.. contents::
    :local:

概要
=====

- http://gunicorn.org/

- Gunicorn + WSGI で Djangoをホストします
- Gunicornのプロセス起動を supervisord で行います
- supervisord自体はupstartでデーモン管理します。

.. _upstart:

upstart
===============

- http://upstart.ubuntu.com/
- https://ja.wikipedia.org/wiki/Upstart

Debianパッケージでインストール

::

    # aptitude remove sysvinit
    # aptitude install upstart

sysvinit の起動スクリプトは upstartが提供する/etc/init/rc.conf で起動されます。

.. code-bloock:: bash

    # rc - System V runlevel compatibility
    #
    # This task runs the old System V-style rc script when changing between
    # runlevels.
    
    description"System V runlevel compatibility"
    author"Scott James Remnant <scott@netsplit.com>"
    
    start on runlevel [0123456]
    stop on runlevel [!$RUNLEVEL]
    
    export RUNLEVEL
    export PREVLEVEL
    
    task
    
    console output
    exec /etc/init.d/rc $RUNLEVEL

sysvinit前提でインストールされた起動スクリプトも継続して使えます

::

    # /etc/init.d/apache2 stop

    Stopping web server: apache2 ... waiting .

.. _supervisor:

supervisor
==================

- http://supervisord.org/index.html
- PYPIからインストールします。

.. code-block:: bash

    $ sudo pip install supervisor

supervisorの設定ファイル
------------------------------------------

- http://supervisord.org/configuration.html

.. code-block:: bash

    $ echo_supervisord_conf  | sudo tee -a /etc/supervisord.conf
    $ sudo vim /etc/supervisord.conf

設定ファイル例:

.. code-block:: bash

    $ grep -v "^;" /etc/supervisord.conf | grep -v "^$"

::

    [unix_http_server]
    file=/var/run/supervisor.sock
    [supervisord]
    logfile=/var/log/supervisor/supervisord.log
    logfile_maxbytes=50MB        ; (max main logfile bytes b4 rotation;default 50MB)
    logfile_backups=10           ; (num of main logfile rotation backups;default 10)
    loglevel=info                ; (log level;default info; others: debug,warn,trace)
    pidfile=/var/run/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
    nodaemon=false               ; (start in foreground if true;default false)
    minfds=1024                  ; (min. avail startup file descriptors;default 1024)
    minprocs=200                 ; (min. avail process descriptors;default 200)
    [rpcinterface:supervisor]
    supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
    [supervisorctl]
    serverurl=unix:///var/run/supervisor.sock               ; unix:// URL for a Unix socket
    [include]
    files = /etc/supervisord.conf.d/*.ini
    

supervisorのupstart起動ファイル
------------------------------------------


.. code-block:: bash

    $ vim /etc/init/supervisord.conf

.. code-block:: bash

    description "supervisord"
     
    start on runlevel [2345]
    stop on runlevel [!2345]
     
    respawn
    script 
       exec /usr/local/bin/supervisord -n -c /etc/supervisord.conf
    end script

supervisorの起動
----------------------------

.. code-block:: bash

    $ sudo initctl reload-configuration
    $ sudo initctl list  | grep super

    supervisord stop/waiting

    $ sudo initctl start supervisord

    supervisord start/running, process 2268
    
ログで確認( /etc/supervisord.confにログファイル設定されている)

::

    $ sudo more /var/log/supervisor/supervisord.log 

    2013-06-25 10:57:14,153 CRIT Supervisor running as root (no user in config file)
    2013-06-25 10:57:14,205 INFO RPC interface 'supervisor' initialized
    2013-06-25 10:57:14,205 CRIT Server 'unix_http_server' running without any HTTP authentication checking
    2013-06-25 10:57:14,205 INFO supervisord started with pid 2268

ソケット,PIDファイル

::

    $ ls -l /var/run/supervisor*

    srwx------ 1 root root 0  6月 25 10:57 /var/run/supervisor.sock
    -rw-r--r-- 1 root root 5  6月 25 10:57 /var/run/supervisord.pid

プロセス

::

    $ ps ax | grep supervisor

     2268 ?        Ss     0:00 /usr/bin/python /usr/local/bin/supervisord -n -c /etc/supervisord.conf


Gunicorn
==============

- Djangoのサイトを同じvirtualenvにインストールする

インストール
------------------------------------

.. code-block:: bash

    $ pip install gunicorn
    $ pip install setproctitle


サイトの設定ファイル
------------------------------------

- http://docs.gunicorn.org/en/latest/configure.html

.. code-block:: bash

    $ ls app/settings.py
    app/settings.py

    $ vim gunicorn.conf.py

.. code-block:: python

    import os
    import sys
    
    # for Gunicorn to find app.wsgi:application
    #
    DIR= os.path.dirname( os.path.abspath( __file__ ) ) 
    sys.path.append( DIR )

    # logs directory
    #
    LOGS= os.path.join(DIR,'logs')
    if not os.path.isdir( LOGS ):
        os.makedirs( LOGS )
    
    # Gunicorn Configuration
    #
    bind = "127.0.0.1:8000"
    accesslog = os.path.join(LOGS,"gunicorn.access.log") 
    errorlog = os.path.join(LOGS,"gunicorn.error.log") 
    proc_name="mysite"

supervisorでの起動ファイル
------------------------------------

起動コマンドをsupervisordに登録します

::

    $ sudo vim /etc/supervisord.conf.d/mysite.ini 

::

    [program:mysite]
    command=/home/system/ve/dev/bin/gunicorn -c /home/system/ve/dev/src/mysite/gunicorn.conf.py  app.wsgi:application
    ;directory=/opt/www/memo
    user=system
    autostart=true
    autorestart=true
    redirect_stderr=true
    ;environment=PYTHON_EGG_CACHE=/opt/www/memo/.python-eggs


::

    $ sudo supervisorctl reread
    mysite: available

    $ sudo  supervisorctl add ikkiweb
    mysite: added process group

    $ lsof -i:8000

    COMMAND    PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
    gunicorn: 2300 system    8u  IPv4   9961      0t0  TCP localhost:8000 (LISTEN)
    gunicorn: 2305 system    8u  IPv4   9961      0t0  TCP localhost:8000 (LISTEN)


    $ ps ax | grep mysite 

    2300 ?        S      0:00 gunicorn: master [mysite]                                                                      
    2305 ?        S      0:00 gunicorn: worker [mysite] 


HTTPサーバーの設定
=======================

apache mod_proxy
------------------

::

    $ sudo a2enmod proxy
    $ sudo a2enmod proxy_http

::

    $ sudo aptitude install libapache2-mod-macro
    $ sudo a2enmod macro


仮想サーバーのhttpd.conf
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- サイトまるごとGunicornのワーカーに食わせる例
- スタティックファイルをapacheに処理させるためにProxyに例外を登録すること

.. code-block:: xml

    <Macro Resource>
        ServerAdmin webmaster@localhost
        ProxyPreserveHost On

        #: python manage.py collectstatic goes to assets
        Alias /assets /home/system/ve/dev/src/mysite/app/assets 

        <Location /assets >
            #: Exclude Proxy
            ProxyPass !
        </Location>

       <Location / >
            ProxyPass http://127.0.0.1:8000/
            ProxyPassReverse http://127.0.0.1:8000/
       </Location>

        LogLevel warn
        ErrorLog  /home/system/server/apache2/mysite/logs/error.log
        CustomLog /home/system/server/apache2/mysite/logs/access.log combined
    </Macro>

    <Macro Certs>
        SSLEngine on
        SSLCertificateChainFile /root/ssl/dvcacert.cer
        SSLCertificateFile /root/ssl/mysite.crt
        SSLCertificateKeyFile /root/ssl/mysite.key
    </Macro>

    <VirtualHost *:80>
       Use Resource
    </VirtualHost>

    <VirtualHost *:443>
       Use Resource
       Use Certs
    </VirtualHost>

