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
