=============
UnitTest
=============

.. contents::
    :local:

テストの実行
==============

プラウザ起動
------------------------

- http://host/path/app/webroot/test.php にアクセスし、目的のテストを選択すればいいです。

モデルのテスト
==============

Userモデル
----------------

- app/Model/User.php を作成します 

.. literalinclude:: php/unittest_model_user.php
    :language: php

Userモデルのスト
------------------------------

- app/Test/Case/Model/UserTest.php を作成します   

.. literalinclude:: php/unittest_test_user.php
    :language: php





