.. code-block:: csharp

        // BouncyCastle

        public static IMac GetMac(string alg)
        {
            Regex re = new Regex("^(?<alg>[H])S(?<bits>\\d+)$");
            Match m = re.Match(alg);
            if (m != null)
                return MacUtilities.GetMac(
                            string.Format("HMAC-SHA{0}", 
                                    m.Groups["bits"].Value ));
            return null;
        }

        public static byte[] HmacSign(
                    string key, 
                    string pem,     //ignored for HMAC
                    string alg, 
                    byte[] data)
        {
            IMac mac = GetMac(alg);

            byte[] signature = new byte[mac.GetMacSize()];

            mac.Init( new KeyParameter(Encoding.UTF8.GetBytes(key) ));
            mac.BlockUpdate(data, 0, data.Length);
            mac.DoFinal(signature,0);

            return signature;
        }
