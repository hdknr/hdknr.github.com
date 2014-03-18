A.3.4.  Initialization Vector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generate a random 128 bit JWE Initialization Vector.  

In this example, the value is:

::

   [3, 22, 60, 12, 43, 67, 104, 105, 108, 108, 105, 99, 111, 116, 104,
   101]

Encoding this JWE Initialization Vector as 
BASE64URL(JWE Initialization Vector) gives this value:

::

     AxY8DCtDaGlsbGljb3RoZQ

Python
~~~~~~~

.. code-block:: python

    >>> from jose.utils import base64
    >>> iv = [3, 22, 60, 12, 43, 67, 104, 105, 108, 108, 105, 99, 111, 116, 104,
    ...    101]
            >>> iv = ''.join(chr(i) for i in iv)
    >>> base64.base64url_encode(iv) == 'AxY8DCtDaGlsbGljb3RoZQ'
    True

(draft23)
