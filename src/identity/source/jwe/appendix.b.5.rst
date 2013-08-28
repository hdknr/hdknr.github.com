B.5. Create Input to HMAC Computation
------------------------------------------------

Concatenate the AAD, the Initialization Vector, the Ciphertext, and
the AL value.  The result of this concatenation is:

.. code-block:: javascript

   [101, 121, 74, 104, 98, 71, 99, 105, 79, 105, 74, 66, 77, 84, 73, 52,
   83, 49, 99, 105, 76, 67, 74, 108, 98, 109, 77, 105, 79, 105, 74, 66,
   77, 84, 73, 52, 81, 48, 74, 68, 76, 85, 104, 84, 77, 106, 85, 50, 73,
   110, 48, 3, 22, 60, 12, 43, 67, 104, 105, 108, 108, 105, 99, 111,
   116, 104, 101, 40, 57, 83, 181, 119, 33, 133, 148, 198, 185, 243, 24,
   152, 230, 6, 75, 129, 223, 127, 19, 210, 82, 183, 230, 168, 33, 215,
   104, 143, 112, 56, 102, 0, 0, 0, 0, 0, 0, 1, 152]


( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-13#appendix-B.5 )
