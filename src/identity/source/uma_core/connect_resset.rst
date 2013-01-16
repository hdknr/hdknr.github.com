Resource Set Descriptor for OpenID Connect
---------------------------------------------------

If an OpenID Connect OP works as an UMA AM,  the OP can return the UserInfo 
in which Users' resource at Host are included as an Aggregated Claim , or
OAuth Access Tokens to the Host endpoint are includde.

To make OpenID Connet OP as a middle man, 
the Host gives extra parameters in UMA Resoure Set Description
for Protection API.

.. glossary::
   
    token_endpoint
        Connect OP ask the Host to issue an access token and an refresh token at this endpoint.
        Requests are authenticated by OAuth Bear Token Profile with **credentai_token**.

    credential_token
        Token for the Token Endpoint request authtentiction
        
    refresh_token
        Token to refresh an access token and the other reflesh token.
         
    resource_endpoint
        Users resource is returned from this endpoint in exchange for access token. 


The following JSON is an non-normative sample to be put by Host to Connect OP as AM
for Protecttion API.

.. code-block:: javascript

    {
      "name": "Photo Album",

      "icon_uri": "http://www.example.com/icons/flower.png",

      "scopes": [
        "http://photoz.example.com/dev/scopes/view",
        "http://photoz.example.com/dev/scopes/all"
      ],

      "token_endpoint": "https://photoz.example.com/dev/token/",
      "credential_token" : "fdsafdsafdsafa",      
      "refresh_token" : "432gsafgds9",
      "resource_endpoint": "https://photoz.example.com/dev/resource/",
    }

If the User configure to return his UserInfo including resource at Host,
the OP refreshes an access token in exchange for the **refresh_tokne** first,
then get the resource at **token_endpoint** in exchange for the access token.

After the resource is returned in JWT form to the OP, OP include it as an 
Aggregated Claim in the UserInfo( which is to be returnd to the other RP).

If the User configure to return an access token to the Host in UserInfo,
OP includes the access token given by Host' **token_endpoint** in the UserInfo.



