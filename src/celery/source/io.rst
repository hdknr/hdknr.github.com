=====================
スケーラブル I/O
=====================

.. contents:: I/O

API
=====

I/O多重化
---------

- I/Oが可能になったファイル識別子の一覧の通知をもらう仕組み
- 通知をもらったらファイル識別子に対してread/writeを行う。

epoll
^^^^^^^^^

- Linux

kqueue
^^^^^^^^^

- BSD

Overlapped I/O 
^^^^^^^^^^^^^^

- Windows

非同期I/O
-----------

- 通知が起きた時には read/write が完了している
- readの場合は、データをバッファで受け取っている。

IOCP
^^^^^^^^^

- Windows

AIO
^^^^^^^^^^

- AIX
- Solaris
- Linux は librt で pthread 実装

Libraries
===========

libevent
-----------

- epoll/kqueueの仮想化

libev
---------

libuv
---------

Highlevel Library
===================

eventlet
----------

gevent
--------

Twisted
--------

Tornado
---------


