A.2.  Example Nested JWT
------------------------------------------------------------

This example shows how a JWT can be used as the payload of 
a JWE or JWS to create a Nested JWT.  

In this case, 
the JWT Claims Set is first signed, and then encrypted.

The inner signed JWT is identical to the example 
in :ref:`Appendix A.2 <jws.appendix.a.2>` of [JWS].  

Therefore, 
its computation is not repeated here.  

This example then encrypts this inner JWT to the recipient 
using :term:`RSAES-PKCS1-V1_5` and :term:`AES_128_CBC_HMAC_SHA_256`.

The following example JOSE Header 
(with line breaks for display purposes only) declares that:

-   the Content Encryption Key is encrypted to the recipient 
    using the RSAES-PKCS1-V1_5 algorithm to produce the JWE Encrypted Key,

-   the Plaintext is encrypted 
    using the AES_128_CBC_HMAC_SHA_256 algorithm 
    to produce the JWE Ciphertext, and

-   the Plaintext is itself a JWT.

::

  {"alg":"RSA1_5","enc":"A128CBC-HS256","cty":"JWT"}

Base64url encoding the octets of the UTF-8 representation of the JOSE
Header yields this encoded JOSE Header value:

::

  eyJhbGciOiJSU0ExXzUiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiY3R5IjoiSldUIn0

The computation of this JWT is identical to the computation of the
JWE in Appendix A.2 of [JWE], other than that different JOSE Header,
Plaintext, JWE Initialization Vector, and Content Encryption Key values
are used.  (The RSA key used is the same.)

The Payload used is the octets of the ASCII representation of the JWT
at the end of Appendix Section A.2.1 of [JWS] (with all whitespace
and line breaks removed), which is a sequence of 458 octets.

The JWE Initialization Vector value used is:

::

    [82, 101, 100, 109, 111, 110, 100, 32, 87, 65, 32, 57, 56, 48, 53,
    50]

This example uses the Content Encryption Key represented 
by the base64url encoded value below:

::

     GawgguFyGrWKav7AX4VKUg

The final result for this Nested JWT (with line breaks for display
purposes only) is:

::

  eyJhbGciOiJSU0ExXzUiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiY3R5IjoiSldU
  In0.
  g_hEwksO1Ax8Qn7HoN-BVeBoa8FXe0kpyk_XdcSmxvcM5_P296JXXtoHISr_DD_M
  qewaQSH4dZOQHoUgKLeFly-9RI11TG-_Ge1bZFazBPwKC5lJ6OLANLMd0QSL4fYE
  b9ERe-epKYE3xb2jfY1AltHqBO-PM6j23Guj2yDKnFv6WO72tteVzm_2n17SBFvh
  DuR9a2nHTE67pe0XGBUS_TK7ecA-iVq5COeVdJR4U4VZGGlxRGPLRHvolVLEHx6D
  YyLpw30Ay9R6d68YCLi9FYTq3hIXPK_-dmPlOUlKvPr1GgJzRoeC9G5qCvdcHWsq
  JGTO_z3Wfo5zsqwkxruxwA.
  UmVkbW9uZCBXQSA5ODA1Mg.
  VwHERHPvCNcHHpTjkoigx3_ExK0Qc71RMEParpatm0X_qpg-w8kozSjfNIPPXiTB
  BLXR65CIPkFqz4l1Ae9w_uowKiwyi9acgVztAi-pSL8GQSXnaamh9kX1mdh3M_TT
  -FZGQFQsFhu0Z72gJKGdfGE-OE7hS1zuBD5oEUfk0Dmb0VzWEzpxxiSSBbBAzP10
  l56pPfAtrjEYw-7ygeMkwBl6Z_mLS6w6xUgKlvW6ULmkV-uLC4FUiyKECK4e3WZY
  Kw1bpgIqGYsw2v_grHjszJZ-_I5uM-9RA8ycX9KqPRp9gc6pXmoU_-27ATs9XCvr
  ZXUtK2902AUzqpeEUJYjWWxSNsS-r1TJ1I-FMJ4XyAiGrfmo9hQPcNBYxPz3GQb2
  8Y5CLSQfNgKSGt0A4isp1hBUXBHAndgtcslt7ZoQJaKe_nNJgNliWtWpJ_ebuOpE
  l8jdhehdccnRMIwAmU1n7SPkmhIl1HlSOpvcvDfhUN5wuqU955vOBvfkBOh5A11U
  zBuo2WlgZ6hYi9-e3w29bR0C2-pp3jbqxEDw3iWaf2dc5b-LnR0FEYXvI_tYk5rd
  _J9N0mg0tQ6RbpxNEMNoA9QWk5lgdPvbh9BaO195abQ.
  AVO9iT5AV4CzvDJCdhSFlQ


(draft23)
