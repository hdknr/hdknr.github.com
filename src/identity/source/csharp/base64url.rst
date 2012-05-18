.. code-block:: csharp

     public static string ToBase64Url(byte[] input)
     {
         StringBuilder result = new StringBuilder(Convert.ToBase64String(input).TrimEnd('='));
         result.Replace('+', '-');
         result.Replace('/', '_');
         return result.ToString();
     }

     public static byte[] FromBase64Url(string base64ForUrlInput)
     {
         int padChars = (base64ForUrlInput.Length % 4) == 0 ? 0 : (4 - (base64ForUrlInput.Length % 4));
         StringBuilder result = new StringBuilder(base64ForUrlInput, base64ForUrlInput.Length + padChars);
         result.Append(String.Empty.PadRight(padChars, '='));
         result.Replace('-', '+');
         result.Replace('_', '/');
         return Convert.FromBase64String(result.ToString());
     }
