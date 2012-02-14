A.3.1.  Encoding
^^^^^^^^^^^^^^^^^^^^^^^^

The :term:`JWS Header` for this example 
differs from the previous example because a different algorithm is being used. 
The :term:`JWS Header` used is:

::

    {"alg":"ES256"}

The following byte array contains the UTF-8 characters for the JWS Header:

::

    [123, 34, 97, 108, 103, 34, 58, 34, 69, 83, 50, 53, 54, 34, 125]

Base64url encoding this UTF-8 representation yields this Encoded JWS Header value:

::

    eyJhbGciOiJFUzI1NiJ9

The JWS Payload used in this example, which follows, is the same as in the previous examples. Since the Encoded JWS Payload will therefore be the same, its computation is not repeated here.


::

    {"iss":"joe",
     "exp":1300819380,
     "http://example.com/is_root":true}

Concatenating the Encoded JWS Header, a period character, and the Encoded JWS Payload yields this JWS Signing Input value (with line breaks for display purposes only):

::

    eyJhbGciOiJFUzI1NiJ9
    .
    eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlfQ


The UTF-8 representation of the JWS Signing Input is the following byte array:

::

    [101, 121, 74, 104, 98, 71, 99, 105, 79, 105, 74, 70, 85, 122, 73, 49, 78, 105, 74, 57, 46, 101, 121, 74, 112, 99, 51, 77, 105, 79, 105, 74, 113, 98, 50, 85, 105, 76, 65, 48, 75, 73, 67, 74, 108, 101, 72, 65, 105, 79, 106, 69, 122, 77, 68, 65, 52, 77, 84, 107, 122, 79, 68, 65, 115, 68, 81, 111, 103, 73, 109, 104, 48, 100, 72, 65, 54, 76, 121, 57, 108, 101, 71, 70, 116, 99, 71, 120, 108, 76, 109, 78, 118, 98, 83, 57, 112, 99, 49, 57, 121, 98, 50, 57, 48, 73, 106, 112, 48, 99, 110, 86, 108, 102, 81]

The ECDSA key consists of a public part, the EC point (x, y), and a private part d. The values of the ECDSA key used in this example, presented as the byte arrays representing big endian integers are: 


Parameter Name /Value

    x
        [127, 205, 206, 39, 112, 246, 196, 93, 65, 131, 203, 238, 111, 219, 75, 123, 88, 7, 51, 53, 123, 233, 239, 19, 186, 207, 110, 60, 123, 209, 84, 69] 

    y
        [199, 241, 68, 205, 27, 189, 155, 126, 135, 44, 223, 237, 185, 238, 185, 244, 179, 105, 93, 110, 169, 11, 36, 173, 138, 70, 35, 40, 133, 136, 229, 173] 

    d
        [142, 155, 16, 158, 113, 144, 152, 191, 152, 4, 135, 223, 31, 93, 119, 233, 203, 41, 96, 110, 190, 210, 38, 59, 95, 87, 194, 19, 223, 132, 244, 178] 


The ECDSA :term:`private part` **d** is then passed to an ECDSA signing function, 
which also takes the curve type, P-256, 
the hash type, SHA-256, 
and the UTF-8 representation of the :term:`JWS Signing Input` as inputs. 
The result of the signature is the EC point (R, S), 
where R and S are unsigned integers. 

In this example, the R and S values, 
given as byte arrays representing big endian integers are: 


Result Name / Value


    R
        [14, 209, 33, 83, 121, 99, 108, 72, 60, 47, 127, 21, 88, 7, 212, 2, 163, 178, 40, 3, 58, 249, 124, 126, 23, 129, 154, 195, 22, 158, 166, 101] 

    S
        [197, 10, 7, 211, 140, 60, 112, 229, 216, 241, 45, 175, 8, 74, 84, 128, 166, 101, 144, 197, 242, 147, 80, 154, 143, 63, 127, 138, 131, 163, 84, 213] 


Concatenating the S array to the end of the R array and base64url encoding the result produces this value for the Encoded JWS Signature: 

::

    DtEhU3ljbEg8L38VWAfUAqOyKAM6-Xx-F4GawxaepmXFCgfTjDxw5djxLa8ISlSApmWQxfKTUJqPP3-Kg6NU1Q


(v.03)
