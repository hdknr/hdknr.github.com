NOTE.2: Claims-Gathering Flow for Clients Operated by End-Users
========================================================================

.. note::
    - "3.5.1. Claims-Gathering Flow for Clients Operated by End-Users"

.. note::
    - 自然人
    - 組織人

A client, 
whether web-based or native, is operated by an end-user in
one of two typical situations:

   -  The :term:`requesting party` is a natural person 
      (for example, a friend of the resource owner); 
      the requesting party may even be the resource owner herself.

   -  The requesting party is a legal person such as a corporation, and
      the end-user operating the client is acting as an agent of that
      legal person 
      (for example, a customer support specialist representing a credit card company).

For convenience, 
this specification refers to the end-user as a ":term:`requesting end-user`" 
to cover both cases, 
which differ only at the level of business agreements 
(and potentially law), rather than technology.  

The :term:`authorization server` has a variety of options 
at this point for satisfying the resource owner's policy; 
this specification does not dictate a single answer.  

For example, 
the authorization server could require the requesting end-user to
register for and/or log in to a local authorization server account,
or to fill in a questionnaire, or to complete a purchase.  
It could even require several of these operations, 
where the order is treated as significant.  
A variety of claim profiling can be defined to achieve these effects.

An end-user-driven client MUST redirect the requesting end-user to
the authorization server to complete the process of authorization.
The redirection MUST include a URI query parameter with the name
":term:`ticket`" whose value conveys the :term:`permission ticket` 
for which the need_claims error was received; 
for example, 
"ticket=016f84e8-f9b9-11e0-bd6f-0021cc6004de".  

Each claim profile MUST provide the following capabilities:

.. glossary::

   redirect URI  
      A means by which the client MUST supply the URI to
      which the authorization server MUST redirect 
      the :term:`requesting end-user` 
      at the end of the claims-gathering process.

   callback URI  
      A means by which the client OPTIONALLY supplies a
      callback URI for the authorization server to use.

   state  
      A means by which the client SHOULD supply an opaque value used
      to maintain state between the request and the callback; this
      serves as a protection against XSRF attacks.

.. note::
    - Authz Requestの条件を言っているような...


OpenID Connect Claim Profile
-------------------------------------------------------

.. note::
    - draft08, "3.5.1.1.  OpenID Connect Claim Profile"

This section defines the OpenID Connect claim profile for UMA.

Following is a summary:

   -  Identifying URI: http://docs.kantarainitiative.org/uma/profiles/uma-claim-openid-1.0

   -  Profile author and contact information: Thomas Hardjono
      (hardjono@mit.edu)

   -  Updates or obsoletes: None; this profile is new.

   -  Syntax and semantics of claim data: As defined below.  The claim
      data format leverages the OpenID Connect protocol and the reserved
      claims defined in that specification.

   -  Claims gathering method: As defined below.

   -  Error states: None additional.

   -  Security and privacy considerations: None additional.

   -  Binding obligations: Binding obligations that apply to the use of
      this claim profile are documented in :term:`[UMA-obligations]`.

If an authorization server supports the OpenID Connect claim profile,
it MUST supply the "openid" value for one of its
"claim_profiles_supported" values in its configuration data.

To conform to this option, the authorization server MUST do the following:

   -  Serve as a conforming OpenID Relying Party according to :term:`[OIDCCore]`

   -  Be able to utilize at least all of the reserved claims defined in
      [OIDCCore] in evaluating policy and adding :term:`authorization data` to RPTs

   -  Use the OpenID Connect "redirect_uri" and "state" request parameters 
      as appropriate

The authorization server can then use any conforming OpenID Connect
mechanisms and typical user interfaces for engaging with the UserInfo
endpoints of OpenID Providers and Claims Providers, potentially
allowing for the delivery of "trusted claims" (such as a verified
email address or a date or birth) on which authorization policy for
access may depend.

