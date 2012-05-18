==============================
JOSE JWS:Implementation
==============================

.. contents:: JOSE JWS Implementation


JWS Token
==========

base64url
----------

Python:

.. include:: python/base64url.rst

C#:


.. include:: csharp/base64url.rst

Token
------

create_jws_token_rsa()
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import json

    def create_jws_token_rsa(header,payload ,pem_private_key):    
        ''' 
            :param header: JWS Header JSON
            :param payload: JWS Payload in JSON
            :param pem_private_key: RSA Private Key in PEM format    
        '''    
        jws_header= json.dumps( header )        #dumps produdes utf8 string by default
        jws_payload= json.dumps( payload ) 

        encoded_jws_header = to_base64url(jws_header)
        encoded_jws_payload= to_base64url(jws_payload)

        jws_secured_input = "%s.%s" % ( encoded_jws_header, encoded_jws_payload )
        jws_signature = rsa_sign(pem_private_key,header['alg'],jws_secured_input )

        encoded_jws_signature = to_base64url(jws_signature) 
        jws_token = "%s.%s.%s" % ( encoded_jws_header,encoded_jws_payload, encoded_jws_signature ) 

        return jws_token


.. code-block:: python

    token = create_jws_token_rsa(
            {"typ":"JWT","alg":"RS256"},
            {"iss":"alice","aud":"bob","user_id":"charlie"},
            Idp.objects.get(issuer="me").private_key            #: Load private key
            )

verify_jws_token_rsa()
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    def verify_jws_token_rsa(jws_token,pem_x509): 
        ''' 
            :param jws_token:  JWS Token
            :param pem_x509:   X.509 Certificate
        '''
        (encoded_jws_header,encoded_jws_payload,encoded_jws_signature) = jws_token.split('.')

        jws_header = from_base64url(encoded_jws_header)
        jws_payload = from_base64url(encoded_jws_payload)
        jws_signature=from_base64url(encoded_jws_signature)

        jws_secured_input = "%s.%s" % ( encoded_jws_header, encoded_jws_payload )
        header = json.loads(jws_header)

        is_valid = rsa_verify(pem_x509,header['alg'],jws_secured_input, jws_signature )
       
        return is_valid==1,header,json.loads(jws_payload) 

.. todo::
    pem_x509 can be None for session wise certificate negotiation.
    There should be the other utility which fetch and validate the certficate
    based on **header** decoded from **jws_token** .

.. code-block:: python
    
    (is_valid,header,payload) = verify_jws_token_rsa(       
                                    token,
                                    Op.objects.get(issuer="alice").x509_cert_cache ) 

So what is rsa_sign() and rsa_verify() ?

X.509
======

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

.. code-block:: python

        from M2Crypto import X509
        import utils
        def x5t(cert_string,format=0): 
            ''' format 
                = 0 (M2Crypto.X509.DER_FORMAT)
                = 1 (M2Crypto.X509.PEM_FORMAT) 
            '''
            cert = X509.load_cert_string(cert_string,format)
            return utils.to_base64url(
                    utils.from_hex_string(
                        cert.get_fingerprint(md='sha1')) )


Sign/Verify with RSA Key and X.509 Certificate
-----------------------------------------------------------------

sha_name()
^^^^^^^^^^^^^^^^

- select proper SHA digest function for **alg** .

.. code-block:: python

    import re

    def sha_name(alg):
        ''' 
            :param alg: Algorithms defined in JWA
        '''
        return "sha%(bits)s" % re.search(r'[HRE]S(?P<bits>\d+)$',alg).groupdict()

rsa_sign()
^^^^^^^^^^^^^^^^

Python:

.. include:: python/rsa_sign.rst

rsa_verify()
^^^^^^^^^^^^^^^^^^^^^^^^

Python:

.. include:: python/rsa_verify.rst
