==============================
JOSE JWS:Implementation
==============================

.. contents:: JOSE JWS Implementation

.. todo::

    - ECDSA must be implemented

JWS Token
==========

base64url
----------

Python
^^^^^^^^^^^^

.. include:: python/base64url.rst

C#:
^^^^^^^^^^^^

.. include:: csharp/base64url.rst

Token
------

jws_create_token()
^^^^^^^^^^^^^^^^^^^^^^^^

Python
~~~~~~~~~~~~

.. include:: python/jws_create_token.rst

C#
~~~~~~~~~~~~

.. include:: csharp/jws_create_token.rst


jws_verify_token()
^^^^^^^^^^^^^^^^^^^^^^^^

Python
~~~~~~~~~~~~~~~

.. include:: python/jws_verify_token.rst

C#
~~~~~~

.. include:: csharp/jws_verify_token.rst


So what is _sign() and _verify() ?
Actula funcitons will vary based on "alg"orithm paramter:
rsa_sign() and rsa_vefiy() for RSA, hmac_sign() and hamc_verify for HMAC. 

RSA and X.509
==================

Key negotiation in advance
-------------------------------

Any RP and OP can negotiate their private keys and X.509 certificate 
in advance before a OpenID Connect session begins.

RP : Registartion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- An Relying Party  can register it's X.509 certificate via :doc:`reg`.
- :term:`x509_url` is the RP's X.509 Certificate for OP 
  to verify requsets' signatures, or public-encrypt token and other data. 
- If RP ask OP to encrypt wth the other public key, 
  :term:`x509_encryption_url` can be specified.
- If you want to specify :term:`jwk_url` as well, both keys must be the same.
- So do :term:`x509_encryption_url` and :term:`jwk_encryption_url`.
- Format is :term:`PEM`

OP:Discovery Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- OP can advertise its public key for signing and encrypton via :doc:`discovery` 
- As with RP in :doc:`reg`, both :term:`x509_url` and :term:`x509_encryption_url` work
  in the same way. 
- So do :term:`jwk_url` and :term:`jwk_encryption_url`.
- Format is :term:`PEM`

Session-wise Key Negotiation 
-----------------------------------

Any RP can specifiy its X.509 certificate for the private key used to sign a OpenID Request Object.
Also any OP can specify its X.509 certificate for the private key used to sign tokens or response data.
To do those, JWS header provides the following X.509 parameters.  {See :ref:`jws.4.1` )

.. list-table:: JWS X.509 Header Parameters
    :widths: 10 45 45 

    *   - x5u
        - URL, like as :term:`x509_url` in :doc:`reg` and :doc:`discovery`.  
        - Format of data returned by this URL is :term:`PEM` 

    *   - x5c
        - X.509 certificate(chain) used this JWS 
        - base64-encode :term:`DER`/:term:`BER` ( **NOT** in :term:`base64url` )

    *   - x5t
        - SHA-1 thumprint of ::term:`DER` (binary) encoded X.509 certificate
        - base64url encoded thumprint   

Fingerprint of specifed :term:`PEM` certificate.

Python
^^^^^^^^^^^^

.. include:: python/thumprint.rst

C#
^^^^^^^^^^^^

.. include:: csharp/thumprint.rst


Sign/Verify with RSA Key and X.509 Certificate
-----------------------------------------------------------------

sha_name()
^^^^^^^^^^^^^^^^

- select proper SHA digest function for **alg** .

Python
~~~~~~~~~~~~~

.. include:: python/sha_name.rst

C#
~~~~~~~~~~~~~

.. include:: csharp/sha_name.rst

rsa_sign()
^^^^^^^^^^^^^^^^

Python
~~~~~~~~~~~~~~~~~~~~

.. include:: python/rsa_sign.rst

C#
~~~~~~~~~~~~~~~~~~~~

.. include:: csharp/rsa_sign.rst

rsa_verify()
^^^^^^^^^^^^^^^^^^^^^^^^

Python
~~~~~~~~~~~

.. include:: python/rsa_verify.rst

C#
~~~~~~~~~~~

.. include:: csharp/rsa_verify.rst


PEM in C#
^^^^^^^^^^^^^^^^^^^^^^^^

Because it's not easy to read PEM formatted data in Microsoft library,
BouncyCastle can be used to load X.509 certificate and private key.

X.509 Certificate im PEM
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: csharp/pem_cert.rst

DER Private Key im PEM
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: csharp/pem_key.rst


HMAC and Shared Secret
=================================

Shared Secrete negotiation  on Client  Registartion
------------------------------------------------------------

Audience must register his shared secret as :term:`client_secret` on :doc:`reg`  process.

Signature?
------------

No. JWS Signature for HMAC is not signature actually.
Verifier must repeat the same hmac_sign() process as creator did  
and check if JWS Signature value produced by the verifier is exactly same as the one received.

hmac_sign()
--------------

Python
^^^^^^^^^

.. include:: python/hmac_sign.rst

C#
^^^^^^^^^

.. include:: csharp/hmac_sign.rst

hmac_verify()
--------------

Python
^^^^^^^^^

.. include:: python/hmac_verify.rst

C#
^^^^^^^^^

.. include:: csharp/hmac_verify.rst

Libraries
========================

Python
----------

.. include:: python/lib.rst

C#
----------

.. include:: csharp/lib.rst

