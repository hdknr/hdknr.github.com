A.2.7.  Complete Representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assemble the final representation: 
The Compact Serialization of this result is the string 
BASE64URL(UTF8(JWE Protected Header)) || '.' ||
BASE64URL(JWE Encrypted Key) || '.' || 
BASE64URL(JWE Initialization Vector) || '.' || 
BASE64URL(JWE Ciphertext) || '.' || 
BASE64URL(JWE Authentication Tag).

The final result in this example (with line breaks for display
purposes only) is:

::

     eyJhbGciOiJSU0ExXzUiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.
     UGhIOguC7IuEvf_NPVaXsGMoLOmwvc1GyqlIKOK1nN94nHPoltGRhWhw7Zx0-kFm
     1NJn8LE9XShH59_i8J0PH5ZZyNfGy2xGdULU7sHNF6Gp2vPLgNZ__deLKxGHZ7Pc
     HALUzoOegEI-8E66jX2E4zyJKx-YxzZIItRzC5hlRirb6Y5Cl_p-ko3YvkkysZIF
     NPccxRU7qve1WYPxqbb2Yw8kZqa2rMWI5ng8OtvzlV7elprCbuPhcCdZ6XDP0_F8
     rkXds2vE4X-ncOIM8hAYHHi29NX0mcKiRaD0-D-ljQTP-cFPgwCp6X-nZZd9OHBv
     -B3oWh2TbqmScqXMR4gp_A.
     AxY8DCtDaGlsbGljb3RoZQ.
     KDlTtXchhZTGufMYmOYGS4HffxPSUrfmqCHXaI9wOGY.
     9hH0vgRfYgPnAHOd8stkvw

(draft23)
