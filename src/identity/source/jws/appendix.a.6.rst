A.6.  Example JWS Using JWS JSON Serialization
========================================================

This section contains an example using the JWS JSON Serialization.

This example demonstrates the capability 
for conveying multiple digital signatures and/or MACs 
for the same payload.

.. note::
    - 複数のデジタル署名(or MAC)を１つのペイロードに入れられる

The JWS Payload used in this example is the same as that used 
in the examples in :ref:`Appendix A.2 <jws.appendix.a.2>` 
and :ref:`Appendix A.3 <jws.appendix.a.3>` 
(with line breaks for display purposes only):

::

  eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFt
  cGxlLmNvbS9pc19yb290Ijp0cnVlfQ

.. note::
    ーこの例では2つのデジタル署名を使っている
    - RSASSA-PKCS-v1_5 SHA-256
    - ECDSA P-256 SHA-256

Two digital signatures are used in this example: 
the first using RSASSA-PKCS-v1_5 SHA-256 
and the second using ECDSA P-256 SHA-256.

For the first, 
the JWS Protected Header and key are the same as in :ref:`Appendix A.2 <jws.appendix.a.2>`, 
resulting in the same JWS Signature value; 
therefore, its computation is not repeated here.  

For the second, 
the JWS Protected Header and key are the same as in :ref:`Appendix A.3 <jws.appendix.a.3>`, 
resulting in the same JWS Signature value; therefore, 
its computation is not repeated here.

(draft20)
