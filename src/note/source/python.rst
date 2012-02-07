======================
Python
======================

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

