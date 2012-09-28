==========
Jenkins
==========


.. contents::
    :local:


Debian Install
=================

- http://pkg.jenkins-ci.org/debian/
- :term:`wheezy` の例です。

キー入手
---------------------

.. code-block:: bash

    (main)hdknr@wzy:~$ wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
    OK

apt source追加
---------------------

.. code-block:: bash

    (main)hdknr@wzy:~$ echo "deb http://pkg.jenkins-ci.org/debian binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list

    deb http://pkg.jenkins-ci.org/debian binary/

apt 更新
---------------------

.. code-block:: bash

    (main)hdknr@wzy:~$ sudo aptitude update

    ...
    取得: 2 http://pkg.jenkins-ci.org binary/ Release [2,126 B]
    取得: 3 http://pkg.jenkins-ci.org binary/ Packages [564 B] 
    ... 

    Ign http://pkg.jenkins-ci.org binary/ Translation-ja_JP                                                     
    Ign http://pkg.jenkins-ci.org binary/ Translation-ja   
    ....

Jenkinsインストール
---------------------

- Debian の :term:`daemon` パッケージを使っています。

.. code-block:: bash

    (main)hdknr@wzy:~$ sudo apt-get install jenkins
    パッケージリストを読み込んでいます... 完了
    依存関係ツリーを作成しています                
    状態情報を読み取っています... 完了
    以下の特別パッケージがインストールされます:
      daemon
    以下のパッケージが新たにインストールされます:
      daemon jenkins
    アップグレード: 0 個、新規インストール: 2 個、削除: 0 個、保留: 1 個。
    49.0 MB のアーカイブを取得する必要があります。
    この操作後に追加で 49.5 MB のディスク容量が消費されます。
    続行しますか [Y/n]? Y

    取得:1 http://ftp.jp.debian.org/debian/ wheezy/main daemon amd64 0.6.4-1 [97.4 kB]
    取得:2 http://pkg.jenkins-ci.org/debian/ binary/ jenkins 1.483 [48.9 MB]                 
    49.0 MB を 52秒 で取得しました (928 kB/s)                                                                                
    以前に未選択のパッケージ daemon を選択しています。
    (データベースを読み込んでいます ... 現在 74071 個のファイルとディレクトリがインストールされています。)
    (.../daemon_0.6.4-1_amd64.deb から) daemon を展開しています...
    以前に未選択のパッケージ jenkins を選択しています。
    (.../archives/jenkins_1.483_all.deb から) jenkins を展開しています...
    man-db のトリガを処理しています ...
    daemon (0.6.4-1) を設定しています ...
    jenkins (1.483) を設定しています ...
    システムユーザ `jenkins' (UID 110) を追加しています...
    新しいユーザ `jenkins' (UID 110) をグループ `nogroup' に追加しています...
    ホームディレクトリ `/var/lib/jenkins' は作成しません。
    insserv: warning: script 'K01hdknr' missing LSB tags and overrides
    insserv: warning: script 'hdknr' missing LSB tags and overrides
    insserv: script celery_workman: service Celery already provided!
    insserv: script celery_workman: service Worker already provided!
    insserv: script celery_workman: service Manager already provided!
    [ ok ] Starting Jenkins Continuous Integration Server: jenkins.

.. _jenkins.files:

ファイル
==========

一覧
--------

.. code-block:: bash

    (main)hdknr@wzy:~$ dpkg -L jenkins
    
    /usr
      ├── share
      │    ├── jenkins
      │    │    └── jenkins.war
      │    └── doc
      │         └── jenkins
      │               ├── copyright
      │               └── changelog.gz

    /etc
      ├── default
      │    └── jenkins
      ├── init.d
      │    └── jenkins
      ├── logrotate.d
      │    └── jenkins

    /var
      ├── cache
      │    └── jenkins
      ├── run
      │    └── jenkins
      ├── lib
      │    └── jenkins
      ├── log
      │    └── jenkins

.. _jenkins.files.appconfig:

/etc/default/jenkins
------------------------------

- :doc:`apache` の仮想サーバーとの連携を考えると prefix オプションを入れておいた方がいいです。
   
    - http://your_server:8080/your_prefix でアクセスできます。

以下の例では prefixを "/jenkins" に変えています。

.. code-block::  bash

    (main)hdknr@wzy:~$ grep -v "^$" /etc/default/jenkins  | grep -v "^#"

    NAME=jenkins
    JAVA=/usr/bin/java
    PIDFILE=/var/run/jenkins/jenkins.pid
    JENKINS_USER=jenkins
    JENKINS_WAR=/usr/share/jenkins/jenkins.war
    JENKINS_HOME=/var/lib/jenkins
    RUN_STANDALONE=true
    JENKINS_LOG=/var/log/jenkins/$NAME.log
    MAXOPENFILES=8192
    HTTP_PORT=8080
    AJP_PORT=-1
    PREFIX=/jenkins
    JENKINS_ARGS="--webroot=/var/cache/jenkins/war --httpPort=$HTTP_PORT --ajp13Port=$AJP_PORT --prefix=/jenkins"

.. _jenkins.files.initd:
    
/etc/init.d/jenkins
----------------------

.. literalinclude:: _static/jenkins/etc_init_d_jenkins.bash
    :language: bash

起動
====

コマンド
----------

- :ref:`jenkins.files.initd` 参照

::

    (main)hdknr@wzy:~$ sudo /etc/init.d/jenkins stop
    [ ok ] Stopping Jenkins Continuous Integration Server: jenkins.

    (main)hdknr@wzy:~$ sudo /etc/init.d/jenkins start
    [ ok ] Starting Jenkins Continuous Integration Server: jenkins.

    (main)hdknr@wzy:~$ sudo /etc/init.d/jenkins restart
    [ ok ] Restarting Jenkins Continuous Integration Server: jenkins.    

TCP8080
----------

::

    (main)hdknr@wzy:~$ sudo lsof -i:8080 

    COMMAND  PID    USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
    java    5861 jenkins  123u  IPv6 172748      0t0  TCP *:http-alt (LISTEN)

その他::

    (main)hdknr@wzy:~$ sudo lsof -c java | grep TCP
    java    5861 jenkins  123u  IPv6 172748      0t0    TCP *:http-alt (LISTEN)
    java    5861 jenkins  134u  IPv6 172760      0t0    TCP *:57163 (LISTEN)
    java    5861 jenkins  135u  IPv6 172761      0t0    TCP *:59136 (LISTEN)

lsof一覧
---------------

.. literalinclude:: _static/jenkins/lsof_jenkins.txt
    :language: bash


mod_proxyでアクセス
------------------------------

前提
^^^^^^

- :ref:`jenkins.files.appconfig` で prefix を設定(例えば/jenkins )していること。
- :ref:`apache.mod_proxy` を有効にしていること( mod_ajp, mod_rewrite などでも出来なくはないです)
- :ref:`apache.mod_macro` をインストールしていること。

設定
^^^^^^

- Jenkinsの設定マクロ

    .. literalinclude:: _static/apache/mod_macro/conf/macro.jenkins.xml
        :language: xml

- このマクロで仮想ディレクトリを定義した例。 このファイルは、httpd.confからインクルードされます。

    .. literalinclude:: _static/apache/mod_macro/conf/vdir.all.conf
        :language: xml


