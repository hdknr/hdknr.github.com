====================================
ASP.NET ViewEngine
====================================

.. contents:: ASP.NET View Engine


View Engineカスタマイズ
================================

View Engineクラスを用意
--------------------------------

Razor View Engineのカスタマイズ

.. code-block:: csharp

     using System.Web.Mvc;
     
     namespace AdConnect.Views
     {
         public class AppViewEngine : RazorViewEngine
         {
             public AppViewEngine()
             {
                // ビューのサーチパスのカスタマイズ

                 var viewLocations = new[] {  
                 "~/Views/Connect/{1}/{0}.cshtml",
     
                 "~/Views/{1}/{0}.cshtml",  
     
                 "~/Views/Shared/{0}.cshtml"
                 };
     
                 this.PartialViewLocationFormats = viewLocations;
                 this.ViewLocationFormats = viewLocations;
     
             }
         }
     }

global.asax.cs でビューの指定
-----------------------------------

.. code-block:: csharp

    protected void Application_Start()
    {
        AreaRegistration.RegisterAllAreas();

        RegisterGlobalFilters(GlobalFilters.Filters);
        RegisterRoutes(RouteTable.Routes);

        //ViewEngine
        ViewEngines.Engines.Clear();
        ViewEngines.Engines.Add(new AdConnect.Views.AppViewEngine());
    } 
     
