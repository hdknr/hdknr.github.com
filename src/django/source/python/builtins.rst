Python: __builtin__
-----------------------------------

__builtins__
^^^^^^^^^^^^^^^^^^^^

::

    (docs)hdknr@sqg:~/ve/docs/src/hdknr.github.com/src/django/app$ python manage.py shell
    Python 2.6.6 (r266:84292, Dec 26 2010, 22:31:48) 
    [GCC 4.4.5] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> dir()
    ['__builtins__']

辞書です

::

    >>> type(__builtins__)
    <type 'dict'>


__builtins__ の builtin functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> sorted([ k for k,v in __builtins__.items() if callable(v) and str(v).find('function')>0 ])
    ['__import__', 
    'abs', 'all', 'any', 'apply', 'bin', 'callable', 'chr', 'cmp', 
    'coerce', 'compile', 'delattr', 'dir', 'divmod', 'eval', 'execfile', 
    'filter', 'format', 'getattr', 'globals', 'hasattr', 'hash', 'hex', 
    'id', 'input', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 
    'locals', 'map', 'max', 'min', 'next', 'oct', 'open', 'ord', 'pow', 
    'print', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'round',
    'setattr', 'sorted', 'sum', 'unichr', 'vars', 'zip']
    

collection 操作
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

sorted
~~~~~~~~~~~~~~~~~~

map と reduce
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> map( lambda x: x + 1, [ 1,2,3])
    [2, 3, 4]

.. code-block:: python

    >> reduce( lambda x,y: x + y , [1,2,3])
    6
    >>> reduce( lambda x,y: x + y , [1,2,3],100)
    106

all と any
~~~~~~~~~~~~~~

.. code-block:: python

    >>> all( map( lambda x: x.isdigit(), ['aaa','bbb','123'] ))
    False
    
    >>> any( map( lambda x: x.isdigit(), ['aaa','bbb','123'] ))
    True

zip
~~~~~~

.. code-block:: python

    >>> zip( (1,2), ('a','b') )
    [(1, 'a'), (2, 'b')]

    >>> zip( (1,2,3), ('a','b','c') )
    [(1, 'a'), (2, 'b'), (3, 'c')]


filter
~~~~~~~~~~~~

iter
~~~~~~~~~~~~

list ,dict , tuple
~~~~~~~~~~~~~~~~~~~~~~~~



slice
~~~~~~~~~~~~~~~~~~

sum
~~~~~~~~~~~~~~~~~~
