=========
south
=========

.. contents:: South

リソース
=============

- チュートリアル : http://ae35.bitbucket.org/south-doc-ja/tutorial/

インストール
===============

::

    $ pip install South
    Downloading/unpacking South
      Downloading South-0.7.3.tar.gz (70Kb): 70Kb downloaded
      Running setup.py egg_info for package South
    Installing collected packages: South
      Running setup.py install for South
    Successfully installed South
    Cleaning up...

::

    yolk -l | grep South
    South           - 0.7.3        - active 


settings.py
---------------

::

    (main)hdknr@sqg:~/remote$ svn diff settings.py

    Index: settings.py
    ===================================================================
    --- settings.py (リビジョン 1006)
    +++ settings.py (作業コピー)
    @@ -155,5 +155,9 @@
     }
     
     #
    +INSTALLED_APPS +=('south',)  #: for Model Migration


syncdb
-----------

- syncdb忘れずに

::

    (main)hdknr@sqg:~/remote$ python manage.py syncdb
    Syncing...
    Creating tables ...
    Creating table south_migrationhistory
    Installing custom SQL ...
    Installing indexes ...
    Installed 25 object(s) from 1 fixture(s)
    
    Synced:
     > django.contrib.auth
     > django.contrib.contenttypes
     > django.contrib.sessions
     > django.contrib.sites
     > django.contrib.messages
     > django.contrib.staticfiles
     > django.contrib.admin
     > south
    
    Not synced (use migrations):
     - membership
    (use ./manage.py migrate to migrate these)


初期化(schemamigration --initial)
------------------------------------------------

:: 

    (main)hdknr@sqg:~/remote$ python manage.py schemamigration  membership --initial
    Creating migrations directory at '/home/hdknr/ve/main/src/remote/membership/migrations'...
    Creating __init__.py in '/home/hdknr/ve/main/src/remote/membership/migrations'...
     + Added model membership.Member
     + Added model membership.Prospect
     + Added model membership.Service
     + Added model membership.Order
     + Added model membership.MemberSerial
    Created 0001_initial.py. You can now apply this migration with: ./manage.py migrate membership

- この時点で migrations ディレクトリが作成される

::

    (main)hdknr@sqg:~/remote$ svn status
    M       settings.py
    ?       membership/migrations
    (main)hdknr@sqg:~/ve/main/src/c
    }}}
    {{{
    (main)hdknr@sqg:~/ve/main/src/remote$ tree membership/migrations/
    membership/migrations/
    ├── 0001_initial.py
    ├── __init__.py
    └── __init__.pyc
    
    0 directories, 3 files

::

    (main)hdknr@sqg:~/ve/main/src/remote$ wc membership/migrations/*.py
      301  1175 24811 membership/migrations/0001_initial.py
        0     0     0 membership/migrations/__init__.py
      301  1175 24811 合計


- 既にテーブルがあるので、--fake で最初のマイグレーションを走らせる

::

    (main)hdknr@sqg:~/remote$ python manage.py migrate  membership --fake 0001
     - Soft matched migration 0001 to 0001_initial.
    Running migrations for membership:
     - Migrating forwards to 0001_initial.
     > membership:0001_initial
       (faked)

- この時点でヒストリが作成

::

    mysql> select * from south_migrationhistory;
    +----+------------+--------------+---------------------+
    | id | app_name   | migration    | applied             |
    +----+------------+--------------+---------------------+
    |  2 | membership | 0001_initial | 2012-02-19 19:50:53 |
    +----+------------+--------------+---------------------+
    1 row in set (0.06 sec)

モデル修正
===============

- membership.models.Memberにフィールドを追加する

:: 

    (main)hdknr@sqg:~/remote$ vi membership/models.py
    (main)hdknr@sqg:~/remote$ svn diff
    Index: membership/models.py
    ===================================================================
    --- membership/models.py        (リビジョン 1010)
    +++ membership/models.py        (作業コピー)
    @@ -102,7 +102,9 @@
             
         objects = MemberManager()
     
    +    has_error = models.BooleanField(u'エラー修了',default=False, )

マイグレーションスクリプト作成
================================================

 - マイグレーション名を指定せずに --auto でマイグレーションスクリプトを生成させる

::

    (main)hdknr@sqg:~/remote$ python manage.py schemamigration membership --auto
     + Added field has_error on membership.Member
    Created 0002_auto__add_field_member_has_error.py. 
    You can now apply this migration with: ./manage.py migrate membership

::

    (main)hdknr@sqg:~/remote$ svn status
    M       membership/models.py
    ?       membership/migrations/0002_auto__add_field_member_has_error.py


マイグレート
==============

- マイグレーション

:: 

    (main)hdknr@sqg:~/remote$ python manage.py migrate membership
    Running migrations for membership:
     - Migrating forwards to 0002_auto__add_field_member_has_error.
     > membership:0002_auto__add_field_member_has_error
     - Loading initial data for membership.
    Installed 25 object(s) from 1 fixture(s)


- テーブルに追加されている (:doc:`tools_mandb` )

::

    (main)hdknr@sqg:~/remote$ python manage.py db --c ddl --t membership_member;
    
    CREATE TABLE `membership_member` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      -- 途中省略
      --
      `has_error` tinyint(1) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=304 DEFAULT CHARSET=utf8;
    }}}

- ヒストリ 確認

::

    (main)hdknr@sqg:~/remote$ python manage.py db --c data --t south_migrationhistory > membership/migrations/hsitory.sql

::

    (main)hdknr@sqg:~/remote$ grep INSERT membership/migrations/history.sql 

    INSERT INTO `south_migrationhistory` 
    (`id`, `app_name`, `migration`, `applied`) 
    VALUES 
    (1,'membership','0001_initial','2012-02-19 19:50:53'),
    (2,'membership','0002_auto__add_field_member_has_error','2012-02-19 19:52:52');
