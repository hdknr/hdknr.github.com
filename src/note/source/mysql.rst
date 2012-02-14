===========
MySQL
===========

.. contents:: MySQL

management
===============

- `パスワード変更 <http://hdknr.com/post/80662982/mysql-set-password-for>`_
- `パスワードリセット <http://dev.mysql.com/doc/refman/4.1/ja/resetting-permissions.html>`_
- 

トレースをとるには？
------------------------------------

- my.cnf に ログファイルの場所を指定してリスタート ( RedHat? : /etc/my.cnf , Debian : /etc/mysql/my.cnf )

::
    [mysqld]
    log=/tmp/xxx.log
    # Debian では /etc/mysql/my.cnfにコメントアウトされているlogエントリを使ったほうがいいです。

- Debianでは /var/log/mysql/mysql.log がデフォルトのようです。 

特権ユーザ−
--------------

.. code-block:: mysql

    REVOKE ALL PRIVILEGES ON * . * FROM  'prospects'@'localhost';
    
    GRANT ALL PRIVILEGES ON * . * TO  'prospects'@'localhost' WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0 ;
    

SQL
=====

- 年月集約

.. code-block:: mysql

    select date_format(card_expire, '%%Y-%%m') as month, count(*) as count 
    from credit_card  
    group by date_format(card_expire, '%%Y-%%m')
    oorder by card_expire;

- テーブルコピー

.. code-block:: mysql

     create table myiduser_bk as select * from myiduser;


- `正規表現 <http://dev.mysql.com/doc/refman/5.1/ja/regexp.html>`_

.. code-block:: mysql
    
    select count(*) from HOGE where userid  REGEXP '[[:digit:]]{6}';
    select count(*) from HOGE where userid NOT REGEXP '[[:digit:]]{6}';

- データベース作成


.. code-block:: mysql

    CREATE DATABASE `newdatabase` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;


- encoding

    - `xoops: ujis環境のxoopsをutf8環境にあるmysql に移行 <http://hidelafoglia.livejournal.com/47093.html>`_

.. code-block:: mysql

    SET CHARACTER SET utf8;

エンコーディング確認

.. code-block:: mysql

     show variables like "char%";

- `照合順序 <http://harajuku-tech.posterous.com/mysql37-collationitpro>`_



mysqldump
===================================


Fixture用にMySQLダンプを作る
---------------------------------------------

**complete-insert**  で可変カラム対応
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- スキーマが変わるとエラーになる

::

    ERROR 1136 (21S01) : Column count doesn't match value count at row 1

- **complete-insert**  オプションでdump を作成する。

::

    $ mysqldump -u $ROOT --password=$PWD --no-create-info --complete-insert  $APP_DB > ../dump.sql 


1行1SQLで落とす ( --skip-extended-insert )
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    $ mysqldump -c --order-by-primary --skip-extended-insert -u root --password=password mydb



指定したテーブルのみ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    $ mysqldump -u ユーザ名 -p -t データベース名 テーブル1 テーブル2...> ファイル名


DDL分のみ
^^^^^^^^^^^

::

    --no-data, -d 


Trouble
===========

- PHPで確認

::

      $link = mysql_connect($host_url,$user,$pass) or  die('Could not connect: ' . mysql_error());



Python
=======

- `Django: MySQLのテーブルデータサイズなどの取得 <http://harajuku-tech.posterous.com/django-mysql>`_

