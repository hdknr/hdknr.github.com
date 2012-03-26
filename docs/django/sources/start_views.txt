===========
Start Views
===========

.. contents:: Start Views

テンプレート無しのシンプルビュー
========================================

- :py:class:`django.template.Template`
- :py:class:`django.template.RequestContext`
- :py:class:`django.http.HttpResponse`

.. code-block:: python

    def default(request):
        from django import template
        from django.http import HttpResponse
        id=4
        return HttpResponse(
            template.Template("""
            <html><head><title>Sample</title></head> <body> <h1> hello </h1>
            <a href="{% url myapp_task task_id=id %}"
            """
            ).render( template.RequestContext(request,{'id':id}) )
        )   


Class Based Generic View
===============================

- :py:mod:`django.views.generic.base`
- :py:mod:`django.views.generic.edit`
- :py:mod:`django.views.generic.list`


エラーページ
================

エラーテンプレート
------------------------------

- TEMPLATE_DIRS のルートにエラーページを置く
    
    - 500.html
    - 400.html
    - 403.html

- `contrib/admin/templates/admin/ <https://code.djangoproject.com/browser/django/trunk/django/contrib/admin/templates/admin/>`_

デフォルトのエラー処理
----------------------------

- 400   :py:func:`django.views.defaults.page_not_found`
- 500   :py:func:`django.views.defaults.server_error`

- urls.py で定義するとデフォルトをオーバーライドできます。 ( :py:mod:`django.conf.urls.defaults` )
 
.. automodule:: django.conf.urls.defaults
    :members:
 
