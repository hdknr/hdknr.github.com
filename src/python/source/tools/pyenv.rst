=============
pyenv
=============


.. contents::
    :local:



インストール準備
======================

- `Common Build Problems <https://github.com/yyuu/pyenv/wiki/Common-build-problems>`_


インストール
======================

- `From Github <https://github.com/yyuu/pyenv#basic-github-checkout>`_

::
 
    $ cd
    $ git clone git://github.com/yyuu/pyenv.git .pyenv


::

    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' > ~/.bash_pyenv
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_pyenv
    $ echo 'eval "$(pyenv init -)"' >> ~/.bash_env


::

    $ source ~/.bash_env
    $ exec $SHELL


Pythonバージョンインストール
===============================

::

    $ pyenv install 2.7.5

