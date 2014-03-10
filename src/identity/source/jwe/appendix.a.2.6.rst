A.2.6.  Content Encryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encrypt the Plaintext with 
:ref:`AES_128_CBC_HMAC_SHA_256` using 
the CEK as the encryption key, 
the JWE Initialization Vector, and 
the Additional Authenticated Data value above.  

The steps for doing this using the values 
from Appendix A.3 are detailed in Appendix B.  

The resulting Ciphertext is:

::

    [40, 57, 83, 181, 119, 33, 133, 148, 198, 185, 243, 24, 152, 230, 6,
    75, 129, 223, 127, 19, 210, 82, 183, 230, 168, 33, 215, 104, 143,
    112, 56, 102]

The resulting Authentication Tag value is:

::

    [246, 17, 244, 190, 4, 95, 98, 3, 231, 0, 115, 157, 242, 203, 100,
    191]

Encoding this JWE Ciphertext as BASE64URL(JWE Ciphertext) gives this
value:

::

  KDlTtXchhZTGufMYmOYGS4HffxPSUrfmqCHXaI9wOGY

Encoding this JWE Authentication Tag 
as BASE64URL(JWE Authentication Tag) gives this value:

::

  9hH0vgRfYgPnAHOd8stkvw

(draft23)
