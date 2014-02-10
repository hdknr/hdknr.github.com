A.2. Key Management Algorithm Identifier Cross-Reference
------------------------------------------------------------------


This section contains a table cross-referencing the JWE "alg"
(algorithm) values defined in this specification with the equivalent
identifiers used by other standards and software packages.

   +------+------------------------+--------------------+--------------+
   | JWE  | XML ENC                | JCA                | OID          |
   +------+------------------------+--------------------+--------------+
   | RSA1 | http://www.w3.org/2001 | RSA/ECB/PKCS1Paddi | 1.2.840.1135 |
   | _5   | /04/xmlenc#rsa-1_5     | ng                 | 49.1.1.1     |
   +------+------------------------+--------------------+--------------+
   | RSA- | http://www.w3.org/2001 | RSA/ECB/OAEPWithSH | 1.2.840.1135 |
   | OAEP | /04/xmlenc#rsa-oaep-mg | A-1AndMGF1Padding  | 49.1.1.7     |
   |      | f1p                    |                    |              |
   +------+------------------------+--------------------+--------------+
   | ECDH | http://www.w3.org/2009 |                    | 1.3.132.1.12 |
   | -ES  | /xmlenc11#ECDH-ES      |                    |              |
   +------+------------------------+--------------------+--------------+
   | A128 | http://www.w3.org/2001 |                    | 2.16.840.1.1 |
   | KW   | /04/xmlenc#kw-aes128   |                    | 01.3.4.1.5   |
   +------+------------------------+--------------------+--------------+
   | A192 | http://www.w3.org/2001 |                    | 2.16.840.1.1 |
   | KW   | /04/xmlenc#kw-aes192   |                    | 01.3.4.1.25  |
   +------+------------------------+--------------------+--------------+
   | A256 | http://www.w3.org/2001 |                    | 2.16.840.1.1 |
   | KW   | /04/xmlenc#kw-aes256   |                    | 01.3.4.1.45  |
   +------+------------------------+--------------------+--------------+


(draft20)

