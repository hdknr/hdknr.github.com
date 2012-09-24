=========
apache
=========

.. contents::
    :local:
    
.. glossary::
    
    apache
        apache webserver

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

mod_rewrite : URL リライト
-------------------------------

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



.. _apache.mod_macro:

mod_macro
===========

- http://people.apache.org/~fabien/mod_macro/ 

