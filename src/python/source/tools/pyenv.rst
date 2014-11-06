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

::

    $ grep pyenv .bashrc
    source ~/.bash_pyenv

    $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_pyenv
    $ source .bashrc
    $ exec $SHELL

作成
------

::

    hdknr@ubuntu:~$ pyenv virtualenv 2.7.8 myenv
    hdknr@ubuntu:~$ pyenv virtualenvs
    * myenv (created from /home/hdknr/.pyenv/versions/2.7.8)

アクティベート
----------------------------

::

    hdknr@ubuntu:~$ pyenv activate myenv  
    (myenv)hdknr@ubuntu:~$ 

:: 

    (myenv)hdknr@ubuntu:~$ deactivate 
    hdknr@ubuntu:~$ 


問題
======

setuptoolsの問題でインストールできない
------------------------------------------------

::

    $ pyenv install 2.7.8
    Downloading Python-2.7.8.tgz...
    -> http://yyuu.github.io/pythons/74d70b914da4487aa1d97222b29e9554d042f825f26cb2b93abd20fdda56b557
    Installing Python-2.7.8...
    Installing setuptools from https://bootstrap.pypa.io/ez_setup.py...
    error: failed to install setuptools via ez_setup.py
    
    BUILD FAILED
    
    Inspect or clean up the working tree at /tmp/python-build.20140917062116.9839
    Results logged to /tmp/python-build.20140917062116.9839.log
    
    Last 10 log lines:
        downloader_factory=options.downloader_factory,
      File "/tmp/python-build.20140917062116.9839/ez_setup.py", line 287, in download_setuptools
        downloader(url, saveto)
      File "/tmp/python-build.20140917062116.9839/ez_setup.py", line 224, in download_file_wget
        _clean_check(cmd, target)
      File "/tmp/python-build.20140917062116.9839/ez_setup.py", line 169, in _clean_check
        subprocess.check_call(cmd)
      File "/root/.pyenv/versions/2.7.8/lib/python2.7/subprocess.py", line 540, in check_call
        raise CalledProcessError(retcode, cmd)
    subprocess.CalledProcessError: Command '['wget', 'https://pypi.python.org/packages/source/s/setuptools/setuptools-5.7.zip', '--quiet', '--output-document', '/tmp/python-build.20140917062116.9839/Python-2.7.8/setuptools-5.7.zip']' returned non-zero exit status 1
    
curlの問題:

- https://github.com/yyuu/pyenv/issues/60
- https://github.com/yyuu/pyenv/issues/200

解決::

    $ EZ_SETUP_OPTS="--insecure" pyenv install -v 2.7.8
