Appendix B. Encryption Algorithm Identifier Cross-Reference
============================================================================================

This appendix contains a table cross-referencing the ":term:`alg`"
(algorithm) and ":term:`enc`" (encryption method) values used in this
specification with the equivalent identifiers used by other standards
and software packages.  
See XML Encryption :term:`[W3C.REC-xmlenc-core-20021210]`, 
XML Encryption 1.1 :term:`[W3C.CR-xmlenc-core1-20120313]`, and 
Java Cryptography Architecture :term:`[JCA]` 
for more information about the names defined by those
documents.

For the composite algorithms "A128CBC+HS256" and "A256CBC+HS512", the
corresponding AES CBC algorithm identifiers are listed.

   +----------+--------+--------------------------+--------------------+
   | Algorith | JWE    | XML ENC                  | JCA                |
   | m        |        |                          |                    |
   +----------+--------+--------------------------+--------------------+
   | RSAES-PK | RSA1_5 | http://www.w3.org/2001/0 | RSA/ECB/PKCS1Paddi |
   | CS1-V1_5 |        | 4/xmlenc#rsa-1_5         | ng                 |
   +----------+--------+--------------------------+--------------------+
   | RSAES    | RSA-OA | http://www.w3.org/2001/0 | RSA/ECB/OAEPWithSH |
   | using    | EP     | 4/xmlenc#rsa-oaep-mgf1p  | A-1AndMGF1Padding  |
   | Optimal  |        |                          |                    |
   | Asymmetr |        |                          |                    |
   | ic       |        |                          |                    |
   |  Encrypt |        |                          |                    |
   | ion      |        |                          |                    |
   |   Paddin |        |                          |                    |
   | g (OAEP) |        |                          |                    |
   +----------+--------+--------------------------+--------------------+
   | Elliptic | ECDH-E | http://www.w3.org/2009/x |                    |
   | Curve    | S      | mlenc11#ECDH-ES          |                    |
   | Diffie-H |        |                          |                    |
   | ellman   |        |                          |                    |
   |  Ephemer |        |                          |                    |
   | alStatic |        |                          |                    |
   +----------+--------+--------------------------+--------------------+
   | Advanced | A128KW | http://www.w3.org/2001/0 |                    |
   | Encrypti |        | 4/xmlenc#kw-aes128       |                    |
   | on       |        |                          |                    |
   |  Standar |        |                          |                    |
   | d(AES)   |        |                          |                    |
   |  Key Wra |        |                          |                    |
   | pAlgorit |        |                          |                    |
   | hmusing  |        |                          |                    |
   |   128 bi |        |                          |                    |
   | t keys   |        |                          |                    |
   +----------+--------+--------------------------+--------------------+
   | AES Key  | A256KW | http://www.w3.org/2001/0 |                    |
   | Wrap     |        | 4/xmlenc#kw-aes256       |                    |
   | Algorith |        |                          |                    |
   | musing   |        |                          |                    |
   |  256 bit |        |                          |                    |
   |  keys    |        |                          |                    |
   +----------+--------+--------------------------+--------------------+
   | AES in   | A128CB | http://www.w3.org/2001/0 | AES/CBC/PKCS5Paddi |
   | Cipher   | C+HS25 | 4/xmlenc#aes128-cbc      | ng                 |
   | Block    | 6      |                          |                    |
   | Chaining |        |                          |                    |
   | (CBC)    |        |                          |                    |
   | mode     |        |                          |                    |
   | with     |        |                          |                    |
   | PKCS #5  |        |                          |                    |
   | padding  |        |                          |                    |
   | using    |        |                          |                    |
   | 128 bit  |        |                          |                    |
   | keys     |        |                          |                    |
   +----------+--------+--------------------------+--------------------+
   | AES in   | A256CB | http://www.w3.org/2001/0 | AES/CBC/PKCS5Paddi |
   | CBC mode | C+HS51 | 4/xmlenc#aes256-cbc      | ng                 |
   | with     | 2      |                          |                    |
   | PKCS #5  |        |                          |                    |
   | padding  |        |                          |                    |
   | using    |        |                          |                    |
   | 256 bit  |        |                          |                    |
   | keys     |        |                          |                    |
   +----------+--------+--------------------------+--------------------+
   | AES in   | A128GC | http://www.w3.org/2009/x | AES/GCM/NoPadding  |
   | Galois/C | M      | mlenc11#aes128-gcm       |                    |
   | ounter   |        |                          |                    |
   |  Mode    |        |                          |                    |
   |  (GCM)   |        |                          |                    |
   |  using   |        |                          |                    |
   |  128 bit |        |                          |                    |
   |  keys    |        |                          |                    |
   +----------+--------+--------------------------+--------------------+
   | AES GCM  | A256GC | http://www.w3.org/2009/x | AES/GCM/NoPadding  |
   | using    | M      | mlenc11#aes256-gcm       |                    |
   | 256 bit  |        |                          |                    |
   | keys     |        |                          |                    |
   +----------+--------+--------------------------+--------------------+


(draft 06, http://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-06#appendix-B )
