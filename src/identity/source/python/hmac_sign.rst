.. code-block:: python
    
    import hmac,hashlib

    def digester(alg):
        ''' 
            :param alg: Algorithms defined in JWA
        '''
        return getattr(hashlib,
                "sha%(bits)s" % re.search(r'[HRE]S(?P<bits>\d+)$',alg).groupdict())
    
    def hmac_sign(secret,pem,alg,data ):
        '''
            :param secret: shared secret
            :param pem: ignored by HMAC
            :param alg: JWA algorithm
            :param data: data to be signed.
        '''
        return hmac.new(key,data,digester(alg) ).digest()
