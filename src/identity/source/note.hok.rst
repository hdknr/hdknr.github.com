============================
Holder-of-Key JWS
============================

by HDKNR

For higher LoA, 
OpenID Connect with JWS may support holder-of-key tokens, 
and Connect request may support TLS with client certificates.  
Mimicking some great SAML works is easy to do those :
`SAML V2.0 Holder-of-Key Assertion Profile Version 1.0 <http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml2-holder-of-key.html>`_ and 
`SAML V2.0 Holder-of-Key Web Browser SSO Profile Version 1.0 <http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-holder-of-key-browser-sso.html>`_ .

JWS
====

:doc:`jws` is easily extended to include a holder-of-key info, i,e, **X.509 Data** in SAML HoK. 
I'm not sure if we have to provide multiple X.509 Data in a single JWS token now.
JWS Header may have "**sbj**", 
which  means "subject confirmation" 
and is equal to **<saml:SubjectConfirmationData>** in SAML HoK. 

"**sbj**" claims contains JSON object 
in which describes a certificate for  the "**atesting entity**".    
"atesting entity" can be an **End-User** 
if the JWS token is an **Identity Token(id_token)** of Connect, 
also a Relying Party if the JWS token is **Access Token(access_token)** of OAuth.

JWS with "**sbj**" looks like this:


.. code-block:: javascript

    {
        "alg": "RS256",
        "typ": "access_token",
        "x5u": "public key url for issuing party(authz server)",
        "sbj": 
            {
                "x5c": "copy of OAuth client's certificate"    
            }
    }

"sbj" must one of 4 claims if we follow the SAML HoK:

    1. "x5c"
            Base64url encoding copy of atesting entity's  X.509 certificate.

    2. "x5i"
            Copy of "**Subject Key Identitier**"  in atesting entity's  X.509 certificate.

    3. "x5s"
            Serial number isseud by a Certificate Authority in atesting entity's  X.509 certificate.   

    4. "x5n"
            Copy of  "**DN(Distinguished Name)**" in atesting entity's  X.509 certificate.


"x5c" is best for server entities to validate holder-of-key, but too big for a JWS token.
"x5i" > "x5s" > "x5n" may be the best order in rest. But "x5i" is only for certificates which 
inlcude extended parameter. So "x5s" may be MUST if entities in a OAuth/Connect circle support holder-of-key.


Endpoints
==========

OAuth and Connect endpoints SHOULD accept TLS with client certifaictes if they supoort holder-of-key validation.
Such endpoints may be Authorization endpoints, Token endpoints,Resource endpoints and Request Registraton endpoinst of Connect.
Endpoints may simplly follow the SAML HoK tao.

Implict Flow
=============

If the case is without a Request Registration of Connect, 
there is no chance for an issuer(Authz Server) 
to check the Relying Party's client certificate for the Implicit Flow.
If an issuer thinks of the registered certificate as the valid X.509 certificate,
it may work.

If a case is for javascript access to resource with HoK-ed JWS access token, 
JWS '**sbj**' is for End-User('s User Agent).
That needs some tricky selection flow at Authorization Endpoint.

sbj for ID Token
==================

This may be restricted to the case in which id_token is used as User Agent session cookie for Issuer to authenticate the User Agent.
User Agent should be installed End User's client certificated at his computer.


.. note::
    - But, it MUST be too big to use in session cookie if sbj is a copy of a certificate.
    - Because End User's client certificate MUST be disclosed to RPs, this might not be good idea.
