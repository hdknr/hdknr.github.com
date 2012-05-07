=========================
Debian Linux
=========================


.. glossary::

    Debian
        http://www.debian.org/

.. contents:: Debian

Documents
=============

- http://manpages.debian.net/cgi-bin/man.cgi

Install
=========

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
    root_setup# aptitude install pkg-config


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

リードオンリー::

    $ git clone git://github.com/hdknr/bin.git

その他
=======

証明書
--------

一覧::

    $ find /usr/share/ca-certificates/ -name "*.crt" -print | while read C ; do echo "***" `basename $C` ; openssl x509 -noout -in $C -subject; done > cert.list 
