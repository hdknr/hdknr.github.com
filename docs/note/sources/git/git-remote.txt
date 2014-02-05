git remote (git-remote) - manage set of tracked repositories 
===============================================================

シンタックス
-------------

::

    git remote add [-t <branch>] [-m <master>] [-f] [--tags|--no-tags] [--mirror=<fetch|push>] <name> <url>


リモートレポジトリの表示
----------------------------

::

    git remote [-v | --verbose]

::

    $ git remote -v

    origin  ssh://git@github.com/hdknr/pyjwkest.git (fetch)
    origin  ssh://git@github.com/hdknr/pyjwkest.git (push)


リモートレポジトリを削除
---------------------------

.. code-block:: bash

    $ git remote rm hidelafoglia


URLを変更(http->sshとか)


::

    $ git remote set-url origin git@github.com:hdknr/orevim.git



Fork先を追加して、Fork先のコミットを反映する
----------------------------------------------------------------------

俺Fork(origin)のみの状態:: 

    $ git remote -v

    origin  ssh://git@github.com/hdknr/pyjwkest.git (fetch)
    origin  ssh://git@github.com/hdknr/pyjwkest.git (push)


Forkもと(rohe)を追加:: 

    $ git remote add rohe https://github.com/rohe/pyjwkest.git

    $ git remote -v

    origin  ssh://git@github.com/hdknr/pyjwkest.git (fetch)
    origin  ssh://git@github.com/hdknr/pyjwkest.git (push)
    rohe    https://github.com/rohe/pyjwkest.git (fetch)
    rohe    https://github.com/rohe/pyjwkest.git (push)

Fork元のmasterをpull::


    $ git pull rohe master

    remote: Counting objects: 126, done.
    remote: Compressing objects: 100% (56/56), done.
    remote: Total 100 (delta 54), reused 77 (delta 31)
    Receiving objects: 100% (100/100), 32.37 KiB, done.
    Resolving deltas: 100% (54/54), completed with 11 local objects.
    From https://github.com/rohe/pyjwkest
     * branch            master     -> FETCH_HEAD
    Updating c7422fe..420d698
    Fast-forward
     script/jwdecrypt.py           |    8 +-
     script/jwenc.py               |    8 +-
     script/jwk_create.py          |    6 +-
     setup.py                      |   19 ++--
     src/jwkest/__init__.py        |   71 +++++++++---
     src/jwkest/aes_key_wrap_m2.py |  105 +++++++++++++++++
     src/jwkest/gcm.py             |  136 ++++++++++++++--------
     src/jwkest/jwe.py             |  590 +++++++++++++++++++++++++++++++++++++++++++++++++++++++----------------------------------------
     src/jwkest/jwk.py             |  454 +++++++++++++++++++++++++++++++++++++++++++++++++------------------------
     src/jwkest/jws.py             |  349 +++++++++++++++++++++++++++++++++++++++++++-------------
     tests/test_0_jwk.py           |  119 +++++++++++--------
     tests/test_1_jws.py           |  171 ++++++++++++++++++++--------
     tests/test_2_jwe.py           |  310 +++++++++++++++++++++++++++++++++++++++-----------
     13 files changed, 1624 insertions(+), 722 deletions(-)
     create mode 100644 src/jwkest/aes_key_wrap_m2.py
    
::

    $ git status
    
    # On branch master
    # Your branch is ahead of 'origin/master' by 17 commits.
    #
    nothing to commit (working directory clean)

俺フォークへpush::

    $ git push
    Counting objects: 126, done.
    Compressing objects: 100% (33/33), done.
    Writing objects: 100% (100/100), 32.37 KiB, done.
    Total 100 (delta 54), reused 100 (delta 54)
    To ssh://git@github.com/hdknr/pyjwkest.git
       c7422fe..420d698  master -> master

