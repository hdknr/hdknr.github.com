========================================================
The OAuth 2.0 Authorization Protocol
========================================================

.. contents:: Table of Contents

Based on `The OAuth 2.0 Authorization Protocol draft-ietf-oauth-v2-31 <http://tools.ietf.org/html/draft-ietf-oauth-v2-31>`_

.. _oauth_abstract:

.. include:: oauth/abstract.rst

.. _oauth_1:

.. include:: oauth/1.rst

.. _oauth_1_1:

.. include:: oauth/1_1.rst

.. _oauth_1_2:

.. include:: oauth/1_2.rst

.. _oauth_1_3:

.. include:: oauth/1_3.rst

.. note::

    1.3 used to be 1.5 in v.20.

.. _oauth_1_3_1:

.. include:: oauth/1_3_1.rst

.. _oauth_1_3_2:

.. include:: oauth/1_3_2.rst

.. _oauth_1_3_3:

.. include:: oauth/1_3_3.rst

.. _oauth_1_3_4:

.. include:: oauth/1_3_4.rst

.. _oauth_1_4:

.. include:: oauth/1_4.rst

.. _oauth_1_5:

.. include:: oauth/1_5.rst

.. _oauth_1_6:

.. include:: oauth/1_6.rst

.. _oauth_2:

.. include:: oauth/2.rst

.. _oauth_2_1:

.. include:: oauth/2_1.rst

.. _oauth_2_2:

.. include:: oauth/2_2.rst

.. _oauth_2_3:

.. include:: oauth/2_3.rst

.. _oauth_2_3_1:

.. include:: oauth/2_3_1.rst

.. _oauth_2_3_2:

.. include:: oauth/2_3_2.rst

.. _oauth_2_4:

.. include:: oauth/2_4.rst

.. _oauth_3:

.. include:: oauth/3.rst

.. _oauth_3_1:

.. include:: oauth/3_1.rst

.. _oauth_3_1_1:

.. include:: oauth/3_1_1.rst

.. _oauth_3_1_2:

.. include:: oauth/3_1_2.rst

.. _oauth_3_1_2_1:

.. include:: oauth/3_1_2_1.rst

.. _oauth_3_1_2_2:

.. include:: oauth/3_1_2_2.rst

.. _oauth_3_1_2_3:

.. include:: oauth/3_1_2_3.rst

.. _oauth_3_1_2_4:

.. include:: oauth/3_1_2_4.rst

.. _oauth_3_1_2_5:

.. include:: oauth/3_1_2_5.rst

.. _oauth_3_2:

.. include:: oauth/3_2.rst

.. _oauth_3_2_1:

.. include:: oauth/3_2_1.rst

.. _oauth_3_3:

.. include:: oauth/3_3.rst

.. _oauth_4:

.. include:: oauth/4.rst

.. _oauth_4_1:

.. include:: oauth/4_1.rst

.. _oauth_4_1_1:

.. include:: oauth/4_1_1.rst

.. _oauth_4_1_2:

.. include:: oauth/4_1_2.rst

.. _oauth_4_1_2_1:

.. include:: oauth/4_1_2_1.rst

.. _oauth_4_1_3:

.. include:: oauth/4_1_3.rst

.. _oauth_4_1_4:

.. include:: oauth/4_1_4.rst


.. _oauth_4_2:

4.2.  Implicit Grant
------------------------

.. glossary::

    Implicit Grant
        The :term:`implicit` grant type is used to obtain :term:`access tokens` (it does not support the issuance of refresh tokens) 
        and is optimized for public clients known to operate a particular redirection URI.  
        These clients are typically implemented in a browser using a scripting language such as JavaScript.

As a redirection-based flow, the client must be capable of interacting with the resource owner's user-agent 
(typically a web browser) and capable of receiving incoming requests (via redirection) from the authorization server.

Unlike the authorization code grant type in which the client makes separate requests for authorization and access token, 
the client receives the access token as the result of the authorization request.

.. note::
    Implicit grant is the only way to obtain an :term:`access token` directly without intermidiate credentials.

The implicit grant type does not include client authentication, and relies on the presence of the resource owner and 
the registration of the redirection URI.  
Because the access token is encoded into the redirection URI, 
it may be exposed to the resource owner and other applications residing on its device.

Figure 4: Implicit Grant Flow ::

     +----------+
     | Resource |
     |  Owner   |
     |          |
     +----------+
          ^
          |
         (B)
     +----|-----+          Client Identifier     +---------------+
     |         -+----(A)-- & Redirection URI --->|               |
     |  User-   |                                | Authorization |
     |  Agent  -|----(B)-- User authenticates -->|     Server    |
     |          |                                |               |
     |          |<---(C)--- Redirection URI ----<|               |
     |          |          with Access Token     +---------------+
     |          |            in Fragment
     |          |                                +---------------+
     |          |----(D)--- Redirection URI ---->|   Web-Hosted  |
     |          |          without Fragment      |     Client    |
     |          |                                |    Resource   |
     |     (F)  |<---(E)------- Script ---------<|               |
     |          |                                +---------------+
     +-|--------+
       |    |
      (A)  (G) Access Token
       |    |
       ^    v
     +---------+
     |         |
     |  Client |
     |         |
     +---------+


The flow illustrated in Figure 4 includes the following steps:

   (A)  The client initiates the flow by directing the resource owner's user-agent to the authorization endpoint.  
        The client includes its client identifier, requested scope, local state, 
        and a redirection URI to which the authorization server will send the user-agent back once access is granted (or denied).

   (B)  The authorization server authenticates the resource owner (via the user-agent) and 
        establishes whether the resource owner grants or denies the client's access request.

   (C)  Assuming the resource owner grants access, the authorization server redirects the user-agent back to the client 
        using the redirection URI provided earlier.  
        The redirection URI includes the access token in the URI fragment [#]_ .

   (D)  The user-agent follows the redirection instructions by making a request to the web-hosted client resource 
        (which does not include the fragment).  
        The user-agent retains the fragment information locally.

   (E)  The web-hosted client resource returns a web page (typically an HTML document with an embedded script) 
        capable of accessing the full redirection URI including the fragment retained by the user-agent, 
        and extracting the access token (and other parameters) contained in the fragment.

   (F)  The user-agent executes the script provided by the web-hosted client resource locally, 
        which extracts the access token and passes it to the client.

.. [#] URI fragemets ( string after **#** in URL) are not exposed to any other entity other than user agents. If a security token is encoded in somewhere in URL other than fragments( i,e. path string or query string ), your user agent may disclose that security token to other 3rd party entity with HTTP Referer request parameter.

.. _oauth_4_2_1:

.. include:: oauth/4_2_1.rst

.. _oauth_4_2_2:

.. include:: oauth/4_2_2.rst

.. _oauth_4_2_2_1:

.. include:: oauth/4_2_2_1.rst




.. _oauth_4_3:

.. include:: oauth/4_3.rst

.. _oauth_4.3_1:

.. include:: oauth/4_3_1.rst

.. _oauth_4.3_2:

.. include:: oauth/4_3_2.rst

.. _oauth_4.3_3:

.. include:: oauth/4_3_3.rst

.. _oauth_4_4:

.. include:: oauth/4_4.rst

.. _oauth_4_4_1:

.. include:: oauth/4_4_1.rst

.. _oauth_4_4_2:

.. include:: oauth/4_4_2.rst

.. _oauth_4_4_3:

.. include:: oauth/4_4_3.rst



.. _oauth_4_5:

.. include:: oauth/4_5.rst

.. _oauth_5:

.. include:: oauth/5.rst

.. _oauth_5_1:

.. include:: oauth/5_1.rst

.. _oauth_5_2:

.. include:: oauth/5_2.rst

.. _oauth_6:

.. include:: oauth/6.rst

.. _oauth_7:

.. include:: oauth/7.rst

.. _oauth_7_1:

.. include:: oauth/7_1.rst

.. _oauth_8:

.. include:: oauth/8.rst

.. _oauth_8_4:

.. include:: oauth/8_4.rst

.. _oauth_9:

.. include:: oauth/9.rst

.. _oauth_10:

.. include:: oauth/10.rst

.. _oauth_11:

.. include:: oauth/11.rst

.. _oauth_11_2:

.. include:: oauth/11_2.rst

.. _oauth_11_3:

.. include:: oauth/11_3.rst

.. _oauth_11_4:

11.4. The OAuth Extensions Error Registry
----------------------------------------------------

This specification establishes the OAuth extensions error registry.

Additional error codes used together with other protocol extensions 
(i.e. extension grant types, access token types, or extension parameters) 
are registered on the advice of one or more Designated Experts 
(appointed by the IESG or their delegate), with a Specification Required 
(using terminology from [RFC5226]).  
However, to allow for the allocation of values prior to publication, 
the Designated Expert(s) may approve registration 
once they are satisfied that such a specification will be published.

Registration requests should be sent to the [TBD]@ietf.org mailing list 
for review and comment, with an appropriate subject 
(e.g., "Request for error code: example"). 
[[ Note to RFC-EDITOR: The name of the mailing list should be determined 
in consultation with the IESG and IANA.  
Suggested name: oauth-ext-review. ]]

Within at most 14 days of the request, 
the Designated Expert(s) will either approve or deny the registration request, 
communicating this decision to the review list and IANA.  
Denials should include an explanation and, 
if applicable, suggestions as to how to make the request successful.

Decisions (or lack thereof) made by the Designated Expert can be first appealed 
to Application Area Directors 
(contactable using app-ads@tools.ietf.org email address or directly by looking up their email addresses 
on http://www.iesg.org/ website) and, 
if the appellant is not satisfied with the response, to the full IESG 
(using the iesg@iesg.org mailing list).

IANA should only accept registry updates from the Designated Expert(s), 
and should direct all requests for registration to the review mailing list.

.. _oauth_13:

.. include:: oauth/13.rst

.. _oauth_13_1:

.. include:: oauth/13_1.rst

.. _oauth_13_2:

.. include:: oauth/13_2.rst
