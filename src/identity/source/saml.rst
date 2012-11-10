========
SAML
========

.. contents::
    :local:

Webサービスセキュリティの主要４仕様

    - SAML
    - :doc:`xacml`
    - WS-Security
    - XKMS

Assertion
===========

- (サブジェクトの)認証 Assertion
- (サブジェクトの)属性 Assertion
- (サブジェクトが特定のリソースにアクセスできるかの)認可決定 Assertion

認証
-----

- ヘッダー
    
    - バージョン
    - 識別子
    - Issuer 
    - 発行日時

- 条件

    - 有効期間  
    - Audience条件

- ステートメント

    - 認証時刻
    - 認証手段(パスワード,Kerberos,X.509, ICカード....)
    - サブジェクト

- 署名

属性
-----

- ヘッダー
- 条件
- ステートメント

    - サブジェクト
    - 属性記述

- 署名

認可決定
---------

- ヘッダー
- 条件
- ステートメント

    - サブジェクト
    - アクセス認可 ( Permit, Deny, Intermidiate )
    - 行動指定 (Read, Write ... )
    - 裏付けるアサーション ( 参照 )

- 署名


Protocol
===============

Provisioning
=================

SPML - http://ja.wikipedia.org/wiki/SPML

Access Controll
================

:doc:`xacml`

Python
=======

- https://github.com/tachang/PySAML/blob/master/SAML.py


Terms
=========

.. glossary::

    SAMLオーソリティ
        認証や属性情報の提示を行うシステム

