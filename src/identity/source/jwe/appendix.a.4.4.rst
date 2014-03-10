A.4.4.  Complete JWE Header Values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Combining the per-recipient, protected, and unprotected header values
supplied, the JWE Header values used for the first and second
recipient respectively are:

::

  {"alg":"RSA1_5",
   "kid":"2011-04-29",
   "enc":"A128CBC-HS256",
   "jku":"https://server.example.com/keys.jwks"}

and

::

  {"alg":"A128KW",
   "kid":"7",
   "enc":"A128CBC-HS256",
   "jku":"https://server.example.com/keys.jwks"}
