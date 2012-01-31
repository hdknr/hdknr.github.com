=================
Cross Reference
=================

.. contents:: Cross Reference

クロスリファレンス
===================

書式 ::

    :ref:`タイトル<ターゲット>` 
    :role:`title <target>` 

リファレンスターゲット ::

    .. _ターゲット:


表(table)
=============

以下のように **.. table::** ディレクティブ を使った表に対してもクロスリファレンスを定義することができる。:

.. code-block:: rst 

    .. _xref.table.1:
    
    .. table:: Table 1: JSON Web Signature Reserved Algorithm Values 
    
     +------------------------------+-----------------------------------------------------------+
     | Alg Parameter Value          | Algorithm                                                 |   
     +==============================+===========================================================+
     | HS256                        | HMAC using SHA-256 hash algorithm                         |   
     +------------------------------+-----------------------------------------------------------+
     | ......                       | ....................................                      |   
     +------------------------------+-----------------------------------------------------------+

以下のようにクロスリファレンス書式を使って任意の文中にリンクを置く事で :ref:`表1 <xref.table.1>`  にジャンプできます。

.. code-block:: rst

   :ref:`表1 <xref.table.1>` 

表１:

.. _xref.table.1:

.. table:: Table 1: JSON Web Signature Reserved Algorithm Values 

 +------------------------------+-----------------------------------------------------------+
 | Alg Parameter Value          | Algorithm                                                 |   
 +==============================+===========================================================+
 | HS256                        | HMAC using SHA-256 hash algorithm                         |   
 +------------------------------+-----------------------------------------------------------+
 | HS384                        | HMAC using SHA-384 hash algorithm                         |   
 +------------------------------+-----------------------------------------------------------+
 | HS512                        | HMAC using SHA-512 hash algorithm                         |   
 +------------------------------+-----------------------------------------------------------+
 | RS256                        | RSA using SHA-256 hash algorithm                          |   
 +------------------------------+-----------------------------------------------------------+
 | RS384                        | RSA using SHA-384 hash algorithm                          |   
 +------------------------------+-----------------------------------------------------------+
 | RS512                        | RSA using SHA-512 hash algorithm                          |   
 +------------------------------+-----------------------------------------------------------+
 | ES256                        | ECDSA using P-256 curve and SHA-256 hash algorithm        |   
 +------------------------------+-----------------------------------------------------------+
 | ES384                        | ECDSA using P-384 curve and SHA-384 hash algorithm        |   
 +------------------------------+-----------------------------------------------------------+
 | ES512                        | ECDSA using P-521 curve and SHA-512 hash algorithm        |   
 +------------------------------+-----------------------------------------------------------+


用語(term/glossary)
====================

ソート
-------

**:sorted:** を入れるとソートされます。

.. code-block:: rst

    .. glossary::
       :sorted:

複数定義
--------

.. code-block:: rst

    Access Token
    Access Tokens
        アクセストークン

で、 :term:`Access Token` と :term:`Access Tokens` の複数のtermに対して１つの定義を記述できます。

例
---

.. glossary::
    :sorted:

    Connect
        OpenID Connect プロトコル

    Access Token
    Access Tokens
        アクセストークン

Python シンボル
===============

 - :ref:`ドメイン <sphinx:domains>`  参照。

クラス (:py:class:)
--------------------

.. code-block:: rst

    :py:class:`django.conf.BaseSettings` 

と記述すると、 :py:class:`django.conf.BaseSettings` に飛ぶ事ができます。


:py:func:`django.core.serializers.serialize` 

:py:mod:`django.core.serializers`

