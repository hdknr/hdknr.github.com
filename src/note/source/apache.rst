=========
apache
=========

.. contents::
    :local:
    
.. glossary::
    
    apache
        apache webserver

インストール
===============

Debian
--------

.. code-block:: bash

    $ sudo aptitude install apache2

- `履歴 <static/apache/aptitude_apache2.txt>`_

apxs2 コンパイラとかの為に

.. code-block:: bash

    $ sudo aptitude install apache2-threaded-dev 

設定
========

ディレクトリリスティング
--------------------------------------------

::

     Options Indexes Includes FollowSymLinks

設定ファイル確認
------------------

:: 

    # /usr/sbin/apache2ctl configtest

    Syntax OK

基本認証
---------

- http://hdknr.posterous.com/itapachebasi

.. code-block:: xml

   <Directory "/var/www/html/member">
       AuthType Basic
       AuthName "Secret Zone"
       AuthUserFile /etc/httpd/.htpasswd
       Require user secret
   </Directory>

SSL
----

- sslを有効にする。

.. code-block:: bash

    # a2enmod ssl
    Module ssl installed; run /etc/init.d/apache2 force-reload to enable.

- SSLPassPhraseDialog cannot occur within <VirtualHost> section


管理
======

ログ
-----

graceful で再起動した？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    [Thu Feb 20 10:40:43 2014] [notice] Graceful restart requested, doing restart


パーサー
^^^^^^^^

- http://code.google.com/p/apachelog/

トラブル
==========

おそい？
---------

HostNameLookupをOffにする 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  - defaultではoffのようです。


DocumentRoot does not exist ? あるのに
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

アクセス権的にもOK:

::

    # sudo /etc/init.d/httpd restart
    Stopping httpd:                                            [FAILED]
    Starting httpd: Warning: DocumentRoot [/var/eccube/www] does not exist

SELinux! :

    # getenforce
    Enforcing

無効:

    # setenforce 0
    # getenforce
    Permissive

リブート時に無効にさせる:

    # vi /etc/sysconfig/selinux
    SELINUX=disabled

.. _apache.mod_rewrite:

mod_rewrite : URL リライト
=============================================

- 有効

.. code-block:: bash

    $ sudo a2enmod rewrite
    $ sudo /etc/init.d/apache2 force-reload 

- 設定したいディレクトリの.htaccsss

::

    Options FollowSymLinks
    RewriteEngine   On

    RewriteRule ^$  /wine/  [R]

- `サーバー変数 <http://harajuku-tech.posterous.com/htaccess-rewrit>`_
- `拡張子操作 <http://harajuku-tech.posterous.com/modrewrite-html-php>`_

.. _apache.mod_proxy:

mod_proxy
=============================================

- http://httpd.apache.org/docs/2.2/ja/mod/mod_proxy.html

- sudo a2enmod proxy

    .. literalinclude:: _static/apache/enable_mod_proxy.txt 
        :language: bash

.. _apache.mod_macro:

mod_macro
===========

- http://people.apache.org/~fabien/mod_macro/ 

インストール
----------------

::

    The current version for Apache 2.4 is 1.2.1. 
    For Apache 2.2, use 1.1.11. 
    For Apache 2.0, use 1.1.6. 
    It won't work with Apache 1.3 for which you should use version 1.1.2. 

- apache 2.2 には mod_macro-1.1.11 をインストールします。

.. literalinclude:: _static/apache/mod_macro.install.txt
    :language: bash

.. _apache.mod_macro.conf:

mod_macro設定パターン
------------------------

.. _apache.mod_macro.tree:

ツリー
^^^^^^^^^

::

    $base
      |
      +-- $host
            |
            +--- conf
            |     |
            |     +---- macro.httpd.xml
            |     +---- macro.auth.xml
            |     +---- macro.ssl.xml
            |     +---- macro.jenkins.xml
            |     +---- macro......xml
            |     |
            |     +---- httpd.conf
            |     +---- vdir.all.conf
            |     |
            |     +---- .htpasswd.user
            |     +---- .htpasswd.admin
            |     +---- .htpasswd.....
            |
            +--- logs
            |     |
            |     +---- access.log
            |     +---- error.log
            |
            +--- www
                  |
                  +---- index.html
                  +---- .....
                  |
                  
    

.. _apache.mod_macro.conf.macro.httpd.xml:

macro.httpd.xml
^^^^^^^^^^^^^^^^^

.. literalinclude:: _static/apache/mod_macro/conf/macro.httpd.xml
    :language: xml

.. _apache.mod_macro.conf.httpd.conf:

httpd.conf
^^^^^^^^^^^^^^^^^

- :ref:`apache.mod_macro.conf.macro.httpd.xml` をつかって httpd.conf を定義する。
- 以下の例は dev.lafoglia.jp サイトの仮想サーバーの例。

    .. literalinclude:: _static/apache/mod_macro/conf/httpd.conf
        :language: xml

- これをシンボリックリンクする

    ::

        $ ls -l /etc/apache2/sites-enabled/

        合計 0
        lrwxrwxrwx 1 root root 26  9月 26 11:36 000-default -> ../sites-available/default
        lrwxrwxrwx 1 root root 49  9月 27 05:33 dev.lafoglia.jp.conf -> /home/hdknr/sites/dev.lafoglia.jp/conf/httpd.conf


.. _apache.mod_dav_svn:

mod_dav_svn
=============

- :doc:`debian` パッケージだと簡単です。

    .. literalinclude:: _static/apache/mod_dav_svn.install.txt
    

