A.4.2.  JWE Protected Header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Plaintext is encrypted using the AES_128_CBC_HMAC_SHA_256
algorithm to produce the common JWE Ciphertext and JWE Authentication
Tag values.  The JWE Protected Header value representing this is:

::

  {"enc":"A128CBC-HS256"}

Encoding this JWE Protected Header as BASE64URL(UTF8(JWE Protected
Header)) gives this value:

::

  eyJlbmMiOiJBMTI4Q0JDLUhTMjU2In0

(draft23)
