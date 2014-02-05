=========================
Debian Linux
=========================


.. glossary::

    Debian
        http://www.debian.org/

.. contents:: Debian
    :local:

Documents
=============

- http://manpages.debian.net/cgi-bin/man.cgi

Install
=========

.. _debian.install.release:

Release
---------

.. glossary::

    wheezy
        - http://www.debian.org/releases/wheezy/
        - パッケージ : http://packages.debian.org/ja/wheezy/

よくやる一括インストール
----------------------------------------

::

    wget -O - http://hdknr.github.com/docs/note/sources/debian.txt | sed -n 's/root_setup\$\s\+\(.\+\)/\1/p' |tr -d "\r" | bash

::

    root_setup# apt-get install wget curl lsb-release rsync -y
    root_setup# aptitude install build-essential make gcc g++ bison -y 
    root_setup# aptitude install lsof locate ntpdate sudo tmux screen vim dnsutils openssh-client openssh-server -y 
    root_setup# aptitude install unzip subversion git mercurial -y
    root_setup# aptitude install libyaml-dev -y
    root_setup# aptitude install pkg-config -y
    root_setup# aptitude install apparix tree  -y
    root_setup# aptitude install libpq-dev  libmemcached-dev -y

インストール後
-----------------

viに変更::

    $ sudo update-alternatives --config editor

sudo の設定::

    $ visudo

開発機はめんどくさいので::

    hdknr   ALL=(ALL) NOPASSWD: ALL


sshキー作成::

    $ ssh-keygen -b 2048

俺コマンドツール(githubにキーを登録しておく)::

    $ git clone git@github.com:hdknr/bin.git

::

    $ git clone https://github.com/hdknr/bin.git

リードオンリー::

    $ git clone git://github.com/hdknr/bin.git

その他のパッケージ
--------------------

- :doc:`jenkins` は入れた方がいいですね。


.. _debian.git:

AWSインスタンス
----------------------------

ロケールの設定
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    root@ip-10-132-8-118:~# locale-gen ja_JP
    Generating locales (this might take a while)...
      en_US.UTF-8... done
      ja_JP.UTF-8... done
    Generation complete.
    
    
    root@ip-10-132-8-118:~# dpkg-reconfigure locales
    Generating locales (this might take a while)...
      en_US.UTF-8... done
      ja_JP.UTF-8... done
    Generation complete.


タイムゾーン
-----------

- 日本にしてみる

.. code-block:: bash

    $ tzselect
    $ TZ='Asia/Tokyo'; export TZ

その他
=======

- ユーザー : :doc:`user` 
- シェル : :doc:`bash`

cron
------

- ログの確認

.. code-block:: bash

    $ tail -f /var/log/cron

証明書
--------

一覧::

    $ find /usr/share/ca-certificates/ -name "*.crt" -print | while read C ; do echo "***" `basename $C` ; openssl x509 -noout -in $C -subject; done > cert.list 

キーサーバー
----------------

キーサーバーが古くてパッケージレポジトリの更新が出来ない::

    W: 署名照合中にエラーが発生しました。リポジトリは更新されず、過去のインデックスファイルが使われます。
    GPG エラー: http://packages.groonga.org squeeze Release: 公開鍵を利用できないため、以下の署名は検証できませんでした
    : NO_PUBKEY 72A7496B45499429

キーをインストールする (キーサーバーによっては存在しない場合があるので注意 )

.. code-block:: bash

    $ sudo gpg --keyserver pgp.mit.edu  --recv-keys 72A7496B4549942

インストールされたキーの一覧

.. code-block:: bash

    $ sudo apt-key list

キーの更新

.. code-block:: bash

    $ sudo gpg --armor --export 72A7496B45499429 | sudo apt-key add -


.. _debian.packages:

パッケージ
============

.. glossary::

    daemon
        - C、C++ 又は Perl 以外の言語 (すなわち、/bin/sh や Java) で デーモンを書く用途に役立ちます。
        - http://packages.debian.org/ja/wheezy/daemon
