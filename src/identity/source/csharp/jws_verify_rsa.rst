.. code-block:: csharp

        public static bool VerifyTokenRsa(string jws_token, string pem_x509)
        {
            Match m=  (new Regex(@"^(?<encoded_jws_header>.+)\.(?<encoded_jws_payload>.+)\.(?<encoded_jws_signature>.+)$")).Match(jws_token);
            string jws_header = Encoding.UTF8.GetString( Jose.Utils.FromBase64Url(m.Groups["encoded_jws_header"].Value)) ;
            string jws_payload = Encoding.UTF8.GetString( Jose.Utils.FromBase64Url(m.Groups["encoded_jws_header"].Value)) ;
            byte[] jws_signature = Jose.Utils.FromBase64Url(m.Groups["encoded_jws_signature"].Value);

            string jws_secured_input = m.Groups["encoded_jws_header"].Value + "." +  m.Groups["encoded_jws_payload"].Value;

            Dictionary<string,object> header = JsonConvert.DeserializeObject<Dictionary<string,object>>(jws_header);

            Console.WriteLine("jws_secured_input={0}", jws_secured_input);
            Console.WriteLine("ALG={0}", (string)header["alg"]);

            bool ret = RsaVerify(pem_x509, (string)header["alg"], 
                           Encoding.UTF8.GetBytes(jws_secured_input),
                            jws_signature);

            return ret;
        }


.. code-block:: csharp

        // just a sample
        bool ret = Jose.Jws.VerifyTokenRsa(token, GetOpByName("alice").x509_cache);
