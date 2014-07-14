================================================================================
OpenID Connect Native Application Token Provisioning Profile 1.0
================================================================================

.. contents::
    :local:

Abstract
============

OpenID Connect 1.0 is a simple identity layer 
on top of the OAuth 2.0 protocol.  

It allows Clients to verify the identity of the End-User 
based on the authentication performed by an Authorization Server, 
as well as to obtain basic profile information 
about the End-User in an interoperable and RESTful manner.

The OpenID Connect Native Application Token Provisioning Profile 1.0
is a profile of the OpenID Connect Standard 1.0 specification
designed to enable 'authorization agents' on devices, ie native
applications that obtain OAuth access tokens on behalf of other
native applications.

Status of this Memo
------------------------------

OIDF-Drafts are working documents of the OpenID Foundation (OIDF).

OIDF-Drafts are draft documents valid for a maximum of six months and
may be updated, replaced, or obsoleted by other documents at any
time.  It is inappropriate to use OIDF-Drafts as reference material
or to cite them other than as "work in progress."

This OIDF-Draft will expire on May 29, 2014.

Copyright Notice
------------------

Copyright (C) OpenID Foundation (2013).  All Rights Reserved.


1.  Introduction
====================================

OpenID Connect Native Application Token Provisioning Profile 1.0 
is a profile of the OpenID Connect Core 1.0 [OpenID.Core] specification
that stipulates how a specialized OpenID Connect Client 
called an :term:`Token Agent` can obtain tokens 
on behalf of other installed native applications 
- thereby provisioning tokens to those applications and
so enabling a Single SignOn experience for End-Users.


1.1.  Requirements Notation and Conventions
----------------------------------------------------------------------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in [RFC2119].

Throughout this document, values are quoted to indicate that they are
to be taken literally.  When using these values in protocol messages,
the quotes MUST NOT be used as part of the value.

1.2.  Terminology
----------------------------

This specification uses the terms "Access Token", "Refresh Token",
"Authorization Code", "Authorization Grant", "Authorization Server",
"Authorization Endpoint", "Client", "Client Identifier", "Client
Secret", "Protected Resource", "Resource Owner", "Resource Server",
and "Token Endpoint" defined by OAuth 2.0 [RFC6749].  This
specification also defines the following terms:

.. glossary::

   Token Agent 
   TA  
        A native application that obtains access tokens 
        on behalf of other native applications 
        - thereby enabling a Single SignOn experience 
        for Native Application end users 
        because the End-Users need only explicitly 
        authenticate the _TA_ once per Authorization Server.

   AppInfo Endpoint  
        A protected resource that the _TA_ can call 
        (using its primary access token) 
        to obtain metadata corresponding to a set of applications 
        - both web & native.  

        The _TA_ uses the application metadata 
        in order to obtain secondary access tokens for those applications.

   Primary Token  
        An OAuth token 
        (access, refresh, and id_token)
        obtained by the _TA_ for its own uses.

   Secondary Token  
        An OAuth access token 
        obtained by the _TA_ on behalf of another native application.

2.  Overview
==================

More and more applications, 
both enterprise on-prem and cloud-based, 
are accessed through REST APIs in addition to, 
or instead of, browser-based access.  

Mobile clients will be a key consumer of such APIs.  

Native installed applications 
(e.g for iOS , Android, BlackBerry, etc devices) 
offer an important alternative to web or browser-based applications.  

Both models have their pros/cons.


OAuth 2.0 is an authentication & authorization framework 
for such REST APIs.  

Critically, 
OAuth 2.0 is explicitly designed to support the variety of different client types 
that will be accessing REST APIs 
- both applications running on web servers 
within the enterprise calling out to the cloud/partners etc, 
as well as applications running on mobile phones 
belonging to employees and customers.  

OAuth supports this variety of client types 
by defining multiple mechanisms for 'getting a token', 
the different mechanisms acknowledging the constraints of particular client types.


For accessing protected resources behind an API using OAuth for authentication, 
the mobile application requires an access token 
- this to be presented on the HTTP calls to the API.

The high-level sequence 
by which the client obtains and uses an access token is:

-  Get the User authenticated 
   at the corresponding Authorization Server (AS)

-  (OPT) Get the AS to obtain the User's consent 
   for the client's access of the API

-  Accept the token(s) delivered back by the AS

-  Attach the access token to REST API calls

The presumption is that each native application client 
will perform the above steps.  

When a User has multiple native applications 
on their device (as is more and more the case) 
this may be an unacceptable usability burden.


This burden can be reduced 
by introducing an 'authorization agent' (TA) onto the device.  

Rather than each native application directly obtaining its own OAuth tokens, 
the direct token retrieval is assumed by the authorization agent, 
with the tokens then handed over to the native applications for their normal use.  

Rather than the user individually authenticating 
and authorizing each native application,
they do so only for the authorization agent 
- this then bootstrapping subsequently obtaining tokens 
for the other native applications.

Because the User only authenticates 
and authorizes the authorization agent, 
the usability burden is significantly reduced.

The _TA_ model is shown below:

::

     +-------------+
     | Device      |
     | +--------+  |                                          +---------------+
     | |        |-------- Login & Authorization (1)---------->|               |
     | |        |  |                                          |               |
     | |  Token |<------ Primary Tokens for TA - (2)----------|               |
     | |  Agent |  |                                          |     AS        |
     | |        |---- Request Secondary tokens for apps (3)-->|               |
     | |        |  |                                          |               |
     | |        |<-------Secondary Tokens for apps (4)--------|               |
     | |        |  |                                          +---------------+
     | +--------+  |                                             /\    /\
     |    /\       |                                              |    |
     |    | Pass   |                                        Validate tokens (7)
     |    |Tokens  |                                              |    |
     |    \/ (5)   |                                             \/    |
     | +--------+  |                                           +-----+ |
     | |  App1  | -|--------- API Call with token (6)--------> | RS1 | |
     | +--------+  |                                           +-----+ \/
     | +--------+  |                                           +---------+
     | |  App2  | -|--------- API Call with token (6)--------> |  RS2    |
     | +--------+  |                                           +---------+
     | +--------+  |                                           +---------------+
     | |  App3  | -|--------- API Call with token (6)--------> |    RS3        |
     | +--------+  |                                           +---------------+
     +-------------+
    
    
                                     Figure 1

Note: 

    the token validation of Step 7 may require a call 
    to the issuing AS (as shown) 
    or may be achieved locally via a digital signarture verification.

A _TA_ must be able to obtain tokens (both primary & secondary) 
from Authorization Servers.  

This specification profiles 
the OpenID Connect Standard 1.0 specification for those interactions.  

The _TA_ engages in messaging with the relevant Authorization Servers
according to this profile in order to obtain the secondary OAuth
access tokens on behalf of other native applications.


3.  Deployment Models
================================================

The authorization agent model can be applied for two different
categories of native applications

1.  multiple native applications that call APIs associated with a
    single policy domain, e.g. multiple native applications created
    by a consumer retailer or SaaS provider.

2.  multiple native applications that call APIs associated with
    different policy domains, e.g. multiple applications used by an
    enterprise employee to access SaaS services relevant to their
    role.

While both scenarios imply the User authenticating and authorizing
each native application individually, in the first case the User
would interact with the same AS each time.  In the latter, it would
be different ASs.

4.  Token Agent Authentication
============================================

A _TA_ MUST authenticate to the AS both when obtaining primary or
secondary tokens.


5.  Token Agent Registration
============================================

A _TA_ is a specialized OpenID Connect Client and, as such, MUST be
registered with an AS.

This profile does not dictate a particular registration model but
registration MUST result in the _TA_ having client credentials to be
used on the subsequent protocol flows defined here, ie. to obtain
both primary & secondary tokens.

OpenID Connect Dynamic Client Registration 1.0 [OpenID.Registration]
MAY be used to provide individual client_id and credentials for each
instance of a TA.

6.  ID Token
====================================

The ID Token is a security token that contains Claims 
about the authentication event and other requested Claims.  

The ID Token is represented as a JSON Web Token (JWT) [JWT].

The ID Token is used to manage the authentication event.  
The user is passed as the value of "sub" is scoped to the "iss".

The ID Token is audience restricted to either the _TA_ or a remote AS
via the "aud" (audience) Claim.

In the _TA_ model, 
"id_token" may have two different types of "aud" (audience).

1.  one targeted at the _TA_, 
    returned to it in exchange for the authz code.

2.  one targeted at a remote AS, 
    returned to the _TA_ in exchange for a refresh token.  

    The _TA_ exchanges such an id_token 
    at the corresponding remote AS 
    using an assertion flow for a secondary access token.

The following is a non-normative example of a base64url decoded ID
Token with the _TA_ as the value of "aud" (with line wraps for
display purposes only):

.. code-block:: javascript

  {
   "iss": "https://server.example.com",
   "sub": "24400320",
   "aud": "TA-client-ID",
   "exp": 1311281970,
   "iat": 1311280970
  }

The following is a non-normative example of 
a base64url decoded ID Token with the remote AS 
as the value of "aud" and the _TA_ 
as the value of "azp" (with line wraps for display purposes only):

.. code-block:: javascript

  {
   "iss": "https://server.example.com",
   "sub": "24400320",
   "azp": "TA-client-ID",
   "aud": "https://server.partner.com",
   "exp": 1311281970,
   "iat": 1311280970
  }

7.  Protocol Flows
========================================

This section details the various protocol flows 
that the _TA_ and other actors engage in.

7.1.  Primary Token Retrieval
------------------------------------------

The _TA_ first performs an OpenID Connect flow to obtain its own
primary tokens.  The _TA_ MUST use the code flow, which consists of
the following steps:

1.  _TA_ prepares an Authorization Request containing the desired
    request parameters.

2.  _TA_ sends a request to the Authorization Server.

3.  Authorization Server authenticates the End-User.

4.  Authorization Server obtains the End-User Consent/Authorization.

5.  Authorization Server sends the End-User back to the _TA_ with a
    "code".

6.  _TA_ sends the "code" to the Token Endpoint to receive primary
    Access Token, Refresh Token and ID Token in the response.

7.1.1.  Token Agent Prepares Authorization Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To initiate obtaining primary tokens, 
the _TA_ prepares an Authorization Request 
to the Authorization Endpoint.

The scheme used in the Authorization Endpoint URL MUST be HTTPS.

Clients MAY construct the request using the HTTP "GET" or the HTTP
"POST" method.

This profile further constrains the following request parameters:

.. glossary::

    response_type  
        This value MUST be "code".

Other REQUIRED parameters in the request include the following:

.. glossary::

    client_id  
        OAuth 2.0 Client Identifier for the _TA_.

    scope  
        OAuth 2.0 "scope" value.  

        It MUST include "openid" as one of the space delimited ASCII strings.

        It MUST also include "aza".

    redirect_uri  
        Redirection URI to which the response will be sent.

        This MUST be pre-registered with the provider.

The following is a non-normative example of an Authorization Request
URL (with line wraps for display purposes only):

::

  https://server.example.com/authorize?
    response_type=code
    &client_id=s6BhdRkqt3
    &redirect_uri=https%3A%2F%2Fclient.example.org%2Fcb
    &scope=openid%20aza

7.1.2.  Token Agent Sends Request to Authorization Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Having constructed the Authorization Request, 
the _TA_ sends it to the Authorization Endpoint.  

This MAY happen via HTTPS redirect, hyperlinking, 
or any other secure means of directing the User-Agent to the URL.

7.1.3.  Authorization Server Authenticates End-User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The authorization server authenticates the resource owner 
to make sure that the consent is obtained from the right party.  

The exact method of how the authentication is performed 
is out of scope of this specification.

7.1.4.  Authorization Server Obtains End-User Consent/Authorization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Authorization Server MAY obtain an authorization decision.  

This can done by presenting the End-User with a dialogue 
that allows the End-User to recognize what he is consenting 
to and obtain his consent or by establishing consent via other means 
(for example, via previous administrative consent).

The "openid" scope value declares 
that this OAuth 2.0 request is an OpenID Connect request.

The "aza" scope value declares that the _TA_ is requesting tokens
that can be used to obtain other secondary tokens for those
applications relevant to the End-User.

7.1.5.  Authorization Server Sends End-User Back to Trust Agent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the authorization is determined, 
the Authorization Server returns a successful response or an error response.

7.1.5.1.  Success Case - End-User Granted Authorization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the Resource Owner grants the authorization request initiated 
by the _TA_, 
the Authorization Server issues a "code" and delivers it to the _TA_ by 
adding the following query parameters 
to the query component of the redirection URI 
using the "application/x-www-form-urlencoded" format 
as defined in Section 4.1.2 of OAuth 2.0 [RFC6749].

.. glossary::

   code  
        REQUIRED.  OAuth 2.0 authorization code.

   state  
        OAuth 2.0 state value.  

        REQUIRED if the "state" parameter is present 
        in the Authorization Request from the _TA_.  

        The _TA_ MUST verify that the "state" value 
        is equal to the exact value of "state" parameter 
        in the Authorization Request.

7.1.5.2.  Error Case - End-User Denied Authorization or Invalid Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the End-User denies the authorization or the End-User
authentication fails, 
the Authorization Server MUST return the error
authorization response as defined 
in 4.1.2.1 of OAuth 2.0 [RFC6749].  

No other parameters SHOULD be returned.

7.1.6.  Token Agent Obtains Primary ID Token, Access Token and Refresh Token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once having obtained the "code", 
the _TA_ requests the corresponding primary tokens at the Token Endpoint as follows:

7.1.6.1.  Token Agent Sends Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The _TA_ makes a request to the token endpoint as described 
in Section 4.1.3 of OAuth 2.0 [RFC6749].

The _TA_ MUST authenticate to the Token Endpoint as described 
in Section 2.3 of OAuth 2.0 [RFC6749].

7.1.6.2.  Token Agent Receives Tokens
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The _TA_ receives a response with the following parameters as
described in Section 4.1.4 of OAuth 2.0 [RFC6749].  The response
should be encoded using UTF-8.

.. glossary::

   access_token  

        REQUIRED.  

        Primary Access Token for the AppInfo Endpoint.

   token_type  
        REQUIRED.  

        OAuth 2.0 token type value.  

        The value MUST be "bearer". 
        _TA_ implementing this profile MUST support the OAuth 2.0 Bearer Token Usage [RFC6750] specification.  

        This profile only describes the use of bearer tokens.

   id_token  
        REQUIRED.  

        Primary ID Token.

   expires_in  
        OPTIONAL.  

        Expiration time of the Access Token in seconds.

   refresh_token  
        REQUIRED.  

        Primary Refresh Token.

The following is a non-normative example (with line wraps for the
display purposes only):

::

     HTTP/1.1 200 OK
     Content-Type: application/json
     Cache-Control: no-store
     Pragma: no-cache
     {
      "access_token":"SlAV32hkKG",
      "token_type":"bearer",
      "expires_in":3600,
      "refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA",
      "id_token":"eyJ0 ... NiJ9.eyJ1c ... I6IjIifX0.DeWt4Qu ... ZXso"
     }

7.2.  AppInfo Endpoint
------------------------------------------------------

To obtain application metadata information, the _TA_ MAY make a GET
or POST request to the AppInfo Endpoint.

AppInfo Endpoint Servers MUST require the use of a transport-layer
security mechanism.  The AppInfo Endpoint Server MUST support TLS 1.2
RFC 5246 [RFC5246] and/or TLS 1.0 [RFC2246] and MAY support other
transport-layer mechanisms with equivalent security.

7.2.1.  AppInfo Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

_TA_ MAY send requests with the following parameters 
to the AppInfo Endpoint to obtain further information 
about the applications for which the TA can obtain secondary tokens.  

The AppInfo Endpoint is an OAuth 2.0 [RFC6749] Protected Resource 
that complies with the OAuth 2.0 Bearer Token Usage [RFC6750] specification.  

As such, 
the Access Token SHOULD be specified via the HTTP Authorization header.


.. glossary::

   access_token  
        REQUIRED.  

        Access Token obtained from an OpenID Connect Authorization Request.  

        This parameter MUST only be sent using one method 
        through either the HTTP Authorization header 
        or a form- encoded HTTP POST body parameter.

   schema  
        REQUIRED.  

        Schema in which the data is to be returned.  

        The only defined "schema" value is "aza".

7.2.2.  AppInfo Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The AS MUST determine the authorizations attached to the primary
refresh token sent by the _TA_ and respond accordingly.

The AS MUST NOT include metadata for an application that the End-User
is not authorized to use.

The AS returns the application metadata information to the _TA_ in
the form of JSON, an example of which is shown below

.. code-block:: javascript

   {
       "schema": "urn:aza:schemas:core:1.0",
       "branding": {
           "companyname": "ABS",
           "companyiconurl": "http://www.ABS.com/logo.gif"
       },
       "apps": {
           "appcount": "1",
           "app": [
               {
                   "name": "Boxx",
                   "type": "native",
                   "scope": "urn:oauth:boxx",
                   "iconurl": "http://www.example.com/pic.png",
                   "customurl": "boxxnative"
               }
           ]
       }
   }

The _TA_ MAY use the information from the AppInfo endpoint 
to build a user interface for the user, 
displaying the applications they are authorized to use.

The _TA_ MUST use the value of the "scope" parameter to indicate the
desired targeted application when subsequently requesting a secondary
access token for that application.

If using the custom URL scheme mechanism to pass the secondary access
token to the relevant application, the _TA_ MUST use the value of the
"customurl" parameter when constructing the URL.

7.3.  Primary access token refresh
---------------------------------------------------------------

The _TA_ MAY use its primary refresh token to obtain fresh primary
access tokens for its own use on calls to the AppInfo endpoint.

If the _TA_ does not specify a scope of any native application on its
refresh call, it is requesting a fresh primary access token.

The _TA_ MUST NOT share its primary access or refresh tokens with
other native applications.

7.4.  Secondary Access Token Retrieval
---------------------------------------------------------------

The _TA_ can use its primary refresh token to obtain secondary access
tokens for native applications.  Depending on the requirements of the
targeted application, a secondary access token is either directly
returned for the refresh token, or an id_token that csn be
subsequently exchanged at an AS hosted by the application provider.
The second scenario supports deployments where some native
applications are already associated withnan AS, and the application
RS is preconfigured to only validate tokens against that AS.

The _TA_ can be prompted to obtain an secondary access token for an
application either due to a user clicking on an icon displayed by the
_TA_ (a launcher model) , or by the native application asking the
_TA_ for a token (presumably after being launched through the OS
native UI).

7.4.1.  Secondary access token request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The _TA_ MUST use its primary refresh token to request of the AS a
secondary access token - specifying as a scope the relevant native
application to be targeted (rather than itself).  The _TA_ MAY obtain
the relevant scope parameter for a particular native application via
the AppInfo endpoint or through some other mechanism.

Example of a refresh call where the _TA_ is asking for a secondary
access token for a native application with a specified scope of
"urn:oauth:boxx".

::
    
    POST /as/token.oauth2 HTTP/1.1
    Host: as.example.com
    Content-Type: application/x-www-form-urlencoded;charset=UTF-8
    
    grant_type=refresh_token&refresh_token=qANLTbu17rk17lPszecHRi7rqJt46pG1qx0nTAqXWH&scope=urn:oauth:boxx


7.4.2.  Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The AS MUST verify that the End-User is authorized to use the
particular native application for which the secondary access token
was requested.

The AS MAY check local policy, or MAY call out to an external policy
store.

If authorized, the AS returns the secondary access token or id_token,
depending on the policy configured for that application.

The AS MAY bind the secondary access token to the specific native
application through cryptographic or other means.

7.4.3.  Secondary access token retrieval from remote AS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TBD - show how the TA 1) obtains an id_token using the refresh token
and 2) uses that id_token to request of a secondary AS an access
token.

7.5.  Validation
---------------------------------------------

When an RS receives a secondary access token on an API call from a
native application, it will need to validate that access token to
determine whether to approve the request or not.

This profile does not dictate a particular validation model.

Depending on the nature of the secondary access token, the RS MAY
call back to the issuing AS for validation.  Alternatively the RS MAY
validate the token *locally*, ie through verification of a signature
over that token.

8.  Native Application Interactions
======================================================

This section outlines how an _TA_ might pass secondary access tokens
to corresponding native applications, or how the native application
might request of the _TA_ such a secondary access token.

8.1.  Token Agent passes secondary access token to Application
------------------------------------------------------------------------

Once it has obtained a secondary access token for a particular native
application, the _TA_ MUST deliver that secondary access token to
that application.

The _TA_ MUST NOT deliver a secondary access token to an application
for which it was not issued.

This profile does not stipulate a particular mechanism for the
delivery of the secondary access token, depending as it does on the
mobile OS support for inter-app messaging.

One mechanism supported by both iOS and Android is the use of custom
URL schemes.  In this model, a native appliction registers itself
with the mobile OS as the handler for URLs in a given scheme - when
the OS subsequently sees URLs in this scheme, it hands them over to
the native application.

To use this model, each native application that wants _TA_
integration must register itself as the handler for a unique URL
scheme.

Follows is the Android mechanism

.. code-block:: xml

    <activity android:name=".MyAppRegisterAccount" android:label="@string/addAccount" >
            <intent-filter>
                    <action android:name="android.intent.action.VIEW"/>
                    <category android:name="android.intent.category.DEFAULT"/>
                    <category android:name="android.intent.category.BROWSABLE"/>
                    <data android:scheme="nativeapp" />
            </intent-filter>
    </activity>

The same URL scheme identifier must be configured into the AS and
AppInfo endpoint when the native application is configured so that
access tokens can be appropriately targeted.

After obtaining an access token for a particular native application,
the _TA_ builds a URL in the corresponding custom scheme that
includes the token.

The URL MUST

-  have a scheme corresponding to the appropriate native application

-  have an 'access_token' parameter with the token value to be passed

For instance

::

   nativeapp://new_token?access_token=PeRTSD9RQrbiuoaHVPxV41MzW1qS

8.2.  Application requests secondary access token of Token Agent
----------------------------------------------------------------------

A _TA_ SHOULD support an native application being able to request of
the _TA_ an access token, as compared to the _TA_ handing an
unsolicited access token to an application.

One mechanism to achive this is that, upon installation, the _TA_
register itself as the handler for URLs with a particular scheme.A
native applicaton can construct URLs in that scheme as a means of
requesting of the _TA_ that an access token be obtained.


9.  Security Considerations
=================================================

TBD

10.  Privacy Considerations
=================================================

TBD


11.  IANA Considerations
=================================================

This document makes no requests of IANA.


12.  Normative References
=================================================

.. code-block::

   [JWT]      
              Jones, M., Bradley, J., and N. Sakimura, "JSON Web Token
              (JWT)", Internet-Draft draft-ietf-oauth-json-web-token,
              May 2013.

   [OpenID.Core]
              Sakimura, N., Bradley, J., Jones, M., de Medeiros, B.,
              Mortimore, C., and E. Jay, "OpenID Connect Standard 1.0",
              December 2013.

   [OpenID.Registration]
              Sakimura, N., Bradley, J., and M. Jones, "OpenID Connect
              Dynamic Client Registration 1.0", July 2013.

   [RFC2119]  
              Bradner, S., "Key words for use in RFCs to Indicate
              Requirement Levels", BCP 14, RFC 2119, March 1997.

   [RFC2246]  
              Dierks, T. and C. Allen, "The TLS Protocol Version 1.0",
              RFC 2246, January 1999.

   [RFC5246]  
              Dierks, T. and E. Rescorla, "The Transport Layer Security
              (TLS) Protocol Version 1.2", RFC 5246, August 2008.

   [RFC6749]  
              Hardt, D., "The OAuth 2.0 Authorization Framework",
              RFC 6749, October 2012.

   [RFC6750]  
              Jones, M. and D. Hardt, "The OAuth 2.0 Authorization
              Framework: Bearer Token Usage", RFC 6750, October 2012.

Appendix A.  Acknowledgements
================================================

The following have contributed to the development of this
specification.

      Chuck Mortimore

      Brian Campbell

      Scott Tomilson

      John Bradley

Appendix B.  Notices
==========================================

   Copyright (c) 2013 The OpenID Foundation.

The OpenID Foundation (OIDF) grants to any Contributor, developer,
implementer, or other interested party a non-exclusive, royalty free,
worldwide copyright license to reproduce, prepare derivative works
from, distribute, perform and display, this Implementers Draft or
Final Specification solely for the purposes of (i) developing
specifications, and (ii) implementing Implementers Drafts and Final
Specifications based on such documents, provided that attribution be
made to the OIDF as the source of the material, but that such
attribution does not indicate an endorsement by the OIDF.

The technology described in this specification was made available
from contributions from various sources, including members of the
OpenID Foundation and others.  Although the OpenID Foundation has
taken steps to help ensure that the technology is available for
distribution, it takes no position regarding the validity or scope of
any intellectual property or other rights that might be claimed to
pertain to the implementation or use of the technology described in
this specification or the extent to which any license under such
rights might or might not be available; neither does it represent
that it has made any independent effort to identify any such rights.
The OpenID Foundation and the contributors to this specification make
no (and hereby expressly disclaim any) warranties (express, implied,
or otherwise), including implied warranties of merchantability, non-
infringement, fitness for a particular purpose, or title, related to
this specification, and the entire risk as to implementing this
specification is assumed by the implementer.  The OpenID Intellectual
Property Rights policy requires contributors to offer a patent
promise not to assert certain patent claims against other
contributors and against implementers.  The OpenID Foundation invites
any interested party to bring to its attention any copyrights,
patents, patent applications, or other proprietary rights that may
cover technology that may be required to practice this specification.

Appendix C.  Document History
============================================================

   [[ To be removed from the final specification ]]

   -01

   o  Initial draft

   o  Added OIDF Standard Notice

   o  Changed reference to Core from Standard

   o  Changed diagam step 2 tokens, made 5 and 7 bidirectional arrows

   -02

   o  Second draft

Authors' Addresses
==============================

   Paul Madsen
   Ping Identity

   Email: paul.madsen@gmail.com


   Ashish Jain
   VMware

   Email: itickr@gmail.com


   Andy Zmolek
   Enterproid

   Email: andy.zmolek@enterproid.com


   John Bradley
   Ping Identity

   Email: jbradley@pingidentity.com

Full Copyright Statement
========================================

   Copyright (C) OpenID Foundation (2013).  All Rights Reserved.

   The OpenID Foundation (OIDF) grants to any Contributor, developer,
   implementer, or other interested party a non-exclusive, royalty free,
   worldwide copyright license to reproduce, prepare derivative works
   from, distribute, perform and display, this Implementers Draft or
   Final Specification solely for the purposes of (i) developing
   specifications, and (ii) implementing Implementers Drafts and Final
   Specifications based on such documents, provided that attribution be
   made to the OIDF as the source of the material, but that such
   attribution does not indicate an endorsement by the OIDF.

   The technology described in this specification was made available
   from contributions from various sources, including members of the
   OpenID Foundation and others.  Although the OpenID Foundation has
   taken steps to help ensure that the technology is available for
   distribution, it takes no position regarding the validity or scope of
   any intellectual property or other rights that might be claimed to
   pertain to the implementation or use of the technology described in
   this specification or the extent to which any license under such
   rights might or might not be available; neither does it represent
   that it has made any independent effort to identify any such rights.
   The OpenID Foundation and the contributors to this specification make
   no (and hereby expressly disclaim any) warranties (express, implied,
   or otherwise), including implied warranties of merchantability, non-
   infringement, fitness for a particular purpose, or title, related to
   this specification, and the entire risk as to implementing this
   specification is assumed by the implementer.  The OpenID Intellectual
   Property Rights policy requires contributors to offer a patent
   promise not to assert certain patent claims against other
   contributors and against implementers.  The OpenID Foundation invites
   any interested party to bring to its attention any copyrights,
   patents, patent applications, or other proprietary rights that may
   cover technology that may be required to practice this specification.


Intellectual Property
================================================

For OpenID Foundation's IPR Policy, refer to
http://openid.net/ipr/OpenID_IPR_Policy_(Final_Clean_20071221).pdf
