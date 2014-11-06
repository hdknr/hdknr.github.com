==============
CentOS
==============

.. contents::
    :local:

インストール
=============

ネットインストール
------------------

例えば、

 +--------------+-------------------------------+
 | ホスト       | ftp.riken.jp                  |
 +--------------+-------------------------------+
 | パス         | Linux/centos/5.10/os/x86_64   |
 +--------------+-------------------------------+

.. _centos.repos:

レポジトリの追加
--------------------

- `Installing RHEL EPEL Repo on Centos 5.x or 6.x <http://www.rackspace.com/knowledge_center/article/installing-rhel-epel-repo-on-centos-5x-or-6x>`_

5.x::

    # wget http://dl.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm
    # wget http://rpms.famillecollet.com/enterprise/remi-release-5.rpm
    # sudo rpm -Uvh remi-release-5*.rpm epel-release-5*.rpm

6.x::

    # wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
    # wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
    # sudo rpm -Uvh remi-release-6*.rpm epel-release-6*.rpm

確認::

    # # ls -a /etc/yum.repos.d/ -I "*Cent*"
    .  ..  epel-testing.repo  epel.repo  remi.repo

--enablerepo=remi ::

    # yum --enablerepo=remi search python26

    

.. _centos.build_tools:

ビルド環境
==========

.. code-block:: bash
    
    $ sudo yum install gcc gcc-c++  autoconf automake kernel-devel ncurses-devel


ネットワーク
==============

/etc/sysconfig/network-script
------------------------------------------

- 固定アドレス

    ::

        $ more /etc/sysconfig/network-scripts/ifcfg-eth1
        # Intel Corporation 82540EM Gigabit Ethernet Controller
        DEVICE=eth1
        #BOOTPROTO=dhcp
        ONBOOT=yes
        HWADDR=08:00:27:73:c4:1b
        #
        BOOTPROTO=none
        IPADDR=192.168.56.80
        NETMASK=255.255.255.0


nameserver
------------

dig::

    $ sudo yum install bind-utils


ツール
======

tmux
-----

パッケージインストール
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- :ref:`centos.repos`

::

    $ sudo yum --enablerepo=remi install tmux



ソースインストール
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- 古いCentOSに :doc:`tmux` をインストール
- :ref:`centos.build_tools` は入れておく
- libeventビルド & インストールj

    .. code-block:: bash

        $ wget https://github.com/downloads/libevent/libevent/libevent-2.0.21-stable.tar.gz --no-check-certificate
        $ tar zxvf libevent-2.0.21-stable.tar.gz
        $ cd libevent-2.0.21-stable
        $ ./configure && make && sudo make install

- so設定

    .. code-block:: bash

        $ cd /etc/ld.so.conf.d/
        $ echo /usr/local/lib | sudo tee -a libevent2.conf
        $ sudo ldconfig  
        $ ldconfig -p | grep libevent
              libevent_pthreads-2.0.so.5 (libc6,x86-64) => /usr/local/lib/libevent_pthreads-2.0.so.5
              libevent_extra-2.0.so.5 (libc6,x86-64) => /usr/local/lib/libevent_extra-2.0.so.5
              libevent_extra-1.4.so.2 (libc6,x86-64) => /usr/lib64/libevent_extra-1.4.so.2
              libevent_core-2.0.so.5 (libc6,x86-64) => /usr/local/lib/libevent_core-2.0.so.5
              libevent_core-1.4.so.2 (libc6,x86-64) => /usr/lib64/libevent_core-1.4.so.2
              libevent-2.0.so.5 (libc6,x86-64) => /usr/local/lib/libevent-2.0.so.5
              libevent-1.4.so.2 (libc6,x86-64) => /usr/lib64/libevent-1.4.so.2

- tmux ビルド

    .. code-block:: bash

        $ wget http://downloads.sourceforge.net/tmux/tmux-1.8.tar.gz
        $ tar xvfz tmux-1.8.tar.gz
        $ cd tmux-1.8
        $ ./configure && make && sudo make install
        $ tmux -V
        tmux 1.8

