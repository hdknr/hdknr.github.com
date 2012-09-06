==========
requests
==========

.. automodule:: app.boa.tests.requests_tests
    :members:   

- py:class:`app.boa.tests.requests_test.RequestsTest`


Cheat
=======

JSON
-----

.. code-block::

    import reuqests
    j = request.get('http://test.com/data').json

オレオレ証明書サイト
------------------------

.. code-block::

    import reuqests
    res = request.get('https://trac.hdknr.com/',verify=False)

