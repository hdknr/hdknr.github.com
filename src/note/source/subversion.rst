=============
Subversion
=============

.. contents::
    :local:


post-commit
=============


.. code-block:: bash
    
    CODE=cms
    REPO=cms
    TITLE="lafoglia-$CODE"
    URL=https://trac.lafoglia.jp/$CODE/trac/browser
    NOTIFY="develoeprs@lafoglia.jp"
    PROJECT=lafoglia-$CODE
    /home/sites/trac.lafoglia.jp/prj/sync.sh $CODE $REPO
    REPOSITORY=$1
    REVISION=$2
    SENDMAIL=/usr/sbin/sendmail
    ICONV=/usr/bin/iconv
    SVNLOOK=/usr/bin/svnlook
    NKF=/usr/bin/nkf
    LC=ja_JP.UTF-8
    {
            LOGMSG=`LANG=$LC $SVNLOOK -r $REVISION log $REPOSITORY`
            echo "From: $NOTIFY"
            echo "To: $NOTIFY"
            echo Subject: $TITLE  r${REVISION} `$SVNLOOK -r $REVISION dirs-changed $REPOSITORY|sed 's;/$;;'`
            echo "Content-Type: text/plain; charset=utf8"
            echo
            (
                    echo "Log message for $URL"
                    echo $LOGMSG
                    echo
                    echo -n "Author: "
                    LANG=$LC $SVNLOOK -r $REVISION author $REPOSITORY
                    LANG=$LC $SVNLOOK -r $REVISION date   $REPOSITORY
                    echo
                    echo "Files changed:"
                    LANG=$LC $SVNLOOK -r $REVISION changed $REPOSITORY
                    echo
                    LANG=$LC $SVNLOOK -r $REVISION diff $REPOSITORY
            ) 
    } 2>&1 | $SENDMAIL $NOTIFY


このハンドラで使われている同期スクリプトは以下のようになっています。
:term:`virtualenv` でも動作させることがあるので :term:`Python` と trac-admin をフルパスで指定しています。

.. code-block:: bash

    #!/bin/bash
    #
    PY=/home/system/ve/main/bin/python
    TA=/home/system/ve/main/bin/trac-admin
    BASE=`dirname $0`
    echo $BASE/$1
    $PY $TA $BASE/$1/trac repository resync $2
    


コマンド
================


svn log
--------


svn diff
---------


コミット内容
^^^^^^^^^^^^^

- r1022の修正内容

.. code-block:: bash

    $svn diff -r 1021:1022
