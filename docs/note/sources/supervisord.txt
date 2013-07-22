========================
supervisord
========================

.. contents::
    :local:


インストール
=============

- :ref:`python.pythonz` でPythonごとインストールするのがいいのでは。
- `例 <https://www.evernote.com/shard/s302/sh/142a50e9-c330-4477-8613-e9c560583f66/ec3c6a1152e32c61cca562992de7ff2b>`_

pip
---

- root 環境でいれてみる

.. code-block:: bash

       root@wzy:~# pip install supervisor

/etc/supervisord.conf
---------------------------

.. code-block:: bash

    root@wzy:~# echo_supervisord_conf > /etc/supervisord.conf
    root@wzy:~# mkdir /etc/supervisord.conf.d/
    root@wzy:~# mkdir /var/log/supervisor

修正

.. code-block:: bash

    root@wzy:~# grep -v "^;" /etc/supervisord.conf  | grep -v "^$"

    [unix_http_server]
    file=/var/run/supervisor.sock                   ; socket file
    [supervisord]
    logfile=/var/log/supervisor/supervisord.log   ; main log file
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
    files = /etc/supervisord.conf.d/*.ini                   ; ** includes


デーモン化
------------

- supervisord自体が落ちないように :doc:`upstart` で起動するのがよいのでは


.. code-block:: bash

    root@wzy:~# vi /etc/init/supervisord.conf

    description "supervisord"
     
    start on runlevel [2345]
    stop on runlevel [!2345]
     
    respawn
    script 
       export PYTHONZ_ROOT=/usr/local/pythonz
       . /root/.bash_extra/python-2.7.3.bash    
       exec "`which python | sed -e s/python$//`"supervisord -n -c /etc/supervisord.conf
    end script

