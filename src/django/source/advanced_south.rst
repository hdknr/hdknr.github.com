
- test ランナー動かす時には、 south をオフったほうがよい？

.. code-block:: python

    if 'test' not in sys.argv:
        INSTALLED_APPS +=('south',)  #: for Model Migration

