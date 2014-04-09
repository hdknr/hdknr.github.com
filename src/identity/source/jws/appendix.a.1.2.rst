A.1.2.  Validating
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since the "alg" Header Parameter is "HS256", 
we validate the HMAC SHA-256 value contained in the JWS Signature.

To validate the HMAC value, 
we repeat the previous process of 
using the correct key and the JWS Signing Input 
as input to the HMAC SHA-256 function 
and then taking the output and determining 
if it matches the JWS Signature.  

If it matches exactly, 
the HMAC has been validated.

(draft25)
