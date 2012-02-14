Appendix B.  Algorithm Identifier Cross-Reference
============================================================

This appendix contains a table cross-referencing the :term:`alg` values 
used in this specification with the equivalent identifiers 
used by other standards and software packages. 

See XML DSIG [RFC3275] and Java Cryptography Architecture [JCA] 
for more information about the names defined by those documents. 

 +----------------------+-----------+-------------------------------------------------------+-------------------+-----------------------+
 | Algorithm            | JWS       | XML DSIG                                              | JCA               | OID                   |
 +======================+===========+=======================================================+===================+=======================+
 | HMAC                 | HS256     | http://www.w3.org/2001/04/xmldsig-more#hmac-sha256    | HmacSHA256        | 1.2.840.113549.2.9    |
 | using SHA-256        |           |                                                       |                   | [#]_                  |
 | hash algorithm       |           |                                                       |                   |                       |
 +----------------------+-----------+-------------------------------------------------------+-------------------+-----------------------+
 | HMAC                 | HS384     | http://www.w3.org/2001/04/xmldsig-more#hmac-sha384    | HmacSHA384        | 1.2.840.113549.2.10   |
 | using SHA-384        |           |                                                       |                   | [#]_                  |
 | hash algorithm       |           |                                                       |                   |                       |
 +----------------------+-----------+-------------------------------------------------------+-------------------+-----------------------+
 | HMAC                 | HS512     | http://www.w3.org/2001/04/xmldsig-more#hmac-sha512    | HmacSHA512        | 1.2.840.113549.2.11   |
 | using SHA-512        |           |                                                       |                   | [#]_                  |
 | hash algorithm       |           |                                                       |                   |                       |
 +----------------------+-----------+-------------------------------------------------------+-------------------+-----------------------+
 | RSA                  | RS256     | http://www.w3.org/2001/04/xmldsig-more#rsa-sha256     | SHA256withRSA     | 1.2.840.113549.1.1.11 |
 | using SHA-256        |           |                                                       |                   | [#]_                  |
 | hash algorithm       |           |                                                       |                   |                       |
 +----------------------+-----------+-------------------------------------------------------+-------------------+-----------------------+
 | RSA                  | RS384     | http://www.w3.org/2001/04/xmldsig-more#rsa-sha384     | SHA384withRSA     | 1.2.840.113549.1.1.12 |
 | using SHA-384        |           |                                                       |                   | [#]_                  |
 | hash algorithm       |           |                                                       |                   |                       |
 +----------------------+-----------+-------------------------------------------------------+-------------------+-----------------------+
 | RSA                  | RS512     | http://www.w3.org/2001/04/xmldsig-more#rsa-sha512     | SHA512withRSA     | 1.2.840.113549.1.1.13 |
 | using SHA-512        |           |                                                       |                   | [#]_                  |
 | hash algorithm       |           |                                                       |                   |                       |
 +----------------------+-----------+-------------------------------------------------------+-------------------+-----------------------+
 | ECDSA using          | ES256     | http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256   | SHA256withECDSA   | 1.2.840.10045.3.1.7   |
 | P-256 curve and      |           |                                                       |                   | 1.2.840.10045.4.3.2   |
 | SHA-256              |           |                                                       |                   | [#]_                  |
 | hash algorithm       |           |                                                       |                   |                       |
 +----------------------+-----------+-------------------------------------------------------+-------------------+-----------------------+
 | ECDSA using          | ES384     | http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha384   | SHA384withECDSA   | 1.3.132.0.34          |
 | P-384 curve and      |           |                                                       |                   | 1.2.840.10045.4.3.3   |
 | SHA-384              |           |                                                       |                   | [#]_                  |
 | hash algorithm       |           |                                                       |                   |                       |
 +----------------------+-----------+-------------------------------------------------------+-------------------+-----------------------+
 | ECDSA using          | ES512     | http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha512   | SHA512withECDSA   | 1.3.132.0.35          |
 | P-512 curve and      |           |                                                       |                   | 1.2.840.10045.4.3.4   |
 | SHA-512              |           |                                                       |                   | [#]_                  |
 | hash algorithm       |           |                                                       |                   |                       |
 +----------------------+-----------+-------------------------------------------------------+-------------------+-----------------------+

.. [#] hamcWithSHA256 http://www.oid-info.com/get/1.2.840.113549.2.9
.. [#] hamcWithSHA384 http://www.oid-info.com/get/1.2.840.113549.2.10
.. [#] hamcWithSHA512 http://www.oid-info.com/get/1.2.840.113549.2.11 
.. [#] sha256WithRSAEncryption http://www.oid-info.com/get/1.2.840.113549.1.1.11
.. [#] sha384WithRSAEncryption http://www.oid-info.com/get/1.2.840.113549.1.1.12 
.. [#] sha512WithRSAEncryption http://www.oid-info.com/get/1.2.840.113549.1.1.13 
.. [#] ecdsa-with-SHA256 http://www.oid-info.com/get/1.2.840.10045.4.3.2
.. [#] ecdsa-with-SHA384 http://www.oid-info.com/get/1.2.840.10045.4.3.3
.. [#] ecdsa-with-SHA512 http://www.oid-info.com/get/1.2.840.10045.4.3.4 

(v.03)
