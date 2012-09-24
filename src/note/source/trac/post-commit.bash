.. code-block:: bash
    
    #: configure

    BASEDIR=/thome/sites
    CODE=apps
    REPO=apps
    CNAME=trac.lafoglia.jp
    NOTIFY="developers@$CNAME"
    TITLE="$CNAME-$CODE"
    SCRIPT=sync.bash
    URL=https://$CNAME/$CODE/trac/browser
    PROJECT=$CODE

    #: Execute Trac Synchronization

    $BASEDIR/$CNAME/prj/$SCRIPT  $CODE $REPO

    #: Mail to group

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
    
