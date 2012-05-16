=================
Entity Framework
=================


インストール
============

- "ツール">"Library Package Manager" > "Package Manager Console" でPackage Manager Console を開く
- プロンプトにコマンドを投入してインストール。

::

    PM> Install-Package EntityFramework


    'EntityFramework 4.3.1' already installed.
    Successfully added 'EntityFramework 4.3.1' to AdConnectUnit.


- プロジェクトにパッケージが追加されます(package.config)。


.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <packages>
      <package id="EntityFramework" version="4.3.1" />
    </packages>


- データベースにアクセスするための設定ファイルが追加されます(App.config/Web.config )

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <configuration>
      <configSections>
        <!-- For more information on Entity Framework configuration, visit http://go.microsoft.com/fwlink/?LinkID=237468 -->
        <section name="entityFramework" 
            type="System.Data.Entity.Internal.ConfigFile.EntityFrameworkSection, EntityFramework, Version=4.3.1.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
      </configSections>
      <entityFramework>
        <defaultConnectionFactory type="System.Data.Entity.Infrastructure.SqlConnectionFactory, EntityFramework">
          <parameters>
            <parameter value="Data Source=.\SQLEXPRESS; Integrated Security=True; MultipleActiveResultSets=True" />
          </parameters>
        </defaultConnectionFactory>
      </entityFramework>
    </configuration>
    

How To
===================

- `Entity Framework を Visual Studio C# Expressに入れてみる <http://note.harajuku-tech.org/entityframework-visual-studio-c-express>`_
- `My first "LINQ to Entities" <http://note.harajuku-tech.org/linq-to-entities-my-first-linq-to-entities>`_
- `abstratクラスの定義は継承できます <http://note.harajuku-tech.org/aspnet-mvc-entity-framework-abstrat>`_ 
- `NUnitからもテスト可能 <http://note.harajuku-tech.org/nunit-entity-framework-431-code-first-model>`_
- `コンテキスト1 <http://note.harajuku-tech.org/aspnet-mvc-1>`_
- `コンテキスト2 <http://note.harajuku-tech.org/aspnet-mvc-2-db>`_

その他
======

- `単純なテスト <http://note.harajuku-tech.org/nunit>`_
- `aspnet_regiis.exe -i 実行すること <http://note.harajuku-tech.org/aspnet-40-aspnetregiisexe-i>`_ 
- `ASP.NET 4.0 を有効にする  <http://note.harajuku-tech.org/iis70-aspnet-20-40>`_
- `JSONを返す <http://note.harajuku-tech.org/aspnet-mvc-json>`_
- `Control/View <http://note.harajuku-tech.org/aspnet-controller-and-view>`_
- `DirectoryサービスでActive Directoryにアクセス <http://note.harajuku-tech.org/systemdirectoryservices>`_


