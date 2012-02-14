Appendix C.  Notes on implementing base64url encoding without padding
====================================================================================

This appendix describes how to implement base64url encoding and decoding functions 
without padding based upon standard base64 encoding and decoding functions that do use padding.

To be concrete, example C# code implementing these functions is shown below. Similar code could be used in other languages.

::

    static string base64urlencode(byte [] arg)
    {
      string s = Convert.ToBase64String(arg); // Standard base64 encoder
      s = s.Split('=')[0]; // Remove any trailing '='s
      s = s.Replace('+', '-'); // 62nd char of encoding
      s = s.Replace('/', '_'); // 63rd char of encoding
      return s;
    }

    static byte [] base64urldecode(string arg)
    {
      string s = arg;
      s = s.Replace('-', '+'); // 62nd char of encoding
      s = s.Replace('_', '/'); // 63rd char of encoding
      switch (s.Length % 4) // Pad with trailing '='s
      {
        case 0: break; // No pad chars in this case
        case 2: s += "=="; break; // Two pad chars
        case 3: s += "="; break; // One pad char
        default: throw new System.Exception(
          "Illegal base64url string!");
      }
      return Convert.FromBase64String(s); // Standard base64 decoder
    }

As per the example code above, the number of '=' padding characters 
that needs to be added to the end of a base64url encoded string 
without padding to turn it into one with padding is a deterministic function of the length of the encoded string. Specifically, if the length mod 4 is 0, no padding is added; if the length mod 4 is 2, two '=' padding characters are added; if the length mod 4 is 3, one '=' padding character is added; if the length mod 4 is 1, the input is malformed.

An example correspondence between unencoded and encoded values follows. The byte sequence below encodes into the string below, which when decoded, reproduces the byte sequence.

::

    3 236 255 224 193

    A-z_4ME


(v.03)
