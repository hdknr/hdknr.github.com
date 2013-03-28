A.1.8. Plaintext Encryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encrypt the :term:`Plaintext` with :term:`AES GCM` 
using the :term:`CMK` as the encryption key, 
the :term:`JWE Initialization Vector`, 
and the ":term:`additional authenticated data`" value above, 
requesting a 128 bit ":term:`authentication tag`" output.

The resulting Ciphertext is:

.. code-block:: javascript

   [253, 237, 181, 180, 97, 161, 105, 207, 233, 120, 65, 100, 45, 122,
   246, 116, 195, 212, 102, 37, 36, 175]


The resulting "authentication tag" value is:

.. code-block:: javascript

   [237, 94, 89, 14, 74, 52, 191, 249, 159, 216, 240, 28, 224, 147, 34,
   82]

(draft08, http://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-08#appendix-A.1.8) 
