.. code-block:: csharp

        public static X509Certificate CertificateFromPem(string certificate)
        {
            TextReader c = new StringReader(certificate);
            PemReader pem2 = new PemReader(c);
            X509Certificate x509 = (X509Certificate)pem2.ReadObject();

            return x509;
        }
