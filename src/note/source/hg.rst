==========
Mercurial
==========

.. contents:: Mercurial

Basic
=======

changeset
---------

- **cset**
- http://mercurial.selenic.com/wiki/ChangeSet
- 単一不可分な変更
- commit すると changeset が作られます( checkin ともいいます )。
- `head`_ ではありません。
- root : 親無し changeset

metainfo
^^^^^^^^^^

- nodeid
- 変更ファイル一覧
- commiter:誰が
- commnet :なぜ
- time/date,tz : いつ
- `branch`_ 名 : デフォルトが `default`_ 

marge changeset
------------------------

- 複数の `changeset`_ をマージした１つのチェンジセット。
- つまり複数の paranet を持つ。


revision
----------

- `changeset`_ の番号

head
-------

- マージされていないチェンジセット

tip
----

- tipは `head` です。
- リポジトリおいて最も新しく追加された `revision`_ であると同時に、最も新しく変更された `head`_ のこと

default
--------

デフォルトブランチ

- svn :  trunk
- git :  maste

branch
-------

- http://mercurial.selenic.com/wiki/Branch
- "diverged line of development"

branchは4つの方法で作成される

- レポジトリクローン
- `anonymous branch`_
- `named branch`_
- `bookmarks`

anonymous branch
-------------------------

- 匿名ブランチ , 名無しブランチ
- 共通の親から派生した2つ以上のリビジョン
- 次の場合に作られる

    - ある親リビジョンnから派生したリビジョンn+1をcommitした後に、同じ親からリビジョンn+2を作成したとき
    - リモートリポジトリの更新をpullしたとき

named branch
--------------

- ある親から派生したリビジョンとその子孫につけられる名前
- リポジトリは初期状態で単一の名前付きブランチ(`default`_)を持っている
- また、そのブランチのHEADリビジョンを指す。


multiple heads
---------------------

- `anonymous branch`_ が複数できている状態の事

bookmarks
------------

- `changeset` へのタグみたいなもの
- :doc:`git` のブランチに近い
- `branch` はデフォルトで消し去れないが、 `bookmarks` は消す事ができる
- ローカルでブランチングする時には `bookmarks` を使って、　チームのマスターでは計画的に `branch` を作成する。

Cheat
======

- http://troter.jp/mercurial-cheatsheet/

未登録ファイルを全て追加
----------------------------------------

オプション、引数無しで hg add 

:: 

    (docs)hdknr@sqg:~/ve/docs/tmp/bitinit$ hg status
    R requirments.txt
    ? AUTHORS
    ? INSTALL
    ? LICENSE
    ? MANIFEST.in
    ? NOTICE
    ? README
    ? conf.yml
    ? requirements.txt
    ? setup.cfg
    ? setup.py

    (docs)hdknr@sqg:~/ve/docs/tmp/bitinit$ hg add
    AUTHORS を追加登録中
    INSTALL を追加登録中
    LICENSE を追加登録中
    MANIFEST.in を追加登録中
    NOTICE を追加登録中
    README を追加登録中
    conf.yml を追加登録中
    requirements.txt を追加登録中
    setup.cfg を追加登録中
    setup.py を追加登録中

Flow
=====

- hgflow : https://bitbucket.org/yujiewu/hgflow/wiki/Home


Bitbucket
==========

- API : http://confluence.atlassian.com/display/BITBUCKET/Repositories
   

設定
=============================================================================

.. _hg.hgrc:

hgrc
-----------

- http://www.selenic.com/mercurial/hgrc.5.html
- 設定
- $HOME/.hgrc
- `man hgrc <http://linux.die.net/man/5/hgrc>`_ 
-  ユーザ−名

::
    
    [ui]
    username=hdknr

mercurial.ini
---------------

- Windowsの場合はmercurial.ini
- $HOMEPATH/mercurial.ini 

    - C:\Users\Administrator とか。


Git/Mercurial
======================


.. list-table::
    :header-rows: 1

    * - タスク
      - :doc:`Git <git>`
      - Mercural

    * - 最初の取得
      - git clonse {{url}}
      - hg clone {{url}}

    * - 最新の取得(のみ)(a)
      - git fetch
      - hg pull

    * - 取得したもので更新(b)
      - git merge origin/master
      - :ref:`hg.update` 

    * - 最新を取得して更新(a+b)
      - git pull
      - hg pull -u




オリジナルから更新を反映
------------------------------

hg
^^^^

取り込み予定のリモートの変更内容::

    hg incoming https://bitbucket.org/birkenfeld/sphinx

リモートに対する自分の変更点の内容確認::

     hg outgoing https://bitbucket.org/birkenfeld/sphinx

必要であれば、各チェンジセットの内容をみる ::

    hg diff -c 3536:660be19d7963

リモートから取り込む ::

    hg pull https://bitbucket.org/birkenfeld/sphinx

マージする ::

    hg merge

コミット::

    hg commit -m "Merged latest original updates "

自分のリモートにpush ::

     hg push --new-branch


- http://note.harajuku-tech.org/mercurial-sphinx-devfork
- http://note.harajuku-tech.org/-bitbucket-atlassian-japan-confluence

git
^^^

mankyd というリモートを追加して、それを自分のmasterにpullする。

::

    git remote add mankyd https://github.com/mankyd/jinjatag.git
    git pull mankyd master

チェンジセットの変更内容をみる
------------------------------------

:: 
    
    hg diff -c 3536:660be19d7963

履歴参照
============================================================================

log
-----

- 一覧
- **--rev リビジョン** で個別のチェンジセット


ツリー表示(glog)
----------------------

:ref:`hg.glog` を使う為に、extension の `設定`
 　
::

    [extensions]
    graphlog =
    

::

    $ hg glog

履歴操作
============================================================================


削除(strip)
------------

- :ref:`hg.strip` コマンドを使うには :term:`MqExtension` が必要

- hgrc に設定

::

    [extensions]
    mq =
 

.. _hg.tag:

タグ
============================================================================

一覧
-----

::

    (sandbox)hdknr@wzy:~/ve/sandbox/src/hg/hgsandbox$ hg tags
    
    tip                                5:9990e681399a
    f1.1-completed                     5:9990e681399a
    f1-completed                       3:1f70b972f390

記録
-----

- タグ付けはそれ自体がチェンジセットとして記録されます。

    - HEADにタグを付けると、それはHEADではなくなる

::

    (sandbox)hdknr@wzy:~/ve/sandbox/src/hg/hgsandbox$ hg head
    チェンジセット:   3:1f70b972f390
    ブックマーク:     hoge
    タグ:             tip
    ユーザ:           hdknr
    日付:             Thu Aug 09 19:12:34 2012 +0900
    要約:             add hi.py to hoge bookmark
    
    (sandbox)hdknr@wzy:~/ve/sandbox/src/hg/hgsandbox$ hg tag f1-completed

    (sandbox)hdknr@wzy:~/ve/sandbox/src/hg/hgsandbox$ hg head
    チェンジセット:   4:04d5fc842ae5
    ブックマーク:     hoge
    タグ:             tip
    ユーザ:           hdknr
    日付:             Fri Aug 10 04:34:22 2012 +0900
    要約:             Added tag f1-completed for changeset 1f70b972f390
    
    (sandbox)hdknr@wzy:~/ve/sandbox/src/hg/hgsandbox$ hg log -r 3
    チェンジセット:   3:1f70b972f390
    タグ:             f1-completed
    ユーザ:           hdknr
    日付:             Thu Aug 09 19:12:34 2012 +0900
    要約:             add hi.py to hoge bookmark
    

ローカルタグ(-l)
---------------------

- ローカルレポジトリだけのタグを付ける事ができる。
- タグ付けのチェンジログは記録されません。
- タグの一覧でも表示されます。

.. code-block:: bash

    (sandbox)hdknr@wzy:~/ve/sandbox/src/hg/hgsandbox$ hg head
    チェンジセット:   5:9990e681399a
    ブックマーク:     hoge
    タグ:             tip
    ユーザ:           hdknr
    日付:             Fri Aug 10 04:36:56 2012 +0900
    要約:             echo current time
    
    (sandbox)hdknr@wzy:~/ve/sandbox/src/hg/hgsandbox$ hg tag f1.1-completed -l

    (sandbox)hdknr@wzy:~/ve/sandbox/src/hg/hgsandbox$ hg head
    チェンジセット:   5:9990e681399a
    ブックマーク:     hoge
    タグ:             f1.1-completed
    タグ:             tip
    ユーザ:           hdknr
    日付:             Fri Aug 10 04:36:56 2012 +0900
    要約:             echo current time



移動
-----

チェンジセットを明示的にしてして **--force** オプション指定するとtagが付け替え出来るようです。

.. code-block:: bash

    % hg tag 
        --repository C:\Shared\Projects\MvcSandbox 
        --rev 2 
        --user hdknr 
        --message=Moved tag ProjectEnrolled to changeset 6c2cb0b59567 (from changeset f0d19b3cde59) 
        --force 
        ProjectEnrolled


Bookmark
================================================================================================


Command
================================================================================================

(`コマンド一覧 <http://mercurial.selenic.com/wiki/HgCommands>`_ )

.. _hg.update:

hg update
-----------

- `作業領域の内容更新します。 <http://mercurial.selenic.com/wiki/Update>`_
- (ないしリビジョンの切り替え)
- alias : update,up,checout,co
- ブランチ、リビジョンも切り替えます。

    .. code-block:: bash
    
            (main)hdknr@wzy:~/ve/main/src/adconnect/samples/X509$ hg update RefCtlr
            ファイルの更新数 0、 マージ数 0、 削除数 0、 衝突未解消数 0

            (main)hdknr@wzy:~/ve/main/src/adconnect/samples/X509$ hg branch
            RefCtlr

            (main)hdknr@wzy:~/ve/main/src/adconnect/samples/X509$ hg update default
            ファイルの更新数 0、 マージ数 0、 削除数 0、 衝突未解消数 0

            (main)hdknr@wzy:~/ve/main/src/adconnect/samples/X509$ hg branch
            default
        

.. _hg.glog:

hg glog
----------

- グラフィックログの表示。 http://mercurial.selenic.com/wiki/GraphlogExtension

.. _hg.strip:

hg strip
-----------

- `チェンジセットを削除 <http://mercurial.selenic.com/wiki/Strip>`_
- :term:`MqExtension`

.. _hg.bookmark:
.. _hg.bookmarks:

hg bookmarks
---------------

- ブックマークの管理 

hg revert
-------------

- `親リビジョンの状態でファイルを復旧 <http://mercurial.selenic.com/wiki/Revert>`_
- rm した時とかコミット前だったらこれで対応可能。

-  -a --all                  引数指定が無い場合に、 全ファイルの内容を復旧
-  -d --date 日時            当該日時の最新リビジョンを使用
-  -r --rev リビジョン       当該リビジョン時点の内容で復旧
-  -C --no-backup            取り消し実施前内容のバックアップを抑止
-  -I --include パターン [+] パターンに合致したファイルを処理対象に追加
-  -X --exclude パターン [+] パターンに合致したファイルを処理対象から除外
-  -n --dry-run              実施予定の処理内容の表示のみで処理実施は抑止
-     --mq                   パッチ管理リポジトリへの操作

Extensions
=============

.. glossary::

    MqExtension
        - 本体同梱されてます。
        - http://mercurial.selenic.com/wiki/MqExtension

