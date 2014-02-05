================
RabbitMQ
================

.. contents::
    :local:

インストール
==============

Debian(Wheezy)
---------------

apt-line:

.. literalinclude:: rabbitmq/wheezy_aptline.bash
    :language: bash 

パブリックキー:

.. literalinclude:: rabbitmq/wheezy_pubkey.bash
    :language: bash 

インストール:

.. literalinclude:: rabbitmq/wheezy_aptget.bash
    :language: bash 

管理ツール:

.. literalinclude:: rabbitmq/wheezy_tool.bash
    :language: bash 

TCPポート:

.. literalinclude:: rabbitmq/wheezy_tcp.bash
    :language: bash 

ブラウザでアクセス:

    .. image:: rabbitmq/tcp-15672.png
        :scale: 50 %

管理
======

仮想ホスト
------------

一覧:

.. literalinclude:: rabbitmq/list_vhosts.bash
    :language: bash 

追加

.. literalinclude:: rabbitmq/add_vhosts.bash
    :language: bash 

ユーザー
--------

追加 :

.. literalinclude:: rabbitmq/add_users.bash
    :language: bash 

一覧:

.. literalinclude:: rabbitmq/list_users.bash
    :language: bash 

タグ追加 :

.. literalinclude:: rabbitmq/set_user_tags.bash
    :language: bash 


パーミッション
---------------

追加:

.. literalinclude:: rabbitmq/set_permissions.bash
    :language: bash 


一覧:

.. literalinclude:: rabbitmq/list_permissions.bash
    :language: bash 


ユーザーのパーミッション:

.. literalinclude:: rabbitmq/list_user_permissions.bash
    :language: bash 


