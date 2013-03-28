A.1.1. JWE Header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following example JWE Header declares that:

   -  the :term:`Content Master Key` is encrypted to the recipient 
      using the :term:`RSAES OAEP` algorithm to produce the :term:`JWE Encrypted Key` and

   -  the :term:`Plaintext` is encrypted using the :term:`AES GCM` algorithm 
      with a **256 bit key** to produce the :term:`Ciphertext`.

.. code-block:: javascript

     {"alg":"RSA-OAEP","enc":"A256GCM"}

( draft 08, http://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-08#appendix-A.1.1 )
