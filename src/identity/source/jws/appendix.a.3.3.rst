A.3.3.  Validating
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since the alg parameter in the header is "ES256", we validate the ECDSA P-256 SHA-256 signature contained in the JWS Signature. If any of the validation steps fail, the signed content MUST be rejected.

First, we validate that the JWS Header string is legal JSON.

Validating the JWS Signature is a little different from the first example. First, we base64url decode the Encoded JWS Signature as in the previous examples but we then need to split the 64 member byte array that must result into two 32 byte arrays, the first R and the second S. We then pass (x, y), (R, S) and the UTF-8 representation of the JWS Signing Input to an ECDSA signature verifier that has been configured to use the P-256 curve with the SHA-256 hash function.

As explained in :ref:`Section 6.3 <jws.6.3>`, 
the use of the **k** value in ECDSA means 
that we cannot validate the correctness of the signature in the same way we validated 
the correctness of the HMAC. 

Instead, implementations MUST use an ECDSA validator to validate the signature. 

(v.03)
