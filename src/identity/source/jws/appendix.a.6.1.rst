A.6.1.  JWS Per-Signature Protected Headers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The JWS Protected Header value used for the first signature is:

::

     {"alg":"RS256"}

Encoding this JWS Protected Header 
as BASE64URL(UTF8(JWS Protected Header)) gives this value:

::

     eyJhbGciOiJSUzI1NiJ9

The JWS Protected Header value used for the second signature is:

::

     {"alg":"ES256"}

Encoding this JWS Protected Header 
as BASE64URL(UTF8(JWS Protected Header)) gives this value:

::

     eyJhbGciOiJFUzI1NiJ9

(draft 24)
