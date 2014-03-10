A.4.7.  Complete JWE JSON Serialization Representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The complete JSON Web Encryption JSON Serialization for these values
is as follows (with line breaks for display purposes only):

::

     {"protected":
       "eyJlbmMiOiJBMTI4Q0JDLUhTMjU2In0",
      "unprotected":
       {"jku":"https://server.example.com/keys.jwks"},
      "recipients":[
       {"header":
         {"alg":"RSA1_5"},
        "encrypted_key":
         "UGhIOguC7IuEvf_NPVaXsGMoLOmwvc1GyqlIKOK1nN94nHPoltGRhWhw7Zx0-
          kFm1NJn8LE9XShH59_i8J0PH5ZZyNfGy2xGdULU7sHNF6Gp2vPLgNZ__deLKx
          GHZ7PcHALUzoOegEI-8E66jX2E4zyJKx-YxzZIItRzC5hlRirb6Y5Cl_p-ko3
          YvkkysZIFNPccxRU7qve1WYPxqbb2Yw8kZqa2rMWI5ng8OtvzlV7elprCbuPh
          cCdZ6XDP0_F8rkXds2vE4X-ncOIM8hAYHHi29NX0mcKiRaD0-D-ljQTP-cFPg
          wCp6X-nZZd9OHBv-B3oWh2TbqmScqXMR4gp_A"},
       {"header":
         {"alg":"A128KW"},
        "encrypted_key":
         "6KB707dM9YTIgHtLvtgWQ8mKwboJW3of9locizkDTHzBC2IlrT1oOQ"}],
      "iv":
       "AxY8DCtDaGlsbGljb3RoZQ",
      "ciphertext":
       "KDlTtXchhZTGufMYmOYGS4HffxPSUrfmqCHXaI9wOGY",
      "tag":
       "Mz-VPPyU4RlcuYv1IwIvzw"
     }
