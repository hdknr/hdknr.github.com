=============
pyenv
=============


.. contents::
    :local:



インストール準備
======================

- `Common Build Problems <https://github.com/yyuu/pyenv/wiki/Common-build-problems>`_


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

    $ sudo yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel


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
    $ source ~/.bash
    $ exec $SHELL


Pythonバージョンインストール
===============================

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

