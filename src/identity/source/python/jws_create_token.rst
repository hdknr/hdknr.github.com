.. code-block:: python

    import json

    def jws_create_token(header,payload ,secret,pem_private_key):    
        ''' 
            :param header: JWS Header JSON
            :param payload: JWS Payload in JSON
            :param secret: Shared Secret for HMAC
            :param pem_private_key: RSA/DSA Private Key in PEM format    
        '''    
        jws_header= json.dumps( header )        #dumps produdes utf8 string by default
        jws_payload= json.dumps( payload ) 

        encoded_jws_header = to_base64url(jws_header)
        encoded_jws_payload= to_base64url(jws_payload)

        jws_secured_input = "%s.%s" % ( encoded_jws_header, encoded_jws_payload )
        jws_signature = _sign(secret,pem_private_key,
                                header['alg'],
                                jws_secured_input )

        encoded_jws_signature = to_base64url(jws_signature) 
        jws_token = "%s.%s.%s" % ( encoded_jws_header,encoded_jws_payload, encoded_jws_signature ) 

        return jws_token


.. code-block:: python

    #  alg : [HRE]S[256|384|512]

    token = create_jws_token_rsa(
            {"typ":"JWT","alg":"RS256"},                    #:Header
            {"iss":"alice","aud":"bob","user_id":"charlie"},#:Payload
            secret,                                         #:for HMAC
            Idp.objects.get(issuer="me").private_key        #: Load private key
            )

