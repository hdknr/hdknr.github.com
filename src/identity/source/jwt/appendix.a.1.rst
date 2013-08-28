A.1. Example Encrypted JWT
------------------------------------

This example encrypts the same claims as used in Section 3.1 
to the recipient using RSAES-PKCS1-V1_5 and AES_128_CBC_HMAC_SHA_256.

The following example JWE Header 
(with line breaks for display purposes only) declares that:

   -  the Content Encryption Key is encrypted to the recipient using the
      RSAES-PKCS1-V1_5 algorithm to produce the JWE Encrypted Key and

   -  the Plaintext is encrypted using the AES_128_CBC_HMAC_SHA_256
      algorithm to produce the Ciphertext.

      :: 
    
         {"alg":"RSA1_5","enc":"A128CBC-HS256"}

Other than using the octets of the UTF-8 representation of 
the JWT Claims Set from Section 3.1 as the plaintext value, 
the computation of this JWT is identical to the computation of the JWE 
in Appendix A.2 of [JWE], including the keys used.

The final result in this example (with line breaks for display purposes only) is:

::

     eyJhbGciOiJSU0ExXzUiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.
     QR1Owv2ug2WyPBnbQrRARTeEk9kDO2w8qDcjiHnSJflSdv1iNqhWXaKH4MqAkQtM
     oNfABIPJaZm0HaA415sv3aeuBWnD8J-Ui7Ah6cWafs3ZwwFKDFUUsWHSK-IPKxLG
     TkND09XyjORj_CHAgOPJ-Sd8ONQRnJvWn_hXV1BNMHzUjPyYwEsRhDhzjAD26ima
     sOTsgruobpYGoQcXUwFDn7moXPRfDE8-NoQX7N7ZYMmpUDkR-Cx9obNGwJQ3nM52
     YCitxoQVPzjbl7WBuB7AohdBoZOdZ24WlN1lVIeh8v1K4krB8xgKvRU8kgFrEn_a
     1rZgN5TiysnmzTROF869lQ.
     AxY8DCtDaGlsbGljb3RoZQ.
     MKOle7UQrG6nSxTLX6Mqwt0orbHvAKeWnDYvpIAeZ72deHxz3roJDXQyhxx0wKaM
     HDjUEOKIwrtkHthpqEanSBNYHZgmNOV7sln1Eu9g3J8.
     fiK51VwhsxJ-siBMR-YFiA


( https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-11#appendix-A.1 )
