=============
pyenv
=============


.. contents::
    :local:



インストール準備
======================

- `Common Build Problems <https://github.com/yyuu/pyenv/wiki/Common-build-problems>`_

Debian Squeeze
------------------

.. code-block:: bash

    $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm

    パッケージリストを読み込んでいます... 完了
    依存関係ツリーを作成しています                
    状態情報を読み取っています... 完了
    wget はすでに最新バージョンです。
    curl はすでに最新バージョンです。

    以下の特別パッケージがインストールされます:
      binfmt-support binutils cpp cpp-4.4 dpkg-dev fakeroot g++ g++-4.4 gcc gcc-4.4 
      libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl libc-dev-bin
      libc6-dev libdpkg-perl libffi-dev libffi5 libgmp3c2 libgomp1 libmpfr4 libncurses5-dev 
      libreadline6-dev libstdc++6-4.4-dev libtimedate-perl linux-libc-dev llvm-dev
      llvm-runtime manpages-dev patch

    提案パッケージ:
      binutils-doc cpp-doc gcc-4.4-locales debian-keyring g++-multilib g++-4.4-multilib 
      gcc-4.4-doc libstdc++6-4.4-dbg gcc-multilib autoconf automake1.9 libtool flex bison
      gdb gcc-doc gcc-4.4-multilib libmudflap0-4.4-dev libgcc1-dbg libgomp1-dbg libmudflap0-dbg 
      libcloog-ppl0 libppl-c2 libppl7 glibc-doc sqlite3-doc libstdc++6-4.4-doc
      llvm-doc make-doc ed diffutils-doc

    以下のパッケージが新たにインストールされます:
      binfmt-support binutils build-essential cpp cpp-4.4 dpkg-dev fakeroot g++ g++-4.4 gcc gcc-4.4 
      libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
      libbz2-dev libc-dev-bin libc6-dev libdpkg-perl libffi-dev libffi5 libgmp3c2 
      libgomp1 libmpfr4 libncurses5-dev libreadline-dev libreadline6-dev libsqlite3-dev
      libssl-dev libstdc++6-4.4-dev libtimedate-perl linux-libc-dev llvm llvm-dev 
      llvm-runtime make manpages-dev patch zlib1g-dev

    アップグレード: 0 個、新規インストール: 38 個、削除: 0 個、保留: 0 個。


CentOS
--------

::

    $ sudo yum install python26 python26-devel
    $ sudo  cp /usr/bin/python2.6 /usr/bin/python

    cp: `/usr/bin/python' を上書きしてもよろしいですか(yes/no)? yes

    $ python -V
    Python 2.6.8

::
    
    $ echo "alias python=python2.6" >> ~/.bashrc
    $ source ~/.bashrc

::

    $ sudo yum install -y vim gcc gcc-c++ make git patch openssl-devel zlib-devel readline-devel sqlite-devel bzip2-devel bzip2 sqlite


インストール
======================

- `From Github <https://github.com/yyuu/pyenv#basic-github-checkout>`_

::
 
    $ cd
    $ git clone git://github.com/yyuu/pyenv.git .pyenv


::

    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' > ~/.bash_pyenv
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_pyenv
    $ echo 'eval "$(pyenv init -)"' >> ~/.bash_pyenv


::

    $ echo "source ~/.bash_pyenv" >> .bashrc 
    $ source ~/.bashrc
    $ exec $SHELL


Pythonバージョンインストール
===============================

一覧

::

    $ pyenv install -l | grep "2.7"

      2.7
      2.7-dev
      2.7.1
      2.7.2
      2.7.3
      2.7.4
      2.7.5
      2.7.6
      ironpython-2.7.4
      jython-2.7-beta1
      jython-2.7-beta2
      stackless-2.7-dev
      stackless-2.7.2
      stackless-2.7.3
      stackless-2.7.4
      stackless-2.7.5
      stackless-2.7.6

::

    $ pyenv install 2.7.5


きりかえ
===========

::
    
    # 現在のシェルのバージョン切り替え
    $ pyenv shell 2.7.5

    # カレントディレクトリのバージョン切り替え
    $ pyenv local 2.7.5

    # 全体のバージョン切り替え
    $ pyenv global 2.7.5


pytenv-virtual
=================

- https://github.com/yyuu/pyenv-virtualenv

インストール
--------------

::

    $ git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
    $ exec "$SHELL"



