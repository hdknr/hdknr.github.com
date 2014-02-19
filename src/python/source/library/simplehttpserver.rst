==========================================================
:mod:`SimpleHTTPServer` --- HTTP リクエストハンドラ
==========================================================

.. module:: SimpleHTTPServer
   :synopsis: このモジュールは HTTP サーバに基本的なリクエストハンドラを提供します。

.. note::

   - :mod:`SimpleHTTPServer` -> Python 3 :mod:`http.server` 

- :mod:`SimpleHTTPServer` は :class:`SimpleHTTPRequestHandler` クラス1つを提供
- :class:`BaseHTTPServer.BaseHTTPRequestHandler` に対して互換性があります
- :mod:`公式 <py:SimpleHTTPServer>`

クラス定義
==============

:mod:`SimpleHTTPServer` モジュールでは以下のクラスを定義しています:


.. class:: SimpleHTTPRequestHandler(request, client_address, server)

    - カレントディレクトリ以下でHTTPDを提供
    - 多くの作業は基底クラス :class:`BaseHTTPServer.BaseHTTPRequestHandler` で行われます。
    - このクラスは関数 :func:`do_GET` および :func:`do_HEAD`  を実装しています。


メンバー
============

   :class:`SimpleHTTPRequestHandler` では以下のメンバ変数を定義:


   .. attribute:: server_version

      この値は ``"SimpleHTTP/" + __version__`` になります。 ``__version__`` はこのモジュールで定義されている値です。


   .. attribute:: extensions_map

      拡張子を MIME 型指定子に対応付ける辞書です。標準の型指定は空文字列で表され、この値は ``application/octet-stream``
      と見なされます。対応付けは大小文字の区別をするので、小文字のキーのみを入れるべきです。

メソッド
============

   :class:`SimpleHTTPRequestHandler` では以下のメソッドを定義しています:


   .. method:: do_HEAD()

        -  ``'HEAD'`` を処理( ``GET`` リクエストの時に送信されるものと同じヘッダを送信 )
        - :meth:`do_GET`  メソッドを参照


   .. method:: do_GET()

        - カレントディレクトリをルートに相対的なパスとして解釈し、ファイルシステムと対応
        - パスがカレントディレクトリ('/')だと、 ``index.html`` か ``index.htm`` 返す
        - パス=ディレクトリであれば、 :meth:`list_directory` でファイル一覧を処理して返答
        
            - :func:`os.listdir` をディレクトリのスキャンに用いていて、これが失敗すると ``404`` 

        - パス=ファイルであれば内容を返す

            - :exc:`IOError` 例外が起きれば、 ``404`` 、 ``'File not found'``  
            - 正常の場合、 *extensions_map* 変数をでコンテントタイプを推測

        - ヘッダー

            - ``'Content-type:'``  (拡張子ベース)
            - ``'Content-Lenght;'`` (ファイルサイズ )
            - ``'Last-Modified:'`` (ファイルの更新日時)


関数
============

:func:`test` 関数
---------------------
    
- :class:`SimpleHTTPRequestHandler` をハンドラとして使うサーバを作る例

例
============

コード
----------------

.. code-block:: python

   import SimpleHTTPServer
   import SocketServer
 
   PORT = 8000
 
   Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
 
   httpd = SocketServer.TCPServer(("", PORT), Handler)
 
   print "serving at port", PORT
   httpd.serve_forever()

インタプリタ
----------------

- ``-m`` スイッチ :  :mod:`SimpleHTTPServer` モジュール
- 引数 ``ポート番号``

.. code-block:: bash

     $ python -m SimpleHTTPServer 8000

その他
===========

.. seealso::

   Module :mod:`BaseHTTPServer`
      Web サーバおよび要求ハンドラの基底クラス実装。

