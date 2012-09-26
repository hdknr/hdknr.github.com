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

- apache 2.2 には mod_macro-1.1.11 をインストールします。

.. literalinclude:: _static/apache/mod_macro.install.txt
    :language: bash

.. _apache.mod_dav_svn:

mod_dav_svn
=============

- :doc:`debian` パッケージだと簡単です。

    .. literalinclude:: _static/apache/mod_dav_svn.install.txt
    

