Appendix B.  Encryption Algorithm Identifier Cross-Reference
=================================================================================

This appendix contains a table cross-referencing the alg (algorithm) and enc (encryption method) values used in this specification with the equivalent identifiers used by other standards and software packages. See XML Encryption [W3C.REC‑xmlenc‑core‑20021210], XML Encryption 1.1 [W3C.CR‑xmlenc‑core1‑20110303], and Java Cryptography Architecture [JCA] for more information about the names defined by those documents.


.. list-table::  Table 5: Encryption Algorithm Identifier Cross-Reference 

    *   - Algorithm   
        - JWE 
        - XML ENC 
        - JCA


    *   - RSA using RSA-PKCS1-1.5 padding 
        - RSA1_5  
        - http://www.w3.org/2001/04/xmlenc#rsa-1_5    
        - RSA/ECB/PKCS1Padding

    *   - RSA using Optimal Asymmetric Encryption Padding (OAEP)  
        - RSA-OAEP    
        - http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p 
        - RSA/ECB/OAEPWithSHA-1AndMGF1Padding

    *   - Elliptic Curve Diffie-Hellman Ephemeral Static  
        - ECDH-ES 
        - http://www.w3.org/2009/xmlenc11#ECDH-ES 
        - TBD

    *   - Advanced Encryption Standard (AES) Key Wrap Algorithm RFC 3394 [RFC3394] using 128 bit keys 
        - A128KW  
        - http://www.w3.org/2001/04/xmlenc#kw-aes128  
        - TBD

    *   - Advanced Encryption Standard (AES) Key Wrap Algorithm RFC 3394 [RFC3394] using 256 bit keys 
        - A256KW  
        - http://www.w3.org/2001/04/xmlenc#kw-aes256  
        - TBD

    *   - Advanced Encryption Standard (AES) using 128 bit keys in Cipher Block Chaining mode 
        - A128CBC 
        - http://www.w3.org/2001/04/xmlenc#aes128-cbc 
        - AES/CBC/PKCS5Padding

    *   - Advanced Encryption Standard (AES) using 256 bit keys in Cipher Block Chaining mode 
        - A256CBC 
        - http://www.w3.org/2001/04/xmlenc#aes256-cbc 
        - AES/CBC/PKCS5Padding

    *   - Advanced Encryption Standard (AES) using 128 bit keys in Galois/Counter Mode    
        - A128GCM 
        - http://www.w3.org/2009/xmlenc11#aes128-gcm  
        - AES/GCM/NoPadding

    *   - Advanced Encryption Standard (AES) using 256 bit keys in Galois/Counter Mode    
        - A256GCM 
        - http://www.w3.org/2009/xmlenc11#aes256-gcm  
        - AES/GCM/NoPadding

(00)
