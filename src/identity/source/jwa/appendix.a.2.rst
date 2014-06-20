A.2. Key Management Algorithm Identifier Cross-Reference
------------------------------------------------------------------

This section contains a table cross-referencing the JWE "alg"
(algorithm) values defined in this specification with the equivalent
identifiers used by other standards and software packages.

+-------+------------------------+--------------------+-------------+
| JWE   | XML ENC                | JCA                | OID         |
+-------+------------------------+--------------------+-------------+
| RSA1_ | http://www.w3.org/2001 | RSA/ECB/PKCS1Paddi | 1.2.840.113 |
| 5     | /04/xmlenc#rsa-1_5     | ng                 | 549.1.1.1   |
+-------+------------------------+--------------------+-------------+
| RSA-O | http://www.w3.org/2001 | RSA/ECB/OAEPWithSH | 1.2.840.113 |
| AEP   | /04/xmlenc#rsa-oaep-mg | A-1AndMGF1Padding  | 549.1.1.7   |
|       | f1p                    |                    |             |
+-------+------------------------+--------------------+-------------+
| RSA-O | http://www.w3.org/2009 | RSA/ECB/OAEPWithSH | 1.2.840.113 |
| AEP-2 | /xmlenc11#rsa-oaep &   | A-256AndMGF1Paddin | 549.1.1.7   |
| 56    |  http://www.w3.org/200 | g&                 |             |
|       | 9/xmlenc11#mgf1sha256  |  MGF1ParameterSpec |             |
|       |                        | .SHA256            |             |
+-------+------------------------+--------------------+-------------+
| ECDH- | http://www.w3.org/2009 | ECDH               | 1.3.132.1.1 |
| ES    | /xmlenc11#ECDH-ES      |                    | 2           |
+-------+------------------------+--------------------+-------------+
| A128K | http://www.w3.org/2001 | AESWrap            | 2.16.840.1. |
| W     | /04/xmlenc#kw-aes128   |                    | 101.3.4.1.5 |
+-------+------------------------+--------------------+-------------+
| A192K | http://www.w3.org/2001 | AESWrap            | 2.16.840.1. |
| W     | /04/xmlenc#kw-aes192   |                    | 101.3.4.1.2 |
|       |                        |                    | 5           |
+-------+------------------------+--------------------+-------------+
| A256K | http://www.w3.org/2001 | AESWrap            | 2.16.840.1. |
| W     | /04/xmlenc#kw-aes256   |                    | 101.3.4.1.4 |
|       |                        |                    | 5           |
+-------+------------------------+--------------------+-------------+

(draft27)
