.. code-block:: python

    from M2Crypto import RSA,util
    import hashlib

    def rsa_sign(private_key_pem, alg, secure_input ,passphrase=None):
        '''
            :param private_key_pem: PEM string of private key of signer
            :param alg: Algorithms defined in JWA
            :param secure_input: Message for digest input
            :param passphrase: (optional) pass phrase for private key
    
        '''
        def _passphrase():
            return passphrase

        callback = _passphrase if passphrase else util.passphrase_callback  
        key = RSA.load_key_string(private_key_pem,callback=callback )
        
        sha=sha_name(alg)
        
        return key.sign( getattr(hashlib,sha)(secure_input).digest(),sha)
