A.2.3.  Validating
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since the :term:`alg` parameter in the header is "RS256", 
we validate the RSA SHA-256 signature contained in the JWS Signature. 
If any of the validation steps fail, 
the signed content MUST be rejected.

First, we validate that the :term:`JWS Header` string is legal JSON.

Validating the JWS Signature is a little different 
from the previous example. 

First, 
we base64url decode the :term:`Encoded JWS Signature` 
to produce a signature S to check. 

We then pass (n, e), 
S and the UTF-8 representation of the :term:`JWS Signing Input` 
to an RSA signature verifier that has been configured 
to use the SHA-256 hash function.


(v.03)
