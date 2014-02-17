======================
Windows Note
======================

.. contents::
    :local:

AWS
=====

- DNSサーバーを変更する ( :doc:`active_directory` のドメインに接続するなら必須 )
- まず最初にサーバー名を帰る事(ここでリブートしない)
- 次にUIを日本語化する( リブート必要 )

    - `UI を日本語化する <https://www.evernote.com/shard/s302/sh/0d9b22fb-3618-4165-8240-5a43d6fb48e5/8b272279faf43643c18e7eb13e884e14>`_

- Chrome をインストールする

    - `IEのゾーンセキュリティアラートをChromeのインストールが終わる迄解除する <https://www.evernote.com/shard/s302/sh/fec9954f-f2e4-4330-a7cb-4137956b7713/285c720a8586a47cd6333ebc47e4d7af>`_


キーボード
=============

Macのキーボードで「かな」、「英数」をIMEの切り替えに使う
------------------------------------------------------------

- AutoHotKey( http://www.autohotkey.com ) から適当なバイナリをインストールする
- 設定ファイルを開いて追加する( `参考 <http://d.hatena.ne.jp/fuenor/20090610/1244639263>`_ )

    ::

        ;Mac keyboard
        #USEHOOK
        vkE9sc071 Up::Send,{vkF3sc029 Down}{VkF3sc029 Up}  ;Apple英数->半全
        vkFFsc072 Up::Send,{vkF3sc029 Down}{VkF3sc029 Up}  ;Appleかな->半全
        #USEHOOK off


その他
======

- :doc:`active_directory`
