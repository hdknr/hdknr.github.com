Appendix F.  Document History
==========================================

[[ to be removed by the RFC editor before publication as an RFC ]]

   -14

   o  Removed "PBKDF2" key type and added "p2s" and "p2c" header
      parameters for use with the PBES2 algorithms.

   o  Made the RSA private key parameters that are there to enable
      optimizations be RECOMMENDED rather than REQUIRED.

   o  Added algorithm identifiers for AES algorithms using 192 bit keys
      and for RSASSA-PSS using HMAC SHA-384.

   o  Added security considerations about key lifetimes, addressing
      issue #18.

   o  Added an example ECDH-ES key agreement computation.

   -13

   o  Added key encryption with AES GCM as specified in
      draft-jones-jose-aes-gcm-key-wrap-01, addressing issue #13.

   o  Added security considerations text limiting the number of times
      that an AES GCM key can be used for key encryption or direct
      encryption, per Section 8.3 of NIST SP 800-38D, addressing issue
      #28.

   o  Added password-based key encryption as specified in
      draft-miller-jose-jwe-protected-jwk-02.

   -12

   o  In the Direct Key Agreement case, the Concat KDF AlgorithmID is
      set to the octets of the UTF-8 representation of the "enc" header
      parameter value.

   o  Restored the "apv" (agreement PartyVInfo) parameter.

   o  Moved the "epk", "apu", and "apv" Header Parameter definitions to
      be with the algorithm descriptions that use them.

   o  Changed terminology from "block encryption" to "content
      encryption".

   -11

   o  Removed the Encrypted Key value from the AAD computation since it
      is already effectively integrity protected by the encryption
      process.  The AAD value now only contains the representation of
      the JWE Encrypted Header.

   o  Removed "apv" (agreement PartyVInfo) since it is no longer used.

   o  Added more information about the use of PartyUInfo during key
      agreement.

   o  Use the keydatalen as the SuppPubInfo value for the Concat KDF
      when doing key agreement, as RFC 2631 does.

   o  Added algorithm identifiers for RSASSA-PSS with SHA-256 and SHA-
      512.

   o  Added a Parameter Information Class value to the JSON Web Key
      Parameters registry, which registers whether the parameter conveys
      public or private information.

   -10

   o  Changed the JWE processing rules for multiple recipients so that a
      single AAD value contains the header parameters and encrypted key
      values for all the recipients, enabling AES GCM to be safely used
      for multiple recipients.

   -09

   o  Expanded the scope of the JWK parameters to include private and
      symmetric key representations, as specified by
      draft-jones-jose-json-private-and-symmetric-key-00.

   o  Changed term "JWS Secured Input" to "JWS Signing Input".

   o  Changed from using the term "byte" to "octet" when referring to 8
      bit values.

   o  Specified that AES Key Wrap uses the default initial value
      specified in Section 2.2.3.1 of RFC 3394.  This addressed issue
      #19.

   o  Added Key Management Mode definitions to terminology section and
      used the defined terms to provide clearer key management
      instructions.  This addressed issue #5.

   o  Replaced "A128CBC+HS256" and "A256CBC+HS512" with "A128CBC-HS256"
      and "A256CBC-HS512".  The new algorithms perform the same
      cryptographic computations as [I-D.mcgrew-aead-aes-cbc-hmac-sha2],
      but with the Initialization Vector and Authentication Tag values
      remaining separate from the Ciphertext value in the output
      representation.  Also deleted the header parameters "epu"
      (encryption PartyUInfo) and "epv" (encryption PartyVInfo), since
      they are no longer used.

   o  Changed from using the term "Integrity Value" to "Authentication
      Tag".

   -08

   o  Changed the name of the JWK key type parameter from "alg" to
      "kty".

   o  Replaced uses of the term "AEAD" with "Authenticated Encryption",
      since the term AEAD in the RFC 5116 sense implied the use of a
      particular data representation, rather than just referring to the
      class of algorithms that perform authenticated encryption with
      associated data.

   o  Applied editorial improvements suggested by Jeff Hodges.  Many of
      these simplified the terminology used.

   o  Added seriesInfo information to Internet Draft references.

   -07

   o  Added a data length prefix to PartyUInfo and PartyVInfo values.

   o  Changed the name of the JWK RSA modulus parameter from "mod" to
      "n" and the name of the JWK RSA exponent parameter from "xpo" to
      "e", so that the identifiers are the same as those used in RFC
      3447.

   o  Made several local editorial changes to clean up loose ends left
      over from to the decision to only support block encryption methods
      providing integrity.

   -06

   o  Removed the "int" and "kdf" parameters and defined the new
      composite Authenticated Encryption algorithms "A128CBC+HS256" and
      "A256CBC+HS512" to replace the former uses of AES CBC, which
      required the use of separate integrity and key derivation
      functions.

   o  Included additional values in the Concat KDF calculation -- the
      desired output size and the algorithm value, and optionally
      PartyUInfo and PartyVInfo values.  Added the optional header
      parameters "apu" (agreement PartyUInfo), "apv" (agreement
      PartyVInfo), "epu" (encryption PartyUInfo), and "epv" (encryption
      PartyVInfo).

   o  Changed the name of the JWK RSA exponent parameter from "exp" to
      "xpo" so as to allow the potential use of the name "exp" for a
      future extension that might define an expiration parameter for
      keys.  (The "exp" name is already used for this purpose in the JWT
      specification.)

   o  Applied changes made by the RFC Editor to RFC 6749's registry
      language to this specification.

   -05

   o  Support both direct encryption using a shared or agreed upon
      symmetric key, and the use of a shared or agreed upon symmetric
      key to key wrap the CMK.  Specifically, added the "alg" values
      "dir", "ECDH-ES+A128KW", and "ECDH-ES+A256KW" to finish filling in
      this set of capabilities.

   o  Updated open issues.

   -04

   o  Added text requiring that any leading zero bytes be retained in
      base64url encoded key value representations for fixed-length
      values.

   o  Added this language to Registration Templates: "This name is case
      sensitive.  Names that match other registered names in a case
      insensitive manner SHOULD NOT be accepted."

   o  Described additional open issues.

   o  Applied editorial suggestions.

   -03

   o  Always use a 128 bit "authentication tag" size for AES GCM,
      regardless of the key size.

   o  Specified that use of a 128 bit IV is REQUIRED with AES CBC.  It
      was previously RECOMMENDED.

   o  Removed key size language for ECDSA algorithms, since the key size
      is implied by the algorithm being used.

   o  Stated that the "int" key size must be the same as the hash output
      size (and not larger, as was previously allowed) so that its size
      is defined for key generation purposes.

   o  Added the "kdf" (key derivation function) header parameter to
      provide crypto agility for key derivation.  The default KDF
      remains the Concat KDF with the SHA-256 digest function.

   o  Clarified that the "mod" and "exp" values are unsigned.

   o  Added Implementation Requirements columns to algorithm tables and
      Implementation Requirements entries to algorithm registries.

   o  Changed AES Key Wrap to RECOMMENDED.

   o  Moved registries JSON Web Signature and Encryption Header
      Parameters and JSON Web Signature and Encryption Type Values to
      the JWS specification.

   o  Moved JSON Web Key Parameters registry to the JWK specification.

   o  Changed registration requirements from RFC Required to
      Specification Required with Expert Review.

   o  Added Registration Template sections for defined registries.

   o  Added Registry Contents sections to populate registry values.

   o  No longer say "the UTF-8 representation of the JWS Secured Input
      (which is the same as the ASCII representation)".  Just call it
      "the ASCII representation of the JWS Secured Input".

   o  Added "Collision Resistant Namespace" to the terminology section.

   o  Numerous editorial improvements.

   -02

   o  For AES GCM, use the "additional authenticated data" parameter to
      provide integrity for the header, encrypted key, and ciphertext
      and use the resulting "authentication tag" value as the JWE
      Authentication Tag.

   o  Defined minimum required key sizes for algorithms without
      specified key sizes.

   o  Defined KDF output key sizes.

   o  Specified the use of PKCS #5 padding with AES CBC.

   o  Generalized text to allow key agreement to be employed as an
      alternative to key wrapping or key encryption.

   o  Clarified that ECDH-ES is a key agreement algorithm.

   o  Required implementation of AES-128-KW and AES-256-KW.

   o  Removed the use of "A128GCM" and "A256GCM" for key wrapping.

   o  Removed "A512KW" since it turns out that it's not a standard
      algorithm.

   o  Clarified the relationship between "typ" header parameter values
      and MIME types.

   o  Generalized language to refer to Message Authentication Codes
      (MACs) rather than Hash-based Message Authentication Codes (HMACs)
      unless in a context specific to HMAC algorithms.

   o  Established registries: JSON Web Signature and Encryption Header
      Parameters, JSON Web Signature and Encryption Algorithms, JSON Web
      Signature and Encryption "typ" Values, JSON Web Key Parameters,
      and JSON Web Key Algorithm Families.

   o  Moved algorithm-specific definitions from JWK to JWA.

   o  Reformatted to give each member definition its own section
      heading.

   -01

   o  Moved definition of "alg":"none" for JWSs here from the JWT
      specification since this functionality is likely to be useful in
      more contexts that just for JWTs.

   o  Added Advanced Encryption Standard (AES) Key Wrap Algorithm using
      512 bit keys ("A512KW").

   o  Added text "Alternatively, the Encoded JWS Signature MAY be
      base64url decoded to produce the JWS Signature and this value can
      be compared with the computed HMAC value, as this comparison
      produces the same result as comparing the encoded values".

   o  Corrected the Magic Signatures reference.

   o  Made other editorial improvements suggested by JOSE working group
      participants.

   -00

   o  Created the initial IETF draft based upon
      draft-jones-json-web-signature-04 and
      draft-jones-json-web-encryption-02 with no normative changes.

   o  Changed terminology to no longer call both digital signatures and
      HMACs "signatures".


( https://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-14#appendix-F )
