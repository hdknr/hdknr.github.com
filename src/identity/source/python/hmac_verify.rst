.. code-block:: python

    def hmac_verify(secret,pem,alg,data,signature):
        '''
            :param secret: shared secret
            :param pem: ignored by HMAC
            :param alg : JWA algorithm 
            :param data: data signed
            :param signature: produced signature
        '''
        #: hmac_sign is used by a verifier to check if same or not

        return signature == hmac_sign(secret,alg,data )


