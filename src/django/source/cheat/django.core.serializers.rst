.. _cheat.django.core.serializers:

Cheat
-------------------------------

.. _cheat.django.core.serializers.deserialize:

JSONからモデルを復元するには？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:py:func:`django.core.serializers.deserialize`  を使います。

.. code-bock:: Python

    def models_from_json(filename):
        ''' JSONからモデルを復元する
        '''
        from django.core import serializers
        for obj in serializers.deserialize('json',open(filename).read()):
            try:
                obj.save()
            except Exception,e:   
                print e

Unicode エスケープシーケンスじゃなくて可読できるようにするには、ensure_ascii=Falseにします。
indent指定するといいでしょう。

::

    serializers.serialize("json",[self], ensure_ascii=False,indent=indent)


