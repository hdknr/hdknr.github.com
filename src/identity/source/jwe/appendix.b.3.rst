B.3. 64 Bit Big Endian Representation of AAD Length
------------------------------------------------------------

The Additional Authenticated Data (AAD) in this example is:

.. code-block:: javascript

   [101, 121, 74, 104, 98, 71, 99, 105, 79, 105, 74, 66, 77, 84, 73, 52,
   83, 49, 99, 105, 76, 67, 74, 108, 98, 109, 77, 105, 79, 105, 74, 66,
   77, 84, 73, 52, 81, 48, 74, 68, 76, 85, 104, 84, 77, 106, 85, 50, 73,
   110, 48]

This AAD is 51 bytes long, which is 408 bits long.  The octet string
AL, which is the number of bits in AAD expressed as a big endian 64
bit unsigned integer is:

.. code-block:: javascript

   [0, 0, 0, 0, 0, 0, 1, 152]

.. note::
    - AADのビット数です。オクテット数ではありません。

( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-13#appendix-B.3 )
