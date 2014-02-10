A.1. Digital Signature/MAC Algorithm Identifier Cross-Reference
------------------------------------------------------------------------


This section contains a table cross-referencing the JWS digital
signature and MAC "alg" (algorithm) values 
defined in this specification with the equivalent identifiers 
used by other standards and software packages.

   +-----+-------------------------------+--------------+--------------+
   | JWS | XML DSIG                      | JCA          | OID          |
   +-----+-------------------------------+--------------+--------------+
   | HS2 | http://www.w3.org/2001/04/xml | HmacSHA256   | 1.2.840.1135 |
   | 56  | dsig-more#hmac-sha256         |              | 49.2.9       |
   +-----+-------------------------------+--------------+--------------+
   | HS3 | http://www.w3.org/2001/04/xml | HmacSHA384   | 1.2.840.1135 |
   | 84  | dsig-more#hmac-sha384         |              | 49.2.10      |
   +-----+-------------------------------+--------------+--------------+
   | HS5 | http://www.w3.org/2001/04/xml | HmacSHA512   | 1.2.840.1135 |
   | 12  | dsig-more#hmac-sha512         |              | 49.2.11      |
   +-----+-------------------------------+--------------+--------------+
   | RS2 | http://www.w3.org/2001/04/xml | SHA256withRS | 1.2.840.1135 |
   | 56  | dsig-more#rsa-sha256          | A            | 49.1.1.11    |
   +-----+-------------------------------+--------------+--------------+
   | RS3 | http://www.w3.org/2001/04/xml | SHA384withRS | 1.2.840.1135 |
   | 84  | dsig-more#rsa-sha384          | A            | 49.1.1.12    |
   +-----+-------------------------------+--------------+--------------+
   | RS5 | http://www.w3.org/2001/04/xml | SHA512withRS | 1.2.840.1135 |
   | 12  | dsig-more#rsa-sha512          | A            | 49.1.1.13    |
   +-----+-------------------------------+--------------+--------------+
   | ES2 | http://www.w3.org/2001/04/xml | SHA256withEC | 1.2.840.1004 |
   | 56  | dsig-more#ecdsa-sha256        | DSA          | 5.4.3.2      |
   +-----+-------------------------------+--------------+--------------+
   | ES3 | http://www.w3.org/2001/04/xml | SHA384withEC | 1.2.840.1004 |
   | 84  | dsig-more#ecdsa-sha384        | DSA          | 5.4.3.3      |
   +-----+-------------------------------+--------------+--------------+
   | ES5 | http://www.w3.org/2001/04/xml | SHA512withEC | 1.2.840.1004 |
   | 12  | dsig-more#ecdsa-sha512        | DSA          | 5.4.3.4      |
   +-----+-------------------------------+--------------+--------------+
   | PS2 | http://www.w3.org/2007/05/xml | SHA256withRS | 1.2.840.1135 |
   | 56  | dsig-more#sha256-rsa-MGF1     | AandMGF1     | 49.1.1.10    |
   +-----+-------------------------------+--------------+--------------+
   | PS3 | http://www.w3.org/2007/05/xml | SHA384withRS | 1.2.840.1135 |
   | 84  | dsig-more#sha384-rsa-MGF1     | AandMGF1     | 49.1.1.10    |
   +-----+-------------------------------+--------------+--------------+
   | PS5 | http://www.w3.org/2007/05/xml | SHA512withRS | 1.2.840.1135 |
   | 12  | dsig-more#sha512-rsa-MGF1     | AandMGF1     | 49.1.1.10    |
   +-----+-------------------------------+--------------+--------------+

(draft20)
