A.3.1.  JWE Header
^^^^^^^^^^^^^^^^^^^^^^

The following example JWE Protected Header declares that:

-  the Content Encryption Key is encrypted to the recipient 
   using the AES Key Wrap algorithm with a 128 bit key 
   to produce the JWE Encrypted Key and

o  the Plaintext is encrypted using the :term:`AES_128_CBC_HMAC_SHA_256`
   algorithm to produce the Ciphertext.

.. code-block:: javascript

  {"alg":"A128KW","enc":"A128CBC-HS256"}

Encoding this JWE Protected Header 
as BASE64URL(UTF8(JWE Protected Header)) gives this value:

::

    eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0


.. code-block:: python

    >>> from jose.utils import base64
    >>> base64.base64url_encode('{"alg":"A128KW","enc":"A128CBC-HS256"}')

    'eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0'


(draft21)
