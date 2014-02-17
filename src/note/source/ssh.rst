============
ssh/sshd
============


- 特定のコマンドだけの実行を許す
    - http://harajuku-tech.posterous.com/openssh-bnote
    - これにより対話ログインができなくなる

許可判定コマンド
====================

rsyncだけ許す設定
--------------------------------

rsyncの確認 ~/.ssh/authorized_keys ::

    command="/root/bin/check-rsync.sh"  ssh-rsa AAAAB3NzaC1yc2EAAAABIwAA......

チェックコマンド ::

    #!/bin/sh
    
    case "$SSH_ORIGINAL_COMMAND" in
    *\&*)
    echo "Rejected"
    ;;
    *\;*)
    echo "Rejected"
    ;;
    rsync\ --server*)
    $SSH_ORIGINAL_COMMAND
    ;;
    *)
    echo "Rejected"
    ;;
    esac
    
その他
=========

RSAキー作成
------------------

::

    $ ssh-keygen -t rsa -b 2048

ファイル名指定 

.. code-block:: bash

    $ ssh-keygen -t rsa -b 2048 -f mykey

WindowsのPuttyでつかうには？
----------------------------

- puttygenで"Load"で拡張子を問わずにExplorerからロード
- PPKに保存する


