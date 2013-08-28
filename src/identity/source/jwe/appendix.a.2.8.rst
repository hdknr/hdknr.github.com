A.2.8. Plaintext Encryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encrypt the Plaintext with AES_128_CBC_HMAC_SHA_256 using the CEK as
the encryption key, the JWE Initialization Vector, and the Additional
Authenticated Data value above.  The steps for doing this using the
values from Appendix A.3 are detailed in Appendix B.  The resulting
Ciphertext is:

.. code-block:: javascript

   [40, 57, 83, 181, 119, 33, 133, 148, 198, 185, 243, 24, 152, 230, 6,
   75, 129, 223, 127, 19, 210, 82, 183, 230, 168, 33, 215, 104, 143,
   112, 56, 102]

The resulting Authentication Tag value is:

.. code-block:: javascript

   [246, 17, 244, 190, 4, 95, 98, 3, 231, 0, 115, 157, 242, 203, 100,
   191]

( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-13#appendix-A.2.8 )
