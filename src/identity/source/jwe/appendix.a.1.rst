A.1. Example JWE using RSAES OAEP and AES GCM
--------------------------------------------------------

This example encrypts the plaintext "**Live long and prosper.**" 
to the recipient using :term:`RSAES OAEP` and :term:`AES GCM`.  

The AES GCM algorithm has an integrated integrity check.  

The representation of this plaintext is:

.. code-block:: javascript

   [76, 105, 118, 101, 32, 108, 111, 110, 103, 32, 97, 110, 100, 32,
   112, 114, 111, 115, 112, 101, 114, 46]


( draft 08, http://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-08#appendix-A.1 )
