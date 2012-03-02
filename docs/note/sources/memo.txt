======
メモ
======

iframe
----------------------------------------

iframeの親ページを移動させるには、parenet を使う

::

    <a onclick="window.parent.location.href='http://hdknr.com/#access_token=_your_token_'">移動</a>


ssh-keygen
----------------------------------------

- 出力ファイル指定 : -f オプション でパス指定。  .pub 付きで同じディレクトリに公開鍵が作成される。

::

    tact@sqg:~$ ssh-keygen -f hoge/mykey.rsa

    Generating public/private rsa key pair.
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in hoge/mykey.rsa.
    Your public key has been saved in hoge/mykey.rsa.pub.
    The key fingerprint is:
    f9:bb:38:26:8b:89:46:1f:ea:84:eb:bc:ee:9d:16:48 tact@sqg
    The key's randomart image is:
    +--[ RSA 2048]----+
    |                 |
    |                 |
    |                 |
    | E       .       |
    |. .     S        |
    | o...    .       |
    |...o..    .      |
    |.o+ooo. o. .     |
    |=O=oo .+..o.     |
    +-----------------+
    tact@sqg:~$ ls hoge/
    mykey.rsa  mykey.rsa.pub

