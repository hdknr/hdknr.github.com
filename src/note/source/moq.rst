======
Moq
======

.. contents:: Moq


ASP.NET MVCコントローラのモック
==========================================

コントローラ例
------------------------

URLからサーバーのホストのDNS名を取り出してJSONで返答するコントローラ

.. code-block:: csharp

    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Web;
    using System.Web.Mvc;
    using System.Web.Routing;
    using System.Web.Security;
    
    using RestSharp;
    
    namespace Connect.Controllers
    {
        public class DiscoveryController : Controller
        {
            Connect.Models.ConnectContext ctx = new Models.ConnectContext();
    
            public ActionResult OpenIDConfiguration()
            {
                //IMPLEMENT
                string iss_id = Request.Url.Authority;
                Connect.Models.Issuer iss = ctx.GetIssuerByIdentifier(iss_id);
    
                return Json(new Dictionary<string, string>() { { "issuer", iss_id } },
                    JsonRequestBehavior.AllowGet);
            }
    
        }
    }

コントローラモック
----------------------------

.. code-block:: csharp

    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Text;
    
    using Moq;
    
    using System.Web;
    using System.Web.Mvc;
    using System.Web.Routing;
    
    namespace AdConnectTest
    {
        public class Request
        {
    
            public void ControlerTest()
            {
                // テストするコントローラ
    
                var controler =  new Connect.Controllers.DiscoveryController() ;
    
                // ControllerContextのモックオブジェクト
                Mock<ControllerContext> controllerContextMock = new Mock<ControllerContext>();
                
                // Request.User.IsInRole に対するスタブ(OpenIDConfigurationコントローラでは使っていません)
                controllerContextMock.Setup(
                    x => x.HttpContext.User.IsInRole( It.Is<string>(s => s.Equals("admin")) ) 
                    ).Returns(true);
    
                // Request.Url に対するスタブ 
                controllerContextMock.Setup(
                    x => x.HttpContext.Request.Url
                       
                    ).Returns(
                        new Uri("http://hoge.com/" )
                    );
    
                // コントローラにコンテキストを割当
                controler.ControllerContext = controllerContextMock.Object;
    
                // コントローラの実行
                ActionResult config = controler.OpenIDConfiguration();
    
                var jconfig = (JsonResult)config;                   // JsonResultを返すコントローラ
                var dict = (Dictionary<string,string>)jconfig.Data; // データはDictionary<string,string>
    
                Console.WriteLine(dict["issuer"]);      // issuerを表示してみる
            }
        }
    }

RestSharp リクエスターのモック
========================================


RestClientを使ったリクエスタ
------------------------------

.. code-block:: csharp 

    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Text;
    
    using RestSharp;
    
    namespace Connect
    {
        public class Requester
        {
            protected string _url;
            protected IRestClient _client;
    
            public Requester(string url, IRestClient client = null)
            {
                this._url = url;
                this._client = client;
            }
            public static IRestResponse Call(string url,IRestClient client = null)
            {
                if (client == null)
                {
                    client = new RestClient(url);
                }
                else
                {
                    client.BaseUrl = url;
                }
                var request = new RestRequest(new Uri(url), Method.GET);
                var response = client.Execute(request);
    
                return response;
            }
            public IRestResponse Request()
            {
                return Requester.Call( this._url, this._client);
            }
        }
    }
    

リクエスタを使ってHTMLをダウンロードしDOMで返す
--------------------------------------------------------

.. code-block::  csharp

    using RestSharp;
    using HtmlAgilityPack;  // for HtmlDocument object
    
    using System.Web;
    using System.Web.Mvc;
    using System.Web.Routing;

    public class RequestSample
    {

        HtmlDocument GetDocument( string url, IRestClient client=null)
        {

            var response = Connect.Requester.Call(url, client);
            HtmlDocument doc = new HtmlDocument();
            doc.LoadHtml(response.Content);

            return doc;
        }
    }

RestClientモック
--------------------------------

.. code-block:: csharp

        public void Reg()
        {
            // IRestClient(RestClientの親クラス ) のモック
            var mock = new Mock<IRestClient>();

            //任意のIRestRequestに対し、テストHTMLを返すスタブ 
            mock.Setup(
                        x => x.Execute(It.IsAny<IRestRequest>()))
                    .Returns(
                        // RestRespo
                        new RestResponse {
                            StatusCode = System.Net.HttpStatusCode.OK,
                            Content = "<html><body><h1>hello</h1></body></html>"
                            }
                    );

            string url = "http://www.asahi.com/";

            // テスト
            HtmlDocument doc = GetDocument(url, mock.Object);

            // 結果の表示
            Console.WriteLine(
                    doc.DocumentNode.SelectSingleNode("/descendant-or-self::h1").InnerText
            );
            
        }
