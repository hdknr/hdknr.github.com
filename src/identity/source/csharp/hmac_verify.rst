.. code-block:: csharp

        public static bool HmacVerify(
                string key, 
                string pem, // ignored for HMAC
                string alg, 
                byte[] data, byte[] signature)
        {
            return signature.SequenceEqual( HmacSign(key, alg, data )); 
        }
