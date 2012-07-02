.. list-table:: Request

    *   - 
        - OAuth
        - OAuth
        - OAuth
        - OAuth
        - Connect
        - Connect
        - Connect

    *   - (profile)
        - Code
        - Implicit
        - Owner Password
        - Client Credential
        - Basic
        - Implict
        - Standard

    *   - response_type
        - REQUIRED 

          ("code")

        - REQUIRED 

          ("token")

        - (N/A) 
        - (N/A) 
        - REQUIRED 

          ("code")

        - REQUIRED 

          ("token id_token") 

        - REQUIRED 

          ("code" , "code id_token","id_token","token","token id_token","code token","code token id_token")

    *   - client_id 
        - REQUIRED
        - REQUIRED 
        - (N/A) 
        - (N/A) 
        - REQUIRED 
        - REQUIRED 
        - REQUIRED 

    *   - redirect_uri 
        - OPTIONAL
        - OPTIONAL
        - (N/A) 
        - (N/A) 
        - REQUIRED 
        - REQUIRED
        - REQUIRED

    *   - scope
        - OPTIONAL
        - OPTIONAL
        - (N/A) 
        - (N/A) 
        - REQUIRED
        - REQUIRED 
        - REQUIRED 

          ("openid (+ ["profile", "email", "address", "phone" ]))

    *   - state
        - RECOMMENDED
        - RECOMMENDED
        - (N/A) 
        - (N/A) 
        - RECOMMENDED 
        - RECOMMENDED 
        - RECOMMENDED

    *   - nonce
        - (N/A) 
        - (N/A) 
        - (N/A) 
        - (N/A)
        - (N/A)
        - OPTIONAL 
        - OPTIONAL 

    *   - display
        - (N/A)
        - (N/A)
        - (N/A)
        - (N/A)
        - OPTIONAL
        - OPTIONAL
        - OPTIONAL

    *   - prompt
        - (N/A)
        - (N/A)
        - (N/A)
        - (N/A)
        - OPTIONAL
        - OPTIONAL
        - OPTIONAL

    *   - request
        - (N/A)
        - (N/A)
        - (N/A)
        - (N/A)
        - (N/A)
        - (N/A)
        - OPTIONAL

    *   - request_uri
        - (N/A)
        - (N/A)
        - (N/A)
        - (N/A)
        - (N/A)
        - (N/A)
        - OPTIONAL

    *   - id_token
        - (N/A)
        - (N/A)
        - (N/A)
        - (N/A)
        - (N/A)
        - (N/A)
        - OPTIONAL
