========================
エラー処理
========================

.. contents::
    :local:

display_errors
==================

php.ini
--------------------

- デフォルトは Off

    ::
    
        display_errors = Off

ini_set
-----------

- コードで有効化

    .. code-block:: php

        ini_set('display_errors',1);

    
- ただし、このコード中のシンタックスエラーは表示しない。
- 表示させるには、シンタックスエラーが起きないコードで ini_set して、実際のコードを require_once する


    .. code-block:: php

        <?PHP
        ini_set('display_errors',1);
        require_once( __DIR__ . "/main.php" );

log_errors
============

php.ini
--------

    ::

        log_errors = On

syslogに出力
----------------

- userファイシリティ、 httpdタグ

    ::

        error_log = syslog

    
    Debian::

        hdknr@wzy:~$ sudo tail -f /var/log/messages

        Dec 28 13:41:39 wzy apache2: PHP Parse error:  syntax error, unexpected '$url_clean' (T_VARIABLE) in /home/hdknr/php/code/connect/tests/url_check.php on line 6
