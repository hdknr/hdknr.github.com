Appendix A.  Relationship of JWTs to SAML Tokens
=========================================================

SAML 2.0 [OASIS.saml‑core‑2.0‑os] provides a standard for creating tokens with much greater expressivity 
and more security options than supported by JWTs. 

However, the cost of this flexibility and expressiveness is both size and complexity. 
In addition, 
SAML's use of XML [W3C.CR‑xml11‑20021015] and XML DSIG [RFC3275] only contributes to the size of SAML tokens.

JWTs are intended to provide a simple token format 
that is small enough to fit into HTTP headers and query arguments in URIs. 
It does this by supporting a much simpler token model than SAML and using the JSON [RFC4627] object encoding syntax. 
It also supports securing tokens using Hash-based Message Authentication Codes (HMACs) 
and digital signatures using a smaller (and less flexible) format than XML DSIG.

Therefore, 
while JWTs can do some of the things SAML tokens do, 
JWTs are not intended as a full replacement for SAML tokens, 
but rather as a compromise token format to be used when space is at a premium.

(v.06)
