=============
定期的実行
=============

( :ref:`guide-beat` )

beat
======

- ワーカーとBeatを分離して動かすと動いている

    - http://note.harajuku-tech.org/celery-periodic-task

- RabbitMQ, Django(MySQL)でうごいています。

Misc
=====

celeryd(ワーカー)でbeat をうごかせるか？
------------------------------------------------

Macで動いていない(気のせい？)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Debianでは動いた
^^^^^^^^^^^^^^^^^^^^^^

amqp
~~~~~~~~~~~~~~

::

    (tact)hdknr@wzy:~/ve/tact/src/paloma/example/app$ sudo /etc/init.d/paloma start

    running command
    palaoma workder  
        ['/home/hdknr/ve/tact/bin/paloma_worker.py', 'celeryd', '--loglevel', 'DEBUG', '--pidfile', '/tmp
    /celery.pid', '--logfile', '/tmp/celery.log', '--beat', '--scheduler', 'djcelery.schedulers.DatabaseScheduler']

    /home/hdknr/ve/tact/local/lib/python2.7/site-packages/djcelery/loaders.py:110: UserWarning: Using settings.DEBUG leads to a memory leak, never use this setting in production environments!  warnings.warn("Using settings.DEBUG leads to a memory leak, never " 
     -------------- celery@wzy v3.0.5 (Chiastic Slide)
    ---- **** ----- 
    --- * ***  * -- [Configuration]
    -- * - **** --- . broker:      amqp://guest@localhost:5672//
    - ** ---------- . app:         default:0x1534410 (djcelery.loaders.DjangoLoader)
    - ** ---------- . concurrency: 1 (processes)
    - ** ---------- . events:      OFF (enable -E to monitor this worker)
    - ** ---------- 
    - *** --- * --- [Queues]
    -- ******* ---- . celery:      exchange:celery(direct) binding:celery
    --- ***** ----- 

    [Tasks]
      . celery.backend_cleanup
      . celery.chain
      . celery.chord
      . celery.chord_unlock
      . celery.chunks
      . celery.group
      . celery.map
      . celery.starmap
      . paloma.tasks.bounce
      . paloma.tasks.enqueue_schedule
      . paloma.tasks.send_email
      . paloma.tasks.trigger_schedule
    
celery.log::

    [2012-08-07 11:22:56,328: DEBUG/MainProcess] (0.000) SELECT `djcelery_periodictasks`.`ident`, `djcelery_periodictasks`.`last_update` FROM `djcelery_periodictasks` WHERE `djcelery_periodictasks`.`ident` = 1 ; args=(1,)
    [2012-08-07 11:22:56,329: DEBUG/Beat] Celerybeat: Waking up in 5.00 seconds.

インターバルが到達したとき::

    [2012-08-07 11:40:48,253: DEBUG/Beat] Current schedule:

    <ModelEntry: celery.backend_cleanup celery.backend_cleanup(*[], **{}) {<crontab: 0 4 * * * (m/h/d/dM/MY)>}> 33 
    <ModelEntry: NotifyTiimeMail paloma.tasks.trigger_schedule(*[None], **{}) {<freq: 1.00 minute>}>

Django Broker
~~~~~~~~~~~~~~

Django Brokerでも動いたが、ampq brokerと違って、BeatのログがCeleryには出ない。




