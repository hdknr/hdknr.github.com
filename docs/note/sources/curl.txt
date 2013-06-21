=====
curl
=====

.. contents::
    :local:

ファイルに保存
===================

curl -O
---------

curl -O $URL で wget の用にファイルをダウンロード

curl -o filename
-----------------

curl -o $filename $URL でファイル名を指定してダウンロード

.. _curl.basicauth:

基本認証
=========

- 401 + WWW-Authenticate が帰る基本認証がかかったサイト

::

    $ curl -I http://test3.hdknr.net                                                                       

    HTTP/1.1 401 Authorization Required
    Date: Fri, 21 Jun 2013 08:08:28 GMT
    Server: Apache/2.2.22 (Debian)
    WWW-Authenticate: Basic realm="Input Your ID and Password."
    Vary: Accept-Encoding
    Content-Type: text/html; charset=iso-8859-1

- `--basic` と `--user ユーザー名:パスワード` オプションで　Authorization ヘッダーを送る 

::

    $ curl -I --basic --user webmaster:orenopassword http://test3.hdknr.net

    HTTP/1.1 200 OK
    Date: Fri, 21 Jun 2013 08:08:08 GMT
    Server: Apache/2.2.22 (Debian)
    X-Powered-By: PHP/5.4.4-14
    Set-Cookie: PHPSESSID=3h5hik58rjco6ce9nep2tsrac0; path=/
    Expires: Mon, 26 Jul 1997 05:00:00 GMT
    Cache-Control: no-store, no-cache, must-revalidate
    Pragma: no-cache
    Last-Modified: Fri, 21 Jun 2013 08:08:08 GMT
    Cache-Control: post-check=0, pre-check=0
    Vary: Accept-Encoding
    Content-Type: text/html; charset=EUC-JP
