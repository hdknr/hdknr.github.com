==============================
rbenv: Ruby環境のインストール
==============================

.. contents::
    :local:

rbenv
======

- https://github.com/sstephenson/rbenv

rbenvのインストール
==============================

Debian
----------------

パッケージ更新:

.. code-block:: bash

    sudo apt-get update && sudo apt-get upgrade

依存パッケージインストール:

.. code-block:: bash

    sudo apt-get install build-essential openssl libreadline6 libreadline6-dev \
        curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-0 \
        libsqlite3-dev sqlite libxml2-dev libxslt-dev autoconf libc6-dev \
        ncurses-dev automake libtool bison subversion

rbenvインストール:

.. code-block:: bash

    sudo apt-get install rbenv


環境設定
----------

Linux環境設定(.bashrcで読めるようにしておく):


.. code-block:: bash

    vi /home/hdknr/.bash_extra/rbenv.bash

    export PATH=$HOME/.rbenv/bin:$PATH
    eval "$(rbenv init - bash)"


ruby-build のインストール
==========================================

- ruby-buildをgithubからrbenvのプラグインとしていれる

    - 新しいgit pullしてRubyのバージョンに対応できるようになる

.. code-block:: bash

    git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build


rbenv を使ってRubyの特定のバージョンをインストール
=======================================================

インストール可能なバージョンの確認
--------------------------------------------

.. code-block:: bash

    $ rbenv install -l  

    usage: rbenv install VERSION
           rbenv install /path/to/definition
    
    Available versions:
      1.8.6-p383
      1.8.6-p420
      :
      :

1.9.3-p448をインストール
----------------------------------------

.. code-block:: bash

    $ rbenv install 1.9.3-p448

    Downloading yaml-0.1.4.tar.gz...
    -> http://dqw8nmjcqpjn7.cloudfront.net/36c852831d02cf90508c29852361d01b
    Installing yaml-0.1.4...
    /home/hdknr/.rbenv/plugins/ruby-build/bin/ruby-build: 105 行: [: /proc/cpuinfo:1: 整数の式が予期されます
    Installed yaml-0.1.4 to /home/hdknr/.rbenv/versions/1.9.3-p448
    
    Downloading ruby-1.9.3-p448.tar.gz...
    -> http://dqw8nmjcqpjn7.cloudfront.net/a893cff26bcf351b8975ebf2a63b1023
    Installing ruby-1.9.3-p448...
    Installed ruby-1.9.3-p448 to /home/hdknr/.rbenv/versions/1.9.3-p448

- :doc:`gem` もインストールされます！

Rubyのバージョンの切り替え
--------------------------------

.. code-block:: bash

    $ rbenv global 1.9.3-p448


rehash
--------

.. code-block:: bash

    $ rbenv rehash

- 参考 : http://rhysd.hatenablog.com/entry/20120226/1330265121


