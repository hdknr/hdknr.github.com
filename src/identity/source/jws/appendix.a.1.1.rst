A.1.1.  Encoding
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following example :term:`JWS Header` declares 
that the data structure is a JSON Web Token (JWT) [JWT] 
and the :term:`JWS Signing Input` is signed using the HMAC SHA-256 algorithm. 
Note that 
white space is explicitly allowed in :term:`JWS Header strings` 
and no canonicalization is performed before encoding.

::

    {"typ":"JWT",
     "alg":"HS256"}

The following byte array contains the UTF-8 characters for the JWS Header:

:: 
    [123, 34, 116, 121, 112, 34, 58, 34, 74, 87, 84, 34, 44, 13, 10, 32, 34, 97, 108, 103, 34, 58, 34, 72, 83, 50, 53, 54, 34, 125]

Base64url encoding this UTF-8 representation yields this Encoded JWS Header value:

::

    eyJ0eXAiOiJKV1QiLA0KICJhbGciOiJIUzI1NiJ9

The JWS Payload used in this example follows. (Note that the payload can be any base64url encoded content, and need not be a base64url encoded JSON object.)

::

    {"iss":"joe",
     "exp":1300819380,
     "http://example.com/is_root":true}
    
The following byte array contains the UTF-8 characters for the JWS Payload:

::
    [123, 34, 105, 115, 115, 34, 58, 34, 106, 111, 101, 34, 44, 13, 10, 32, 34, 101, 120, 112, 34, 58, 49, 51, 48, 48, 56, 49, 57, 51, 56, 48, 44, 13, 10, 32, 34, 104, 116, 116, 112, 58, 47, 47, 101, 120, 97, 109, 112, 108, 101, 46, 99, 111, 109, 47, 105, 115, 95, 114, 111, 111, 116, 34, 58, 116, 114, 117, 101, 125]

Base64url encoding the above yields the Encoded JWS Payload value:

::

    eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlfQ

Concatenating the Encoded JWS Header, a period character, and the Encoded JWS Payload yields this JWS Signing Input value (with line breaks for display purposes only):

:: 

    eyJ0eXAiOiJKV1QiLA0KICJhbGciOiJIUzI1NiJ9
    .
    eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlfQ


The UTF-8 representation of the JWS Signing Input is the following byte array:

::

    [101, 121, 74, 48, 101, 88, 65, 105, 79, 105, 74, 75, 86, 49, 81, 105, 76, 65, 48, 75, 73, 67, 74, 104, 98, 71, 99, 105, 79, 105, 74, 73, 85, 122, 73, 49, 78, 105, 74, 57, 46, 101, 121, 74, 112, 99, 51, 77, 105, 79, 105, 74, 113, 98, 50, 85, 105, 76, 65, 48, 75, 73, 67, 74, 108, 101, 72, 65, 105, 79, 106, 69, 122, 77, 68, 65, 52, 77, 84, 107, 122, 79, 68, 65, 115, 68, 81, 111, 103, 73, 109, 104, 48, 100, 72, 65, 54, 76, 121, 57, 108, 101, 71, 70, 116, 99, 71, 120, 108, 76, 109, 78, 118, 98, 83, 57, 112, 99, 49, 57, 121, 98, 50, 57, 48, 73, 106, 112, 48, 99, 110, 86, 108, 102, 81]

HMACs are generated using keys. This example uses the key represented by the following byte array:

:: 

    [3, 35, 53, 75, 43, 15, 165, 188, 131, 126, 6, 101, 119, 123, 166, 143, 90, 179, 40, 230, 240, 84, 201, 40, 169, 15, 132, 178, 210, 80, 46, 191, 211, 251, 90, 146, 210, 6, 71, 239, 150, 138, 180, 195, 119, 98, 61, 34, 61, 46, 33, 114, 5, 46, 79, 8, 192, 205, 154, 245, 103, 208, 128, 163]

Running the HMAC SHA-256 algorithm on the UTF-8 representation of the JWS Signing Input with this key yields the following byte array:

::
    
    [116, 24, 223, 180, 151, 153, 224, 37, 79, 250, 96, 125, 216, 173, 187, 186, 22, 212, 37, 77, 105, 214, 191, 240, 91, 88, 5, 88, 83, 132, 141, 121]

Base64url encoding the above HMAC output yields the Encoded JWS Signature value:

:: 

    dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk

(v.03)

