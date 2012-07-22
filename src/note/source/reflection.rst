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

メソッド名を名前を指定して実行
===============================

this.alg にアルゴリズムを決める変数が入っているので、そのアルゴリズムに応じて署名を作成。

.. code-block:: csharp

        public string Tokenize(byte[] data)
        {
            string src = do_somehting(data );

            return ToBase64Url( this.Sign(src ) );
        }

        public byte[] Sign(string src)
        {
            return (byte[])this.GetType()
                    .GetMethod(string.Format("Sign_{0}", this.alg))
                    .Invoke(this, new object[] { secured_input });
        }
        public byte[] Sign_HS256(string src)
        {
            byte[] sig = null;
            // 実際の処理
            return sig;
        }
        public byte[] Sign_HS386(string src)
        {
            byte[] sig = null;
            // 実際の処理
            return sig;
        }
        public byte[] Sign_HS512(string src)
        {
            byte[] sig = null;
            // 実際の処理
            return sig;
        }

        
