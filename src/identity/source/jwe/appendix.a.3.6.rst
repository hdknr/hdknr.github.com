A.3.6.  Content Encryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encrypt the Plaintext with AES_128_CBC_HMAC_SHA_256 
using the CEK as the encryption key, 
the JWE Initialization Vector, 
and the Additional Authenticated Data value above.  

The steps for doing this 
using the values from this example are detailed 
in :ref:`Appendix B <jwe.appendix.b>`.  

The :ref:`resulting Ciphertext <jwe.appendeix.b.2>` is:

::

   [40, 57, 83, 181, 119, 33, 133, 148, 198, 185, 243, 24, 152, 230, 6,
   75, 129, 223, 127, 19, 210, 82, 183, 230, 168, 33, 215, 104, 143,
   112, 56, 102]

The resulting Authentication Tag value is:


::

   [83, 73, 191, 98, 104, 205, 211, 128, 201, 189, 199, 133, 32, 38,
   194, 85]

Encoding this JWE Ciphertext as BASE64URL(JWE Ciphertext) gives this
value:

::

     KDlTtXchhZTGufMYmOYGS4HffxPSUrfmqCHXaI9wOGY

Encoding this JWE Authentication Tag 
as BASE64URL(JWE Authentication Tag) gives this value:


::

     U0m_YmjN04DJvceFICbCVQ


(draft21)
