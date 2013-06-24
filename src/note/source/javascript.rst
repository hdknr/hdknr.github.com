===========
javascript
===========


.. contents:: 
    :local:


map関数
=========

..  code-block:: javascript

    > [undefined,null,'hello'].map(function(i){ return typeof(i)})
    [ 'undefined', 'object', 'string' ]

.. _javascript.node.js:

正規表現
==========

- 他言語の互換性が欲しいならば、 XRegExp ( https://github.com/slevithan/xregexp )

node.js
=========

CLI
====

    - :ref:`javascript.node.js`
    - Rhino (Java)
    - SpiderMonkey (C)
    - PhantomJS : https://github.com/ariya/phantomjs

Tests
=========

- http://www.slideshare.net/KojiNakamura/jstdd

.. glossary::

    QUnit
        - http://qunitjs.com/
        - シンプル
        - jQuery開発で使われている
        - :ref:`javascript.node.js` で動かしたり出来る

    Jasmine
        - http://pivotal.github.com/jasmine/
        - Rails
        - Jasmine-node で :ref:`javascript.node.js` で動かせる

    Mocha
        - http://visionmedia.github.com/mocha/
        - CLI

    Vows
        - https://github.com/cloudhead/vows
        - CLI

テストランナー
------------------

    - Selenium
    - JsTestDriver
    - BusterJS ( http://docs.busterjs.org/en/latest/ )
    - Testacular


Javascript Beautifier
=====================

- http://note.harajuku-tech.org/js-beautify-python



JavaScript : The Good Parts
==============================     

Good Parts
------------------

- Good Parts    : 良いパーツ
- Bad  Parts    : 悪いパーツ
- Awful Parts   : ひどいパーツ

文法
-----

ホワイトスペース
^^^^^^^^^^^^^^^^^^^^

コメント
^^^^^^^^^^^

- ラインコメント(//)を使う事。ブロックコメントは使わないように。

    .. code-block:: javascript

        /*
            var a = /a*/.match(s);
        */   //** This block makes a syntax error

オブジェクト
-------------------------

関数
-------------------------

継承
-------------------------

配列
-------------------------

正規表現
-------------------------

メソッド
-------------------------

スタイル
-------------------------

美しい機能
-------------------------

Awfull Parts
-------------------------

Bad Parts
-------------------------

JSLint
------------

Syntax Diagram
------------------------------------

JSON
------------------------------------
