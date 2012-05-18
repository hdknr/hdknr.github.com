.. code-block:: python

    from M2Crypto import X509

    def rsa_verify(x509_pem, alg, secure_input ,signature):
        '''       
            :param x509_pem: PEM string of signer's X.509 certificate
            :param alg: Algorithms defined in JWA
            :param secure_input: Message for digest input
            :param signature: signature which OP has signed.
        '''
    
        pub= X509.load_cert_string(x509_pem).get_pubkey()
        sha=sha_name(alg)
        return pub.get_rsa().verify( getattr(hashlib,sha)(secure_input).digest(),signature,sha)

