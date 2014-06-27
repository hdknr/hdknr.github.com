C.2.  JOSE Header
------------------------

The following example JWE Protected Header declares that:

   o  the Content Encryption Key is encrypted to the recipient using the
      PSE2-HS256+A128KW algorithm to produce the JWE Encrypted Key,

   o  the Salt (p2s) is [ 217, 96, 147, 112, 150, 117, 70, 247, 127, 8,
      155, 137, 174, 42, 80, 215 ],

   o  the Iteration Count (p2c) is 4096,

   o  the Plaintext is encrypted using the AES_128_CBC_HMAC_SHA_256
      algorithm to produce the Ciphertext, and

   o  the content type is application/jwk+json.

.. code-block:: javascript

     {
      "alg":"PBES2-HS256+A128KW",
      "p2s":"2WCTcJZ1Rvd_CJuJripQ1w",
      "p2c":4096,
      "enc":"A128CBC-HS256",
      "cty":"jwk+json"
     }

Encoding this :term:`JWE Protected Header` 
as BASE64URL(UTF8(JWE Protected Header)) gives this value:

::
     eyJhbGciOiJQQkVTMi1IUzI1NitBMTI4S1ciLCJwMnMiOiIyV0NUY0paMVJ2ZF9DSn
     VKcmlwUTF3IiwicDJjIjo0MDk2LCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiY3R5Ijoi
     andrK2pzb24ifQ

.. code-block:: python

    from jose import base64
    
    header = '''
    eyJhbGciOiJQQkVTMi1IUzI1NitBMTI4S1ciLCJwMnMiOiIyV0NUY0paMVJ2ZF9DSn
    VKcmlwUTF3IiwicDJjIjo0MDk2LCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiY3R5Ijoi
    andrK2pzb24ifQ
    '''.replace('\n', '')
    
    import json
    print json.dumps(
        json.loads(base64.base64url_decode(header)),
        indent=2)

(draft20)
