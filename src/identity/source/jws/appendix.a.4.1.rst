A.4.1.  Encoding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The JWS Protected Header for this example differs from the previous
example because different ECDSA curves and hash functions are used.
The JWS Protected Header used is:

.. code-block:: javascript

  {"alg":"ES512"}

The octets representing UTF8(JWS Protected Header) in this case are:

::

    [123, 34, 97, 108, 103, 34, 58, 34, 69, 83, 53, 49, 50, 34, 125]

Encoding this JWS Protected Header as BASE64URL(UTF8(JWS Protected
Header)) gives this value:

::

    eyJhbGciOiJFUzUxMiJ9

The JWS Payload used in this example, is the ASCII string "Payload".
The representation of this string is the octet sequence:

::
    
    [80, 97, 121, 108, 111, 97, 100]

Encoding this JWS Payload as BASE64URL(JWS Payload) gives this value:

::

  UGF5bG9hZA

Combining these as BASE64URL(UTF8(JWS Protected Header)) || '.' ||
BASE64URL(JWS Payload) gives this string (with line breaks for
display purposes only):

::

  eyJhbGciOiJFUzUxMiJ9.UGF5bG9hZA

The resulting JWS Signing Input value, which is the ASCII
representation of above string, is the following octet sequence:

::

    [101, 121, 74, 104, 98, 71, 99, 105, 79, 105, 74, 70, 85, 122, 85,
    120, 77, 105, 74, 57, 46, 85, 71, 70, 53, 98, 71, 57, 104, 90, 65]

This example uses the elliptic curve key represented in JSON Web Key
[JWK] format below (with line breaks for display purposes only):

::

  {"kty":"EC",
   "crv":"P-521",
   "x":"AekpBQ8ST8a8VcfVOTNl353vSrDCLLJXmPk06wTjxrrjcBpXp5EOnYG_
        NjFZ6OvLFV1jSfS9tsz4qUxcWceqwQGk",
   "y":"ADSmRA43Z1DSNx_RvcLI87cdL07l6jQyyBXMoxVg_l2Th-x3S1WDhjDl
        y79ajL4Kkd0AZMaZmh9ubmf63e3kyMj2",
   "d":"AY5pb7A0UFiB3RELSD64fTLOSV_jazdF7fLYyuTw8lOfRhWg6Y6rUrPA
        xerEzgdRhajnu0ferB0d53vM9mE15j2C"
  }

The ECDSA private part **d** is then passed 
to an ECDSA signing function,
which also takes the curve type, P-521, 
the hash type, SHA-512, and
the JWS Signing Input as inputs.  

The result of the digital signature
is the EC point (R, S), 
where R and S are unsigned integers.  

In this example, 

the R and S values, given as octet sequences representing
big endian integers are:

+--------+----------------------------------------------------------+
| Result | Value                                                    |
| Name   |                                                          |
+--------+----------------------------------------------------------+
| R      | [1, 220, 12, 129, 231, 171, 194, 209, 232, 135, 233,     |
|        | 117, 247, 105, 122, 210, 26, 125, 192, 1, 217, 21, 82,   |
|        | 91, 45, 240, 255, 83, 19, 34, 239, 71, 48, 157, 147,     |
|        | 152, 105, 18, 53, 108, 163, 214, 68, 231, 62, 153, 150,  |
|        | 106, 194, 164, 246, 72, 143, 138, 24, 50, 129, 223, 133, |
|        | 206, 209, 172, 63, 237, 119, 109]                        |
+--------+----------------------------------------------------------+
| S      | [0, 111, 6, 105, 44, 5, 41, 208, 128, 61, 152, 40, 92,   |
|        | 61, 152, 4, 150, 66, 60, 69, 247, 196, 170, 81, 193,     |
|        | 199, 78, 59, 194, 169, 16, 124, 9, 143, 42, 142, 131,    |
|        | 48, 206, 238, 34, 175, 83, 203, 220, 159, 3, 107, 155,   |
|        | 22, 27, 73, 111, 68, 68, 21, 238, 144, 229, 232, 148,    |
|        | 188, 222, 59, 242, 103]                                  |
+--------+----------------------------------------------------------+

The JWS Signature is the value R || S. Encoding the signature as
BASE64URL(JWS Signature) produces this value (with line breaks for
display purposes only):

::

  AdwMgeerwtHoh-l192l60hp9wAHZFVJbLfD_UxMi70cwnZOYaRI1bKPWROc-mZZq
  wqT2SI-KGDKB34XO0aw_7XdtAG8GaSwFKdCAPZgoXD2YBJZCPEX3xKpRwcdOO8Kp
  EHwJjyqOgzDO7iKvU8vcnwNrmxYbSW9ERBXukOXolLzeO_Jn

Concatenating these values in the order Header.Payload.Signature with
period ('.') characters between the parts yields this complete JWS
representation using the JWS Compact Serialization (with line breaks
for display purposes only):

::

  eyJhbGciOiJFUzUxMiJ9
  .
  UGF5bG9hZA
  .
  AdwMgeerwtHoh-l192l60hp9wAHZFVJbLfD_UxMi70cwnZOYaRI1bKPWROc-mZZq
  wqT2SI-KGDKB34XO0aw_7XdtAG8GaSwFKdCAPZgoXD2YBJZCPEX3xKpRwcdOO8Kp
  EHwJjyqOgzDO7iKvU8vcnwNrmxYbSW9ERBXukOXolLzeO_Jn

