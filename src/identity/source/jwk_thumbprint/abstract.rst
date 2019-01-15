Abstract
================

.. note::
    - X.509証明書のダイジェストみたいなもの
    - jkt を定義する

This specification defines 
a means of computing a thumbprint value (a.k.a. :term:`digest)` 
of JSON Web Key (:doc:`JWK <jwk>)` objects analogous 
to the "x5t" (X.509 Certificate SHA-1 Thumbprint) value 
defined for X.509 certificate objects.  

This specification also registers 
the new JSON Web Signature (:doc:`JWS <jws>`) 
and JSON Web Encryption (:doc:`JWE <jwe>`) Header Parameters
and the new JSON Web Key (JWK) member name ":term:`jkt`" 
(JWK SHA-256 Thumbprint) for holding these values.

(draft01)
