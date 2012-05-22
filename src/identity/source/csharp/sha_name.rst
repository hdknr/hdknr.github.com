.. code-block:: csharp

        // Look at "security/SignerUtilities.cs" of BouncyCastle 
        // for RSA signature algorithm.

        public static string SignerName(string alg)
        {
            Regex re= new Regex("^RS(?<bits>\\d+)$");
            Match m = re.Match(alg);
            if( m!= null ){
                return string.Format("SHA{0}WITHRSA", m.Groups["bits"].Value);
            }
            return "";
        }
