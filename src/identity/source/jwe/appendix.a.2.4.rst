A.2.4. Key Encryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encrypt the CEK with the recipient's public key 
using the RSAES-PKCS1-V1_5 algorithm to produce the JWE Encrypted Key. 

.. note::
    - 相手の公開鍵を使ってCEKを非対称暗号化
    - RSA AES PKCS1 v.1.5 

This example uses the RSA key represented in JSON Web Key [JWK] format below 
(with line breaks for display purposes only):

.. code-block:: javascript

     {"kty":"RSA",
      "n":"sXchDaQebHnPiGvyDOAT4saGEUetSyo9MKLOoWFsueri23bOdgWp4Dy1Wl
           UzewbgBHod5pcM9H95GQRV3JDXboIRROSBigeC5yjU1hGzHHyXss8UDpre
           cbAYxknTcQkhslANGRUZmdTOQ5qTRsLAt6BTYuyvVRdhS8exSZEy_c4gs_
           7svlJJQ4H9_NxsiIoLwAEk7-Q3UXERGYw_75IDrGA84-lA_-Ct4eTlXHBI
           Y2EaV7t7LjJaynVJCpkv4LKjTTAumiGUIuQhrNhZLuF_RJLqHpM2kgWFLU
           7-VTdL1VbC2tejvcI2BlMkEpk1BzBZI0KQB0GaDWFLN-aEAw3vRw",
      "e":"AQAB",
      "d":"VFCWOqXr8nvZNyaaJLXdnNPXZKRaWCjkU5Q2egQQpTBMwhprMzWzpR8Sxq
           1OPThh_J6MUD8Z35wky9b8eEO0pwNS8xlh1lOFRRBoNqDIKVOku0aZb-ry
           nq8cxjDTLZQ6Fz7jSjR1Klop-YKaUHc9GsEofQqYruPhzSA-QgajZGPbE_
           0ZaVDJHfyd7UUBUKunFMScbflYAAOYJqVIVwaYR5zWEEceUjNnTNo_CVSj
           -VvXLO5VZfCUAVLgW4dpf1SrtZjSt34YLsRarSb127reG_DUwg9Ch-Kyvj
           T1SkHgUWRVGcyly7uvVGRSDwsXypdrNinPA4jlhoNdizK2zF2CWQ"
     }

The resulting JWE Encrypted Key value is:

.. code-block:: javascript 

   [80, 104, 72, 58, 11, 130, 236, 139, 132, 189, 255, 205, 61, 86, 151,
   176, 99, 40, 44, 233, 176, 189, 205, 70, 202, 169, 72, 40, 226, 181,
   156, 223, 120, 156, 115, 232, 150, 209, 145, 133, 104, 112, 237, 156,
   116, 250, 65, 102, 212, 210, 103, 240, 177, 61, 93, 40, 71, 231, 223,
   226, 240, 157, 15, 31, 150, 89, 200, 215, 198, 203, 108, 70, 117, 66,
   212, 238, 193, 205, 23, 161, 169, 218, 243, 203, 128, 214, 127, 253,
   215, 139, 43, 17, 135, 103, 179, 220, 28, 2, 212, 206, 131, 158, 128,
   66, 62, 240, 78, 186, 141, 125, 132, 227, 60, 137, 43, 31, 152, 199,
   54, 72, 34, 212, 115, 11, 152, 101, 70, 42, 219, 233, 142, 66, 151,
   250, 126, 146, 141, 216, 190, 73, 50, 177, 146, 5, 52, 247, 28, 197,
   21, 59, 170, 247, 181, 89, 131, 241, 169, 182, 246, 99, 15, 36, 102,
   166, 182, 172, 197, 136, 230, 120, 60, 58, 219, 243, 149, 94, 222,
   150, 154, 194, 110, 227, 225, 112, 39, 89, 233, 112, 207, 211, 241,
   124, 174, 69, 221, 179, 107, 196, 225, 127, 167, 112, 226, 12, 242,
   16, 24, 28, 120, 182, 244, 213, 244, 153, 194, 162, 69, 160, 244,
   248, 63, 165, 141, 4, 207, 249, 193, 79, 131, 0, 169, 233, 127, 167,
   101, 151, 125, 56, 112, 111, 248, 29, 232, 90, 29, 147, 110, 169,
   146, 114, 165, 204, 71, 136, 41, 252]

( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-13#appendix-A.2.4 )
