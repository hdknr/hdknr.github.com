Appendix D.  Example ECDH-ES Key Agreement Computation
==================================================================

This example uses ECDH-ES Key Agreement and the Concat KDF to derive
the Content Encryption Key (CEK) in the manner described in
Section 4.7.  In this example, the ECDH-ES Direct Key Agreement mode
("alg" value "ECDH-ES") is used to produce an agreed upon key for AES
GCM with 128 bit keys ("enc" value "A128GCM").

In this example, a sender Alice is encrypting content to a recipient
Bob. The sender (Alice) generates an ephemeral key for the key
agreement computation.  Alice's ephemeral key (in JWK format) used
for the key agreement computation in this example (including the
private part) is:

.. code-block:: javascript

     {"kty":"EC",
      "crv":"P-256",
      "x":"gI0GAILBdu7T53akrFmMyGcsF3n5dO7MmwNBHKW5SV0",
      "y":"SLW_xSffzlPWrHEVI30DHM_4egVwt3NQqeUD7nMFpps",
      "d":"0_NxaRPUMQoAJt50Gz8YiTr8gRTwyEaCumd-MToTmIo"
     }

The recipient's (Bob's) key (in JWK format) used for the key
agreement computation in this example (including the private part) is:

.. code-block:: javascript

     {"kty":"EC",
      "crv":"P-256",
      "x":"weNJy2HscCSM6AEDTDg04biOvhFhyyWvOHQfeF_PxMQ",
      "y":"e8lnCO-AlStT-NJVX-crhB7QRYhiix03illJOVAOyck",
      "d":"VEmDZpDXXK8p8N0Cndsxs924q6nS1RXFASRl6BfUqdw"
     }

Header parameter values used in this example are as follows.  In this
example, the "apu" (agreement PartyUInfo) parameter value is the
base64url encoding of the UTF-8 string "Alice" and the "apv"
(agreement PartyVInfo) parameter value is the base64url encoding of
the UTF-8 string "Bob".  The "epk" parameter is used to communicate
the sender's (Alice's) ephemeral public key value to the recipient
(Bob).

.. code-block:: javascript

     {"alg":"ECDH-ES",
      "enc":"A128GCM",
      "apu":"QWxpY2U",
      "apv":"Qm9i",
      "epk":
       {"kty":"EC",
        "crv":"P-256",
        "x":"gI0GAILBdu7T53akrFmMyGcsF3n5dO7MmwNBHKW5SV0",
        "y":"SLW_xSffzlPWrHEVI30DHM_4egVwt3NQqeUD7nMFpps"
       }
     }

The resulting Concat KDF [NIST.800-56A] parameter values are:

   Z  This is set to the ECDH-ES key agreement output.  (This value is
      often not directly exposed by libraries, due to NIST security
      requirements, and only serves as an input to a KDF.)

   keydatalen  This value is 128 - the number of bits in the desired
      output key (because "A128GCM" uses a 128 bit key).

   AlgorithmID  This is set to the octets representing the UTF-8 string
      "A128GCM" - [65, 49, 50, 56, 71, 67, 77].

   PartyUInfo  This is set to the octets representing the 32 bit big
      endian value 5 - [0, 0, 0, 5] - the number of octets in the
      PartyUInfo content "Alice", followed, by the octets representing
      the UTF-8 string "Alice" - [65, 108, 105, 99, 101].

   PartyVInfo  This is set to the octets representing the 32 bit big
      endian value 3 - [0, 0, 0, 3] - the number of octets in the
      PartyUInfo content "Bob", followed, by the octets representing the
      UTF-8 string "Bob" - [66, 111, 98].

   SuppPubInfo  This is set to the octets representing the 32 bit big
      endian value 128 - [0, 0, 0, 128] - the keydatalen value.

   SuppPrivInfo  This is set to the empty octet sequence.

The resulting derived key, represented as a base64url encoded value is:

::

     jSNmj9QK9ZGQJ2xg5_TJpA

( https://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-14#appendix-D )
