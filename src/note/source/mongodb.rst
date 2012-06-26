============
MongoDB
============

.. contents:: MongoDB

Install 
========

-  http://docs.mongodb.org/manual/tutorial/install-mongodb-on-debian-or-ubuntu-linux/

パッケージキー
-------------------

::

    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10

apt line
------------

/etc/apt/sources.list.d/10gen.list  ::

    deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen


apt-get update/install
-------------------------

::

    sudo apt-get update

::

    sudo apt-get install mongodb-10gen


:: 

    $ sudo lsof -c mongo

    COMMAND   PID    USER   FD   TYPE             DEVICE   SIZE/OFF   NODE NAME
    mongod  15498 mongodb  cwd    DIR                8,1       4096      2 /
    mongod  15498 mongodb  rtd    DIR                8,1       4096      2 /
    mongod  15498 mongodb  txt    REG                8,1    8683688 269570 /usr/bin/mongod
    mongod  15498 mongodb  mem    REG                8,1    1583120 652806 /lib/x86_64-linux-gnu/libc-2.13.so
    mongod  15498 mongodb  mem    REG                8,1      89056 652957 /lib/x86_64-linux-gnu/libgcc_s.so.1
    mongod  15498 mongodb  mem    REG                8,1     530736 653669 /lib/x86_64-linux-gnu/libm-2.13.so
    mongod  15498 mongodb  mem    REG                8,1     991496 261125 /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.17
    mongod  15498 mongodb  mem    REG                8,1     131107 653698 /lib/x86_64-linux-gnu/libpthread-2.13.so
    mongod  15498 mongodb  mem    REG                8,1     136936 653709 /lib/x86_64-linux-gnu/ld-2.13.so
    mongod  15498 mongodb    0u   CHR                1,3        0t0   1199 /dev/null
    mongod  15498 mongodb    1w   REG                8,1       1640 523119 /var/log/mongodb/mongodb.log
    mongod  15498 mongodb    2w   REG                8,1       1640 523119 /var/log/mongodb/mongodb.log
    mongod  15498 mongodb    3r   CHR                1,9        0t0   1204 /dev/urandom
    mongod  15498 mongodb    4uW  REG                8,1          6 523192 /var/lib/mongodb/mongod.lock
    mongod  15498 mongodb    5w   REG                8,1 1073741824 522295 /var/lib/mongodb/journal/j._0
    mongod  15498 mongodb    6u  IPv4              25954        0t0    TCP *:27017 (LISTEN)
    mongod  15498 mongodb    7u  unix 0xffff8800377ba480        0t0  25955 /tmp/mongodb-27017.sock
    mongod  15498 mongodb    8u  IPv4              25958        0t0    TCP *:28017 (LISTEN)
    
mongo
======

起動
-----

何も指定しないとtestデータベースへ接続

.. code-block:: bash


    (main)hdknr@wzy:~/ve/main/src$ mongo

    MongoDB shell version: 2.0.6
    connecting to: test
    > 

ヘルプ
-------

::

    > help
            db.help()                    help on db methods
            db.mycoll.help()             help on collection methods
    
            rs.help()                    help on replica set methods
    
            help admin                   administrative help
            help connect                 connecting to a db help
            help keys                    key shortcuts
            help misc                    misc things to know
            help mr                      mapreduce
    
            show dbs                     show database names
            show collections             show collections in current database
            show users                   show users in current database
            show profile                 show most recent system.profile entries with time >= 1ms
            show logs                    show the accessible logger names
            show log [name]              prints out the last segment of log in memory, 'global' is default
    
            use <db_name>                set current database
    
            db.foo.find()                list objects in collection foo
            db.foo.find( { a : 1 } )     list objects in foo where a == 1
    
            it                           result of the last line evaluated; use to further iterate
    
            DBQuery.shellBatchSize = x   set default number of items to display on shell
    
            exit                         quit the mongo shell

データベース
------------------


初期状態::

    > show dbs

    local   (empty)

test データベースはないが、レコードを追加すると作成される。

::

    > db.hdknr.save( {name : "hideki"} )

    > show dbs

    local   (empty)
    test    0.203125GB

データベース変更::

    > use tiopepe
    switched to db tiopepe

レコード追加すると作成される::

    > db.hdknr.save( {name : "nara" } )
    > show dbs

    local   (empty)
    test    0.203125GB
    tiopepe 0.203125GB




Python Driver
===================

::
    
    pip install --upgrade pymongo



Logfile
=========

/var/log/mongdb/mongdb.log
------------------------------

起動直後

::

    $ more /var/log/mongodb/mongodb.log
    
    Tue Jun 26 03:38:50 [initandlisten] MongoDB starting : pid=15498 port=27017 dbpath=/var/lib/mongodb 64-bit host=wzy
    Tue Jun 26 03:38:50 [initandlisten] db version v2.0.6, pdfile version 4.5
    Tue Jun 26 03:38:50 [initandlisten] git version: e1c0cbc25863f6356aa4e31375add7bb49fb05bc
    Tue Jun 26 03:38:50 [initandlisten] build info: Linux ip-10-110-9-236 2.6.21.7-2.ec2.v1.2.fc8xen #1 SMP Fri Nov 20 17:48:28 EST 2009 x86_64 BOOST_LIB_VERSION=1_41
    Tue Jun 26 03:38:50 [initandlisten] options: { command: [ "run" ], config: "/etc/mongodb.conf", dbpath: "/var/lib/mongodb", logappend: "true", logpath: "/var/log/mongodb/mon
    godb.log" }
    Tue Jun 26 03:38:50 [initandlisten] journal dir=/var/lib/mongodb/journal
    Tue Jun 26 03:38:50 [initandlisten] recover : no journal files present, no recovery needed
    Tue Jun 26 03:38:51 [initandlisten] preallocateIsFaster=true 14.94
    Tue Jun 26 03:38:53 [initandlisten] preallocateIsFaster=true 27.8
    Tue Jun 26 03:38:55 [initandlisten] preallocateIsFaster=true 15.56
    Tue Jun 26 03:38:55 [initandlisten] preallocateIsFaster check took 4.486 secs
    Tue Jun 26 03:38:55 [initandlisten] preallocating a journal file /var/lib/mongodb/journal/prealloc.0
                    314572800/1073741824    29%
                    534773760/1073741824    49%
                    765460480/1073741824    71%
                    975175680/1073741824    90%
    Tue Jun 26 03:39:09 [initandlisten] preallocating a journal file /var/lib/mongodb/journal/prealloc.1
    Tue Jun 26 03:39:12 [initandlisten] preallocating a journal file /var/lib/mongodb/journal/prealloc.2
    Tue Jun 26 03:39:14 [initandlisten] waiting for connections on port 27017
    Tue Jun 26 03:39:14 [websvr] admin web console waiting for connections on port 28017
    Tue Jun 26 03:40:14 [clientcursormon] mem (MB) res:14 virt:100 mapped:0
