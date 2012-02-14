Appendix B.  Relationship of JWTs to Simple Web Tokens (SWTs)
========================================================================

Both JWTs and Simple Web Tokens SWT [SWT], at their core, 
enable sets of claims to be communicated between applications. 

For SWTs, 
both the claim names and claim values are strings. 
For JWTs, 
while claim names are strings, 
claim values can be any JSON type. 

Both token types offer cryptographic protection of their content: 
SWTs with HMAC SHA-256 and 
JWTs with a choice of algorithms, including HMAC SHA-256, RSA SHA-256, and ECDSA P-256 SHA-256.

(v.06)


