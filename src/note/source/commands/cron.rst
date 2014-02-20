=======
cron
=======

.. contents::
    :local:

crontab
=========

- 一覧

    .. code-block:: bash

        $ crontab -l
        $ sudo crontab -l -u user1

- 編集
    .. code-block:: bash

        $ crontab -e


crontab ファイル
------------------

書式
^^^^^^^

.. code-block:: bash


     分　時　日　月　曜日　ユーザ　コマンド

.. list-table:: 意味
    
    *   - 分  
        - 0～59

    *   -  時  
        - 0～23

    *   - 日  
        - 1～31

    *   - 月  
        - 1～12　or jan～dec

    *   - 曜日    

        - 0～7 [0,7は日曜日] or sun～sat

    *   - アスタリスク
        - 任意

.. list-table:: 指定方法

    *   - リスト  
        - 0,15,30,45  
        - 分フィールドで指定した場合、15分に一度処理を実行します。

    *   - 範囲    
        - 1-5 
        - 曜日フィールドで指定した場合、月曜日～金曜日に処理を実行します。

    *   - 共存(リスト+範囲)
        - 1,3,7-9 
        - 時間フィールドで指定した場合、1時、3時、7時、8時、9時に処理を実行します。

    *   - 間隔値(スキップ)
        - 1-5/2   
        - 時間フィールドで指定した場合、1時、3時、5時に処理を実行します。

/etc/crontab
--------------

- crontab  ファイルを修正するたびに  cron を再起動する必要はない。
- cronデーモン は 1 分ごとにスプールディレクトリ(または /etc/crontab ファイル)の最終修正時刻(modtime)をチェック
- もし変更されていれば、  すべての  crontab ファイルの最終修正時刻をチェックし、  変更された  crontab  ファイルを読み直す。 
- crontab コマンドは、crontab ファイルが変更されたかどうかにかかわらず、 スプールディレクトリの最終修正時刻を更新します。

Debian
^^^^^^^^^^^^

- :ref:`anacron` つかっています

.. code-block:: bash

    # /etc/crontab: system-wide crontab
    # Unlike any other crontab you don't have to run the `crontab'
    # command to install the new version when you edit this file
    # and files in /etc/cron.d. These files also have username fields,
    # that none of the other crontabs do.
    
    SHELL=/bin/sh
    PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
    
    # m h dom mon dow user  command
    17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
    25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
    47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
    52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

CentOS
^^^^^^^^^^^

.. code-block:: bash

    SHELL=/bin/bash
    PATH=/sbin:/bin:/usr/sbin:/usr/bin
    MAILTO=root
    HOME=/
    
    # run-parts
    01 * * * * root run-parts /etc/cron.hourly
    02 4 * * * root run-parts /etc/cron.daily
    22 4 * * 0 root run-parts /etc/cron.weekly
    42 4 1 * * root run-parts /etc/cron.monthly


.. _anacron:

Anacron
=========

- http://linux.die.net/man/8/anacron
