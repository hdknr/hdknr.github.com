==============
Test/Debug
==============

.. contents:: Test/Debug 

非同期コールが起きないようにする
==================================

CELERY_ALWAYS_EAGER
-----------------------------

settings.py で Trueに設定するとcelery.app.task.Task.apply_async
が強制的に apply()呼び出しを行うようになります。

.. code-block:: python

    CELERY_ALWAYS_EAGER = True


- @task() デコレータされている関数を delay()すると、 Task.apply_async()され、関数の処理が非同期処理メッセージとしてKombuにキューイングされます。
- CELERY_ALWAY_EAGER = Trueになっていると、 :meth:`~@Task.apply_async`  が、 :meth:`~@Task.apply` をフォワードするようになるので、
  子供タスクが全て終わるまで同期的に処理されます。 

Taskのモニター
===================

celerycam
----------

- Task の状況を Django の :ref:`djcelery.models.TaskState` に定期的に記録します。
- Worker に -E (イベント)オプションを付けて起動します。

    :: 
    
        $ python ../manage.py celeryd -l INFO -E
    
    ::
    
        -------------- celery@wzy v3.0.1 (Chiastic Slide)
        ---- **** ----- 
        --- * ***  * -- [Configuration]
        -- * - **** --- . broker:      amqp://guest@localhost:5672//
        - ** ---------- . app:         default:0x184fa50 (djcelery.loaders.DjangoLoader)
        - ** ---------- . concurrency: 1 (processes)
        - ** ---------- . events:      ON
        - ** ---------- 
        - *** --- * --- [Queues]
        -- ******* ---- . celery:      exchange:celery(direct) binding:celery
        --- ***** ----- 

    

- モニタープロセスを起動します。

    ::
    
            $ python ../manage.py celerycam
    

- Django Admin  で確認します。

    .. image:: debug/celerycam.01.png
        :scale: 60%

    .. image:: debug/celerycam.02.png
        :scale: 60%

 
- Brokerが :term:`RabbitMQ`, :term:`redis` の `時だけ動作するようです <http://stackoverflow.com/questions/5449163/django-celery-admin-interface-showing-zero-tasks-workers>`_ 。


djkombuをAdmin UI で見る
=========================

- Django BrokerだとKombuのメッセージを djkombu.mdels.Message に記録します。

    .. autoclass:: djkombu.models.Message
        :members:
    
- Django Admin UI を追加します。

    - djkombu.models.Queue クラスに __unicode__ を追加してやると見やすいです。

        .. code-block:: python
        
        
                from djkombu.models import Queue as KombuQueue,Message as KombuMessage
        
                ### KombuQueue
                class KombuQueueAdmin(admin.ModelAdmin):
                    list_display=tuple([f.name for f in KombuQueue._meta.fields ])
                admin.site.register(KombuQueue,KombuQueueAdmin)
            
                ### define __unicode__ to Queue class
                #   
                #def __unicode__(self):
                #   
                #   return self.name
        
                ### KombuMessage
                class KombuMessageAdmin(admin.ModelAdmin):
                    list_display=tuple([f.name for f in KombuMessage._meta.fields])
                admin.site.register(KombuMessage,KombuMessageAdmin)

DEBUG=True + print
====================




Admin UIでテーブルを見れるようにする。
=======================================

タスクの結果
=============

指定しないとDjango-celeryが :ref:`djcelery.models.TaskMeta` , :ref:`djcelery.models.TaskSetMeta` に書き込むようです。

.. todo::
    定期的にTaskMetaを削除する必要があるが。。。。 

Kombuのメッセージ
=======================


例:
----

.. code-block:: python

    if settings.DEBUG:
        try:
            from djkombu.models import Queue as KombuQueue,Message as KombuMessage
            from djcelery.models import TaskMeta,TaskSetMeta
    
            ### KombuQueue
            class KombuQueueAdmin(admin.ModelAdmin):
                list_display=tuple([f.name for f in KombuQueue._meta.fields ])
            admin.site.register(KombuQueue,KombuQueueAdmin)
                
            ### KombuMessage
            class KombuMessageAdmin(admin.ModelAdmin):
                list_display=tuple([f.name for f in KombuMessage._meta.fields])
            admin.site.register(KombuMessage,KombuMessageAdmin)
    
            ### TaskMeta
            class TaskMetaAdmin(admin.ModelAdmin):
                list_display=tuple([f.name for f in TaskMeta._meta.fields])
            admin.site.register(TaskMeta,TaskMetaAdmin)
                
            ### TaskSetMeta
            class TaskSetMetaAdmin(admin.ModelAdmin):
                list_display=tuple([f.name for f in TaskSetMeta._meta.fields])
            admin.site.register(TaskSetMeta,TaskSetMetaAdmin)
        
                
        except Exception,e:
            print e
            pass
