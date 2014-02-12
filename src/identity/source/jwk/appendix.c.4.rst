
C.4.  Key Encryption
------------------------------

Encrypt the CEK with a shared passphrase using the
"PBES2-HS256+A128KW" algorithm and the specified Salt and Iteration
Count values to produce the JWE Encrypted Key. This example uses the
following passphrase:

::

     Thus from my lips, by yours, my sin is purged.

The octets representing the passphrase are:

::

   [ 84, 104, 117, 115, 32, 102, 114, 111, 109, 32, 109, 121, 32, 108,
   105, 112, 115, 44, 32, 98, 121, 32, 121, 111, 117, 114, 115, 44, 32,
   109, 121, 32, 115, 105, 110, 32, 105, 115, 32, 112, 117, 114, 103,
   101, 100, 46 ]

The resulting JWE Encrypted Key value is:

::

   [ 201, 236, 143, 112, 12, 234, 200, 211, 33, 241, 255, 65, 112, 63,
   172, 146, 105, 107, 122, 0, 30, 21, 44, 21, 14, 61, 200, 57, 30, 253,
   228, 83, 218, 82, 138, 80, 121, 254, 193, 121 ]

Encoding this JWE Encrypted Key as BASE64URL(JWE Encrypted Key) gives
this value:

::

     yeyPcAzqyNMh8f9BcD-skmlregAeFSwVDj3IOR795FPaUopQef7BeQ

(draft20)
