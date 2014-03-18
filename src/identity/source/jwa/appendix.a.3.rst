A.3. Content Encryption Algorithm Identifier Cross-Reference
---------------------------------------------------------------------


This section contains a table cross-referencing the JWE "enc"
(encryption algorithm) values defined in this specification with the
equivalent identifiers used by other standards and software packages.

For the composite algorithms 
":ref:`A128CBC-HS256`", 
":ref:`A192CBC-HS384`", and
":ref:`A256CBC-HS512`", 
the corresponding AES CBC algorithm identifiers are listed.

+---------+-------------------------+--------------+----------------+
| JWE     | XML ENC                 | JCA          | OID            |
+---------+-------------------------+--------------+----------------+
| A128CBC | http://www.w3.org/2001/ | AES/CBC/PKCS | 2.16.840.1.101 |
| -HS256  | 04/xmlenc#aes128-cbc    | 5Padding     | .3.4.1.2       |
+---------+-------------------------+--------------+----------------+
| A192CBC | http://www.w3.org/2001/ | AES/CBC/PKCS | 2.16.840.1.101 |
| -HS384  | 04/xmlenc#aes192-cbc    | 5Padding     | .3.4.1.22      |
+---------+-------------------------+--------------+----------------+
| A256CBC | http://www.w3.org/2001/ | AES/CBC/PKCS | 2.16.840.1.101 |
| -HS512  | 04/xmlenc#aes256-cbc    | 5Padding     | .3.4.1.42      |
+---------+-------------------------+--------------+----------------+
| A128GCM | http://www.w3.org/2009/ | AES/GCM/NoPa | 2.16.840.1.101 |
|         | xmlenc11#aes128-gcm     | dding        | .3.4.1.6       |
+---------+-------------------------+--------------+----------------+
| A192GCM | http://www.w3.org/2009/ | AES/GCM/NoPa | 2.16.840.1.101 |
|         | xmlenc11#aes192-gcm     | dding        | .3.4.1.26      |
+---------+-------------------------+--------------+----------------+
| A256GCM | http://www.w3.org/2009/ | AES/GCM/NoPa | 2.16.840.1.101 |
|         | xmlenc11#aes256-gcm     | dding        | .3.4.1.46      |
+---------+-------------------------+--------------+----------------+


(draft23)
