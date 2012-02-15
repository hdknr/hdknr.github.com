Appendix A.  Digital Signature/HMAC Algorithm Identifier Cross-Reference
================================================================================================================

This appendix contains a table cross-referencing the digital signature and HMAC alg (algorithm) values used in this specification with the equivalent identifiers used by other standards and software packages. See XML DSIG [RFC3275] and Java Cryptography Architecture [JCA] for more information about the names defined by those documents.

.. list-table::  Table 4: Digital Signature/HMAC Algorithm Identifier Cross-Reference 
    :header-rows: 1

    *   - Algorithm   
        - JWS 
        - XML DSIG    
        - JCA 
        - OID

    *   - HMAC using SHA-256 hash algorithm   
        - HS256   
        - http://www.w3.org/2001/04/xmldsig-more#hmac-sha256  
        - HmacSHA256  
        - 1.2.840.113549.2.9

    *   - HMAC using SHA-384 hash algorithm   
        - HS384   
        - http://www.w3.org/2001/04/xmldsig-more#hmac-sha384  
        - HmacSHA384  
        - 1.2.840.113549.2.10

    *   - HMAC using SHA-512 hash algorithm   
        - HS512   
        - http://www.w3.org/2001/04/xmldsig-more#hmac-sha512  
        - HmacSHA512  
        - 1.2.840.113549.2.11

    *   - RSA using SHA-256 hash algorithm    
        - RS256   
        - http://www.w3.org/2001/04/xmldsig-more#rsa-sha256   
        - SHA256withRSA   
        - 1.2.840.113549.1.1.11

    *   - RSA using SHA-384 hash algorithm    
        - RS384   
        - http://www.w3.org/2001/04/xmldsig-more#rsa-sha384   
        - SHA384withRSA   
        - 1.2.840.113549.1.1.12

    *   - RSA using SHA-512 hash algorithm    
        - RS512   
        - http://www.w3.org/2001/04/xmldsig-more#rsa-sha512   
        - SHA512withRSA   
        - 1.2.840.113549.1.1.13

    *   - ECDSA using P-256 curve and SHA-256 hash algorithm  
        - ES256   
        - http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256 
        - SHA256withECDSA 
        - 1.2.840.10045.4.3.2

    *   - ECDSA using P-384 curve and SHA-384 hash algorithm  
        - ES384   
        - http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha384 
        - SHA384withECDSA 
        - 1.2.840.10045.4.3.3

    *   - ECDSA using P-521 curve and SHA-512 hash algorithm  
        - ES512   
        - http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha512 
        - SHA512withECDSA 
        - 1.2.840.10045.4.3.4
