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

リポジトリおいて最も新しく追加された `revision`_ であると同時に、最も新しく変更された `head`_ のこと

default
--------

デフォルトブランチ

- svn :  trunk
- git :  maste

branch
-------

- http://mercurial.selenic.com/wiki/Branch
- "diverged line of development"

branchは3つの方法で作成される

- レポジトリクローン
- `anonymous branch`_
- `named branch`_

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
   


.hgrc
=======

- 設定
- $HOME/.hgrc
- `man hgrc <http://linux.die.net/man/5/hgrc>`_ 

-  ユーザ−名

::
    
    [ui]
    username=hdknr



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
      - hg update [#]_

    * - 最新を取得して更新(a+b)
      - git pull
      - hg pull -u

.. [#] hg up, hg checkout, hg co 等でも良い



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
