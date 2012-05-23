.. code-block:: csharp

        public static byte[] RsaSign(string secret,string key_pem, 
                    string alg, byte[] secure_input ,string passphrase)
        {
            // secret is isngored for RSA

            var signer = SignerUtilities.GetSigner(SignerName(alg));
            signer.Init(true, RsaPrivateKeyFromPem(key_pem));
            signer.BlockUpdate(secure_input, 0, secure_input.Length);

            return signer.GenerateSignature();
        }

.. todo::

    Find to load PEM private key secured with pass phrase.

