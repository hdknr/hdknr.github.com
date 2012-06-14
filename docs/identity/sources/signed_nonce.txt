==============================================
Decoupling Identity and Authentication
==============================================


Decoupling: Why
=================

- User can select identity providers(OP) for particular service provider(RP).
- User can store his authentication credential only at highly trusted service(AP).
- RP can specify a authentication provider. But RP can't know User's idetifier at authentication provider.
- The trusted service can not correlate Users activity. 


Flow
=======

Connect-Connect Flow
----------------------------


.. seqdiag:: signed_nonce/flow.diag

- AP-OP authentication process can deploy the other protocol like SAML other than OpenID Connect.

Sequence
^^^^^^^^^

1. User starts OpenID Connect sign-in process at a RP.
2. The RP composes Connect Authentication Request to the OP
   ( prepared by the RP or specified by User ).

    - RP can specifiy **AP** and  **protocol** for the User to be authenticated 
      through OpenID Reuqest Object.
 
3. The Authentication Reuqest is redirected to the OP. 
4. The OP holds the OpAuthReq bound to User's anonymous session.
5. The OP composes the other Connect Authentication Request(ApAuthReq) to the AP 
   ( specified by the RP,  prepared by the OP or specified by User ). 
6. The Authentication Reuqest is redirected to the AP. 
7. The AP typically provides a authetication form to the User.
8. The User sends his credential to the AP.
9. The AP issues a nonce, sign it his private key and binds the nonce to the User's sesion information.
10. The AP returns the Authetication Response to the OP through the User' agent.
11. The OP directly request to the AP Token Endpoint to get ID Token(ApIdToken) including signed nonce.

    - singed nounce is :term:`JWT` of which header include "OP" as ":term:`aud`" and "AP" as ":term:`iss`", 
      also of which payload includes "nonce".

12. The OP binds the  ID Token to the OpAuthReq information previously stored.
13. The OP returns the Authetication Response to the RP through the User' agent.
14. The RP directly request to the OP Token Endpoint to get ID Token(OpIdToken) including signed nonce.
15. After validating the OpIdToken, the OP optionaly validate the signed nonce with the AP's public key.
16. The RP now issues the session information based on OpIDToken.

