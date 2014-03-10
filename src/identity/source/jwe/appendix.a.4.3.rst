A.4.3.  JWE Unprotected Header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This JWE uses the "jku" Header Parameter to reference a JWK Set. This
is represented in the following JWE Unprotected Header value as:

::

     {"jku":"https://server.example.com/keys.jwks"}

