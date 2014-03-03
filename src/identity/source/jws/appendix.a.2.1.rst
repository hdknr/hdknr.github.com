A.2.1.  Encoding
^^^^^^^^^^^^^^^^^^^^^^^^

The JWS Protected Header in this example is different 
from the previous example in two ways: 

First, 
because a different algorithm is being used, 
the "alg" value is different.  

Second, 
for illustration purposes only, 
the optional "typ" parameter is not used.  
(This difference is not related to the algorithm employed.)  

The JWS Protected Header used is:

.. code-block:: javascript

  {"alg":"RS256"}

The octets representing UTF8(JWS Protected Header) in this case are:

::

    [123, 34, 97, 108, 103, 34, 58, 34, 82, 83, 50, 53, 54, 34, 125]

.. code-block:: python

    >>> [ ord(i) for i in '{"alg":"RS256"}' ]

    [123, 34, 97, 108, 103, 34, 58, 34, 82, 83, 50, 53, 54, 34, 125]

Encoding this JWS Protected Header 
as BASE64URL(UTF8(JWS Protected Header)) gives this value:

::

    eyJhbGciOiJSUzI1NiJ9

.. code-block:: python

    >>> form jose import base64
    >>> base64.base64url_encode('{"alg":"RS256"}')
    'eyJhbGciOiJSUzI1NiJ9'

The JWS Payload used in this example, which follows, 
is the same as in the previous example.  

Since the BASE64URL(JWS Payload) value will
therefore be the same, 
its computation is not repeated here.

.. code-block:: javascript

  {"iss":"joe",
   "exp":1300819380,
   "http://example.com/is_root":true}

Combining these as 
BASE64URL(UTF8(JWS Protected Header)) || '.' || BASE64URL(JWS Payload) 
gives this string (with line breaks for display purposes only):

::

  eyJhbGciOiJSUzI1NiJ9
  .
  eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFt
  cGxlLmNvbS9pc19yb290Ijp0cnVlfQ

The resulting JWS Signing Input value, which is the ASCII
representation of above string, is the following octet sequence:

:: 

    [101, 121, 74, 104, 98, 71, 99, 105, 79, 105, 74, 83, 85, 122, 73,
    49, 78, 105, 74, 57, 46, 101, 121, 74, 112, 99, 51, 77, 105, 79, 105,
    74, 113, 98, 50, 85, 105, 76, 65, 48, 75, 73, 67, 74, 108, 101, 72,
    65, 105, 79, 106, 69, 122, 77, 68, 65, 52, 77, 84, 107, 122, 79, 68,
    65, 115, 68, 81, 111, 103, 73, 109, 104, 48, 100, 72, 65, 54, 76,
    121, 57, 108, 101, 71, 70, 116, 99, 71, 120, 108, 76, 109, 78, 118,
    98, 83, 57, 112, 99, 49, 57, 121, 98, 50, 57, 48, 73, 106, 112, 48,
    99, 110, 86, 108, 102, 81]

This example uses the RSA key represented in JSON Web Key [JWK]
format below (with line breaks for display purposes only):

::

  {"kty":"RSA",
   "n":"ofgWCuLjybRlzo0tZWJjNiuSfb4p4fAkd_wWJcyQoTbji9k0l8W26mPddx
        HmfHQp-Vaw-4qPCJrcS2mJPMEzP1Pt0Bm4d4QlL-yRT-SFd2lZS-pCgNMs
        D1W_YpRPEwOWvG6b32690r2jZ47soMZo9wGzjb_7OMg0LOL-bSf63kpaSH
        SXndS5z5rexMdbBYUsLA9e-KXBdQOS-UTo7WTBEMa2R2CapHg665xsmtdV
        MTBQY4uDZlxvb3qCo5ZwKh9kG4LT6_I5IhlJH7aGhyxXFvUK-DWNmoudF8
        NAco9_h9iaGNj8q2ethFkMLs91kzk2PAcDTW9gb54h4FRWyuXpoQ",
   "e":"AQAB",
   "d":"Eq5xpGnNCivDflJsRQBXHx1hdR1k6Ulwe2JZD50LpXyWPEAeP88vLNO97I
        jlA7_GQ5sLKMgvfTeXZx9SE-7YwVol2NXOoAJe46sui395IW_GO-pWJ1O0
        BkTGoVEn2bKVRUCgu-GjBVaYLU6f3l9kJfFNS3E0QbVdxzubSu3Mkqzjkn
        439X0M_V51gfpRLI9JYanrC4D4qAdGcopV_0ZHHzQlBjudU2QvXt4ehNYT
        CBr6XCLQUShb1juUO1ZdiYoFaFQT5Tw8bGUl_x_jTj3ccPDVZFD9pIuhLh
        BOneufuBiB4cS98l2SR_RQyGWSeWjnczT0QU91p1DhOVRuOopznQ"
  }

The RSA private key is then passed to the RSA signing function, which
also takes the hash type, SHA-256, and the JWS Signing Input as
inputs.  The result of the digital signature is an octet sequence,
which represents a big endian integer.  In this example, it is:

::

    [112, 46, 33, 137, 67, 232, 143, 209, 30, 181, 216, 45, 191, 120, 69,
    243, 65, 6, 174, 27, 129, 255, 247, 115, 17, 22, 173, 209, 113, 125,
    131, 101, 109, 66, 10, 253, 60, 150, 238, 221, 115, 162, 102, 62, 81,
    102, 104, 123, 0, 11, 135, 34, 110, 1, 135, 237, 16, 115, 249, 69,
    229, 130, 173, 252, 239, 22, 216, 90, 121, 142, 232, 198, 109, 219,
    61, 184, 151, 91, 23, 208, 148, 2, 190, 237, 213, 217, 217, 112, 7,
    16, 141, 178, 129, 96, 213, 248, 4, 12, 167, 68, 87, 98, 184, 31,
    190, 127, 249, 217, 46, 10, 231, 111, 36, 242, 91, 51, 187, 230, 244,
    74, 230, 30, 177, 4, 10, 203, 32, 4, 77, 62, 249, 18, 142, 212, 1,
    48, 121, 91, 212, 189, 59, 65, 238, 202, 208, 102, 171, 101, 25, 129,
    253, 228, 141, 247, 127, 55, 45, 195, 139, 159, 175, 221, 59, 239,
    177, 139, 93, 163, 204, 60, 46, 176, 47, 158, 58, 65, 214, 18, 202,
    173, 21, 145, 18, 115, 160, 95, 35, 185, 232, 56, 250, 175, 132, 157,
    105, 132, 41, 239, 90, 30, 136, 121, 130, 54, 195, 212, 14, 96, 69,
    34, 165, 68, 200, 242, 122, 122, 45, 184, 6, 99, 209, 108, 247, 202,
    234, 86, 222, 64, 92, 178, 33, 90, 69, 178, 194, 85, 102, 181, 90,
    193, 167, 72, 160, 112, 223, 200, 163, 42, 70, 149, 67, 208, 25, 238,
    251, 71]

Encoding the signature as BASE64URL(JWS Signature) produces this
value (with line breaks for display purposes only):

::

  cC4hiUPoj9Eetdgtv3hF80EGrhuB__dzERat0XF9g2VtQgr9PJbu3XOiZj5RZmh7
  AAuHIm4Bh-0Qc_lF5YKt_O8W2Fp5jujGbds9uJdbF9CUAr7t1dnZcAcQjbKBYNX4
  BAynRFdiuB--f_nZLgrnbyTyWzO75vRK5h6xBArLIARNPvkSjtQBMHlb1L07Qe7K
  0GarZRmB_eSN9383LcOLn6_dO--xi12jzDwusC-eOkHWEsqtFZESc6BfI7noOPqv
  hJ1phCnvWh6IeYI2w9QOYEUipUTI8np6LbgGY9Fs98rqVt5AXLIhWkWywlVmtVrB
  p0igcN_IoypGlUPQGe77Rw

Concatenating these values in the order Header.Payload.Signature with
period ('.') characters between the parts yields this complete JWS
representation using the JWS Compact Serialization (with line breaks
for display purposes only):

::

  eyJhbGciOiJSUzI1NiJ9
  .
  eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFt
  cGxlLmNvbS9pc19yb290Ijp0cnVlfQ
  .
  cC4hiUPoj9Eetdgtv3hF80EGrhuB__dzERat0XF9g2VtQgr9PJbu3XOiZj5RZmh7
  AAuHIm4Bh-0Qc_lF5YKt_O8W2Fp5jujGbds9uJdbF9CUAr7t1dnZcAcQjbKBYNX4
  BAynRFdiuB--f_nZLgrnbyTyWzO75vRK5h6xBArLIARNPvkSjtQBMHlb1L07Qe7K
  0GarZRmB_eSN9383LcOLn6_dO--xi12jzDwusC-eOkHWEsqtFZESc6BfI7noOPqv
  hJ1phCnvWh6IeYI2w9QOYEUipUTI8np6LbgGY9Fs98rqVt5AXLIhWkWywlVmtVrB
  p0igcN_IoypGlUPQGe77Rw

(draft20)
