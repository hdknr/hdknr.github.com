=====
Git
=====


.. glossary::

    git
        - http://git-scm.com/
        - http://schacon.github.com/git/git.html
        - http://progit.org/  , http://progit.org/book/ja/

    starting point


.. contents:: git resource


修正を戻す
==========

全て戻す

::

    $ git checkout .

ディレクトリを指定して戻す

::

    $ git checkout docs

リビジョンを指定して戻す

::

    $ git checkout -l 2a6ac3f60426d4ce4604f387033446f750911d8f source/jose.rst

コンフリクト
=============

- http://harajuku-tech.posterous.com/git-pull-conflictgit-commit

Automatic merge failed; fix conflicts and then commit the result.
------------------------------------------------------------------------------------------


::


    $ git pull
    remote: Counting objects: 37, done.
    remote: Compressing objects: 100% (6/6), done.
    remote: Total 24 (delta 18), reused 24 (delta 18)
    Unpacking objects: 100% (24/24), done.
    From github.com:hdknr/hdknr.github.com
       2f14de6..2aedbae  master     -> origin/master
    CONFLICT (delete/modify): src/django/app/boa/models.pyc deleted in HEAD and modified in 2aedbaeddeb1a515f0199162b7e432987b287468. Version 2aedbae
    ddeb1a515f0199162b7e432987b287468 of src/django/app/boa/models.pyc left in tree.
    CONFLICT (delete/modify): src/django/app/settings.pyc deleted in HEAD and modified in 2aedbaeddeb1a515f0199162b7e432987b287468. Version 2aedbaedd
    eb1a515f0199162b7e432987b287468 of src/django/app/settings.pyc left in tree.
    Auto-merging src/django/source/conf.py
    Automatic merge failed; fix conflicts and then commit the result.
    

::

    $ git fetch origin
    $ git reset --hard origin

    HEAD is now at 2aedbae bash

ブランチ
============

git は１つのリポジトリ内に複数のブランチを作成することができます。

.. glossary::

    remote-tracking branch
        ローカルリポジトリに存在しているマスター以外のブランチは、リモートトラッキングブランチと呼ばれて参照できるようになっています。

    local branch
        :ref:`local_branch`

    remote branch
        :ref:`remote_branch`

    tracking branch
        (TBD)

    master branch
        masterブランチは自動的に作成されたデフォルトブランチ

- http://delicious.com/hdknr/git+branch


.. _local_branch:

local brach
-------------------

最初は `master branch` のみです。

::

    $ git branch 
    
    * master


experimental" という名前の新しいブランチを作成するには次のようにします。

::

    $ git branch experimental

    $ git branch

      experimental
    * master

アスタリスク付きが作業中のブランチ。 :ref:`git-checkout` で移動します。

::

    $ git checkout experimental

    M       src/note/source/git.rst
    M       src/note/source/index.rst
    Switched to branch 'experimental'

    $ git branch

    * experimental
      master

experimental の状態確認。

::

    $ git status

    # On branch experimental
    # Changed but not updated:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #       modified:   note/source/git.rst
    #       modified:   note/source/index.rst
    #
    # Untracked files:
    #   (use "git add <file>..." to include in what will be committed)
    #
    #       note/source/debian.rst

もう一回戻って、コミットする。

::

    $ git checkout master

    M       src/note/source/git.rst
    M       src/note/source/index.rst
    Switched to branch 'master'

    (docs)hdknr@cats:~/ve/docs/src/hdknr.github.com/src$ git commit -a -m "gitメモ更新"
    [master bc3cca5] gitメモ更新
     2 files changed, 350 insertions(+), 0 deletions(-)


.. _remote_branch:

remote branch
-------------------
::

    $ git branch -r

    origin/HEAD -> origin/master
    origin/master


Cheat
======

.. raw:: html
   
    (<a href="http://byte.kde.org/~zrusin/git/git-cheat-sheet-medium.png">Original</a><br/>)

    <a href="http://www.textdrop.net/wp-content/uploads/git-cheat-sheet-ja.svg">
    <img src="http://www.textdrop.net/wp-content/uploads/git-cheat-sheet-ja.svg"/>
    </a>


.. _git-config:

git config - Get and set repository or global options
=======================================================================

.. glossary::

    git-config
        - http://schacon.github.com/git/git-config.html

設定ファイル
---------------

- $GIT_DIR/config   レポジトリ設定

    - GIT_CONFIG環境変数で切り替え可能です。 
    
- ~/.gitconfig      ユーザ−設定/いわゆる"global"
- $(prefix)/etc/gitconfig   システム設定

::

    $ dpkg -L git  | grep config

    /usr/lib/git-core/git-config
    /usr/lib/git-core/git-repo-config


変数
----


remote
^^^^^^^^^^

<name>  - 慣例的に "origin" が対象のリモート名。 追加できる。

.. list-table:: git config "remote"

    *   - 変数
        - 内容

    *   - remote.<name>.url
        - リモートのURL ( :ref:`git-fetch` / :ref:`git-push`

    *   - remote.<name>.pushurl
        - プッシュURL (:ref:`git-push` )

    *   - remote.<name>.proxy
        - プロキシ。使わないときは空。

    *   - remote.<name>.fetch
        - :ref:`git-fetch` "refspec" のデフォルト

    *   - remote.<name>.push
        - :ref:`git-push` "refspec" のデフォルト

    *   - remote.<name>.mirror
        - true が設定されると --mirror オプションが適用

    *   - remote.<name>.skipDefaultUpdate
        - If true, this remote will be skipped by default when updating using git-fetch(1) or the update subcommand of git-remote(1).

    *   - remote.<name>.skipFetchAll
        - If true, this remote will be skipped by default when updating using git-fetch(1) or the update subcommand of git-remote(1).

    *   - remote.<name>.receivepack
        - The default program to execute on the remote side when pushing. See option --receive-pack of git-push(1).

    *   - remote.<name>.uploadpack
        - The default program to execute on the remote side when fetching. See option --upload-pack of git-fetch-pack(1).

    *   - remote.<name>.tagopt
        - Setting this value to --no-tags disables automatic tag following when fetching from remote <name>. Setting it to --tags will fetch every tag from remote <name>, even if they are not reachable from remote branch heads. Passing these flags directly to git-fetch(1) can override this setting. See options --tags and --no-tags of git-fetch(1).

    *   - remote.<name>.vcs
        - Setting this to a value <vcs> will cause git to interact with the remote with the git-remote-<vcs> helper.

    *   - remotes.<group>
        - The list of remotes which are fetched by "git remote update <group>". See git-remote(1).

branch
^^^^^^^^^


.. list-table::

    *   - branch.autosetupmerge
        - :ref:`git branch <git-branch>` / :ref:`git-checkout` が新ブランチを作るモード。
          :ref:`git-pull` がブランチの開始地点から適切にマージする。
          
          このオプションが無くても --track / -- no-track でコントロールできる。

            - **false** : 手動 
            - **true **  : 自動 ( :term:`starting point` が :term:`remote-tracking branch` の時に自動セットアップ)
            - **always** :常に ( :term:`starting point` が :term:`remote-tracking branch` だろうと :term:`local branch` だろうと自動セットアップ)  
         
    *   - branch.autosetuprebase
        - When a new branch is created with git branch or git checkout that tracks another branch, this variable tells git to set up pull to rebase instead of merge (see "branch.<name>.rebase"). When never, rebase is never automatically set to true. When local, rebase is set to true for tracked branches of other local branches. When remote, rebase is set to true for tracked branches of remote-tracking branches. When always, rebase will be set to true for all tracking branches. See "branch.autosetupmerge" for details on how to set up a branch to track another branch. This option defaults to never.
         
    *   -  branch.<name>.remote
        -  :ref:`git-fetch` / :ref:`git-push` に指定されたブランチ名の fetch/pushする先
        
           デフォルトが **origin** 

    *   - branch.<name>.merge
        -  Defines, together with branch.<name>.remote, the upstream branch for the given branch. It tells git fetch/git pull/git rebase which branch to merge and can also affect git push (see push.default). When in branch <name>, it tells git fetch the default refspec to be marked for merging in FETCH_HEAD. The value is handled like the remote part of a refspec, and must match a ref which is fetched from the remote given by "branch.<name>.remote". The merge information is used by git pull (which at first calls git fetch) to lookup the default branch for merging. Without this option, git pull defaults to merge the first refspec fetched. Specify multiple values to get an octopus merge. If you wish to setup git pull so that it merges into <name> from another branch in the local repository, you can point branch.<name>.merge to the desired branch, and use the special setting . (a period) for branch.<name>.remote.



-l,--list (  list all )
------------------------------------------------


:: 

    $ git config -l

    user.name=hdknr
    user.email=gmail@hdknr.com
    core.repositoryformatversion=0
    core.filemode=true
    core.bare=false
    core.logallrefupdates=true
    remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
    remote.origin.url=git@github.com:hdknr/hdknr.github.com.git
    branch.master.remote=origin
    branch.master.merge=refs/heads/master


--get (get value: name [value-regex] )
------------------------------------------------------

::

    $ git config --get remote.origin.url

    git@github.com:hdknr/hdknr.github.com.git

.. _git-remote: 

git remote (git-remote) - manage set of tracked repositories 
===============================================================


.. _git-fetch:

git fetch  (git-fetch) - Download objects and refs from another repository
==============================================================================================================================


.. glossary::

    git-fetch
        - http://schacon.github.com/git/git-fetch.html

.. _git-push:

git push  (git-push) - Update remote refs along with associated objects
==============================================================================================================================


.. glossary::

    git-push
        - http://schacon.github.com/git/git-push.html


.. _git-branch:

git branch  (git-branch) - List, create, or delete branches 
==============================================================================================================================


.. glossary::

    git-branch
        - http://schacon.github.com/git/git-branch.html


.. _git-pull:

git pull  (git-pull) - Fetch from and merge with another repository or a local branch
==============================================================================================================================


.. glossary::

    git-pull
        - http://schacon.github.com/git/git-pull.html


.. _git-checkout:

git checkout  (git-checkout) - Checkout a branch or paths to the working tree
==============================================================================================================================


.. glossary::

    git-checkout
        - http://schacon.github.com/git/git-checkout.html


