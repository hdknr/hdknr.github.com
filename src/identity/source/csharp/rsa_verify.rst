.. code-block:: csharp

        public static bool RsaVerify(string secret, // ignored for RSA
                                string x509_pem, 
                                string alg, 
                                byte[] secure_input, byte[] signature)
        {
            RsaKeyParameters pubkey = (RsaKeyParameters)CertificateFromPem(x509_pem).GetPublicKey();

            var signer = SignerUtilities.GetSigner(SignerName(alg));
            signer.Init(false, pubkey);
            signer.BlockUpdate(secure_input, 0, secure_input.Length);

            return signer.VerifySignature(signature);
        }
