A.2. Example JWE using RSAES-PKCS1-V1_5 and AES_128_CBC_HMAC_SHA_256
----------------------------------------------------------------------------

This example encrypts the plaintext "Live long and prosper." 
to the recipient 
using :ref:`RSAES-PKCS1-V1_5` for key encryption and
:ref:`AES_128_CBC_HMAC_SHA_256` for content encryption.  

The representation of this plaintext is:

   [76, 105, 118, 101, 32, 108, 111, 110, 103, 32, 97, 110, 100, 32,
   112, 114, 111, 115, 112, 101, 114, 46]

( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-23#appendix-A.2 ) 

