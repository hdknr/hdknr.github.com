A.1.1. JWE Header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following example JWE Header declares that:

   -  the Content Encryption Key is encrypted to the recipient using the
      RSAES OAEP algorithm to produce the JWE Encrypted Key and

   -  the Plaintext is encrypted using the AES GCM algorithm with a 256
      bit key to produce the Ciphertext.


      ::

        {"alg":"RSA-OAEP","enc":"A256GCM"}

Encoding this JWE Protected Header 
as BASE64URL(UTF8(JWE Protected Header)) gives this value:

::

     eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00ifQ

( draft23, http://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-23#appendix-A.1.1 )
