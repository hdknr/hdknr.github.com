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
    
