========
Terms
========


Digital Identity
=====================

.. glossary::

    Identity
        `ISO and ITU-T defines "identity" as the "set of attributes about an entity"
        <http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20111212/001338.html>`_ by Nat.

        `"Digital Identity - the digital representation of a set of claims made by one digital subject about itself or another digital subject"
        <http://en.wikipedia.org/wiki/Digital_identity>`_ by Wikipedia

            - refered at :ref:`messages_abstract` of :doc:`messages`

Computing
=====================

.. glossary::
    :sorted:

    REST
        `Representational state transfer (REST) is 
        a style of software architecture for distributed hypermedia systems such as the World Wide Web
        <http://en.wikipedia.org/wiki/REST>`_ by Wikipedia

    RESTful
        `Conforming to the REST constraints is referred to as being "RESTful".` by :term:`Wikipedia <REST>`
        
    
    RESTful manner
        :term:`RESTful` style of computing. 
        
        - How :term:`RESTful` OpenID Connect suite ?

Connect
==========

.. glossary::

    Simple Request Method
        :ref:`standard_2_3_1_1`

    Request Parameter Method
        :ref:`standard_2_3_1_2`

    Authorization Header Method
        :ref:`bearer.2.1`


    digitalSignature
        ":ref:`messages_4_3`". X.509 Key Usage (TBD)

    keyEncipherment
        ":ref:`messages_4_4`". X.509 Key Usage (TBD)

    Key Usage
        (TBD) X.509 Key Usage

    Endpoint
    Endpoints
        (TBD)
        

    Session Management Endpoint
    Session Management Endpoints
        (TBD)

    Authentication Context Class Reference
    Authentication Context Class References
        `Supported SAML Authentication Context Classes and Strengths
        <http://technohidelic.posterous.com/supported-saml-authentication-context-classes>`_

    Entity Authentication Assurance Level
        (TBD)( :ref:`messages_1_1` )

    PAPE
        (TBD)( :ref:`messages_1_2` )

    nist_auth_level
        (TBD)( :ref:`messages_1_2` )
        
    ID Tokens
        :term:`ID Token`

    ID Token Verification
        (TBD) ( :ref:`messages_2_1_1` ) 

    openid
        (TBD) openid scope ? ( :ref:`messages_2_1_2` )
    
    client_secret
        (TBD) 

    KeyWrap
        (TBD)
    
    Content Encryption Key
        (TBD)

    Request Object    
        (TBD)

    Discovery Document
        (TBD)

    Signed Request Object
        (TBD)

    Signature Verification
        (TBD)

    Client Registration
        (TBD)

    Authorization Request Message
    Authorization Request Messages
        (TBD)

    User ID Claim
        (TBD)

    Signing Algorithms
        (TBD)

    .well-known
        (TBD)

    Direct Configuration
        (TBD)

    Host
        (TBD)

    Normalization Rules
        For :term:`SWD`. See ":ref:`discovery.2.1` .

    Identifier Normalization
        See ":ref:`discovery.2.1`".

    User Identifier
        (TBD)  ( :ref:`discovery.2.1` )

    Openid Provider
        (TBD)

    Port
        (TBD)

    Provider Discovery
        (TBD)

    Service
        (TBD)

    Tls/Ssl Server Certificate Check
        (TBD)

    URI Scheme
        (TBD)

    Issuer
        (TBD)

    Openid Provider Configuration Document
        (TBD)

    Public Key Location
        (TBD)

    Server Certificate Check
        (TBD)

    SWD Host
        (TBD)

    SWD Principal
        (TBD)

    Unicode Code Points
        (TBD)

OAuth
==========

.. glossary::
    :sorted:

    OAuth
    OAuth 2.0
        :doc:`oauth`

    Authorization Grant Type 
        OAuth grant types defined in :ref:`Section 1.3 <oauth_1_3>`.

    Client Identifier
        :ref:`oauth_2_2`

    Client Authentication
        ( TODO )

    Client Credentials
        See ":ref:`oauth_1_3_4`" .
    
    Grant Type
        :term:`Authorization Grant Type`

    Grant Types
        :term:`Grant Type`

    Protected Resource
        ( TODO  )

    Protected Resources
        :term:`Protected Resource`

    Resource Server
        ":doc:`oauth` " defines a :term:`resource server` as a :ref:`role <oauth_1_1>`. 

    Resource Servers
        :term:`Resource Server`        

    Authorization Code
        :ref:`oauth_1_3_1`

    Authorization Server
        ( TODO ) 

    Authorization Servers
        :term:`Authorization Server`

    Authorization Endpoint
        (  TODO  ) 

    Authorization Request
        (  TODO  ) 

    Authorization Requests
        :term:`Authorization Request`

    Authorization Response
        (  TODO  ) 

    Token Request
        (  TODO  ) 

    Token Requests
        :term:`Token Request`

    Token Response
        (  TODO  ) 

    Authorization Endpoint Request
        :term:`Authorization Request`

    Authorization Endpoint Response
        :term:`Authorization Response`

    Token Endpoint Request
        :term:`Token Request`

    Token Endpoint Response
        :term:`Token Response`

    Access Token
    Access Tokens
        - ":ref:`oauth_5`" in :term:`OAuth` describes access token response at :term:`Token Endpoint`
        - ":ref:`oauth_1_4`" describes what access token is generally in OAuth.

    Access Token Request
    Access Token Requests
        (TBD)

    Access Token Response
    Access Token Responses
        (TBD)

    Refresh Token
        :ref:`oauth_1_5`

    Refresh Tokens
        :term:`Refresh Token`

    Authorization Scope
    Scope
    Access Token Scope
        See  ":ref:`oauth_3_3`"

    Scopes
        :term:`Scope`

    Public Client
        :ref:`oauth_2_1`

    Confidential Client
        :ref:`oauth_2_1`

    Response Type
        :term:`response_type`

    Response Types
        :term:`response_type`

    OAuth Parameters Registry
        :ref:`oauth_11_2`

    Server
        ( TODO )
    
    Client
        ( TODO )

JSON Something
===============

.. glossary::

    JSON
        ( TODO )

    jku
        JSON (Web) Key URL. 
        An absolute URL that refers to a resource for a set of JSON-encoded public keys, 
        one of which corresponds to the key that was used to sign the :term:`JWS`.
        See ":ref:`jws.table.1`".

    Certificate Chains
        (TODO) ( :ref:`jwk.abstract` )
    
    JSON Claims Object
        (TODO)

    URI Query Parameters
        ( TBD )

    base64url
        ( TBD )

    JWE Plaintext
        ( TBD )

    Algorithm
        ( TBD )

    Encryption Method
        ( TBD ) ( :ref:`jwt.5` )

    JWS Header Parameters
        ( TBD ) ( :ref:`jwt.5` )    

    JWE Header Parameters
        ( TBD ) ( :ref:`jwt.5` )    

SAML
======

.. glossary::

    Identity Provider
        IdP (TBD)
        
    Service Provider
        SP (TBD)

    Public Key
        (TBD)

    Private Key 
        (TBD)

    Artifact Resolution Profile
        (TBD)

    Holder-of-Key Web Browser SSO
    Holder-of-Key Web Browser SSO Profile
        (TBD)

    Relay State Mechanizm
        (TBD)

    Holder-of-Key 
        (TBD) 

    Holder-of-Key Assertions
    Holder-of-Key SAML Assertions
        (TBD)

    Certificate Issuer
        (TBD)


    Client Certificates
        (TBD)


    Der
        (TBD)


    Holder-Of-Key
        (TBD)


    Holder-Of-Key Subject Confirmation
        (TBD)


    Issuer Dn
        (TBD)


    Issuer Serial Number
        (TBD)


    Nist
        (TBD)


    Private Key
        (TBD)


    Relaystate Mechanism
        (TBD)


    Saml Assertion
        (TBD)


    Saml Issuers
        (TBD)


    Saml Relying Party
        (TBD)


    Saml Response
        (TBD)


    Security Context
        (TBD)


    Ski
        (TBD)


    Ski Extension
        (TBD)


    Sstc
        (TBD)


    Subject Distinguished Name
        (TBD)


    Subject Key Identifier
        (TBD)


    The Service Provider
        (TBD)


    Tls Handshake
        (TBD)


    Tls Session Key
        (TBD)


    Trust Relationship
        (TBD)


    Trusted Certificate
        (TBD)


    User Agent
        (TBD)


    Web Browser Sso
        (TBD)

    X.509 Issuer
        (TBD)

    Xml Signature
        (TBD)

    Asn.1 Encoding
    Asn.1 Encodings
        (TBD)

    Authentication Request
        (TBD)

    Authentication Statement
        (TBD)

    Bearer Subject Confirmation
        (TBD)

    Ber
        (TBD)

    Cer
        (TBD)



Others
========

.. glossary::

    Direct Communication
        Direct communication is a Client to Server communication which does not pass through the User-Agent.

    Indirect Communication
        In indirect communication, messages are passed through the User-Agent.

    Check Session Endpoint
        A protected resource that, when presented with an access token by the client, returns authentication information about the user represented by that access token.

    UserInfo Request
        (TBD)

    UserInfo Response
        (TBD)
 
    User Info Endpoint
    UserInfo Endpoint
        A protected resource that, when presented with an access token by the client, returns authorized information about the user represented by that access token.

    Query String
        ( TODO )

    Fragment
        ( TODO ) 

    Query String Serialization
        In order to serialize the parameters using the query string serialization, the client constructs the string by adding the following parameters to the end-user authorization endpoint URI query component using the application/x-www-form-urlencoded format as defined by [W3C.REC‑html401‑19991224] (Hors, A., Jacobs, I., and D. Raggett, “HTML 4.01 Specification,” December 1999.).

    GSA
        U.S. General Service Administartion.  http://www.gsa.gov/

    ISO 29115
        ISO/IEC 29115 Entity Authentication Assurance Framework.

    HMAC-SHA
        :term:`HMAC`

    Connect
        :doc:`openid_connect`  

    audience
        (  TODO  ) 

    nonce
        (  TODO  ) 

    schema
        Metadata for JSON returned by :term:`UserInfo Endpoint` (":ref:`basic_4_1`").

    PPID
        Pairwise Pseudonymous Identifier. A set of identifiers bound for a single principal, and each of them is shared in each relation of entities.    
        See :ref:`accounts_overview_PPID` .

    SCIM
        Mortimer, C., Smarr, J., Harding, P., and P. Madsen, “Simple Cloud Identity Management: Core Schema 1.0,” June 2011.
        ( http://www.simplecloud.info/specs/draft-scim-core-schema-01.html )

    vCard 
        ( TODO )

    PortableContacts
        ( TODO ) 

    UserInfo
        ( TODO ) 

    scope
        :term:`OAuth` grant request parameter. See " :ref:`oauth_3_3` ".

         See :ref:`accounts_overview_scope` sample implementation.

    URI Query String Serialization
        Never used by the world other than OpenID/Connect community.  ( :ref:`basic_3_2_1` )

    accounts
        sample applciaiton in which OpenID/Connect is implemented. :doc:`accounts_overview`
        
    Request File Registration Service
        ( TODO )

    Query Component
        ( TODO ) 

    SP800_63
        :doc:`nist-sp-800-63` 

    Two Factor Authentication
        Two-factor authentication (TFA, T-FA or 2FA) is an approach to authentication 
        which requires the presentation of two different kinds of evidence that someone is who they say they are. 
        It is a part of the broader family of multi-factor authentication, 
        which is a defense in depth approach to security. 
        From a security perspective, the idea is to use evidences which have separate range of attack vectors 
        (e.g. logical, physical) leading to more complex attack scenario and consequently, lower risk.
        ( `To Factoor Authenticatkon - Wikipedia <http://en.wikipedia.org/wiki/Two-factor_authentication>`_ )

    Implicit Flow
        ( TODO ) 

    Authorization Code Flow
        ( TODO )

    End-User
        ( TODO )

    End-User Consent
        ( TODO ) 

    SSL
        ( TODO ) 


    HMAC
        ( TODO )

    IMEI
        IMEI is short for International Mobile Equipment Identity and is a unique number given to every single mobile phone.
        `IMEI - Wikipedia <http://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity>`_ .

    
    X-FRAME-OPTION
        The X-Frame-Options HTTP response header can be used to indicate 
        whether or not a browser should be allowed to render a page in a <frame> or <iframe>. 
        Sites can use this to avoid :term:`clickjacking` attacks, by ensuring that their content is not embedded into other sites.

    TLS
        ( TODO )
    
    End-User Authorization Endpoint
        :term:`Authorization Endpoint`

    Sammer
        Slang a person who perpetrates a scam; swindler ( `FreeDictionaly <http://www.thefreedictionary.com/scammer>`_)

    Open Redirectors
        ( TODO )

    Redirection URI
        ( TODO )

    Token
        There are lots of "tokes" defined around in :term:`OAuth` and :term:`Connect` .  
        A "token" may refer to an :term:`Access Token` and somtimes to :term:`Refresh Token`, or both.

    Tokens
        :term:`Token`
    
    Duration
        ( TODO ) 

    Javascript Framebusting
        ( TODO )

    Static Registration
        ( TODO )

    Dynamic Registration
        ( TODO )

    Authorization Header
        ( TODO ) 

    Authorization Headers
        ( TODO ) 

    Clients
        :term:`Client`

    Client Secret
        ( TODO )
    
    Client Secrets
        ( TODO )

    Client ID
        ( TODO )

    Artifact
        ( TODO )

    IANA    
        ( TODO ) (:ref:`oauth_11_2` )
    
    IESG
        ( TODO ) (:ref:`oauth_11_2` )

    Designated Experts 
        ( TODO ) (:ref:`oauth_11_2` )

    Specification Required
        ( TODO ) (:ref:`oauth_11_2` )

Specs
=======

.. glossary::

    JWT
        :doc:`jwt`

    JWS
        :doc:`jws`

    JWE
        :doc:`jwe`

Attacks
==========

.. glossary::
    :sorted:

    CSRF
    XSRF
    XSRF Attacks
        ( TODO )

    Phishing
        ( TODO ) 

    Man-in-the-middle
        ( TODO )

    clickjacking
        Clickjacking is a malicious technique of tricking Web users into revealing confidential information 
        or taking control of their computer while clicking on seemingly innocuous web pages.
        (` Clickjacking - Wikipedia <http://en.wikipedia.org/wiki/Clickjacking>`_ ) .

    Session Fixation
        One person to fixate (set) another person's session identifier (SID). 
        Most session fixation attacks are web based, 
        and most rely on session identifiers being accepted from URLs (query string) or POST data.
        `Session Fixation <http://en.wikipedia.org/wiki/Session_fixation>`_ - Wikipedia.

    Session Poisoining
        Others change  some session data.
        `Session Poisoning <http://en.wikipedia.org/wiki/Session_poisoning>`_ - Wikipedia.

    Online Guessing
        (TBD)

    Pharming
        (TBD)

    Eavesdropping
        (TBD)

    Replay
    Replay Attack
    Replay Attacks
        (  TODO  ) 

        (TBD)
   
    Session Hijack
        (TBD) 
    


TBD
==========

.. glossary::
    :sorted:

    _claim_names Member
        (TBD)

    A128gcm
        (TBD)

    A256gcm
        (TBD)

    Access Grant
        (TBD)

    Access Token Endpoint
        (TBD)

    Access Token Grant Lifetimes
        (TBD)

    Access Token Grants
        (TBD)

    Authorization
        (TBD)

    Bearer
        (TBD)

    Bearer Tokens
        (TBD)

    Claim Source
        (TBD)

    Claims Sources
        (TBD)

    Client Authentication Parameters
        (TBD)

    Ecdh-Es
        (TBD)

    Ecdsa Signatures
        (TBD)

    Encryption Algorithm
        (TBD)

    Error Response
        (TBD)

    Hmac Signatures
        (TBD)

    Hs256
        (TBD)

    Hs384
        (TBD)

    Hs512
        (TBD)

    ID Token Request
        (TBD)

    Implicit
        (TBD)

    Integrated Integrity Check
        (TBD)

    Integrity
        (TBD)

    io3166?1
        (TBD)

    iso639?1
        (TBD)

    Jws Signed Jwt
        (TBD)

    Oauth2.0bearer
        (TBD)

    Openid Providers
        (TBD)

    Pairwise Pseudonymous Identifier
        (TBD)

    Path Component
        (TBD)

    Pem
        (TBD)

    Personally Identifiable Information
        (TBD)

    Plaintext Jwt
        (TBD)

    Public Signing Key
        (TBD)

    Redirect_uris
        (TBD)

    Refresh Token Request
        (TBD)

    Rs256
        (TBD)

    Rsa
        (TBD)

    Signature Algorithm
        (TBD)

    Simple Web Discovery
        (TBD)

    User
        (TBD)

    User_id_type
        (TBD)

    Userinfo Access Log
        (TBD)

    Userinfo Claims
        (TBD)

    Userinfo Data
        (TBD)

UMA
======

.. glossary::

    User Authorization Process
        (TBD)

    AM
        Access Manager

    Authorization API
        (TBD)

    Authorization API Endpoint
        (TBD)

    Authorization Code Grant Type
        (TBD)

    Configuration Data
        (TBD)

    Host Access Token
        (TBD)

    Host Registration Endpoint
        (TBD)

    Hostmeta
        (TBD)

    OAuth-Protected
        (TBD)

    OAuth2
        (TBD)

    Openid Connect
        (TBD)

    PDP
        Policy Decision Point

    PEP
        Policy Enforcement Point

    Permissions
        (TBD)

    Protection API
        (TBD)

    Protection API Endpoints
        (TBD)

    Registration Area
        (TBD)

    Requester Access Token
        (TBD)

    Requester Access Tokens
        (TBD)

    Resource Sets
        (TBD)

    RFC6415
        :rfc:6415

    UMA
        UMA Core protocol

    Uma-Protected
        (TBD)

    User Policies
        (TBD)

    AM Operator
        (TBD)

    Authorization Manager
        (TBD)

    Authorization Proxy
        (TBD)

    Authorizing Users
        (TBD)

    Host Operator
        (TBD)

    Hosts
        :term:`host`

    Phases 2
        :term:`Phase 2`

    Policy
        (TBD)

    Protected API
        (TBD)

    Requested Scope
        (TBD)

    Requesting Parties
        (TBD) :term:`Requester` ?


JWT
====

.. glossary::

    Cryptographic Hash Function
        (TBD)
    
    ECDSA
        (TBD)
    
    HMAC SHA-256
        (TBD)
    
    HMAC SHA-384
        (TBD)
    
    HMAC SHA-512
        (TBD)
    
    Iana JSON Web Encryption Algorithms
        (TBD)
    
    Iana JSON Web Signature Algorithms
        (TBD)
    
    JWS Secured Input
        (TBD)
    
    Mac
        (TBD)
    
    P-256
        (TBD)
    
    PKCS#1
        (TBD)
    
    RSA-PKCS1-1.5
        (TBD)
    
    RSASSA-PKCS1-V1_5
        (TBD)
    
    SHA-256
        (TBD)
    
    SHA-384
        (TBD)
    
    SHA-512
        (TBD)
    
    Shared Key
        (TBD)
    
    White Space
        (TBD)
    
    alg
        (TBD)
    
    enc
        (TBD)
    
    typ
        (TBD)


