========
Logging
========

logrotate
============

CentOS apach
------------------

::

    /path_to_log/logs/*log
    {
        daily
        rotate 60
        missingok
        notifempty
        sharedscripts
        compress
        delaycompress
        postrotate
            /sbin/service httpd reload > /dev/null 2>/dev/null || true
        endscript
    }
