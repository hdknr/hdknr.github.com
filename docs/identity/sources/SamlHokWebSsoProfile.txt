===============================================================
SAML V2.0 Holder-of-Key Web Browser SSO Profile Version 1.0
===============================================================

Committee Specification 02 10 August 2010

http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-holder-of-key-browser-sso.html



Related Work:
==================

    This specification is a cryptographically strong alternative to the SAML V2.0 Web Browser SSO Profile described in the SAML V2.0 Profiles specification [SAML2Prof].

Declared XML Namespace(s):
====================================

    urn:oasis:names:tc:SAML:2.0:profiles:holder-of-key:SSO:browser

Abstract:
===============

The doc:`SAML V2.0 Holder-of-Key Web Browser SSO Profile <SamlHokWebSsoProfile>`  allows 
for **transport** of :term:`holder-of-key assertions` modification of client software 
and maximum compatibility with existing deployments. 

The flow is similar to standard :term:`Web Browser SSO`, 
but an :term:`X.509 certificate` presented by the :term:`user agent` 
via a :term:`TLS handshake` supplies a key to be used in a holder-of-key assertion. 

Proof of possession of the :term:`private key` 
corresponding to the :term:`public key` in the certificate 
resulting from the :term:`TLS handshake` 
strengthens the assurance of the resulting authentication context 
and protects against credential theft. 

Neither the :term:`identity provider` nor the :term:`service provider` is required to validate the certificate.

.. contents:: Table of Contents


.. _SamlHokWebSsoProfile.1:

1 Introduction
=====================

In the scenario addressed by this profile, 
which is an alternate version of the :term:`SAML V2.0 Web Browser SSO Profile [SAML2Prof] <SAML2Prof>`,
a :term:`principal` uses an HTTP :term:`user agent` to access a web-based resource at a :term:`service provider`. 
To do so, 
the user agent presents a :term:`holder-of-key SAML assertion` acquired from its preferred :term:`identity provider`.

The user may first acquire an :term:`authentication request` 
from the :term:`service provider` or a third party. 

The :term:`user agent` transports the :term:`authentication request` 
to the :term:`identity provider` by making an HTTP request over :term:`TLS`. 
An :term:`X.509 certificate` supplied as a result of the :term:`TLS handshake` 
supplies a :term:`public key` that is associated with the :term:`principal`. 

The :term:`identity provider` authenticates the :term:`principal` by any method of its choosing 
and then produces a response containing at least one assertion with :term:`holder-of-key subject confirmation`
and an :term:`authentication statement` for the :term:`user agent` to transport to the :term:`service provider`. 
The :term:`assertion` is then presented by the :term:`user agent` to :term:`the service provider` 
by making an HTTP request over :term:`TLS`. 
An :term:`X.509 certificate` supplied as a result of the :term:`TLS handshake` proves 
possession of the :term:`private key` matching the :term:`public key` bound to the :term:`assertion`. 

Finally, 
the :term:`service provider` consumes the :term:`assertion` 
to create a :term:`security context` for the :term:`principal`.

In what follows, 
a profile of the :term:`SAML Authentication Request Protocol [SAML2Core] <SAML2Core>` is used 
in conjunction with an HTTP binding (section 2.5). 
It is assumed that the user wields an HTTP user agent, 
such as a standard web browser, 
capable of presenting :term:`client certificates` in conjunction with a :term:`TLS handshake`.

.. _SamlHokWebSsoProfile.1.2:

1.2 Terminology
----------------------------

.. glossary::

    TLS
        The term TLS as used in this specification refers to either the Secure Sockets Layer (SSL) Protocol 3.0 [:term:`SSL3`] 
        or any version of the Transport Layer Security (TLS) Protocol [:term:`RFC2246`] [:term:`RFC4346`] [:term:`RFC5246`]. 
        As used in this specification, 
        the term TLS specifically does not refer to the SSL Protocol 2.0 [:term:`SSL2`].

    X.509 certificate
        Unless otherwise noted, 
        the term X.509 certificate refers to an X.509 client certificate 
        as specified in the relevant version of the TLS protocol.

.. _SamlHokWebSsoProfile.1.3:

1.3 Normative References
--------------------------------

.. glossary::

    HoKSSO-XSD
       OASIS Committee Specification 02, Schema for SAML V2.0 Holder-of-Key Web Browser SSO Profile. August 2010. http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-holder-of-key-browser-sso.xsd
    
    RFC2119
      S. Bradner. Key words for use in RFCs to Indicate Requirement Levels. IETF RFC 2119, March 1997. http://www.ietf.org/rfc/rfc2119.txt
    
    RFC2246
      T. Dierks, C. Allen. The TLS Protocol Version 1.0. IETF RFC 2246, January 1999. http://www.ietf.org/rfc/rfc2246.txt
    
    RFC4346
      T. Dierks, E. Rescorla. The Transport Layer Security (TLS) Protocol Version 1.1. IETF RFC 4346, April 2006. http://www.ietf.org/rfc/rfc4346.txt
    
    RFC5246
      T. Dierks, E. Rescorla. The Transport Layer Security (TLS) Protocol Version 1.2. IETF RFC 5246, August 2008. http://www.ietf.org/rfc/rfc5246.txt
    
    RFC5280
      D. Cooper, S. Santesson, S. Farrell, S. Boeyen, R. Housley, W. Polk. Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile. IETF RFC 5280, May 2008. http://www.ietf.org/rfc/rfc5280.txt
    
    SAML2Bind
        OASIS Standard, Bindings for the OASIS Security Assertion Markup Language (SAML) V2.0. March 2005. http://docs.oasis-open.org/security/saml/v2.0/saml-bindings-2.0-os.pdf

    
    SAML2Core

        OASIS Standard, Assertions and Protocols for the OASIS Security Assertion Markup Language (SAML) V2.0. March 2005. http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf
    
    SAML2HoKAP
       OASIS Committee Specification 02, SAML V2.0 Holder-of-Key Assertion Profile. January 2010. http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml2-holder-of-key-cs-02.pdf
    
    SAML2Meta
        OASIS Standard, Metadata for the OASIS Security Assertion Markup Language (SAML) V2.0. March 2005. http://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf
    
    SAML2Prof
        OASIS Standard, Profiles for the OASIS Security Assertion Markup Language (SAML) V2.0. March 2005. http://docs.oasis-open.org/security/saml/v2.0/saml-profiles-2.0-os.pdf
    
    Schema1
      H. S. Thompson et al. XML Schema Part 1: Structures. World Wide Web Consortium Recommendation, May 2001. http://www.w3.org/TR/2001/REC-xmlschema-1-20010502/
    
    SSL3
     A. Freier, P. Karlton, P. Kocher. The SSL Protocol Version 3.0. Netscape Communications Corp., November 18, 1996. http://www.mozilla.org/projects/security/pki/nss/ssl/draft302.txt
    
    XMLSig
       D. Eastlake, J. Reagle, D. Solo, F. Hirsch, T. Roessler. XML Signature Syntax and Processing (Second Edition). World Wide Web Consortium Recommendation, 10 June 2008. http://www.w3.org/TR/xmldsig-core/
    

.. _SamlHokWebSsoProfile.1.4:

1.4 Non-normative References
------------------------------------

.. glossary::
    
    AIXCM
        T. Moreau. Auto Issued X.509 Certificate Mechanism (AIXCM). IETF Internet-Draft, 6 August 2008. http://www.ietf.org/internet-drafts/draft-moreau-pkix-aixcm-00.txt
    
    IDPDisco
        OASIS Committee Specification 01, Identity Provider Discovery Service Protocol and Profile., October 2007. http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-idp-discovery-cs-01.pdf
    
    NISTEAuth
        W. E. Burr et al. Electronic Authentication Guideline. National Institute of Standards and Technology, Draft Special Publication 800-63-1, 12 December 2008. http://csrc.nist.gov/publications/drafts/800-63-rev1/SP800-63-Rev1_Dec2008.pdf
    
    RFC3820
        S. Tuecke, V. Welch, D. Engert, L. Pearlman, M. Thompson. Internet X.509 Public Key Infrastructure (PKI) Proxy Certificate Profile. IETF RFC 3820, June 2004. http://www.ietf.org/rfc/rfc3820.txt
    
    SAML2Secure
        OASIS Standard, Security and Privacy Considerations for the OASIS Security Assertion Markup Language (SAML) V2.0. March 2005. http://docs.oasis-open.org/security/saml/v2.0/saml-sec-consider-2.0-os.pdf
    
    SAML2Simple
        OASIS Committee Draft 04, SAMLv2.0 HTTP POST "SimpleSign" Binding. December 2008. http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-binding-simplesign-cd-04.pdf
    
    SSL2
        K. Hickman. The SSL Protocol. Netscape Communications Corp., February 9, 1995. http://www.mozilla.org/projects/security/pki/nss/ssl/draft02.html
    
    SSTC2NIST
        "Suggested revisions to Draft NIST Special Publication 800-63-1 and the use of Assertions at Level-of-Assurance 4." OASIS SSTC, 4 November 2008. http://www.oasis-open.org/committees/download.php/29904/NIST-800-63-LOA-4-Letter-v2.pdf
    
       
    
.. _SamlHokWebSsoProfile.2:
       
2 Holder-of-Key Web Browser Profile
========================================

.. _SamlHokWebSsoProfile.2.1:

2.1 Required Information
------------------------------------

Identification: 
        urn:oasis:names:tc:SAML:2.0:profiles:holder-of-key:SSO:browser

Contact information: 
        security-services-comment@lists.oasis-open.org

SAML Confirmation Method Identifiers: 
        The SAML V2.0 “holder-of-key” confirmation method identifier, 
        urn:oasis:names:tc:SAML:2.0:cm:holder-of-key, is included in all assertions issued under this profile.

Description: 
        Given below.

Updates: 
        Provides an alternative to the SAML V2.0 Web Browser SSO Profile [SAML2Prof].

.. _SamlHokWebSsoProfile.2.2:

2.2 Background
--------------------

This profile is designed to enhance the security of :term:`SAML assertion` and message exchange 
without requiring modifications to client software. 
A :term:`holder-of-key SAML assertion` is delivered to the :term:`service provider` via an HTTP binding 
(section 2.5) over :term:`TLS`. 

The user agent presents an :term:`X.509 certificate` previously vetted by the :term:`identity provider`, 
resulting in a strong association of the resulting security context 
with the intended user and elimination of numerous attacks (section 4).

Enhanced security is the primary benefit associated with the use of this profile. 
Under ordinary :term:`Web Browser SSO`, 
there is a small chance that a :term:`bearer token` will be stolen in transit, as described in [:term:`SAML2Secure`]. 
Confirming that the presenter of the token is the intended subject through public key cryptography 
virtually eliminates this chance, improving the viability of SAML :term:`Web Browser SSO` for sensitive applications.

Related to this, 
:term:`NIST` has recently revised its E-Authentication Guideline [:term:`NISTEAuth`], 
and in the revision, 
in response to a public comment from the :term:`SSTC` [:term:`SSTC2NIST`], 
:term:`NIST` has clarified the use of "assertions" at NIST level-of-assurance 4. 

As a result of this revised E-Authentication Guideline, 
**“holder-of-key assertions may be used”** as level 4 security tokens 
provided certain requirements are met (section 10.3.2.4 of [:term:`NISTEAuth`]). 

We believe that :term:`holder-of-key SAML assertions` obtained 
via the SAML V2.0 Holder-of-Key Web Browser SSO Profile are cryptographically strong authentication tokens 
that meet the :term:`NIST` requirements.

.. _SamlHokWebSsoProfile.2.3:

2.3 Profile Overview
---------------------------

:ref:`Figure 1 <SamlHokWebSsoProfile.figure.1>` illustrates 
the basic template for achieving :term:`Web Browser SSO` under this profile. 
The following steps are described by the profile. 
Within an individual step, 
there may be one or more actual message exchanges 
depending on the binding used for that step and other deployment-specific behavior.

.. _SamlHokWebSsoProfile.figure.1:

Figure.1
^^^^^^^^^^^^^^^^^^^^

.. image:: _static/Saml/SamlHokWebSsoProfile.figure.1.png

.. _SamlHokWebSsoProfile.2.3.step.1:

1. HTTP Request to Service Provider (section 2.6.1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :term:`principal`, 
via an HTTP user agent, 
makes an HTTP request for a secured resource at the :term:`service provider`. 
at this step, 
the user agent may or may not present an :term:`X.509 certificate` to the :term:`service provider` 
in conjunction with a :term:`TLS handshake`. 
In any event, 
the :term:`service provider` determines that 
no :term:`security context` exists and subsequently initiates :term:`Holder-of-Key Web Browser SSO`.

.. _SamlHokWebSsoProfile.2.3.step.2:

2. Service Provider Determines Identity Provider (section 2.6.2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The service provider determines the principal's preferred identity provider by unspecified means.

.. _SamlHokWebSsoProfile.2.3.step.3:

3. Service Provider Issues <samlp:AuthnRequest> to Identity Provider (section 2.6.3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :term:`service provider` issues a **<samlp:AuthnRequest>** message to be delivered 
by the user agent to the :term:`identity provider`. 
An HTTP binding is used (:ref:`section 2.5 <SamlHokWebSsoProfile.2.5>` ) to transport the message 
to the :term:`identity provider` through the user agent. 
The user agent presents the message to the :term:`identity provider` in an HTTP request over TLS. 
In conjunction with TLS, 
the user agent presents an :term:`X.509 certificate` to the identity provider 
as described in :ref:`section 2.4 <SamlHokWebSsoProfile.2.4>`.

.. _SamlHokWebSsoProfile.2.3.step.4:

4. Identity Provider Identifies Principal and Verifies Key Possession (section 2.6.4)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :term:`principal` is identified by the :term:`identity provider` at this step. 
The :term:`identity provider` identifies the :term:`principal` 
using any authentication method at its disposal 
while honoring any requirements imposed by the service provider in the **<samlp:AuthnRequest>** message. 
The :term:`identity provider` must establish that the user agent holds the :term:`private key` 
corresponding to the :term:`public key` bound to the :term:`X.509 certificate` and 
that the :term:`public key` does in fact belong to the :term:`principal`.

.. _SamlHokWebSsoProfile.2.3.step.5:

5. Identity Provider Issues <samlp:Response> to Service Provider (section 2.6.5)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :term:`identity provider` issues a **<samlp:Response>** message to be delivered 
by the user agent to the :term:`service provider`. 
The response either indicates an error or includes at least an authentication statement in a :term:`holder-of-key assertion`. 
An HTTP binding is used (:ref:`section 2.5 <SamlHokWebSsoProfile.2.5>`) 
to transport the message to the :term:`service provider` through the user agent. 
The user agent presents the message to the :term:`service provider` in an HTTP request over TLS. 
As in step 3, the user agent presents an :term:`X.509 certificate` to the :term:`service provider` 
as described in :ref:`section 2.4 <SamlHokWebSsoProfile.2.4>`.

.. _SamlHokWebSsoProfile.2.3.step.6:

6. Service Provider Grants or Denies Access to Principal (section 2.6.6)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The SAML response is consumed by the :term:`service provider` 
who either responds to the principal's user agent 
by establishing a :term:`security context` for the :term:`principal` and 
returning the requested resource, or by returning an error.


Note
^^^^^^^^^^^^
Note that 
an :term:`identity provider` can initiate this profile at :ref:`step 5  <SamlHokWebSsoProfile.2.3.step.5>`
by issuing a **<samlp:Response>** message to a service provider without the preceding steps. 

.. note::
    Idp Initiated Assertion

The user agent or a third party may also initiate this profile 
by submitting an unsigned request at :ref:`step 3 <SamlHokWebSsoProfile.2.3.step.3>`.


.. _SamlHokWebSsoProfile.2.4:

2.4 TLS Usage
---------------------------------

As noted in the introduction, 
this profile is an alternative to ordinary SAML Web Browser SSO [:term:`SAML2Prof`]. 
The primary difference between that profile and this :term:`Holder-of-Key Web Browser SSO Profile` is that 
the :term:`principal` MUST present an :term:`X.509 certificate` 
and prove possession of the :term:`private key` associated with the :term:`public key` bound to the certificate. 
This leads to :term:`holder-of-key subject confirmation` [:term:`SAML2HoKAP`], 
a type of subject confirmation that is stronger than the :term:`bearer subject confirmation` inherent 
in ordinary :term:`Web Browser SSO`.

The user agent presents an :term:`X.509 certificate` 
in conjunction with a :term:`TLS handshake`. 
It is important to realize that 
the presented certificate need not be a :term:`trusted certificate` 
(although this is certainly permitted). 
However, the certificate MUST be presented via TLS. 
This proves possession of the corresponding :term:`private key`.

According to the TLS protocol, 
validation of the client certificate is optional. 
Likewise this :term:`Holder-of-Key Web Browser SSO Profile` does not require TLS client authentication, 
which is strictly OPTIONAL (but see section 4.3). 
Moreover, 
the authentication method by which the :term:`identity provider` identifies the :term:`principal` is unspecified.

According to the TLS handshake protocol, 
if the TLS server can not validate the client certificate, 
the server may either continue the handshake 
or prematurely terminate the handshake by returning a fatal alert to the client. 
Moreover, 
if the TLS server chooses to send a fatal alert, 
it must immediately close the HTTP connection according to the TLS protocol. 
Clearly this is undesirable, 
so the TLS server MUST be configured to continue the TLS handshake to completion 
even in the presence of an untrusted client certificate. 
The method of doing so depends on the chosen TLS implementation 
and is therefore out of scope with respect to this profile.

In summary, 
the :term:`principal` MUST present an :term:`X.509 certificate` (via TLS) 
and prove possession of the :term:`private key` 
at :ref:`steps 3 <SamlHokWebSsoProfile.2.3.step.3>` and :ref:`5 <SamlHokWebSsoProfile.2.3.step.5>` 
(sections :ref:`2.6.3 <SamlHokWebSsoProfile.2.6.3>` and :ref:`2.6.5 <SamlHokWebSsoProfile.2.6.5>`, resp.). 
However, 
the presentation of an :term:`X.509 certificate` at :ref:`step 1 <SamlHokWebSsoProfile.2.3.step.1>`
(:ref:`section 2.6.1 <SamlHokWebSsoProfile.2.6.1>`) is strictly OPTIONAL.

At the conclusion of the :term:`TLS handshake`, 
the :term:`identity provider` 
(resp., the service provider) 
MUST be able to retrieve the :term:`X.509 certificate` presented by the user agent 
at :ref:`step 4 <SamlHokWebSsoProfile.2.3.step.4>` 
(resp. [#]_ , :ref:`step 6 <SamlHokWebSsoProfile.2.3.step.6>`). 
The consequences of a failure to do so is discussed in detail 
in :ref:`section 2.6.4 <SamlHokWebSsoProfile.2.6.4>` 
(resp., :ref:`section 2.6.6 <SamlHokWebSsoProfile.2.6.6>` ).

At either of :ref:`steps 3 <SamlHokWebSsoProfile.2.3.step.3>` or :ref:`5 <SamlHokWebSsoProfile.2.3.step.5>` (or both), 
the :term:`identity provider` or the :term:`service provider` (resp.) 
MAY use the :term:`public key` bound to the certificate 
or the :term:`TLS session key` to create a :term:`security context` for the :term:`principal`. 
Also, 
at :ref:`step 1 <SamlHokWebSsoProfile.2.3.step.1>`, 
the :term:`service provider` MAY use the :term:`public key` bound to the certificate or 
the :term:`TLS session key` to associate any subsequent exchange with the original request.

.. [#] resp. = respectively, (in listing a number of items or attributes that refer to another list) separately in the order given

.. _SamlHokWebSsoProfile.2.5:

2.5 Choice of Binding
------------------------------------------

The :term:`identity provider` and the :term:`service provider` MUST use a browser-based HTTP binding 
to transmit the SAML protocol message to the other party. 
A SAML HTTP binding [:term:`SAML2Bind`] MAY be used for this purpose:

    HTTP Redirect

    HTTP POST

    HTTP Artifact

This profile does not preclude the use of other browser-based HTTP bindings 
(such as the SAML V2.0 SimpleSign binding [:term:`SAML2Simple`]).

The :term:`identity provider` and the :term:`service provider` independently choose their preferred binding 
(subject to the other party's desire or ability to comply). 
The :term:`service provider` chooses an HTTP binding to transmit the **<samlp:AuthnRequest>** message 
to the :term:`identity provider`. 
Later, 
independent of the service provider's choice of binding, 
the :term:`identity provider` chooses an HTTP binding to transmit the **<samlp:Response>** message 
to the :term:`service provider`. 
The :term:`identity provider` MUST NOT use the HTTP Redirect binding 
since the response typically exceeds the **URL length** permitted by most HTTP user agents.

If the :term:`service provider` uses either the HTTP Redirect or HTTP POST binding, 
the **<samlp:AuthnRequest>** message is delivered directly to the :term:`identity provider` 
at :ref:`step 3 <SamlHokWebSsoProfile.2.3.step.3>` (:ref:`section 2.6.3 <SamlHokWebSsoProfile.2.6.3>`). 
If the :term:`service provider` uses the HTTP Artifact binding, 
the :term:`identity provider` uses the :term:`Artifact Resolution Profile` [:term:`SAML2Prof`] 
to make a callback to the service provider to retrieve the **<samlp:AuthnRequest>** message.

Similarly, 
if the :term:`identity provider` uses the HTTP POST binding, 
the **<samlp:Response>** message is delivered directly to the service provider 
at :ref:`step.5 <SamlHokWebSsoProfile.2.3.step.5>` (:ref:`section 2.6.5 <SamlHokWebSsoProfile.2.6.5>`). 
If the :term:`identity provider` uses the HTTP Artifact binding, 
the :term:`service provider` uses the :term:`Artifact Resolution Profile` 
to make a callback to the :term:`identity provider` to retrieve the **<samlp:Response>** message.


.. _SamlHokWebSsoProfile.2.6:

2.6 Profile Description
------------------------------------------------

The :doc:`SAML V2.0 Holder-of-Key Web Browser SSO Profile <SamlHokWebSsoProfile>` is a profile of 
the SAML V2.0 Authentication Request Protocol [:term:`SAML2Core`]. 
Where this :term:`Holder-of-Key Web Browser SSO` specification conflicts with Core, 
the former takes precedence.

If the request is initiated by the :term:`service provider`, 
begin with section :ref:`2.6.1 <SamlHokWebSsoProfile.2.6.1>`. 
If the request is initiated by the user agent or a third party, 
begin with section :ref:`2.6.4 <SamlHokWebSsoProfile.2.6.4>`. 
If the :term:`identity provider` issues a response without a corresponding request, 
begin with :ref:`section 2.6.5 <SamlHokWebSsoProfile.2.6.5>`. 
The descriptions refer to a single sign-on service and assertion consumer service 
in accordance with their use described in section 4.1.3 of [:term:`SAML2Prof`]. 
Processing rules for all messages are specified in :ref:`section 2.7 <SamlHokWebSsoProfile.2.7>`  of this profile.

.. _SamlHokWebSsoProfile.2.6.1:

2.6.1 HTTP Request to Service Provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The profile may be initiated by an arbitrary HTTP request to the :term:`service provider`. 
The :term:`service provider` is free to use any means 
it wishes to associate the subsequent interactions with the original request. 
For example, 
each of the SAML HTTP bindings discussed in :ref:`section 2.5 <SamlHokWebSsoProfile.2.5>` provides 
a :term:`RelayState mechanism` that the :term:`service provider` MAY use to associate any subsequent exchange 
with the original request.

.. _SamlHokWebSsoProfile.2.6.2:

2.6.2 Service Provider Determines Identity Provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :term:`service provider` determines the principal's preferred identity provider 
by any means at its disposal, 
including but not limited to the SAML V2.0 Identity Provider Discovery Profile [:term:`SAML2Prof`] 
or the Identity Provider Discovery Service Protocol and Profile [:term:`IDPDisco`]. 
If the user agent presents an :term:`X.509 certificate` at the previous step, 
the :term:`service provider` MAY use the :term:`X.509 certificate` as a means of discovery. 
Use of the :term:`X.509 certificate` in this way is out of scope. 
However, see :ref:`section 4.2 <SamlHokWebSsoProfile.4.2>` for relevant discussion.

.. _SamlHokWebSsoProfile.2.6.3:

2.6.3 Service Provider issues <samlp:AuthnRequest> to Identity Provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once an :term:`identity provider` has been selected, 
the location of the single sign-on service 
to which to send a **<samlp:AuthnRequest>** message is determined based on the SAML binding 
chosen by the :term:`service provider` ( :ref:`section 2.5 <SamlHokWebSsoProfile.2.5>`). 
Metadata as described in :ref:`section 2.8 <SamlHokWebSsoProfile.2.8>` MAY be used for this purpose. 
Following the HTTP request by the user agent in :ref:`section 2.6.1 <SamlHokWebSsoProfile.2.6.1>`, 
an HTTP response is returned containing a **<samlp:AuthnRequest>** message or an artifact, 
depending on the SAML binding used, to be delivered to the identity provider's single sign-on service.

Profile-specific rules for the contents of the **<samlp:AuthnRequest>** element are given 
in :ref:`section 2.7.1 <SamlHokWebSsoProfile.2.7.1>`.

.. _SamlHokWebSsoProfile.2.6.4:

2.6.4 Identity Provider Identifies Principal and Verifies Key Possession
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The identity provider must perform two functions in this step: identify the principal presenting the <samlp:AuthnRequest> message and verify that the principal possesses the private key associated with the public key bound to the presented X.509 certificate. The identity provider subsequently binds X.509 data from the certificate (or the certificate itself) to a <saml:SubjectConfirmation> element.

The identity provider MUST establish the identity of the principal (unless it will return an error) prior to the issuance of the <samlp:Response> message. If the ForceAuthn attribute on the <samlp:AuthnRequest> element is present and true, the identity provider MUST freshly establish this identity rather than relying on any existing session it may have with the principal. Otherwise, and in all other respects, the identity provider may use any means to authenticate the user agent, subject to any requirements called out in the <samlp:AuthnRequest> message. In particular, the identity provider MAY use TLS client authentication to identify the principal. That is, the identity provider MAY validate the presented X.509 certificate as described in [RFC5280], but this is by no means a requirement. See section 2.4 for details.

As described in section 2.4, it is REQUIRED that the <samlp:AuthnRequest> message be presented to the identity provider via an HTTP request over TLS that supplies the identity provider with an X.509 certificate and establishes the user agent's possession of the corresponding private key. The certificate resulting from the TLS handshake MUST be used to construct any holder-of-key <saml:SubjectConfirmation> elements in the issued <samlp:Response> element.

Any holder-of-key <saml:SubjectConfirmation> elements included in the response MUST conform to the SAML V2.0 Holder-of-Key Assertion Profile [SAML2HoKAP]. See section 2.7.3 for consequences of this dependency. In addition, note well that the Holder-of-Key Assertion Profile requires that the X.509 certificate obtained as a result of the TLS handshake MUST be known to be associated with the principal (see section 2.4 of [SAML2HoKAP]). Precisely how the identity provider satisfies this requirement is out of scope, but see section 4.3.

If the principal is unable to prove possession of the private key corresponding to the public key in the certificate (via TLS), or the identity provider is unable to retrieve the X.509 certificate resulting from the TLS handshake, the identity provider MUST return an error. Otherwise, the identity provider processes the request following the rules specified in section 2.7.2.

.. _SamlHokWebSsoProfile.2.6.5:

2.6.5 Identity Provider Issues <samlp:Response> to Service Provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Depending on the SAML binding used (section 2.5), the identity provider returns an HTTP response to the user agent containing a <samlp:Response> message or an artifact, to be delivered to the service provider's assertion consumer service. Profile-specific rules regarding the contents of the <samlp:Response> element are included in section 2.7.3.

.. _SamlHokWebSsoProfile.2.6.6:

2.6.6 Service Provider Grants or Denies Access to Principal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As specified in section 2.4, the HTTP request that transports the response issued at the previous step MUST be made over TLS. This supplies proof of possession of the private key and an X.509 certificate to be checked against the X.509 data bound to the assertion's <saml:SubjectConfirmation> element. The TLS protocol also maintains the confidentiality and integrity of the message exchange.

If the principal is unable to prove possession of the private key corresponding to the public key in the certificate (via TLS), or the service provider is unable to retrieve the X.509 certificate resulting from the TLS handshake, the subject is not confirmed and the service provider SHOULD NOT create a security context for the principal.

Otherwise, the service provider MUST process the <samlp:Response> message and any enclosed <saml:Assertion> elements as described in [SAML2Core] and section 2.7.4 below. Any subsequent use of the <saml:Assertion> elements is at the discretion of the service provider and other relying parties, subject to any restrictions on use contained within the assertions themselves or previously established out-of-band policy governing interactions between the identity provider and the service provider.

To complete the profile, the service provider creates a security context for the user. The service provider MAY establish a security context with the user agent using any session mechanism it chooses. In particular, the public key or the TLS session key MAY be used to create the security context as discussed in section 2.4.

.. _SamlHokWebSsoProfile.2.7:

2.7
-------

.. _SamlHokWebSsoProfile.2.7.1:

2.7.1
-------

.. _SamlHokWebSsoProfile.2.8:

2.8
-------

.. _SamlHokWebSsoProfile.4.2:

4.2
----
