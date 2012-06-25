======================
Python
======================

.. contents:: Python

Install
=========

.. code-block:: bash

    Squeeze$ sudo aptitude install python-setuptools vim-python python-dev -y
    Squeeze$ echo PIL supporting library
    Squeeze$ sudo aptitude install libjpeg8 libjpeg8-dev  libfreetype6 libfreetype6-dev liblcms1-dev  python-liblcms python-tk  tcl8.5-dev tk8.5-dev -y


Encoding
==========

ソースコード
------------------

.. code-block:: python

    # -*- coding: utf-8 -*-


プロパティ
===============

setterを定義しないとread-only
---------------------------------

.. code-block:: python


    class Hoge(object):
        def __init__(self):
            self._name=''
        @property
        def fullname(self):
            return self._name
    
    
    h=Hoge()
    h._name='aaa'
    print h.fullname
    h.fullname= 'xxx'
    print h.fullname

    (main)hdknr@sqg:~$ python x.py 
    aaa
    Traceback (most recent call last):
      File "x.py", line 13, in <module>
        h.fullname= 'xxx'
    AttributeError: can't set attribute

ただし、object から派生させること！
    
.. code-block:: python


    class Hoge:
        def __init__(self):
            self._name=''
        @property
        def fullname(self):
            return self._name

    (main)hdknr@sqg:~$ python x.py 
    aaa
    xxx


配列の初期化
===============

.. code-block:: python

    >>> [1]*3
    [1, 1, 1]
    >>> [1,2]*3
    [1, 2, 1, 2, 1, 2]
    >>> [[1,2]]*3
    [[1, 2], [1, 2], [1, 2]]


カナ:半角->全角
==================

- jcconv

:: 
    
    $ pip install jcconv

.. code-block:: python

    >>> import jcconv
    >>> print jcconv.half2kata('ああああｳｴｽﾄｺｰﾄ1234')
    ああああウエストコｰト1234

パスワード
=============

.. code-block:: python

    import string,random

    seed="".join([ string.letters for i in range(2)]) + \
         string.printable[:-6].translate(string.maketrans("\\`'",'012'))
    print "".join([ random.choice( seed )  for i in range(12)])

- django-passwords : https://github.com/dstufft/django-passwords
- Debian : `apg <http://harajuku-tech.posterous.com/debian-apg-generates-several-random-passwords>`_

整数化
=======

- int(x)
- http://www.python.jp/doc/2.5/lib/typesnumeric.html

乱数
====

- random

.. code-block:: python

    import random
    print random.random()

- os.urandom

.. code-block:: python

    >>> import os
    >>> os.urandom(16)
    '\x83\xd9?1\xe5\x0c\xff\xc8\xa5\x870\xd6\xe4u\xfe\xef'
    >>> os.urandom(32)
    'ld\xc6\x88\x12\xddZ\xabs\x97\xb7N\x10J\xe0\xd9!\xd1\x10\xdf\x9b\x02R\xfexk\xeef\x1f\x0bdl'

