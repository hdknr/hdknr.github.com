========
AWS
========


すでにAMIがあるときの起動手順
========================================

1. AMI を登録

2  EBSのリージョンを確認

3. 登録したAMIでインスタンスをリージョンに起動
    
4. Elastic IPの割当

5. EBSのマウント

    例えば、 /dev/sdb1 

5. ssh

::
    
    $ ssh -i you_private_key  root@your_instance.com

6. マウント

::
    
    # mkdir /home
    # mount -t ext3 /dev/sdb1 /home

