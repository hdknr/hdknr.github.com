A.1.3.  Validating
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next we validate the decoded results. 

Since the :term:`alg` parameter in the header is "HS256", 
we validate the HMAC SHA-256 signature contained in the :term:`JWS Signature`. 
If any of the validation steps fail, 
the signed content MUST be rejected.

First, we validate that the JWS Header string is legal JSON.

To validate the signature, 
we repeat the previous process of using the correct key 
and the UTF-8 representation of the :term:`JWS Signing Input` 
as input to a SHA-256 HMAC function 
and then taking the output and determining 
if it matches the :term:`JWS Signature`. 

If it matches exactly, the signature has been validated.

(v.03)
