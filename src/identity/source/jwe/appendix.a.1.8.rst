A.1.8.  Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example illustrates the process of creating a JWE with RSAES
OAEP for key encryption and AES GCM for content encryption.  These
results can be used to validate JWE decryption implementations for
these algorithms.  Note that since the RSAES OAEP computation
includes random values, the encryption results above will not be
completely reproducible.  However, since the AES GCM computation is
deterministic, the JWE Encrypted Ciphertext values will be the same
for all encryptions performed using these inputs.

(draft23)
