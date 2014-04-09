A.2.2.  Validating
^^^^^^^^^^^^^^^^^^^^^^^^

Since the "alg" Header Parameter is "RS256", 
we validate the RSASSA-PKCS-v1_5 SHA-256 digital signature 
contained in the JWS Signature.

Validating the JWS Signature is a little different 
from the previous example.  

We pass (n, e), 
JWS Signature, and the JWS Signing Input 
to an RSASSA-PKCS-v1_5 signature verifier 
that has been configured to use the SHA-256 hash function.

(draft25)
