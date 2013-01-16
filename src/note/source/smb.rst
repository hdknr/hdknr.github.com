====
SMB
====

.. contents:: SMB
    :local:

Mac
====

mount_smbfs
-------------

.. code-block:: bash

    mount_smbfs //username@server/share ~/mnt/

misc
-----

- `Debianに入れてMac Finderから接続 <http://harajuku-tech.posterous.com/samba-on-debian>`_
- `シンボリックリンクが見えない <http://note.harajuku-tech.org/samba>`_


Windows
==========

- `Guest の Debianのファイルを HostのVistaからアクセス <http://hidelafoglia.livejournal.com/62814.html>`_
- `同様にWindowsから <http://harajuku-tech.posterous.com/samba-from-vista64-windows-live>`_

Debian
=======

インストール
--------------

.. code-block:: bash

    $ sudo aptitude install samba smbfs -y

TCPポート ::

    $ sudo lsof -c smb | grep TCP
    smbd    15036 root   28u  IPv6  97201      0t0    TCP *:microsoft-ds (LISTEN)
    smbd    15036 root   29u  IPv6  97203      0t0    TCP *:netbios-ssn (LISTEN)
    smbd    15036 root   30u  IPv4  97205      0t0    TCP *:microsoft-ds (LISTEN)
    smbd    15036 root   31u  IPv4  97207      0t0    TCP *:netbios-ssn (LISTEN)



/etc/samba/smb.conf の簡単な設定 ::

    [global]
       workgroup = WORKGROUP
       security = user
    [homes]
       read only = no


ユーザー追加
^^^^^^^^^^^^^^^^^^^^

Unixがユーザーがあっても必要です ::

    $ sudo smbpasswd -a hdknr

    New SMB password:
    Retype new SMB password:

ACL
^^^^^

- acl, attr のインストール ( aclはext2,ext3 .. , attr は  XFS )

.. code-block:: bash

    $ sudo aptitude install attr acl 


smbfsによるマウント
----------------------------

.. code-block:: bash

    $ sudo mkdir -p /mnt/smb/server
    $ sudo mount -t cifs -o username=admin,password=password,codepage=cp932,iocharset=utf8,defaults //server/server_data /mnt/smb/server

- deafult : rw, suid, dev, exec, auto, nouser, async オプションの全部入り
- codepage, iocharset : 上記の例だとマウント元がWindowsのSHIFT-JISで、Debian側がUTF-8

/etc/fstab で起動時マウント
--------------------------------

.. code-block:: bash

    //server/server_data /mnt/smb/server cifs username=admin,password=password,codepage=cp932,iocharset=utf8,defaults 0 0

.. _smb.smbclient:

smbclient
-------------

インストール::

    $  sudo aptitude install smbclient 

共有(share)の一覧
^^^^^^^^^^^^^^^^^^^^^^^^

wzyというコンピュータのシェア一覧::

    $ smbclient -L wzy

    Enter hdknr's password: 

    Domain=[WORKGROUP] OS=[Unix] Server=[Samba 3.6.6]
    
            Sharename       Type      Comment
            ---------       ----      -------
            print$          Disk      Printer Drivers
            IPC$            IPC       IPC Service (wzy server)
            hdknr           Disk      Home Directories

    Domain=[WORKGROUP] OS=[Unix] Server=[Samba 3.6.6]
    
            Server               Comment
            ---------            -------
            WZY                  wzy server
    
            Workgroup            Master
            ---------            -------
            WORKGROUP            WZY

Samba
======

コマンド
---------

- net - Tool for administration of Samba and remote CIFS servers.
- testparm  -  check an smb.conf configuration file for internal correctness

