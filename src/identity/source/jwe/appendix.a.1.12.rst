A.1.12. Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example illustrates the process of creating a JWE 
with an :term:`Authenticated Encryption` algorithm.  

These results can be used to validate JWE decryption implementations for these algorithms.  
Note that since the :term:`RSAES OAEP` computation includes random values, 
the encryption results above will not be completely reproducible.

However, 
since the :term:`AES GCM` computation is deterministic, 
the :term:`JWE Encrypted Ciphertext` values will be the same 
for all encryptions performed using these inputs.

(draft 08, http://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-08#appendix-A.1.12 )
