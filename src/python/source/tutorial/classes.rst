========
クラス
========

.. contents::
    :local:


クラス
=======


クラス定義
------------


クラスオブジェクト(Class Objects)
---------------------------------------------------


インスタンスオブジェクト(Instance Objects)
---------------------------------------------------


データ属性(Data Attribute)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Smalltalk "インスタンス変数"
- C++ "データメンバー"

- "代入された時に作成される"

    .. code-block:: python


        >>> class A(object):
        ...    pass
        ... 


        >>> a=A()

        >>> [ f for f in dir(a) if not f.startswith('_')]
        []

        >>> a.name="Paul"
        >>> [ f for f in dir(a) if not f.startswith('_')]
        ['name']        


メソッド(Method) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





