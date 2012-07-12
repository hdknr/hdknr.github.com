==================
Unix User
==================

.. contents:: Unix User

groupadd & useradd
====================

::

    $ sudo groupadd -g 2000 paloma 
    $ sudo useradd -g paloma -d /home/paloma -u 2000 -m paloma

ユーザーの存在確認
--------------------


.. code-block:: sh

    #!/bin/sh

    id $USER > /dev/null 2>&1 || exit 0
    # 存在しなかったらこれ以降は実行されません
