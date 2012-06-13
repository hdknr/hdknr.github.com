=================
Entity Framework
=================


.. contents:: Entity Framework

インストール
============

- "ツール">"Library Package Manager" > "Package Manager Console" でPackage Manager Console を開く
- プロンプトにコマンドを投入して `パッケージ <http://nuget.org/packages/EntityFramework/4.3.1>`_ 
  パッケージのインストール。

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
    

マイグレーション
==================

マイグレーションの有効化
---------------------------

::

    PM> Enable-Migrations


無効にするには
^^^^^^^^^^^^^^^^^

- Migrationsフォルダーごと削除
- App.config からDB接続を削除
- 不要であれば、package.config からEntityFramework を削除
- 不要であれば、EntityFramework のアセンブリ参照を削除


マイグレーション追加
------------------------------

::

    PM> Add-Migration session-move-to-connect-lib

マイグレーション反映 
------------------------------

::

    PM> Update-Database

カスケード削除
-----------------

外部キーに ON DELETE CASCADE の制約を付けるには、 
`System.Data.Entity.Migrations.Builders.TableBuilder<TColumns>.ForeignKey() 
<http://msdn.microsoft.com/en-us/library/hh829659%28v=vs.103%29.aspx>`_ メソッドの
３番目の引数を true にする。


.. code-block:: csharp

   public partial class Start : DbMigration
    {   
        public override void Up()
        {   
            CreateTable(
                "Accesses",
                c => new 
                    {   
                        Id = c.Int(nullable: false),
                        access_token = c.String(),
                    })  
                .PrimaryKey(t => t.Id)
                .ForeignKey(
                    "Sessions",     // 参照先テーブル(principalTable)
                    t => t.Id,      // 依存キー表現
                    true            // cascaeDelete(default=false) 
                )   
                .Index(t => t.Id);
             
        }   
    }   



One-To-One Relation
======================

One-To-Oneリレーションでは １方が **プリンシパルエンド** (principal)、もう一方が **依存エンド** (dependent)となります。
プリンシパルエンドは最初にINSERTされるモデルで、依存エンドがなくても存在可能です。
依存エンドはプリンシパルがINSERTされてからINSERTされます。依存エンドはプリンシパルエンドの外部キーを持っているからです。

.. code-block:: csharp

    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Web;
    
    using System.Data.Entity;
    
    using System.ComponentModel.DataAnnotations;        
    // for KeyAttribute,ForeignKeyAttribte
        
    namespace AdConnect.Models
    {
    
        public class Husband
        {
            public int Id { get; set; }
            public Wife Wife { get; set; }
        }
    
        public class Wife
        {
            [Key,ForeignKey("Husband" )]
            public int Id { get; set; }
            public Husband Husband { get; set; }
        }

        public class ConnectContext : DbContext
        {
            public DbSet<Husband> Husbands { get; set; }
            public DbSet<Wife> Wives { get; set; }
        }
    }

プリンシパル

.. code-block:: mysql

    USE [AdConnect.Models.ConnectContext]
    GO
    
    SET ANSI_NULLS ON
    GO
    
    SET QUOTED_IDENTIFIER ON
    GO
    
    CREATE TABLE [dbo].[Husbands](
        [Id] [int] IDENTITY(1,1) NOT NULL,
     CONSTRAINT [PK_Husbands] PRIMARY KEY CLUSTERED 
    (
        [Id] ASC
    )WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, 
           IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
    ) ON [PRIMARY]
    
    GO

依存

.. code-block:: mysql

    USE [AdConnect.Models.ConnectContext]
    GO

    SET ANSI_NULLS ON
    GO
    
    SET QUOTED_IDENTIFIER ON
    GO
    
    CREATE TABLE [dbo].[Wives](
        [Id] [int] NOT NULL,
     CONSTRAINT [PK_Wives] PRIMARY KEY CLUSTERED 
    (
        [Id] ASC
    )WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, 
            IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
    ) ON [PRIMARY]
    
    GO
    
    ALTER TABLE [dbo].[Wives]  WITH CHECK ADD  CONSTRAINT [FK_Wives_Husbands_Id] FOREIGN KEY([Id])
    REFERENCES [dbo].[Husbands] ([Id])
    GO
    
    ALTER TABLE [dbo].[Wives] CHECK CONSTRAINT [FK_Wives_Husbands_Id]
    GO


Metadata
=========

メタデータ取得はめんどくさい気がする。
DbContextをObjetContextに変換して、MetadataWorkspaceにアクセスすることでメタデータの操作をする。
MetadataWorkspaceからモデルクラスの名前(Name)が等しいEntitySetをクエリするとそのテーブルのメタデータ
にアクセスできるっぽい。

.. code-block:: csharp

    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Web;
    
    // メターデータ系のネームスペース
    using System.Data.Entity;
    using System.Data.Objects;
    using System.Data.Metadata.Edm;
    using System.Data.Entity.Infrastructure;
    
    namespace AdConnectTest.Models
    {
        /// データベースコンテキストクラス
    
        public class ConnectContext : DbContext
        {
            // モデルクラス(POCO)
            public DbSet<Connect.Models.Grant> Grants { get; set; }
    
    
            // DbContextからObjectContextを取得
            public ObjectContext ObjectContext
            {
                get
                {
                    return ((IObjectContextAdapter)this).ObjectContext;
                }
            }
    
            // メタ情報
            public MetadataWorkspace Meta
            {
                get { return this.ObjectContext.MetadataWorkspace; }
            }
    
    
            // 指定したモデルクラスのメタ情報
            public EntitySet GetTableMeta(Type model)
            {
    
                return this.Meta.GetItemCollection(DataSpace.SSpace)
                        .GetItems<EntityContainer>()
                        .Single()
                        .BaseEntitySets
                        .OfType<EntitySet>()
                        .Where(s => s.Name == model.Name)
                        .ToArray()[0];
            }
        }
    }

これを実行するには、

.. code-block:: csharp

    // DbContextを生成し、データベース接続を用意する
    Models.ConnectContext ctx = new Models.ConnectContext();

    string grant_table_name = (string)ctx.GetTableMeta( 
                                        typeof(Connect.Models.Grant) // POCO モデルクラス
                                    ).MetadataProperties["Table"].Value;

実際のモデル名は::

    Grants

と複数形が返る。


コマンド
=========
    
- `Enable-Migrations`_ : Enables Code First Migrations をプロジェクトで有効にする
- `Add-Migration`_ : ペンディングのモデル修正のマイグレーションスクリプトをスキャフォールドする
- `Update-Database`_ : ペンディングされたマイグレーションをデータベースに適用
- `Get-Migrations`_ : データベースに適用されたマイグレーションを表示する。

Enable-Migrations
---------------------------

DbContextが決まっていない場合
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Migration対象のDbContextの派生クラスが別のDLLに入っているなど、Wizardが判定できない場合は
クラスがコメントされてMigrations/Configuation.cs が作成されるので、手動で埋める。

::

    PM> Enable-Migrations
    No classes deriving from DbContext found in the current project.
    Edit the generated Configuration class to specify the context to enable migrations for.
    Code First Migrations enabled for project AdConnect.

.. code-block:: csharp

    internal sealed class Configuration : DbMigrationsConfiguration</** TODO: put your Code First context type name here **/>
    {
        public Configuration()
        {
            AutomaticMigrationsEnabled = false;
        }

        protected override void Seed(/** TODO: put your Code First context type name here **/ context)
        {
            //.....
        }
    }

Add-Migration
------------------

::

    PM> Add-Migration Start
    Scaffolding migration 'Start'.
    The Designer Code for this migration file includes a snapshot of your current Code First model. This snapshot is used to calculate the changes to your model when you scaffold the next migration. If you make additional changes to your model that you want to include in this migration, then you can re-scaffold it by running 'Add-Migration 201206060712563_Start' again.


Update-Database
-------------------

::

    PM> Update-Database
    Specify the '-Verbose' flag to view the SQL statements being applied to the target database.
    Applying explicit migrations: [201206050458407_InitialCreate, 201206060520281_Initial].
    Applying explicit migration: 201206050458407_InitialCreate.
    Applying explicit migration: 201206060520281_Initial.

Get-Migrations
-----------------

::

    PM> Get-Migrations -Verbose
    Using NuGet project 'AdConnect'.
    Using StartUp project 'AdConnect'.
    Retrieving migrations that have been applied to the target database.
    Target database is: 'AdConnect.Models.ConnectContext' 
    (DataSource: .\SQLEXPRESS, Provider: System.Data.SqlClient, Origin: Convention).
    201206040429540_NonceTime
    201206030843292_First

ヘルプ::

    PM> get-help Get-Migrations -full.

データベース接続
========================

`DbContext <http://note.harajuku-tech.org/dbcontext-class-systemdataentity>`_ 
でデータベース接続が行われるルールは少しむずかしいです。

プログラムで明示的に指定
------------------------------

DbContextクラスのコンストラクタにデータベース名を指定すると 
app.config で指定したデータベースサーバーに指定した名前でデータベースを作るようです。

TestDatabase というデータベースを作るには以下のようにします 

.. code-block:: csharp

    public class ConnectContext : DbContext
    {
        public ConnectContext()
            : base("TestDatabase")
        {}
    }

.. todo::

    app.config からデータベース名を取得して設定するようにコードすればいいのかな？

接続文字列を追加/編集する方法
------------------------------------

接続文字列を設定すると app.config /web.config だけで制御可能です。
SQL Server(Express)だと "Initial Catalog" がデータベース名になります。
ポイントは **name** 属性に、DbContext クラスのクラス名を指定する、ということです。

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <configuration>
      <configSections>
        <section name="entityFramework" 
                type="System.Data.Entity.Internal.ConfigFile.EntityFrameworkSection, EntityFramework, Version=4.3.1.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
      </configSections>
    
      <!-- ここから追加 
            name : DbContextから派生したConnectContext
            Initial Catalog : SQL Server(Express) のデータベース名
      -->
      <connectionStrings>
       <add 
        name="ConnectContext" 
        connectionString="Server=.\SQLEXPRESS;Initial Catalog=ConnectDB;Integrated Security=true;MultipleActiveResultSets=True;"
        providerName="System.Data.SqlClient"
       />
      </connectionStrings>
      <!-- ここまで追加 -->
      
      <entityFramework>
        <defaultConnectionFactory 
            type="System.Data.Entity.Infrastructure.SqlConnectionFactory, EntityFramework">    
          <parameters>
            <parameter
               value="Data Source=.\SQLEXPRESS; Integrated Security=True; MultipleActiveResultSets=True;Initial Catalog=ConnectDB" />
          </parameters>
        </defaultConnectionFactory>
      </entityFramework>

    </configuration>

これで `Update-Database`_ コマンドを実行すると、(存在しなかったら)データベースを作成してMigrationコードを実行します。

Tools & Libraries
========================

- NuGet
- JSON.Net
- RestSharp ( https://github.com/restsharp/RestSharp.git )
- HtmlAgilePack
- Moq ( https://github.com/Moq )
- BouncyCastle

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

- http://www.asp.net/entity-framework
- ADO.NET Entity Framework (http://msdn.microsoft.com/en-us/library/bb399572.aspx)

CodePlex
----------

- Entity Framework Contrib (http://efcontrib.codeplex.com/)
- Tutorial: ADO.NET Entity Framework ( http://adoeftutorial.codeplex.com/ )
