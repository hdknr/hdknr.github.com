Abstract
===========

This specification describes how to use :term:`bearer tokens` 
in HTTP requests to access OAuth 2.0 :term:`protected resources`.  
**Any party in possession of a bearer token** (a "bearer") can use it 
to get access to the associated resources 
(without demonstrating possession of a cryptographic key).  

To prevent misuse, 
bearer tokens need to be protected from disclosure in storage and in transport.

(:rfc:`6750` )

.. note::
    - ベアラトークンを持っている人は「誰でも」それに関連づけられているリソースにアクセスできる
    - なので、ベアラトークンは部外者に漏らしてはいけません

