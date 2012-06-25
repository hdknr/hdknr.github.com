==================
.NET Reflection 
==================

ジェネリクス型の判定
=======================

あるクラスのDbSet<>型のプロパティ一覧を取得

.. code-block:: csharp

    using System.Reflection;
    using System.Data.Entity;
    using System.Data.Objects;
    using System.Data.Metadata.Edm;
    using System.Data.Entity.Infrastructure;

    Type type  = typeof(MyClass);                                     // 調べたいクラス
    Type dbset = typeof(DbSet<>);                                     // DbSet<>のプロパティだけ欲しい

    foreach (var prop in (
         from p in type.GetProperties()                               // チェックするクラスのプロパティ一覧
         where
            p.PropertyType.IsGenericType &&                           // ジェネリック型？
            dbset.Equals(p.PropertyType.GetGenericTypeDefinition())   // 目的のジェネリック型？
         select p).ToList())
    {
        Console.WriteLine(prop.Name);
    }
