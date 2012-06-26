==============================
Json.Net 
==============================

.. contents:: Json.Net

Resource
============

- `Documentation <http://james.newtonking.com/projects/json/help/>`_

Serialization
================

属性
-----

- http://james.newtonking.com/projects/json/help/SerializationAttributes.html

JsonIgnoreAttribute:シリアライズしません
------------------------------------------

以下の抽象クラスを継承したPOCOは role フィールドがシリアライズされません。

.. code-block:: csharp

    abstract public class Role
    {
        public Role()
        {
            this.role = Roles.Op;
        }
        [JsonIgnore]
        public RoleType role { get; set; }
    }

Deserialization
===================

動的タイプ
------------

コンパイル時にリストアするオブジェクトの型がわからない場合。

JsonConvert.DeserializeObject<T>(string jsonstr) のメソッド情報を取得する
(必要に応じて引数の異なる別のオーバーライドを検索すること)

.. code-block:: csharp

    using System.Reflection;
    using Newtonsoft.Json;

    publc static MethodInfo GetJsonConvertDeserializeObject()
    {
        // Find JsonConvert.DeserializeObject<>(sting jsonstr ) 
        // method information

        var mi = typeof(JsonConvert).GetMethods().Where(m =>
            m.Name == "DeserializeObject" &&
            m.ContainsGenericParameters &&
            m.GetParameters().Length == 1
        ).ToArray<MethodInfo>();

        return mi[0];       // TODO: Exception Hadling
    }

モデルタイプを指定してJSON文字列から復元

.. code-block:: csharp

    public List<object> Deserialize(string jsonstr, string typestr )
    {
        Type model_type = GetModelTypeFromString(typestr);          // TODO : Implement later
        
        Type dtype = typeof(List<>).MakeGenericType(model_type);    // List<モデルクラス> を取得

        return (List<object>)_jsonconvert_deserializeobject
                .MakeGenericMethod(new Type[]{dtype})
                .Invoke(null,new object[]{s}); 
    }


MVCコントローラの応答を Json.Netで返す
==========================================

レスポンスクラス
--------------------------------

.. code-block:: csharp

    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Text;
    
    using Newtonsoft.Json;
    
    using System.Web;
    using System.Web.Mvc;
    using System.Web.Routing;
    
    namespace Connect
    {
        public class JsonDotNetResult : ActionResult
        {
            private object _obj { get; set; }
            public JsonDotNetResult(object obj)
            {
                _obj = obj;
            }
    
            public override void ExecuteResult(ControllerContext context)
            {
                context.HttpContext.Response.AddHeader("content-type", "application/json");
                context.HttpContext.Response.Write(JsonConvert.SerializeObject(_obj));
            }
        }
    
    }

コントローラで返答
------------------------

.. code-block:: csharp

    public ActionResult ServerConfigration()
    {
        return new Connect.JsonDotNetResult(
                new Dictionary<string,string>(){ {"issuer","hogehoge"}} );
    }


リクエスト内容
--------------------

リクエスト::

    Request URL:http://localhost:55547/Debug/ServerConfiguration
    Request Method:GET
    Status Code:200 OK

Request Headersview source:: 

    Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Charset:Shift_JIS,utf-8;q=0.7,*;q=0.3
    Accept-Encoding:gzip,deflate,sdch
    Accept-Language:ja,en-US;q=0.8,en;q=0.6
    Cache-Control:max-age=0
    Connection:keep-alive
    Host:localhost:55547
    User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5

Response Headersview source::

    Cache-Control:private
    Connection:Close
    Content-Length:21
    Content-Type:application/json; charset=utf-8
    Date:Mon, 18 Jun 2012 05:08:17 GMT
    Server:ASP.NET Development Server/10.0.0.0
    X-AspNet-Version:4.0.30319
    X-AspNetMvc-Version:3.0

応答::

    {"issuer":"hogehoge"}

