.. code-block:: csharp

        public static string JwsCreateToken(
            Dictionary<string,object> header,
            object payload, 
            string secret,
            string pem_private_key )
        {
            string jws_header = JsonConvert.SerializeObject(header);
            string jws_payload = JsonConvert.SerializeObject(payload);

            string encoded_jws_header = Jose.Utils.ToBase64Url( Encoding.UTF8.GetBytes(jws_header));
            string encoded_jws_payload = Jose.Utils.ToBase64Url(Encoding.UTF8.GetBytes(jws_payload));

            string jws_secured_input = encoded_jws_header + "." + encoded_jws_payload;

            byte[] jws_signature = _sign(secrete,
                                        pem_private_key, 
                                        (string)header["alg"], 
                                        Encoding.UTF8.GetBytes(jws_secured_input));

            string encoded_jws_signature = Jose.Utils.ToBase64Url(jws_signature);

            return string.Format("{0}.{1}.{2}", 
                        encoded_jws_header, encoded_jws_payload, encoded_jws_signature);
        }

.. code-block:: csharp

        // just a sample
        Dictionary<string, object> header = new Dictionary<string, object>() 
                                                { { "typ", "JWT" }, 
                                                  { "alg", "RS256" } };
        Dictionary<string, object> payload = new Dictionary<string, object>() 
                                                { { "iss", "alice" }, 
                                                  { "aud", "bob" }, 
                                                  { "user_id", "charlie" } };
        // for RSA ( Shared Secret in null )
        string token = Jose.Jws.CreateTokenRsa( header, 
                                                payload, 
                                                null,
                                                GetIdpByName('alice").private_key);

