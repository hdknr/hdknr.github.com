Appendix B. Example AES_128_CBC_HMAC_SHA_256 Computation
===========================================================================================

This example shows the steps in the AES_128_CBC_HMAC_SHA_256
authenticated encryption computation using the values from the example in Appendix A.3.  

As described where this algorithm is defined in Sections 4.8 and 4.8.3 of JWA, 
the AES_CBC_HMAC_SHA2 family of algorithms are implemented using Advanced Encryption
Standard (AES) in Cipher Block Chaining (CBC) mode with PKCS #5
padding to perform the encryption and an HMAC SHA-2 function to
perform the integrity calculation - in this case, HMAC SHA-256.

( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-13#appendix-B )

