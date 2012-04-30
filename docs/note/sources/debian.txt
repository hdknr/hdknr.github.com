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

よくやる
--------

::

    wget -O - http://hdknr.github.com/docs/note/sources/debian.txt | sed -n 's/^setup\$\s\+\(.\+\)/\1/p' |tr -d "\r" | bash

::

    setup$ sudo apt-get install wget curl lsb-release rsync -y
    setup$ sudo aptitude install build-essential make gcc g++ bison -y 
    setup$ sudo aptitude install lsof locate ntpdate sudo tmux screen vim dnsutils openssh-client openssh-server -y 
    setup$ sudo aptitude install unzip subversion -y
    setup$ sudo aptitude install libyaml-dev -y
    setup$ sudo aptitude install pkg-config
