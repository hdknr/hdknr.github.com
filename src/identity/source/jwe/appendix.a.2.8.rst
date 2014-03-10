A.2.8.  Validation
^^^^^^^^^^^^^^^^^^^^^^^^^

This example illustrates the process of creating a JWE with RSAES-
PKCS1-V1_5 for key encryption and AES_CBC_HMAC_SHA2 for content
encryption.  These results can be used to validate JWE decryption
implementations for these algorithms.  Note that since the RSAES-
PKCS1-V1_5 computation includes random values, the encryption results
above will not be completely reproducible.  However, since the AES
CBC computation is deterministic, the JWE Encrypted Ciphertext values
will be the same for all encryptions performed using these inputs.

(draft23)
