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
