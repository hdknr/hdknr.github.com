.. This is sample documentation file for sphinxjp.themes.impressjs.

======================================================
About Digital Identity
======================================================

.. impressjs:: title
   :data-x: 0
   :data-y: 0
   :data-z: -1000
   :data-rotate-x: -90
   :data-scale: 4

    *About Digital Identity*


    .. container:: memo

        <hit space to proceed, or use arrows>

.. impressjs:: AuthN/AuthZ
   :data-x: 1000
   :data-y: 800
   :data-rotate: 180
   :data-rotate-y: -270
   :data-scale: 5

    *AuthN/AuthZ*

    .. container:: bigitems

        * AutheNtication
            - on Subject
            - Principal Token

        * AuthoriZation 
            - on Object
            - Access Token

        * Token
            - Assertion
            - Artifact 
                - Artifact is exchanged to Assertion at Issuer

.. impressjs:: Authetication
   :data-x: -1000
   :data-y: -800
   :data-rotate-y: -300
   :data-scale: 1

    *Authentication*

    .. container:: bigitems

        * Authenticator & Process 

        * Context
            
.. impressjs:: Authetication/Autheticator
   :data-x: -1000
   :data-y: -800
   :data-rotate-y: -300
   :data-scale: 1

    *Authentication/Authenticator*

    .. container:: bigitems

        * Endpoint
            - Principal Authentication Endpoint
            - Resource Endpoint 
                - Principal Assertion or Access Token

        * Primary & Secondary
            - Primary Authenticator ( mainly on Principal Authentication Endpoint )
            - Secondary Authenticator( mainly on Resource Endpoint )
                - Secondary Authenticator bound to a Principal at Principal Authentication Endpoint

        * Authenticator
            - Credential 
            - Assertion
    
        * Process 
            - Secondary Authenticator Validation ( Cookie ... )
            - HTTP Authentication (Basic,Digest...)
            - Credential Validation 
            - Assertion Validation Protocol ( SAML,Connect,...)
            
.. END
