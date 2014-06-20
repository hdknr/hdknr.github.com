A.4.2.  Validating
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since the "alg" Header Parameter is "ES512", we validate the ECDSA
P-521 SHA-512 digital signature contained in the JWS Signature.

Validating this JWS Signature is very similar to the previous
example.  We need to split the 132 member octet sequence of the JWS
Signature into two 66 octet sequences, the first representing R and
the second S. We then pass the public key (x, y), the signature (R,
S), and the JWS Signing Input to an ECDSA signature verifier that has
been configured to use the P-521 curve with the SHA-512 hash
function.

(draft27)
