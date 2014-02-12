
A.3. Example Symmetric Keys
------------------------------


The following example JWK Set contains two symmetric keys represented
as JWKs: one designated as being for use with the AES Key Wrap
algorithm and a second one that is an HMAC key.  (Line breaks are for
display purposes only.)

.. code-block:: javascript

     {"keys":
       [
         {"kty":"oct",
          "alg":"A128KW",
          "k":"GawgguFyGrWKav7AX4VKUg"},

         {"kty":"oct",
          "k":"AyM1SysPpbyDfgZld3umj1qzKObwVMkoqQ-EstJQLr_T-1qS0gZH75
     aKtMN3Yj0iPS4hcgUuTwjAzZr1Z9CAow",
          "kid":"HMAC key used in JWS A.1 example"}
       ]
     }

(draft20)
