==============================
Debian Linux での設定と開始
==============================


Debian Linuxの用意
=====================

- VirtualBox
- Host - Guest 接続

Debian Packageのインストール
==============================

Squeeze::

    $ sudo aptitude install python-setuptools vim-python python-dev -y
    $ sudo aptitude install libjpeg8 libjpeg8-dev  libfreetype6 libfreetype6-dev liblcms1-dev  python-liblcms python-tk  tcl8.5-dev tk8.5-dev -y

Python Virtulaenv
==============================

インストール::

    $ sudo easy_install pip
    $ sudo pip install virtualenv
    $ sudo pip install virtualenvwrapper

virtualenv ホーム ::

    $ mkdir $HOME/ve

.bashrcなど ::

    export WORKON_HOME=$HOME/ve
    source `which virtualenvwrapper.sh`

反映 ::

    $ source .bashrc::
    
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/initialize
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/premkvirtualenv
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/postmkvirtualenv
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/prermvirtualenv
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/postrmvirtualenv
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/predeactivate
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/postdeactivate
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/preactivate
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/postactivate
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/get_env_details
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/premkproject
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/postmkproject
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/prermproject
    virtualenvwrapper.user_scripts creating /home/hdknr/ve/postrmproject


Django & MySQL
==============================

- workon 
- pip install django
- pip install MySQL-python

Repository
==============

- Github
- Mercurial
- Yuor Subversion

Editor
======

- vim
