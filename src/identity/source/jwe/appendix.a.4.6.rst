A.4.6.  Content Encryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encrypt the Plaintext 
with :ref:`AES_128_CBC_HMAC_SHA_256` 
using the CEK as the encryption key, 
the JWE Initialization Vector, and 
the Additional Authenticated Data value above.  

The steps for doing this using the values 
from :ref:`Appendix A.3 <jwe.appendix.a.3>` are detailed 
in :ref:`Appendix B <jwe.appendix.b>`.  

The resulting Ciphertext is:

::

   [40, 57, 83, 181, 119, 33, 133, 148, 198, 185, 243, 24, 152, 230, 6,
   75, 129, 223, 127, 19, 210, 82, 183, 230, 168, 33, 215, 104, 143,
   112, 56, 102]

The resulting Authentication Tag value is:

::

    [51, 63, 149, 60, 252, 148, 225, 25, 92, 185, 139, 245, 35, 2, 47,
    207]

Encoding this JWE Ciphertext as BASE64URL(JWE Ciphertext) gives this
value:

::

  KDlTtXchhZTGufMYmOYGS4HffxPSUrfmqCHXaI9wOGY


Encoding this JWE Authentication Tag as BASE64URL(JWE Authentication
Tag) gives this value:

::

  Mz-VPPyU4RlcuYv1IwIvzw


