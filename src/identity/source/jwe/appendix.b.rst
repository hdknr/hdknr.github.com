Appendix B.  Example AES_128_CBC_HMAC_SHA_256 Computation
===========================================================================

This example shows the steps 
in the :ref:`jwa.AES_128_CBC_HMAC_SHA_256` 
authenticated encryption computation 
using the values from the example in :ref:`Appendix A.3 <jwe.appendix.a.3>`.  

As described where this algorithm is defined 
in :ref:`Sections 4.8 <jwa.4.8>` and :ref:`4.8.3 <jwa.4.8.3>` of JWA, 
the :ref:`jwa.AES_CBC_HMAC_SHA2` family of algorithms are implemented 
using Advanced Encryption Standard (AES) 
in Cipher Block Chaining (CBC) mode 
with PKCS #5 padding 
to perform the encryption and an HMAC SHA-2 function 
to perform the integrity calculation - in this case, HMAC SHA-256.

(draft21)
