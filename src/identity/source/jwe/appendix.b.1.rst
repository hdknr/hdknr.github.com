B.1. Extract MAC_KEY and ENC_KEY from Key
------------------------------------------------------------

The 256 bit AES_128_CBC_HMAC_SHA_256 key K used in this example is:

.. code-block:: javascript

   [4, 211, 31, 197, 84, 157, 252, 254, 11, 100, 157, 250, 63, 170, 106,
   206, 107, 124, 212, 45, 111, 107, 9, 219, 200, 177, 0, 240, 143, 156,
   44, 207]

Use the first 128 bits of this key as the HMAC SHA-256 key MAC_KEY,
which is:

.. code-block:: javascript

   [4, 211, 31, 197, 84, 157, 252, 254, 11, 100, 157, 250, 63, 170, 106,
   206]

Use the last 128 bits of this key as the AES CBC key ENC_KEY, which is:

.. code-block:: javascript

   [107, 124, 212, 45, 111, 107, 9, 219, 200, 177, 0, 240, 143, 156, 44,
   207]

Note that the MAC key comes before the encryption key in the input
key K; this is in the opposite order of the algorithm names in the
identifiers "AES_128_CBC_HMAC_SHA_256" and "A128CBC-HS256".

( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-13#appendix-B.1 )
