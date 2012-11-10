================================================================================================================
NIST SP 800-56A:Recommendation for Pair-Wise Key Establishment Schemes Using Discrete Logarithm Cryptography
================================================================================================================


.. contents::
    :local:


5. CryptographicElements
==============================


.. _nist-sp-800-56a.5.8:

5.8. Key Derivation Functions for Key Agreement Schemes
------------------------------------------------------------------

An Approved key derivation function (KDF) shall be used 
to derive secret keying material from a shared secret. 

The output from a KDF shall only be used for secret keying material, 
such as 
a symmetric key used for data encryption or message integrity, 
a secret initialization vector, or 
a master key that will be used to generate other keys 
(possibly using a different process). 

Non-secret keying material (such as a non-secret initialization vector) 
shall not be generated using the shared secret.

Each call to the KDF requires a freshly computed shared secret, 
and this shared secret shall be zeroized immediately following its use. 

The derived secret keying material shall be computed in its entirety 
before outputting any portion of it. 

In schemes using only static keys, 
the freshly computed shared secret may be the same as the previous shared secret. 
In these cases, 
the initiator supplied nonce (NonceU, see :ref:`Section 6.3 <nist-sp-800-56a.6.3>`) 
used in the scheme will vary so the same :term:`keying material` is not regenerated.

The derived secret keying material may be parsed into one or more keys 
or other secret cryptographic keying material 
(for example, secret initialization vectors). 

If Key Confirmation (KC) or implementation validation testing are to be performed 
as specified in :ref:`Section 8 <nist-sp-800-54a.6.3>` or :ref:`Section 5.2.3 <nist-sp-800-56a.5.2.3>`, 
respectively, 
then the MAC key shall be formed from the first bits of the KDF output 
and zeroized after its use 
(i.e., the MAC key shall not be used for purposes other than key confirmation or implementation validation testing).

This section specifies two Approved KDFs for use in key establishment. 
The Approved methods are provided in :ref:`Section 5.8.1 <nist-sp-600-56a.5.8.1>` 
and :ref:`5.8.2 <nist-sp-600-56a.5.8.2>`. 

Other key derivation methods may be temporarily allowed for backward compatibility. 
These other allowable methods and any restrictions on their use will be specified 
in FIPS 140-2 Annex D. 

Any hash function used in a KDF shall be Approved (see Section 5.1) 
and shall also meet the selection requirements specified herein (see Section 5.5.1).

.. _nist-sp-600-56a.5.8.1:

5.8.1 Concatenation Key Derivation Function (Approved Alternative 1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

5.8.2 ASN.1 Key Derivation Function (Approved Alternative 2) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


