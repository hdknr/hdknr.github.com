B.2. Encrypt Plaintext to Create Ciphertext
------------------------------------------------------------------------------------

Encrypt the Plaintext with AES in Cipher Block Chaining (CBC) mode
using PKCS #5 padding using the ENC_KEY above.  The Plaintext in this
example is:

.. code-block:: javascript

   [76, 105, 118, 101, 32, 108, 111, 110, 103, 32, 97, 110, 100, 32,
   112, 114, 111, 115, 112, 101, 114, 46]

The encryption result is as follows, which is the Ciphertext output:

.. code-block:: javascript

   [40, 57, 83, 181, 119, 33, 133, 148, 198, 185, 243, 24, 152, 230, 6,
   75, 129, 223, 127, 19, 210, 82, 183, 230, 168, 33, 215, 104, 143,
   112, 56, 102]


( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-13#appendix-B.2 )
