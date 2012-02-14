======================================================
OpenID Connect Session Management 1.0 
======================================================

Based on `OpenID Connect Session Management 1.0 - draft 03 <http://openid.net/specs/openid-connect-session-1_0.html>`_ .


.. _session_1:

1.  Introduction
====================

.. glossary::

    Session
        Sessions are used to keep track of information and interactions for users across multiple pages. 
        This creates a sense of continuity, customization, and a more pleasant experience for the users. 
        Visitors to an OpenID relying party site accessing protected resources will be asked for authentication and authorization. 
        Upon user authorization, the user will be granted access to the requested resources. 
        The site may perform other background tasks for the user using the same authenticated session. 
        This allows the user to have a simplified experience without being asked for authorization each time 
        and may even allow the user to go off-line while the tasks are being performed. 
        This specification describes how OpenID Connect sessions can be created, used, and terminated. 


.. _session_3:

3.  Session Management
=========================

OpenID Connect supports life-cycle session management and synchronization for third parties that support authentication 
with the authorization server. 
In addition, session management for fourth parties such as desktop, native or mobile applications that 
utilize authorization server credentials at fourth party web sites are also supported.

.. note::

    :doc:`session` is also  for 4th party in the circle.
   
.. _session_3_1:

3.1.  Creating Sessions
---------------------------

To create a session, the client sends an authorization request to the authorization server with id_token as one of the response_type values.

If the response_type includes the value **code**, 
then an :term:`ID token` is returned in the response of the :term:`Token Endpoint` when the :term:`Access Token` is retrieved.

If the response_type includes the value **token**, 
then an :term:`ID token` is returned as a **fragment parameter**  in the redirect_uri specified in the request.

In either case, an ID Token will also be returned along with the access token 
when submitting a refresh token to the token access endpoint if the initial authorization request included id_token in the response_type parameter.

The ID Token serves as a key to an authenticated user session and contains claims for the user. 

.. note::

    :ref:`issues_33`

.. _session_3_1_1:
  
3.1.1.  ID Token
^^^^^^^^^^^^^^^^^^^^^^^^

.. glossary::

     ID Token
        A token that contains information about the authentication event. 
        It is a signed token, but can be treated as opaque by the Lite profile(:doc:`connect_lite`). 
        Relying partys wanting to process the token directly should refer to the full openID Connect 1.0 specification. 
 

This specification defines an ID Token as a signed JWT [:term:`JWT`] that minimally contains the following claims:

    issuer
        REQUIRED. The unique identifier of the issuer of the claims 

    client_id
        REQUIRED. The unique identifier of the client. 

    user_id
        REQUIRED. A locally unique and never reassigned identifier for the user, 
        which is intended to be consumed by the Client. e.g. "24400320" or "AItOawmwtWwcT0k51BayewNvutrJUqsvl6qs7A4". 
        It MUST NOT exceed 255 ASCII characters in length. 

    audience
        REQUIRED. The JWT [:term:`JWT`] aud (audience) claim. 

    exp
        REQUIRED. The JWT [:term:`JWT`] exp (expiration time) claim. 

    pape
        OPTIONAL. (TBD) If we want this token to be short, we probably want to define a shorter equivalent of PAPE. 

    nonce
        OPTIONAL. If the authorization request includes a nonce request value, then this value is REQUIRED and its value is set to the same value as the request value. 


The ID Token MAY contain other claims. 
The ID Token can be used to access session information from an authenticated session or to pass a session to other applications. 

.. _session_3_1_2:

.. include:: session/3.1.2.rst

.. _session_3_1_3:

.. include:: session/3.1.3.rst

.. _session_3_1_3_1:

.. include:: session/3.1.3.1.rst

.. _session_3_1_4:

.. include:: session/3.1.4.rst

.. _session_3_1_4_1:

.. include:: session/3.1.4.1.rst

.. _session_3_1_4_2:

.. include:: session/3.1.4.2.rst

.. _session_3_1_5:

3.1.5.  Authorization Code (Web Server) Flow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Web server clients can use the OAuth authorization code flow by including code and id_token in the response_type parameter of the authorization request to obtain an ID token. The ID Token is returned along with the access token after the client submits the authorization code to the access token endpoint.

    1. The user-agent makes an authorization request to the authorization endpoint.
    2. The authorization server authenticates the user
    3. The authorization server returns an authorization code.
    4. The client sends authorization code to the token access endpoint.
    5. The authorization server verifies the authorization token and returns an access and ID token
    6. The user-agent and client servlet can then use the session management endpoints by presenting the ID token to the endpoints.

::

                                     +----------------------------------+
    +----------+                     |                                  |
    |          |                     |      +----------------------+    |
    |          |                     |      |    Authorization     |    |
    |          |                     |      |         server       |    |
    |user-agent|                     |      +----------------------+    |
    |          |                     |      |   +---------------+  |    |
    |          |>-----(1)------------|------|-->| Authorization |  |    |
    |          |<-----(3)------------|------|--<| Endpoint (2)  |  |    |
    +----------+                     |      |   +---------------+  |    |
        ^                 +----------|------|--<| Access Token  |  |    |
        |                 | +--------|------|-->| EndPoint      |  |    |
        |                 | |        |      |   +---------------+  |    |
        v                 | |        |      |   | Session       |  |    |
    +----------+          | |        |      |   | Management    |  |    |
    |          |          | |        |      |   | Endpoints     |  +    |
    |client    |<-----(4)-+ |        |      |   +---------------+  |    |
    |servlet   |>-----(5)---+        |      +----------------------+    |
    |          |                     |                                  |
    |          |                     |      +----------------------+    |
    |          |                     |      |     Profile API/     |    |
    |          |                     |      |     UserInfo Endpoint|    |
    |          |<--------------------|-----<|                      |    |
    |          |>--------------------|----->|                      |    |
    +----------+                     |      +----------------------+    |
                                     |                                  |
                                     |                                  |
                                     +----------------------------------+

.. note::

    :ref:`issues_34` 


.. _session_3_1_6:

.. include:: session/3_1_6.rst

.. note::

    :ref:`issues_34` 


.. _session_3_2:

3.2.  Session Management Endpoints
--------------------------------------

To manage a session, the client sends a request to the session management endpoints at the authorization server. 
The session management endpoints at the authorization server are:

    Refresh Session
        Refreshes an expired ID Token 

    Check Session
        Get a plain text JSON structure from a ID Token 

    End Session
        Ends a session 

Authorization servers MUST support the use of the HTTP "GET" method as define in RFC 2616 [RFC2616] 
and MAY support the "POST" method for all session management endpoints. 

.. note::

    :ref:`issues_35` 

.. _session_3_2_2:

3.2.2.  Check Session
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For clients that are not capable of dealing with :term:`JWS` signed :term:`ID Tokens <ID Token>`, 
they can send the ID Token to the Check Session endpoint. 
It will validate the ID Token and return a plain text JSON structure of the ID Token.

Request Parameters:

    id_token
        REQUIRED. A previously issued ID Token 

Response:

    The response body is a plain text JSON structure of the claims in the ID token.

If the ID token is a JWS [JWS], then it is the base64url decoded payload of the signed ID Token. 
In a typical HTTP binding, the response is a HTTP 200 response code with the content-type header set to "application/json".

The following is a non-normative example of a check session request:

.. code-block:: javascript 

    Request:
    POST /op/check_session?id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6
    ImNsaWVudC5leGFtcGxlLmNvbSJ9.eyJpc3N1ZXIiOiJodHRwOlwvXC9zZXJ2ZXIuZXhhbXBs
    ZS5jb20iLCJjbGllbnRfaWQiOiJjbGllbnQuZXhhbXBsZS5jb20iLCJhdWRpZW5jZSI6ImNsa
    WVudC5leGFtcGxlLmNvbSIsImlkIjoidXNlcl8yMzQyMzQiLCJleHAiOjEzMDM4NTI4ODB9.a
    JwagC6501Da-zK-X8Az9B-Y625aSEfxVuBpFEDjOxQ
    
    Response:
    HTTP/1.1 200 OK
    Content-Type: application/json
    
    {
      "issuer":"http://server.example.com",
      "client_id","http://client.example.com",
      "audience", "http://client.example.com",
      "user_id":"user_328723",
      "exp":1303852880
    }


.. _session_5:

5.  Security Considerations
===============================

TBD

.. note::

    :ref:`issues_36`
