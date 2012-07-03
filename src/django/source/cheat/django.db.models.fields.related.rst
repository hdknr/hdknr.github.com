ForeignKey
---------------

ManyToManyField
----------------

Cheat
------

参照フィールドのカスケード削除をできないようにするには?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- http://harajuku-tech.posterous.com/django-foreignkeyondelete

.. code-block:: python

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)

