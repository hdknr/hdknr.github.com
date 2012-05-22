.. code-block:: csharp

        public static RsaKeyParameters RsaPrivateKeyFromPem(string private_key )
        {
            TextReader r = new StringReader(private_key);
            PemReader pem = new PemReader(r);
            return (RsaKeyParameters)((AsymmetricCipherKeyPair )pem.ReadObject()).Private;
        }
