============================
Start Models
============================

QuerySet API
==============

フィールドのユニークリストの出力
---------------------------------------------

- :py:meth:`django.db.models.query.QuerySet.distinct`
- :py:meth:`django.db.models.query.QuerySet.values`

.. code-block:: python

    ServiceRoom.objects.values('subcode').distinct()

::

    [{'subcode': u''}, {'subcode': u'\uff21\u68df'}, ...(remaining elements truncated)...']

チート
======
- :ref:`cheat.django.db.models.list_models`
- :ref:`cheat.django.core.serializers.deserialize`
