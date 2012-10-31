Appendix A. Digital Signature/MAC Algorithm Identifier Cross-Reference
===========================================================================

This appendix contains a table cross-referencing the digital
signature and MAC "alg" (algorithm) values used in this specification
with the equivalent identifiers used by other standards and software
packages.  See XML DSIG [RFC3275], XML DSIG 2.0
[W3C.CR-xmldsig-core2-20120124], and Java Cryptography Architecture
[JCA] for more information about the names defined by those documents.

   +-------+-----+----------------------------+----------+-------------+
   | Algor | JWS | XML DSIG                   | JCA      | OID         |
   | ithm  |     |                            |          |             |
   +-------+-----+----------------------------+----------+-------------+
   | HMAC  | HS2 | http://www.w3.org/2001/04/ | HmacSHA2 | 1.2.840.113 |
   | using | 56  | xmldsig-more#hmac-sha256   | 56       | 549.2.9     |
   | SHA-2 |     |                            |          |             |
   | 56    |     |                            |          |             |
   |  hash |     |                            |          |             |
   |  algo |     |                            |          |             |
   | rithm |     |                            |          |             |
   +-------+-----+----------------------------+----------+-------------+
   | HMAC  | HS3 | http://www.w3.org/2001/04/ | HmacSHA3 | 1.2.840.113 |
   | using | 84  | xmldsig-more#hmac-sha384   | 84       | 549.2.10    |
   | SHA-3 |     |                            |          |             |
   | 84    |     |                            |          |             |
   |  hash |     |                            |          |             |
   |  algo |     |                            |          |             |
   | rithm |     |                            |          |             |
   +-------+-----+----------------------------+----------+-------------+
   | HMAC  | HS5 | http://www.w3.org/2001/04/ | HmacSHA5 | 1.2.840.113 |
   | using | 12  | xmldsig-more#hmac-sha512   | 12       | 549.2.11    |
   | SHA-5 |     |                            |          |             |
   | 12    |     |                            |          |             |
   |  hash |     |                            |          |             |
   |  algo |     |                            |          |             |
   | rithm |     |                            |          |             |
   +-------+-----+----------------------------+----------+-------------+
   | RSASS | RS2 | http://www.w3.org/2001/04/ | SHA256wi | 1.2.840.113 |
   | A     | 56  | xmldsig-more#rsa-sha256    | thRSA    | 549.1.1.11  |
   |  usin |     |                            |          |             |
   | gSHA- |     |                            |          |             |
   | 256   |     |                            |          |             |
   |   has |     |                            |          |             |
   | h alg |     |                            |          |             |
   | orith |     |                            |          |             |
   | m     |     |                            |          |             |
   +-------+-----+----------------------------+----------+-------------+
   | RSASS | RS3 | http://www.w3.org/2001/04/ | SHA384wi | 1.2.840.113 |
   | A     | 84  | xmldsig-more#rsa-sha384    | thRSA    | 549.1.1.12  |
   |  usin |     |                            |          |             |
   | gSHA- |     |                            |          |             |
   | 384   |     |                            |          |             |
   |   has |     |                            |          |             |
   | h alg |     |                            |          |             |
   | orith |     |                            |          |             |
   | m     |     |                            |          |             |
   +-------+-----+----------------------------+----------+-------------+
   | RSASS | RS5 | http://www.w3.org/2001/04/ | SHA512wi | 1.2.840.113 |
   | A     | 12  | xmldsig-more#rsa-sha512    | thRSA    | 549.1.1.13  |
   |  usin |     |                            |          |             |
   | gSHA- |     |                            |          |             |
   | 512   |     |                            |          |             |
   |   has |     |                            |          |             |
   | h alg |     |                            |          |             |
   | orith |     |                            |          |             |
   | m     |     |                            |          |             |
   +-------+-----+----------------------------+----------+-------------+
   | ECDSA | ES2 | http://www.w3.org/2001/04/ | SHA256wi | 1.2.840.100 |
   | using | 56  | xmldsig-more#ecdsa-sha256  | thECDSA  | 45.4.3.2    |
   | P-256 |     |                            |          |             |
   | curve |     |                            |          |             |
   | and   |     |                            |          |             |
   | SHA-2 |     |                            |          |             |
   | 56    |     |                            |          |             |
   |  hash |     |                            |          |             |
   |  algo |     |                            |          |             |
   | rithm |     |                            |          |             |
   +-------+-----+----------------------------+----------+-------------+
   | ECDSA | ES3 | http://www.w3.org/2001/04/ | SHA384wi | 1.2.840.100 |
   | using | 84  | xmldsig-more#ecdsa-sha384  | thECDSA  | 45.4.3.3    |
   | P-384 |     |                            |          |             |
   | curve |     |                            |          |             |
   | and   |     |                            |          |             |
   | SHA-3 |     |                            |          |             |
   | 84    |     |                            |          |             |
   |  hash |     |                            |          |             |
   |  algo |     |                            |          |             |
   | rithm |     |                            |          |             |
   +-------+-----+----------------------------+----------+-------------+
   | ECDSA | ES5 | http://www.w3.org/2001/04/ | SHA512wi | 1.2.840.100 |
   | using | 12  | xmldsig-more#ecdsa-sha512  | thECDSA  | 45.4.3.4    |
   | P-521 |     |                            |          |             |
   | curve |     |                            |          |             |
   | and   |     |                            |          |             |
   | SHA-5 |     |                            |          |             |
   | 12    |     |                            |          |             |
   |  hash |     |                            |          |             |
   |  algo |     |                            |          |             |
   | rithm |     |                            |          |             |
   +-------+-----+----------------------------+----------+-------------+

(draft 06, http://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-06#appendix-A )
