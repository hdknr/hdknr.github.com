A.1.3.  Validating
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next we validate the decoded results. 

Since the :term:`alg` parameter in the header is "HS256", 
we validate the HMAC SHA-256 signature contained in the :term:`JWS Signature`. 
If any of the validation steps fail, 
the JWS MUST be rejected.

First, 
we validate that the JWS Header string is legal JSON.

To validate the HMAC value, 
we repeat the previous process of using the correct key 
and the UTF-8 representation of the :term:`JWS Secured Input`
(which is the same as the ASCII representation) 
as input to the HMAC SHA-256 function 
and then taking the output and determining 
if it matches the :term:`JWS Signature`.  

If it matches exactly, the HMAC has been validated.

(jose-jws draft 02)
