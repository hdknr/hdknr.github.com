========
Postfix
========

.. contents::
    :local:


エイリアス
=============

/etc/aliases
----------------

::

    root: hdknr


設定
=====

.. _postfix.myhostname:

myhostname
-------------

- 自分自身のホスト名です
- 設定されない場合は、ローカルマシン名が使われます
- ロカールマシン名に、ドメイン名が無い場合 .localdomain が補完されます

::

    # hostname --fqdn
    wzy

::

    # postconf | grep ^myhostname
    myhostname = wzy.localdomain
    
.. _postfix.mydomain:

mydomain
----------------

- :ref:`postfix.myhostname` のドメイン名が使われます。

::
    # hostname
    wzy.local.jp

    # hostname --fqdn
    wzy

    # postconf 
    mydomain = local.jp
    myhostname = wzy.local.jp

- ただしいドメイン名でない場合は、 .localdomain となります

::

    # hostname
    wzy.local

    # hostname --fqdn
    wzy

    # postconf 
    mydomain = localdomain
    myhostname = wzy.local


.. _postfix.myorigin:

myorigin
------------

- メールを送信する時にドメイン名として付けます
- 設定されない場合は :ref:`postfix.myhostname` が使われます 


.. _postfix.mydestination:

mydestination
------------------

- メールを他のサーバに転送せずに、ローカルで受信するドメイン名です。
- デフォルトは以下のようになっています
    
    ::

        # postconf -n | grep mydestination 
        # postconf | grep mydestination 

        mydestination = $myhostname, localhost.$mydomain, localhost 

メッセージキュー
================

キューの一覧
------------------

.. code-block:: bash

    $ sudo mailq
    
    
メッセージを読む
------------------

.. code-block:: bash

    $ sudo postcat -q D806CA1937


メッセージ削除
------------------------

.. code-block:: bash

    $ sudo postsuper -d D806CA1937

    postsuper: D806CA1937: removed
    postsuper: Deleted: 1 message

全て削除:


.. code-block:: bash

    $ sudo postsuper -d ALL

    postsuper: Deleted: 9 messages
