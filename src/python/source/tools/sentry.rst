============
sentry
============

.. contents::
    :local:

General
=========

- リアルタイムエラートラッカー
- https://github.com/getsentry/sentry 


インストール
===============

pip install sentry
------------------------

.. literalinclude:: sentry/sentry_pip.bash
    :language: bash

sentry init
-------------

.. literalinclude:: sentry/sentry_init.bash
    :language: bash

編集:

.. literalinclude:: sentry/sentry_conf.diff
    :language: diff

起動
=====

初回起動
--------

.. literalinclude:: sentry/sentry_start_first.bash
    :language: diff

ワーカープロセス
------------------------

.. literalinclude:: sentry/sentry_gunicorn_workers.bash
    :language: diff

データベーステーブル
------------------------------

.. literalinclude:: sentry/sentry_django_sqlite3.bash
    :language: diff

管理コマンド
------------------------------

.. literalinclude:: sentry/sentry_manage.bash
    :language: diff


使ってみる
==========

ログイン
----------

ログイン:

    .. image:: sentry/sentry_ui_login.png
        :scale: 50 %

チームのリスト:    

    .. image:: sentry/sentry_ui_list_team.png           
        :scale: 50 %
    
sentry自身のログ。最初は何もない。:

    .. image:: sentry/sentry_ui_list_internal.png       
        :scale: 50 %

Javaのイベントを起こしてみる
----------------------------------------

サンプル:

.. literalinclude:: sentry/sentry_create_sample_event_java.bash              

イベントが発生した:

    .. image :: sentry/sentry_create_sample_event_java.png
        :scale: 50 %

詳細:

    .. image:: sentry/sentry_create_sample_event_java_detail.png
        :scale: 50 %

元データ:

    .. image:: sentry/sentry_sample_event_java_original.png
        :scale: 50 %

イベントの操作
---------------

- 一覧からチェックすることで解決
- 詳細画面で「Mute」すると「抑制中」。Unmute すると戻る。
- 「未解決」「解決済」「抑制中」で一覧をフィルター


Djangoアプリから記録してみる
==============================

プロジェクト作成
----------------

.. literalinclude:: sentry/django_create_project.bash

設定ファイル
-------------

.. literalinclude:: sentry/django_settings.diff

raven test
-----------

.. literalinclude:: sentry/django_raven_test.bash


.. image:: sentry/djang_raven_test.png 
    :scale: 50 %

