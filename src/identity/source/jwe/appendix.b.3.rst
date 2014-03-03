B.3. 64 Bit Big Endian Representation of AAD Length
------------------------------------------------------------

The Additional Authenticated Data (AAD) in this example is:

::

   [101, 121, 74, 104, 98, 71, 99, 105, 79, 105, 74, 66, 77, 84, 73, 52,
   83, 49, 99, 105, 76, 67, 74, 108, 98, 109, 77, 105, 79, 105, 74, 66,
   77, 84, 73, 52, 81, 48, 74, 68, 76, 85, 104, 84, 77, 106, 85, 50, 73,
   110, 48]

This AAD is 51 bytes long, which is 408 bits long.  The octet string
AL, which is the number of bits in AAD expressed as a big endian 64
bit unsigned integer is:

::

   [0, 0, 0, 0, 0, 0, 1, 152]

.. note::
    - AADのビット数です。オクテット数ではありません。

( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-21#appendix-B.3 )


Python
^^^^^^^^^

.. code-block:: python

    >>> aad_str = ''.join(chr(i) for i in aad)
    >>> aad_str
    'eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0'
    >>> base64.base64url_decode(aad_str)
    '{"alg":"A128KW","enc":"A128CBC-HS256"}

.. code-block:: python

    >>> to_al = lambda x: ( [0,] * 8 + [ord(i) for i in int_to_string(len(x)*8)])[-8:]
    >>> to_al(aad)
    [0, 0, 0, 0, 0, 0, 1, 152]

