A.4.1.  JWE Per-Recipient Unprotected Headers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first recipient uses the RSAES-PKCS1-V1_5 algorithm to encrypt
the Content Encryption Key (CEK).  The second uses AES Key Wrap to
encrypt the CEK.  Key ID values are supplied for both keys.  The two
per-recipient header values used to represent these algorithms and
Key IDs are:

::

  {"alg":"RSA1_5","kid":"2011-04-29"}

and

::

  {"alg":"A128KW","kid":"7"}


(draft23)
