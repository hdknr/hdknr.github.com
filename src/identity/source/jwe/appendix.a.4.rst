A.4.  Example JWE using JWE JSON Serialization
------------------------------------------------

This section contains an example 
using the :ref:`JWE JSON Serialization <jwe.json_serialization>`.

This example demonstrates the capability 
for encrypting the same plaintext to multiple recipients.


Two recipients are present in this example.  

The algorithm and key used for the first recipient 
are the same as that used in :ref:`Appendix A.2 <jwe.appendix.a.2>`.  

The algorithm and key used for the second recipient 
are the same as that used in :ref:`Appendix A.3 <jwe.appendix.a.3>`.  

The resulting JWE Encrypted Key values are therefore the same; 
those computations are not repeated here.

The Plaintext, 
the Content Encryption Key (CEK), 
Initialization Vector, and 
JWE Protected Header are shared by all recipients 
(which must be the case, since the Ciphertext and 
Authentication Tag are also shared).

(draft23)

