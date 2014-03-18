A.3.3.  Key Encryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encrypt the CEK with the shared symmetric key 
using the AES Key Wrap algorithm 
to produce the JWE Encrypted Key. 

This example uses the symmetric key represented 
in JSON Web Key [JWK] format below:

.. code-block:: javascript

     {"kty":"oct",
      "k":"GawgguFyGrWKav7AX4VKUg"
     }

The resulting JWE Encrypted Key value is:

::

   [232, 160, 123, 211, 183, 76, 245, 132, 200, 128, 123, 75, 190, 216,
   22, 67, 201, 138, 193, 186, 9, 91, 122, 31, 246, 90, 28, 139, 57, 3,
   76, 124, 193, 11, 98, 37, 173, 61, 104, 57]

Encoding this JWE Encrypted Key as BASE64URL(JWE Encrypted Key) gives
this value:

::

     6KB707dM9YTIgHtLvtgWQ8mKwboJW3of9locizkDTHzBC2IlrT1oOQ

(draft23)


Python
~~~~~~~~~~~~~~~~~~

- https://gist.github.com/doublereedkurt/4243633
- :rfc:`3394`

.. code-block:: python

    from jose.jwk import Jwk
    from jose.utils import base64

    jstr = '''
    {"kty":"oct",
          "k":"GawgguFyGrWKav7AX4VKUg"
               }
    '''
    jwk = Jwk.from_json(jstr)
    assert jwk.kty.value == 'oct'
    assert jwk.k == "GawgguFyGrWKav7AX4VKUg"

    cek = ''.join(chr(i) for i in [
        4, 211, 31, 197, 84, 157, 252, 254, 11, 100, 157, 250, 63, 170, 106,
        206, 107, 124, 212, 45, 111, 107, 9, 219, 200, 177, 0, 240, 143, 156,
        44, 207])

    key = base64.base64url_decode(jwk.k)
    assert len(key) == 16

    wkey1 = aes_wrap_key(key, cek)
    assert cek == aes_unwrap_key(key, wkey1)

    wkey2 = aes_wrap_key(key, cek)
    assert cek == aes_unwrap_key(key, wkey2)

    assert wkey1 == wkey2

    jwe_encrypted_key = [
        232, 160, 123, 211, 183, 76, 245, 132, 200, 128, 123, 75, 190, 216,
        22, 67, 201, 138, 193, 186, 9, 91, 122, 31, 246, 90, 28, 139, 57, 3,
        76, 124, 193, 11, 98, 37, 173, 61, 104, 57]

    assert jwe_encrypted_key == [ord(i) for i in wkey1]

