A.2.1. JWE Header
^^^^^^^^^^^^^^^^^^^^^^^^

The following example JWE Protected Header declares that:

-  the Content Encryption Key is encrypted to the recipient using the
   RSAES-PKCS1-V1_5 algorithm to produce the JWE Encrypted Key and

-  the Plaintext is encrypted using the AES_128_CBC_HMAC_SHA_256
   algorithm to produce the Ciphertext.

::

     {"alg":"RSA1_5","enc":"A128CBC-HS256"}

Encoding this JWE Protected Header 
as BASE64URL(UTF8(JWE Protected Header)) gives this value:

::

     eyJhbGciOiJSU0ExXzUiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0


( draft23 https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-23#appendix-A.2.1 )


.. note::
    - CEK は RSA AES PKCS1 V.1.5 で非対称暗号化されて JEK となる
    - Plaintextは AES_128_CBC_HMAC_SHA_256 でCEKを使った共有鍵暗号化で Ciphertextとなる

