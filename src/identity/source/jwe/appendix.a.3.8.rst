A.3.8.  Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example illustrates the process of 
creating a JWE with AES Key Wrap for key encryption 
and AES GCM for content encryption.  

These results can be used to validate JWE decryption implementations 
for these algorithms.  

Also, 
since both the AES Key Wrap and AES GCM computations are deterministic, 
the resulting JWE value will be the same for all encryptions 
performed using these inputs.  

Since the computation is reproducible, 
these results can also be used to validate JWE encryption implementations 
for these algorithms.

(draft23)
