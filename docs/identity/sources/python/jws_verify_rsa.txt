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
