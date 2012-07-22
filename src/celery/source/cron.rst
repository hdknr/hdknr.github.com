=============
定期的実行
=============

beat
======


celeryd(ワーカー)でbeat をうごかせるか？
------------------------------------------------

celerydの -B/--beat オプションでワーカー内で定期的なタスク実行が出来ることになっていますが、
`Windowsでは3.0では動かせないようです <http://docs.celeryproject.org/en/latest/faq.html#the-b-beat-option-to-celeryd-doesn-t-work>`_ 。
( Macの Homebrew, Debian Wheezy の環境でも動いていません )

::

    python ../manage.py celeryd \
        --beat  \
        --loglevel=DEBUG \
        --pidfile=/Users/hide/Desktop/tomate.pid \
        --logfile=/Users/hide/Desktop/tomate.log \
        --scheduler=djcelery.schedulers.DatabaseScheduler

::

    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/Users/hide/ve/docs/lib/python2.7/site-packages/billiard/forking.py", line 496, in main
        self = load(from_parent)
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/pickle.py", line 1378, in load
        return Unpickler(file).load()
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/pickle.py", line 858, in load
        dispatch[key](self)
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/pickle.py", line 880, in load_eof
        raise EOFError
    EOFError




