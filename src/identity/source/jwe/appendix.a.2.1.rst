A.2.1. JWE Header
^^^^^^^^^^^^^^^^^^^^^^^^

The following example JWE Header (with line breaks for display
purposes only) declares that:

   -  the Content Encryption Key is encrypted to the recipient using the
      RSAES-PKCS1-V1_5 algorithm to produce the JWE Encrypted Key and

   -  the Plaintext is encrypted using the AES_128_CBC_HMAC_SHA_256
      algorithm to produce the Ciphertext.

::

     {"alg":"RSA1_5","enc":"A128CBC-HS256"}


( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-13#appendix-A.2.1 )


.. note::
    - CEK は RSA AES PKCS1 V.1.5 で非対称暗号化されて JEK となる
    - Plaintextは AES_128_CBC_HMAC_SHA_256 でCEKを使った共有鍵暗号化で Ciphertextとなる

