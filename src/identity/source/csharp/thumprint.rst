.. code-block:: csharp

        public static string GetFingerprint(X509Certificate cert,
                                                string digester_name="SHA1")
        {

            IDigest digester = DigestUtilities.GetDigest(digester_name);
            byte[] der = cert.GetEncoded();

            digester.BlockUpdate(der, 0, der.Length);

            byte[] hash = new byte[digester.GetDigestSize()];
            digester.DoFinal(hash, 0);

            return Jose.Utils.ToBase64Url(hash);
        }

        public static string GetFingerprint(string pem_x509,string 
                                                digerster_name="SHA1")
        {
            return GetFingerprint(CertificateFromPem(pem_x509), digerster_name);
        }
