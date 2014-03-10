A.1. Example JWE using RSAES OAEP and AES GCM
--------------------------------------------------------

This example encrypts the plaintext 
"The true sign of intelligence is not knowledge but imagination." 
to the recipient 
using :term:`RSAES OAEP` for key encryption and :term:`AES GCM` 
for content encryption.  

The representation of this plaintext is:

::

   [84, 104, 101, 32, 116, 114, 117, 101, 32, 115, 105, 103, 110, 32,
   111, 102, 32, 105, 110, 116, 101, 108, 108, 105, 103, 101, 110, 99,
   101, 32, 105, 115, 32, 110, 111, 116, 32, 107, 110, 111, 119, 108,
   101, 100, 103, 101, 32, 98, 117, 116, 32, 105, 109, 97, 103, 105,
   110, 97, 116, 105, 111, 110, 46]

(draft23, http://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-23#appendix-A.1)
