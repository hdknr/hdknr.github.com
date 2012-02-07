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

