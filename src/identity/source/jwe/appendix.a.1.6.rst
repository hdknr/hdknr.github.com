A.1.6.  Content Encryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encrypt the Plaintext with AES GCM using 
the CEK as the encryption key, 
the JWE Initialization Vector, and the 
Additional Authenticated Data value above, 
requesting a 128 bit Authentication Tag output.

The resulting Ciphertext is:

::

   [229, 236, 166, 241, 53, 191, 115, 196, 174, 43, 73, 109, 39, 122,
   233, 96, 140, 206, 120, 52, 51, 237, 48, 11, 190, 219, 186, 80, 111,
   104, 50, 142, 47, 167, 59, 61, 181, 127, 196, 21, 40, 82, 242, 32,
   123, 143, 168, 226, 73, 216, 176, 144, 138, 247, 106, 60, 16, 205,
   160, 109, 64, 63, 192]


The resulting Authentication Tag value is:

::

   [92, 80, 104, 49, 133, 25, 161, 215, 173, 101, 219, 211, 136, 91,
   210, 145]

Encoding this JWE Ciphertext as BASE64URL(JWE Ciphertext) 
gives this value (with line breaks for display purposes only):

::

     5eym8TW_c8SuK0ltJ3rpYIzOeDQz7TALvtu6UG9oMo4vpzs9tX_EFShS8iB7j6ji
     SdiwkIr3ajwQzaBtQD_A

Encoding this JWE Authentication Tag 
as BASE64URL(JWE Authentication Tag) gives this value:

::

     XFBoMYUZodetZdvTiFvSkQ

(draft23)

