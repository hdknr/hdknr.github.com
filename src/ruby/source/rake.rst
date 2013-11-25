=====
rake
=====

.. contents::
    :local:


rake db:setup
===============

- データベースの作成
- スキーマのロード
- :ref:`シードデータで初期化 <rake.db.seeds>`

db/schema.rb
--------------

.. _rake.db.seeds:

rake db:seed
===============

db/seeds.rb
--------------

::

    モデルクラス名.create(:カラム名1 => 値1, :カラム名2 => 値2, ...)

.. code-block:: ruby

    Scope.create [
      {name: 'openid' },
    ]
    
    Account.create [
      { login_id: 'test1', password: 'fsaf32bf!' },
    ]

複雑な処理をするには複雑なスクリプトかけば良い

.. code-block:: ruby

    class SeedImporter

        def initialize
            #...
        end

        def run
            #....
        end

    end

    SeedImporter.new.run

rake db:fixtures:load
========================

- フィクスチャの読み込み
- 既存データは削除されます


test/fixtures/
--------------------


