.. note::

    .. list-table:: ID Token/Session Token
        :widths: 40 30 30


        *   - Claim
            - OIDC(ID Token)
            - OAuth Auth(ID Token/Session Token)
    
        *   - iss(Issuer Identifier)
            - REQUIRED 
            - REQUIRED

        *   - sub(Subject identifier)
            - REQUIRED(String Array/String)
            - REQUIRED(client_id)

        *   - aud(Audience Identifier(s))
            - REQUIRED
            - REQUIRED

        *   - exp(Expiration Time)
            - REQUIRED
            - REQUIRED

        *   - iat(Issued At)
            - REQUIRED
            - REQUIRED

        *   - auth_time
            - REQUIRED
            - REQUIRED

        *   - nonce
            - `OPTIONAL <basic.html#term-nonce>`_
            - N/A 

        *   - at_hash(Access Token hash value)
            - OPTIONAL
            - N/A

        *   - :term:`acr` (:term:`Authentication Context Class Reference`)
            - OPTIONAL
            - N/A

        *   - amr(Authentication Methods References)
            - `OPTIONAL <basic.html#term-amr>`_
            - `OPTIONAL <oauth_auth.html#term-amr>`_

        *   - :term:`azp` (Authorized Party)
            - OPTIONAL/REQUIRED
            - N/A

        *   - :term:`profile`
            - N/A
            - OPTIONAL

        *   - alv(:term:`Authentication Assurance Level`) 
            - `N/A <basic.html#term-acr>`_
            - `OPTIONAL <oauth_auth.html#term-alv>`_
