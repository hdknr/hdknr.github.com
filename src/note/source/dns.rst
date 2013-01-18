==================
Domain Names
==================

.. contents:: Domain Names
    :local:

SPF
====================

554
----

- Google Apps のGmailからFacebookグループに投稿した時のエラー

::

    Technical details of permanent failure:

    Google tried to deliver your message, 
    but it was rejected by the recipient domain. 

    We recommend contacting the other email provider 
    for further information about the cause of this error. 

    The error that the other server returned was: 554 554 5.7.1 POL-P7 

    Please visit http://postmaster.facebook.com/auth_error for more information (state 17).

- 以下で解決

::

    hdknr.com.      300 IN  TXT "v=spf1 a mx include:aspmx.googlemail.com ~all"

.. _dns.windows.bind:

Windows Bind
==============

Install
------------

- ISC からインストーラをダウンロード
- ".\named" ローカルユーザーでサービス起動します。（パスワードはインストール時に設定）
- \Windows\system32\dnsにインストールされます。

    - Vista64 は　C:\windows\SysWOW64\dns
    - Vistaの場合etcの権限に注意

        - named.pidを書き込みに行くので".\named"ユーザーに権限を付与

    - ファイルの編集をする人に権限を付与。

設定ファイル
---------------

- Linuxのbindと一緒。
