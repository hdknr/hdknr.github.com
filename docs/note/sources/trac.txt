=======
Trac
=======

.. contents::
    :local:

.. _trac.apache:

apacheでの配置
===================

前提
-----

- :ref:`apache.mod_macro`  を使って定義を簡略化します。
- {{ cname }} を trac.lafoglia.jp としてapacheで仮想ホストするとします。
- プロジェクトを複数立てるとして、 それぞれのプロジェクト名は {{ prj }} とします。
- :term:`Python` は :term:`virtualenv` として環境を構築します。
- 移行することを考えて、全てのファイルは ベースディレクトリ以下に置きます。
- :ref:`apache.mod_dav_svn` がインストールされていること。

.. _trac.apache.tree:

配置ディレクトリ構成例
------------------------

.. include:: trac/tree.rst

.. _trac.apache.basedir:

ベースディレクトリ
---------------------

- /home/sites を {{ basedir }}とします。 

.. _trac.apache.macro:

apache macro
----------------

マクロ
^^^^^^^^

- VHost : 仮想ホスト
- Trac  : TracとSubversionを動かす仮想ディレクトリ
- SSL   : 証明書とキーの設定
- WSGI  : :term:`mod_wsgi` の設定 

変数
^^^^^^

- $host : {{ cname }}
- $base : {{ basedir }}
- $port : ポート番号( 80, 443 .. )
- $prt  : {{ prj }}
- $prefix : {{ cname }} を短くして分かり易くしたもの

例
^^^^

- {{basedir}}/{{cname}}/conf/macro.def を以下の用にします。

.. include:: trac/macro.rst

.. _trac.apache.basedir.httpd.conf:

httpd.conf
----------------

- :ref:`trac.apache.macro` を使って次のように書きます。

.. include:: trac/httpd.conf.rst

- /home/sites/{{ cname }}/conf/httd.conf に置きます。
- Linuxディストリビューションの apache の設定に読みこませるようにします。

    - :doc:`debian` だと /etc/apache2/site-enabled に置くので以下のようにします。

    ::

        $ ls -l /etc/apache2/sites-enabled/

        合計 0
        lrwxrwxrwx 1 root root 26 2011-06-28 13:58 000-default -> ../sites-available/default
        lrwxrwxrwx 1 root root 48 2011-07-05 16:01 lafoglia.conf -> /home/sites/trac.lafoglia.jp/conf/httpd.conf        

.. _trac.apache.ssl:

ssl.def
----------------

- ssl.def がインクルードされるときにはmacro.def が用意されているので、適切に設定します。

::

    Use SSL trac.laofglia.jp /home/system 
    

Trac/Subversion
==================

- Trac は  {{ basedir }}/{{ cnamme }}/prj/{{ prj }}/trac 
- Subversion は  {{ basedir }}/{{ cnamme }}/prj/{{ prj }}/svn
- Python cache は  {{ basedir }}/{{ cnamme }}/prj/{{ prj }}/cache
- trac{{ prj }} 以下に wsgi.py を置きます。これが仮想ディレクトリごとのapache設定によりWSGIプロセスに読み込まれます。

.. include:: trac/wsgi.py

Subversion同期
==================


同期スクリプト
-----------------

- virualenv のパスを設定します。 
- {{ basedir }} / {{ cnamem }}  /prj/sync.bash とします。

.. include:: trac/sync.bash

post-commit
-----------------

- {{ basedir }}/{{ cname }}/prj/svn/hooks/post-commit から sync.bashを呼びます。

.. include:: trac/post-commit.bash
