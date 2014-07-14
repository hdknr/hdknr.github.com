==========================================================================================
OpenID Connect Native Application Token Agent API Bindings 1.0
==========================================================================================

Abstract
==========================================================================================

OpenID Connect 1.0 is 
a simple identity layer on top of the OAuth 2.0 protocol.  

It allows Clients to verify the identity of 
the End-User based on the authentication 
performed by an Authorization Server, 
as well as to obtain basic profile information 
about the End-User in an interoperable and RESTful manner.

The OpenID Connect Native Application Token Agent API Bindings 1.0 is
a profile of the OpenID Connect Standard 1.0 specification designed
to enable 'authorization agents' on devices, 
ie native applications that obtain OAuth access tokens 
on behalf of other native applications.

Status of this Memo
------------------------

OIDF-Drafts are working documents of the OpenID Foundation (OIDF).

OIDF-Drafts are draft documents valid for a maximum of six months and
may be updated, replaced, or obsoleted by other documents at any
time.  It is inappropriate to use OIDF-Drafts as reference material
or to cite them other than as "work in progress."

This OIDF-Draft will expire on November 2, 2014.

Copyright Notice
------------------------

Copyright (C) OpenID Foundation (2014).  All Rights Reserved.

1.  Introduction
==================================================

OpenID Connect Native Application Token Agent API Bindings 1.0 
is a profile of the OpenID Connect Core 1.0 [OpenID.Core] specification
that stipulates how a specialized OpenID Connect Client 
called an :term:`Token Agent` can obtain tokens 
on behalf of other installed native applications 
- thereby provisioning tokens to those applications and
so enabling a Single SignOn experience for End-Users.  

The API Bindings specification describes the communication 
between the Token Agent and native applications 
in different deployment environments.

1.1.  Requirements Notation and Conventions
---------------------------------------------------------------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in [RFC2119].

Throughout this document, values are quoted to indicate that they are
to be taken literally.  When using these values in protocol messages,
the quotes MUST NOT be used as part of the value.

1.2.  Terminology
--------------------------------

This specification uses the terms "Access Token", "Refresh Token",
"Authorization Code", "Authorization Grant", "Authorization Server",
"Authorization Endpoint", "Client", "Client Identifier", "Client
Secret", "Protected Resource", "Resource Owner", "Resource Server",
and "Token Endpoint" defined by OAuth 2.0 [RFC6749].  This
specification also defines the following terms:

.. glossary::

   Token Agent 
   TA  
      A native application that obtains access tokens on
      behalf of other native applications - thereby enabling a Single
      SignOn experience for Native Application end users because the
      End-Users need only explicitly authenticate the _TA_ once per
      Authorization Server.

   AppInfo Endpoint  
      A protected resource that the _TA_ can call (using
      its primary access token) to obtain metadata corresponding to a
      set of applications - both web & native.  The _TA_ uses the
      application metadata in order to obtain secondary access tokens
      for those applications.

   Primary Token  
      An OAuth token (access, refresh, and id_token)
      obtained by the _TA_ for its own uses.

   Secondary Token  
      An OAuth access token obtained by the _TA_ on behalf
      of another native application.

2.  Overview
=================================================

More and more applications, both enterprise on-prem and cloud-based,
are accessed through REST APIs in addition to, or instead of,
browser-based access.  Mobile clients will be a key consumer of such
APIs.  Native installed applications (e.g for iOS , Android,
BlackBerry, etc devices) offer an important alternative to web or
browser-based applications.  Both models have their pros/cons.

OAuth 2.0 is an authentication & authorization framework for such
REST APIs.  Critically, OAuth 2.0 is explicitly designed to support
the variety of different client types that will be accessing REST
APIs - both applications running on web servers within the enterprise
calling out to the cloud/partners etc, as well as applications
running on mobile phones belonging to employees and customers.  OAuth
supports this variety of client types by defining multiple mechanisms
for 'getting a token', the different mechanisms acknowledging the
constraints of particular client types.

For accessing protected resources behind an API using OAuth for
authentication, the mobile application requires an access token -
this to be presented on the HTTP calls to the API.

The high-level sequence by which the client obtains and uses an
access token is:

o  Get the User authenticated at the corresponding Authorization
   Server (AS)

o  (OPT) Get the AS to obtain the User's consent for the client's
   access of the API

o  Accept the token(s) delivered back by the AS

o  Attach the access token to REST API calls

The presumption is that each native application client will perform
the above steps.  When a User has multiple native applications on
their device (as is more and more the case) this may be an
unacceptable usability burden.

This burden can be reduced by introducing an 'authorization agent'
(TA) onto the device.  Rather than each native application directly
obtaining its own OAuth tokens, the direct token retrieval is assumed
by the authorization agent, with the tokens then handed over to the
native applications for their normal use.  Rather than the user
individually authenticating and authorizing each native application,
they do so only for the authorization agent - this then bootstrapping
subsequently obtaining tokens for the other native applications.
Because the User only authenticates and authorizes the authorization
agent, the usability burden is significantly reduced.

The _TA_ model is shown below

::

    +-------------+
    | Device      |
    | +--------+  |                                          +-------------+
    | |        |-------- Login & Authorization (1)---------->|             |
    | |        |  |                                          |             |
    | |  Token |<------ Primary Tokens for TA - (2)----------|             |
    | |  Agent |  |                                          |     AS      |
    | |        |---- Request Secondary tokens for apps (3)-->|             |
    | |        |  |                                          |             |
    | |        |<-------Secondary Tokens for apps (4)--------|             |
    | |        |  |                                          +-------------+
    | +--------+  |                                             /\    /\
    |    /\       |                                              |    |
    |    | Pass   |                                      Validate tokens (7)
    |    |Tokens  |                                              |    |
    |    \/ (5)   |                                             \/    |
    | +--------+  |                                           +-----+ |
    | |  App1  | -|--------- API Call with token (6)--------> | RS1 | |
    | +--------+  |                                           +-----+ \/
    | +--------+  |                                           +---------+
    | |  App2  | -|--------- API Call with token (6)--------> |  RS2    |
    | +--------+  |                                           +---------+
    | +--------+  |                                           +------------+
    | |  App3  | -|--------- API Call with token (6)--------> |    RS3     |
    | +--------+  |                                           +------------+
    +-------------+
    
    
                                     Figure 1

Note: 
   the token validation of Step 7 may require a call to the
   issuing AS (as shown) or may be achieved locally via a digital
   signarture verification.

A _TA_ must be able to obtain tokens (both primary & secondary) from
Authorization Servers.  This specification profiles the OpenID
Connect Standard 1.0 specification for those interactions.  The _TA_
engages in messaging with the relevant Authorization Servers
according to this profile in order to obtain the secondary OAuth
access tokens on behalf of other native applications.

3.  Deployment Models
===================================

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

4.  Native Application Interactions
========================================

This section outlines how an _TA_ might pass secondary access tokens
to corresponding native applications, or how the native application
might request of the _TA_ such a secondary access token.

4.1.  Token Agent passes secondary access token to Application
--------------------------------------------------------------------

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

o  have a scheme corresponding to the appropriate native application

o  have an 'access_token' parameter with the token value to be passed

For instance

::

   nativeapp://new_token?access_token=PeRTSD9RQrbiuoaHVPxV41MzW1qS

4.2.  Application requests secondary access token of Token Agent
---------------------------------------------------------------------

A _TA_ SHOULD support an native application being able to request of
the _TA_ an access token, as compared to the _TA_ handing an
unsolicited access token to an application.

One mechanism to achive this is that, upon installation, the _TA_
register itself as the handler for URLs with a particular scheme.A
native applicaton can construct URLs in that scheme as a means of
requesting of the _TA_ that an access token be obtained.

5.  Security Considerations
===============================

   TBD

6.  Privacy Considerations
===============================

   TBD

7.  IANA Considerations
===============================

This document makes no requests of IANA.

8.  References
===============================

8.1.  Normative References
---------------------------------

.. glossary::

   [JWT]      
              Jones, M., Bradley, J., and N. Sakimura, "JSON Web Token
              (JWT)", Internet-Draft draft-ietf-oauth-json-web-token,
              May 2013.

   [NATA.Core]
              Madsen, P., Jain, A., Zmolek, A., and T. Bradley, "OpenID
              Connect Native Application Token Agent Core 1.0",
              January 2014.

   [OpenID.Core]
              Sakimura, N., Bradley, J., Jones, M., de Medeiros, B.,
              Mortimore, C., and E. Jay, "OpenID Connect Standard 1.0",
              December 2013.

   [OpenID.Discovery]
              Sakimura, N., Bradley, J., Jones, M., and E. Jay, "OpenID
              Connect Discovery 1.0", December 2013.

   [OpenID.Registration]
              Sakimura, N., Bradley, J., and M. Jones, "OpenID Connect
              Dynamic Client Registration 1.0", December 2013.

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

8.2.  Informative References
------------------------------------


   [OpenID.Implicit]
              Sakimura, N., Bradley, J., Jones, M., de Medeiros, B.,
              Mortimore, C., and E. Jay, "OpenID Connect Implicit Client
              Profile 1.0", July 2013.


Appendix A.  Acknowledgements
==========================================

The following have contributed to the development of this
specification.

      Chuck Mortimore

      Brian Campbell

      Scott Tomilson

      John Bradley

Appendix B.  Document History
==========================================

   [[ To be removed from the final specification ]]

   -01

   o  Initial draft

   o  Added OIDF Standard Notice

   o  Changed reference to Core from Standard

   o  Changed diagam step 2 tokens, made 5 and 7 bidirectional arrows

   -02

   o  Second draft

   o  updated doctype to std to mach connect and updated date

Authors' Addresses
====================================

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
=============================================

   Copyright (C) OpenID Foundation (2014).  All Rights Reserved.

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
===================================

   For OpenID Foundation's IPR Policy, refer to
   http://openid.net/ipr/OpenID_IPR_Policy_(Final_Clean_20071221).pdf

