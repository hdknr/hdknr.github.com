B.7. Truncate HMAC Value to Create Authentication Tag
------------------------------------------------------------

Use the first half (128 bits) of the HMAC output M as the
Authentication Tag output T. This truncated value is:

.. code-block:: javascript

   [83, 73, 191, 98, 104, 205, 211, 128, 201, 189, 199, 133, 32, 38,
   194, 85]

( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-13#appendix-B.7 )

