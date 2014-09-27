=======================================
Self-Issued Assertion 
=======================================

Sequence 
=============

1. Token Client : Start to ask Token Agent(SIOP) to issue an JWT Assertion
--------------------------------------------------------------------------------------------------

- An appcations called "theapp" may advertise its scheme as the "theapp://". 
- "theapp" find the authentication endpoint of a resource server "https://theres.com",
  i.e, "https://threres.com/auth/openid".
- "theapp" open the browser 
  with the uri "https://theres.com/auth/openid?assertion_issuer=https%3A//self-issued.me/&assertion_client=theapp%3A//assertion%3Fstate%3D4321342",
  where:

    - "aasertion_issuer" is the "https://self-issued.me/".
    - "assertion_client" is the URI identfier of "theapp" for receiving the assertion 
       issued by SIOP. 
    - "state" is the unqiue string for "theapp" to identify every each request and response. 

2. Resource Server: Ask SIOP to authenticate the device owner(SIOP AuthReq)
--------------------------------------------------------------------------------

- The browser vists the authentication endpoint of the "theres.com".
- "thers.com" detects the URI is the "Self-Issued Assertion Requset".
- "thres.com" compose the Self-Issued OP authorization request with the parameters of the landing URI.
- The browser opens the Self-Issued OP with the authorization URI.

3. SIOP: Issue ID Token for the Device Owner to the Resource Server.
--------------------------------------------------------------------------------

- SIOP creates the Self Issued authorization response URI.
- The broweer visits "theres.com" with the authorization response URI.


4. Resource Server: Authenticate the Device Owner and delegates to issue an Assertion for Token Client
---------------------------------------------------------------------------------------------------------

- "theres.com" acceps the authorization response from the SIOP and authenticates the device owner.
- The data bound to the "state" parameter tell that "tehapp" expects the SIOP to issued an assertion,
  so "theres.com" compose the URI , "openid://assertion?assertion_client=theapp%3A//assertion%3Fstate%3D4321342".
    
  "assertion_client" is the target URI where the SIOP returns a created assertion to.

- The browser opens the SIOP with the URI.

5. SIOP:  Issue an JWT Assertion for the Token Client
---------------------------------------------------------------------------------------------------------------

- The SIOP detects the assertion request.
- If the device owner accepts this request, the SIOP creates a new JWT using the same privete key for 
  the "sub_jwk" used for issuing ID Token to "theres.com".

  The JWT claims are mostly same as the ID Token to "theres.com", except:

    - "aud" is an array including the client_id of  "theres.com" and "assertion_client".
    - "id_token_jti" tells the ID Token which "theres.com" has accepted.    

- The device open "theapp" with the URI "theapp://assertion?state=4321342&assertion={{jwt}}".

6. Token Client: Ask the Resource Server to issue an Access Token
-----------------------------------------------------------------------------------------------

- The "theapp" accept the URI from the SIOP.
- If the device owner agreed to proceed and "state" is the valid one,
  "theapp" goes to the Token Endpoint with the JWT in "assertion" parameter 
  in the manner of JWT Assertion profile. 

7. Resource Server: Validate the Token Request and issue an Access Token
-------------------------------------------------------------------------------------------

- If the token endpoint validate the assertion and finds it is valid, 
  "theres.com" issues an access token to "theapp".
