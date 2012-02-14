==========================================
OpenID Connect Lite 1.0 (Discontinued)
==========================================


.. glossary::

    OpenID Connect Lite
        Discontinued and Renamed as " :doc:`basic` ".
        Used be defined as  `OpenID Connect Lite 1.0 - draft 10 <http://openid.net/specs/openid-connect-lite-1_0.html>`_ .

Abstract
============

OpenID Connect 1.0 is a simple identity layer on top of :term:`OAuth 2.0` protocol. 
It allows a web site to verify the identity of the user based on the authentication performed by the server, 
as well as to obtain basic profile information about the user in an interoperable and RESTful manner.

OpenID Connect Lite is a profile of the full openID Connect 1.0 Specification designed to be easy to read and impliment for Relying Parties. 
Identity providers should consult the main specification. 
This profile omits Implementation and security considerations for identity providers.


.. _connect_lite_3:

3.  Protocol Flows
=======================

Authorization requests follow two paths, the implicit grant flow, and, the authorization code flow. 
The authorization code flow is suitable for clients that can securely maintain a client secret 
between itself and the authorization server whereas the implicit grant flow is suitable for clients that cannot. 
Clients that do not support TLS MUST use the code flow to prevent the interception of access tokens.

The openID Connect Lite profile only documents clients using the implicit grant flow. 
Identity Providers MUST support both flows. 
Clients wanting to use the code flow and Identity Providers should consult the full openID Connect 1.0 specification.


.. _connect_lite_3_1:

3.1.  openID Connect Scopes
-------------------------------

This profile describes two openID Connect endpoints that the client may request scopes for.

The scopes request what information is to be made available from each of the endpoints for the current user. 
The User may decline a scope request by the client.

To increase conversion a site may elect to only request a subset of the information from the User Info endpoint.

openID Connect uses scopes as defined in 4.2.1 of OAuth 2.0 [:term:`OAuth 2.0`].

The Check Session Endpoint has a single scope

    openid

        REQUIRED requests the user_id and other session information.

The User Info Endpoint scopes are:

    profile

        OPTIONAL requests default profile information.

    email

        OPTIONAL requests an email address.

    address

        OPTIONAL requests an address.

These scopes are additive if a RP wanted the default profile including email and address they would request:

The following is a non-normative example of a Scope Request. ::

    scope=openid profile email phone


.. _connect_lite_3_2:

3.2.  Implicit Flow
-------------------------

The implicit grant flow consists of the following steps:

    1. Client Prepares an Authorization Request containing the desired request parameters.
    2. Client sends a request to the Authorization Server.
    3. Authorization Server Authenticates the End-User.
    4. Authorization Server Obtains the End-User Consent/Authorization.
    5. Authorization Server Sends the End-User back to the Client with an Access Token and ID Token.

.. _connect_lite_3_2_1:

3.2.1.  Client Prepares an Authorization Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


When the user wishes to access a Protected Resource, and the End-User Authorization has not yet been obtained, 
the Client prepares an Authorization Request to the authorization endpoint.

The scheme used in the Authorization URL MUST be HTTPS.

This binding further constrains the following request parameters:

    response_type

        It MUST include token and id_token, as a space separated list. 
        This requests both a access token and id_token to be teturned in the URL fragment of the response.


Other REQUIRED parameters in the request include the following:

    client_id

        The OAuth client identifier.
    
    scope

        It MUST include openid as one of the space sparated strings openid, optional scope strings of profile, email, and address are also supported.

    redirect_uri

        redirection URI where the response will be sent (This MUST be pre-registerd with the provider.

The request MAY contain the following optional parameters:

    state

        RECOMENDED An opaque value used to maintain state between the request and the callback, used to protect against XSRF attacks.

    display

        A string value used to convey desired display format. The value are either none, popup, touch, or mobile.

    prompt

        A space delimited list that can contain login, consent, and select_account. It is used to control the dialogue that is to be shown to the user upon the request.

    nonce

        A random, unique string value used to mitigate the replay attack this value is returned from the Check Session endpoint.


Authorization servers MUST support the use of the HTTP GET method as defined in RFC 2616 [:rfc:`2616`] and 
MAY support the POST method at the authorization endpoint.

If using the HTTP GET method, the parameters are serialized using URI Query String Serialization. 
If using the HTTP POST method, the request parameters are added to the HTTP request entity-body using the application/x-www-form-urlencoded format as defined by [W3C.REC‑html401‑19991224].


The following is a non-normative example of an Authorization Request URL. 
Note that the line wraps within the values are for display purpose only::

    https://server.example.com/authorize?
    response_type=token id_token
    &client_id=s6BhdRkqt3
    &redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb
    &scope=openid profile
    &state=af0ifjsldkj

.. _connect_lite_3_2_2:

3.2.2.  Client Sends a Request to the Authorization Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Having constructed the URL, the client sends the End-User to the HTTPS End-User Authorization Endpoint using the URL. 
This MAY happen via HTTPS redirect, hyperlinking, or any other secure means of directing the User-Agent to the URL through Indirect Communication.

Following is a non-normative example using HTTP redirect. Note: Line wraps are for display purpose only.::

    HTTP/1.1 302 Found
    Location: https://server.example.com/authorize?
    response_type=token id_token
    &client_id=s6BhdRkqt3
    &redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb
    &state=af0ifjsldkj

..  _connect_lite_3_2_3:

3.2.3.  Authorization Server Obtains the End-User Consent/Authorization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Authorization Server MUST obtain an authorization decision, for the requested scopes. 
This MAY be done by presenting the user with a dialogue that allows the user to recognize 
what he is consenting to and obtain his consent or by establishing approval via other means 
(for example, via previous administrative approval).

The openid scope grants the RP access to the user identifier of the authenticated user of the session.

If the user dosen't grant access to the openid scope then an error MUST be returned by the Identity provider.

All other scopes are optional. It is up to the Identity provider to determine if the authentication should proceed 
if the user delines to authorize scopes other than openid.

.. _connect_lite_3_2_4:

3.2.4.  Authorization Server Sends the End-User Back to the Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the authorization is determined, the Authorization Server returns a positive or negative response.

.. _connect_lite_3_2_4_1:

3.2.4.1.  End-User Grants Authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the resource owner grants the access request, the authorization server issues an access token and 
delivers it to the client by adding the following parameters to the fragment component of the redirection URI 
using the application/x-www-form-urlencoded format:

In the implicit flow the entire response is returned in the fragment component of the redirect URL, as defined in 4.2.2 of OAuth 2.0 [OAuth.2.0]
( :ref:`oauth_4_2_2` )

    access_token

        REQUIRED. The Access Token for the User Info Endpoint.

    token_type

        REQUIRED Value MUST be "bearer"

    id_token

        REQUIRED The Access Token for the Check Session Endpoint.

    state

        REQUIRED if the state parameter in the request. Set to the exact value of the state parameter received from the client.

    expires_in

        OPTIONAL The expirery time in seconds of the access_token

    state

        RECOMENDED This is the state value that was sent in the request. It SHOULD be validated to prevent XRSF attacks.([#]_)


.. [#] : The 2nd "state" MUST be ommited. 

The client can then use the Access Token to access protected resources at resource servers.

The following is a non-normative example. Line wraps after the second line is for the display purpose only::

    HTTP/1.1 302 Found
    Location: https://client.example.com/#
    access_token=SlAV32hkKG&
    token_type=bearer&
    id_token=1234567.SlAV32hkKG.abcde1234&
    expires_in=3600&
    &state=af0ifjsldkj



.. _connect_lite_3_2_4_2:

3.2.4.2.  End-User Denies Authorization or Invalid Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


If the user denies the authorization or the user authentication fails, 
the server MUST return the negative authorization response as defined in 4.2.2.1 of OAuth 2.0 [OAuth.2.0]. No other parameter SHOULD be returned.


.. _connect_lite_3_3: 

3.3.  Check Session Endpoint
---------------------------------

The Check Session endpoint validates the id_token and returns a text JSON [:rfc:`4627`] object which contains information 
about the end user associated with the supplied id-token.

The id_token is used to manage the signon event and user identifier, 
separatly from access to the user_info endpoint and other OAuth 2.0 protected resources that the user is granting access to. 
The id_token is scoped to a particular client via the audiance and nonce.

A full explination of how to use the id_token to perform session management can be found in the OpenID Connect Session Management 1.0 [openID.Session]


.. _connect_lite_3_3_1:

3.3.1.  Check Session Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Check Session endpoint is an OAuth 2.0 [OAuth.2.0] protected resource that complies with the Bearer Token [OAuth.2.0.Bearer] specification. 
(:doc:`bearer` )
As such, the access token SHOULD be specified via the HTTP Authorization header.

To request the information about the authentication performed on the user, the following parameter is sent to the Check Session Endpoint.

    id_token

        REQUIRED. 
        The access_token obtained from an OpenID Connect authorization request. 
        This token MUST be sent as the access token.

The following is a non-normative example of a request to the Introspection endpoint:

Request::

    GET /check_session
    Host: server.example.com
    Authorization: Bearer 7Fjfp0Z.Br1KtDRb.nfVdmIw

.. _connect_lite_3_3_2:

3.3.2.  Check Session Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The response is a text JSON [:rfc:`4627`] object using the application/json media type with the following parameters.

    iss

        REQUIRED. The unique identifier of the issuer of the response.

    user_id

        REQUIRED. A locally unique and never reassigned identifier for the user, 
        which is intended to be consumed by the Client. e.g. 24400320 or AItOawmwtWwcT0k51BayewNvutrJUqsvl6qs7A4. 
        It MUST NOT exceed 255 ASCII characters in length.
    
    aud

        REQUIRED. This member identifies the audience that this ID Token is intended for. 
        It is RECOMENDED that aud be the oauth client_id of the RP.
    
    exp

        REQUIRED. Type Integer. 
        Identifies the expiration time on or after which the ID Token MUST NOT be accepted for processing. 
        The processing of this parameter requires that the current date/time MUST be before the expiration date/time listed in the value. 
        Implementers MAY provide for some small leeway, usually no more than a few minutes, to account for clock skew. 
        The value is number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the desired date/time. 
        See RFC 3339 [:rfc:`3339`] for details regarding date/times in general and UTC in particular.

    iso29115

        OPTIONAL. (entity authentication assurance): 
        Specifies the X.eaa / ISO/IEC29115 [ISO29115] entity authentication assurance level of the authentication performed.

    nonce

        OPTIONAL. If the authorization request includes a nonce request value, 
        then this value is REQUIRED and its value is set to the same value as the request value.

    issued_to

        OPTIONAL. The OAuth identifier of the client the token was issued to, only present if diffrent from aud.

The following is a non-normative example of a request to the Introspection endpoint:

Request::

    GET /check_session
    Host: server.example.com
    Authorization: Bearer 7Fjfp0Z.Br1KtDRb.nfVdmIw
    
Response::

    HTTP/1.1 200 OK
    Content-Type: application/json
    
    {
    "iss": "http://server.example.com",
    "user_id": "Jane Doe",
    "aud": "http://client.example.net",
    "exp":1311281970
    }


.. _connect_lite_4:

4.  UserInfo Endpoint
=========================

To obtain the additional attributes and tokens, the client makes a GET or POST request to the UserInfo Endpoint.

NOTE: In the Oauth 2.0 implicit flow, possession of an access token for a user_info endpoint is 
not proof that the user presenitng the token is the subject of the user_info endpoint. 
These tokens may be long lived and do not contain audiance information to validate that they were issued to a particular RP.

The id_token and Check Session Endpoint MUST be used to validate the identity of a session.

.. _connect_lite_4_1:

4.1.  Requesting UserInfo
-----------------------------

Clients MAY send requests with the following parameters to the UserInfo endpoint to obtain further information about the user. The UserInfo endpoint is an OAuth 2.0 [OAuth.2.0] protected resource that complies with the Bearer Token [OAuth.2.0.Bearer] specification. As such, the access token SHOULD be specified via the HTTP Authorization header.


    access_token

        REQUIRED. The access_token obtained from an OpenID Connect authorization request. 
        This parameter MUST only be sent using one method through either HTTP Authorization header or query string.

    schema

        OPTIONAL. The schema in which the data is to be returned. 
        The only predefined value is openid. If this parameter is not included, 
        the response may be a proprietary schema to support backwards compatibility. 
        A URL MAY be passed to define custom schemes not specified by short names. 
        Custom schema names and responses are out of scope for this specification.

    id

        This identifier is reserved for backwards compatibility. It MUST be ignored by the endpoint if the openid schema is used.

The following is a non-normative example. Line wraps are for display purpose only::

    GET /userinfo HTTP/1.1
    Host: server.example.com
    Authorization: Bearer vF9dft4qmT


.. _connect_lite_4_2:

4.2.  Client Receives UserInfo Response
------------------------------------------------------

If the requested schema is openid, the response MUST return a plain text JSON [:rfc:`4627`] structure that contains a set of members that are a subset of those defined below. Additional members (not specified below) MAY also be returned.

The members may be represented in multiple languages and scripts. 
To specify the languages and scripts, BCP47 [:rfc:`5646`] language tags MUST be added to each member names delimited by a #, 
e.g., familyName#ja-Kana-JP for expressing Family Name in Katakana in Japanese, 
which is commonly used to index and represent the phonetics of the Kanji representation of the same represented as familyName#ja-Hani-JP.

.. _connect_lite_table_1:

Table 1: Reserved Member Definitions 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | Member      | Type        | Description                                                                                  |
  +=============+=============+==============================================================================================+
  | user_id     | string      | Identifier for the user at the issuer.                                                       |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | name        | string      | User's full name in displayable form including all name parts,                               |
  |             |             | ordered according to user's locale and preferences.                                          |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | given_name  | string      | Given name or first name of the user.                                                        |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | family_name | string      | Surname or last name of the user.                                                            |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | middle_name | string      | Middle name of the user.                                                                     | 
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | nickname    | string      | Casual name of the user that may or may not be the same as the given_name.                   |
  |             |             | For instance, a nickname value of Mike might be returned alongside                           |
  |             |             | a given_name value of Michael.                                                               |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | profile     | string      | URL of user's profile page.                                                                  | 
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | picture     | string      | URL of the user's profile picture.                                                           |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | website     | string      | URL of user's web page or blog.                                                              |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | email       | string      | The user's preferred e-mail address.                                                         |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | verified    | boolean     | True if the user's e-mail address has been verified; otherwise false.                        |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | gender      | string      | The user's gender: female or male.                                                           |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | birthday    | string      | The user's birthday, represented as a date string in MM/DD/YYYY format. The year MAY be 0000,|
  |             |             | indicating that it is omitted.                                                               |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | zoneinfo    | string      | String from zoneinfo [zoneinfo] timezone database. For example, Europe/Paris or              |
  |             |             | America/Los_Angeles.                                                                         |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | locale      | string      | The user's locale, represented as an RFC 5646 [RFC5646] language tag. This is typically      |
  |             |             | an ISO 639-1 Alpha-2 [ISO639‑1] language code in lowercase and an ISO 3166-1 Alpha-2         | 
  |             |             | [ISO3166‑1] country code in uppercase, separated by a dash. For example, en-US or fr-CA.     |
  |             |             | As a compatibility note, some implementations have used an underscore as the separator       |
  |             |             | rather than a dash, for example, en_US; Implementations MAY choose to accept this locale     |
  |             |             | syntax as well.                                                                              | 
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | phone_number| string      | The user's preferred telephone number. For example, +1 (425) 555-1212 or +56 (2) 687 2400.   |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | address     | JSON object | The user's preferred address. The value of the address member is a JSON [RFC4627] structure  |
  |             |             | containing some or all of these string-valued fields: formatted, street_address, locality,   |
  |             |             | region, postal_code, and country.                                                            |
  |             |             | The street_address field MAY contain multiple lines if the address representation requires   |
  |             |             | it. Implementations MAY return only a subset of the fields of an address, depending upon     |
  |             |             | the information available and the user's privacy preferences.                                |
  |             |             | For example, the country and region might be returned without returning more fine-grained    |
  |             |             | address information.                                                                         |
  +-------------+-------------+----------------------------------------------------------------------------------------------+
  | updated_time| string      | Time the user's information was last updated, represented as a RFC 3339 [RFC3339] datetime.  | 
  |             |             | For example, 2011-01-03T23:58:42+0000.                                                       |
  +-------------+-------------+----------------------------------------------------------------------------------------------+


.. _connect_lite_5:

5.  Discovery and Registration
=================================

Some OpenID Connect installations can use a pre-configured set of OpenID Providers and/or Relying Parties. 
In those cases, it may not be necessary to support dynamic discovery of information about identities or services or dynamic registration of clients.

However, if installations choose to support unanticipated interactions between Relying Parties and 
OpenID Providers that do not have pre-configured relationships, 
they SHOULD accomplish this by implementing the facilities defined in the OpenID Connect Discovery 1.0 [:doc:`discovery`] and OpenID Connect Dynamic Client Registration 1.0 [OpenID.Registration] specifications.


