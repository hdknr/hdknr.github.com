A.2.7. Additional Authenticated Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let the Additional Authenticated Data encryption parameter be the
octets of the ASCII representation of the Encoded JWE Header value.
This AAD value is:

.. code-block:: javascript

   [101, 121, 74, 104, 98, 71, 99, 105, 79, 105, 74, 83, 85, 48, 69,
   120, 88, 122, 85, 105, 76, 67, 74, 108, 98, 109, 77, 105, 79, 105,
   74, 66, 77, 84, 73, 52, 81, 48, 74, 68, 76, 85, 104, 84, 77, 106, 85,
   50, 73, 110, 48]

( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-13#appendix-A.2.7 )
