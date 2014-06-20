Appendix C. Example ECDH-ES Key Agreement Computation
====================================================================

This example uses ECDH-ES Key Agreement 
and the :term:`Concat KDF` to derive the :term:`Content Encryption Key` (CEK) 
in the manner described in :ref:`Section 4.6 <jwa.4.6>`.  

In this example, 
the ECDH-ES Direct Key Agreement mode ("alg" value "ECDH-ES") 
is used to produce an agreed upon key for AES
GCM with a 128 bit key ("enc" value "A128GCM").

In this example, a sender Alice is encrypting content to a recipient
Bob. The sender (Alice) generates an ephemeral key for the key
agreement computation.  

Alice's :term:`ephemeral key` (in JWK format) used
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

Header Parameter values used in this example are as follows.  
In this example, 
the "apu" (agreement PartyUInfo) parameter value is the
base64url encoding of the UTF-8 string "Alice" and 
the "apv" (agreement PartyVInfo) parameter value is 
the base64url encoding of the UTF-8 string "Bob".  

.. code-block:: python

    $ python -c "import base64;print base64.urlsafe_b64encode('Bob').replace('=','');"
    Qm9i

    $ python -c "import base64;print base64.urlsafe_b64encode('Alice').replace('=','');"
    QWxpY2U


The "epk" parameter is used to communicate
the sender's (Alice's) ephemeral public key value 
to the recipient (Bob).

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


   Z  
      This is set to the ECDH-ES key agreement output.  (This value is
      often not directly exposed by libraries, due to NIST security
      requirements, and only serves as an input to a KDF.)  In this
      example, Z is the octet sequence(using JSON array notation):

      .. code-block:: javascript

          [158, 86, 217, 29, 129, 113, 53, 211, 114, 131, 66, 131, 191, 132,
          38, 156, 251, 49, 110, 163, 218, 128, 106, 72, 246, 218, 167, 121,
          140, 254, 144, 196].

   keydatalen  
      This value is 128 - the number of bits in the desired
      output key (because "A128GCM" uses a 128 bit key).

   AlgorithmID  
      This is set to the octets representing the 32 bit big
      endian value 7 - [0, 0, 0, 7] - the number of octets in the
      AlgorithmID content "A128GCM", followed, by the octets
      representing the UTF-8 string "A128GCM" - [65, 49, 50, 56, 71, 67,
      77].

   PartyUInfo  
      This is set to the octets representing the 32 bit big
      endian value 5 - [0, 0, 0, 5] - the number of octets in the
      PartyUInfo content "Alice", followed, by the octets representing
      the UTF-8 string "Alice" - [65, 108, 105, 99, 101].

   PartyVInfo  
      This is set to the octets representing the 32 bit big
      endian value 3 - [0, 0, 0, 3] - the number of octets in the
      PartyUInfo content "Bob", followed, by the octets representing the
      UTF-8 string "Bob" - [66, 111, 98].

   SuppPubInfo  
      This is set to the octets representing the 32 bit big
      endian value 128 - [0, 0, 0, 128] - the keydatalen value.

   SuppPrivInfo  
      This is set to the empty octet sequence.

Concatenating the parameters AlgorithmID through SuppPubInfo results
in an OtherInfo value of:

::

   [0, 0, 0, 7, 65, 49, 50, 56, 71, 67, 77, 0, 0, 0, 5, 65, 108, 105,
   99, 101, 0, 0, 0, 3, 66, 111, 98, 0, 0, 0, 128]

Concatenating the round number 1 ([0, 0, 0, 1]), Z, and the OtherInfo
value results in the Concat KDF round 1 hash input of:

::

   [0, 0, 0, 1,
   158, 86, 217, 29, 129, 113, 53, 211, 114, 131, 66, 131, 191, 132, 38,
   156, 251, 49, 110, 163, 218, 128, 106, 72, 246, 218, 167, 121, 140,
   254, 144, 196,
   0, 0, 0, 7, 65, 49, 50, 56, 71, 67, 77, 0, 0, 0, 5, 65, 108, 105, 99,
   101, 0, 0, 0, 3, 66, 111, 98, 0, 0, 0, 128]

The resulting derived key, which is the first 128 bits of the round 1
hash output is:

::

   [86, 170, 141, 234, 248, 35, 109, 32, 92, 34, 40, 205, 113, 167, 16,
   26]

The base64url encoded representation of this derived key is:

::

     VqqN6vgjbSBcIijNcacQGg

(draft20)
