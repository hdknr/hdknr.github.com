=================================
Simple Web Discovery (SWD)
=================================

Based on Mike Jones' `draft-jones-simple-web-discovery-01 <http://self-issued.info/docs/draft-jones-simple-web-discovery.html>`_ .


.. note::

    John Bradley's proposal to extend multiple issuer support at the same server.

        - http://hg.openid.net/connect/issue/513/basic-12-messages-814-discovery-31-32

Abstract
===========

.. glossary:: 

    SWD
        Simple Web Discovery (SWD) defines a HTTPS GET based mechanism to discover the location of a given type of service 
        for a given principal starting only with a domain name.

.. _swd_1:

1.  Introduction
====================

Simple Web Discovery (SWD) defines a HTTPS GET based mechanism to discover the location of a given type of service 
for a given principal starting only with a domain name. 
SWD requests use the x-www-form-urlencoded format to specify a URI for the principal 
and another URI for the type of service being sought. 
If the request is successful then the response, by default, is a JSON object containing an array of URIs 
that point to where the principal has instances of services of the requested type.

For example, let us say that a requester wants to discover where Joe keeps his calendar. 
The requester could take Joe's e-mail address, joe@example.com 
and take from it its domain to create a HTTPS GET request of the following form::

    GET /.well-known/simple-web-discovery?principal=mailto:joe@example.com&service=urn:adatum.com:calendar HTTP/1.1
    Host: example.com
    
    HTTP/1.1 200 O.K.
    Content-Type: application/json
    
    {
     "locations": ["http://calendars.proseware.com/calendars/joseph"]
    }

Note: The request-URI is left un-encoded in the above example for the sake of readability in the above example.

.. _swd_2:

2.  Simple Web Discovery Request
====================================

Domains that support SWD requests MUST make available a SWD server for their domain at the path .well-known/simple-web-discovery. 
The syntax and semantics of ".well-known" are defined in RFC 5785 [:rfc:`5785`]. 
"simple-web-discovery" MUST point to a SWD server compliant with this specification.

SWD servers MUST support receiving SWD requests via TLS 1.2 as defined in RFC 5246 [:rfc:`5246`] 
and MAY support other transport layer security mechanisms of equivalent security. 
SWD servers MUST reject SWD requests sent over plain HTTP or any other transport that 
does not provide both privacy and validation of the server's identity.

A SWD server is queried using a HTTPS GET request with the previously specified path along 
with a query segment containing a x-www-form-urlencoded form as defined in HTML 4.01 [W3C.REC‑html401‑19991224]. 
The form MUST contain two name/value pairs that MUST appear exactly once, principal and service. 
Both name/value pairs MUST have values that are set to URIs (as defined in RFC 3986 [RFC3986]). 
If any of the previous requirements are not met in a SWD request, then the request MUST be rejected with a 400 Bad Request.

The SWD request form MAY contain additional name/value pairs 
but if those name/value pairs are not recognized by the SWD server 
then the SWD server MUST ignore them for processing purposes.

The principal query component is a URI that identifies an entity. 
The service query component is a URI that identifies a service type. 
The semantics of the SWD query is "Please return the location(s) of instances of the specified service type 
associated with the specified principal". 
The definition of URIs used to identify principals and services are outside the scope of this specification.

.. _swd_3:

3.  Simple Web Discovery Responses
================================================

.. _swd_3_1:

3.1.  Response Containing One or More Locations
------------------------------------------------

Unless another content-type is negotiated, a 200 O.K. response to a SWD request 
that contains the information requested MUST return content of type application/json as defined in RFC 4627 [RFC4627]. 
The JSON response MUST contain a JSON object that contains a member pair whose name is the string locations 
and whose value is an array of strings that are each a URI pointing to a location 
where the desired service type belonging to the specified principal can be found. 
There are no semantics associated with the order in which the URIs are listed in the array.

The JSON object MAY contain other members 
but a receiver of the object MAY ignore any member pairs whose name it does not recognize.

.. _swd_3_2:

3.2.  Redirecting All Simple Web Discovery Requests
------------------------------------------------------------------------------------------------

SWD requests by definition start off by being issued to the .well-known/simple-web-discovery location. 
But locating a SWD server at a root location can prove inconvenient. 
To enable service level redirection a SWD server MAY return a 200 O.k. to an HTTPS request with a content type of application/json 
(or whatever other content type has been negotiated) 
that contains a JSON object that contains a member pair whose name is the string SWD_service_redirect 
whose value is a JSON object with a member pair whose name is location 
and whose value is a string that encodes a URI. 
Optionally the JSON object value of SWD_service_redirect MAY also contain a member 
whose name is expires and whose value is a JSON number that encodes an integer.

A SWD compliant client MUST support the SWD_service_redirect response.

The JSON objects MAY contain other members but a receiver of the objects MAY ignore any pairs whose name it does not recognize.

The location member identifies the URI that the caller MUST redirect all SWD requests 
for that domain to until the expires time is met. 
SWD requests for the redirected domain MUST be constructed by taking the URI returned in the location 
and using it as the base URI to which the SWD form arguments are then added as query parameters. 
The location URI MUST NOT include a query component.

::

    GET /.well-known/simple-web-discovery?principal=mailto:joe@example.com&service=urn:adatum.com:calendar HTTP/1.1
    Host: example.com

    HTTP/1.1 200 O.K.
    Content-Type: application/json
    
    {
     "SWD_service_redirect":
      {
       "location": "https://swd.proseware.com/swd_server",
       "expires": 1300752001
      }
    }
    
::

    GET /swd_server?principal=mailto:joe@example.com&service=urn:adatum.com:calendar HTTP/1.1
    Host: swd.proseware.com
    
    HTTP/1.1 200 O.K.
    Content-Type: application/json
    
    {
     "locations": ["http://calendars.proseware.com/calendars/joseph"]
    }

Note: The request-URIs are left un-encoded in the above example for the sake of readability in the above example.

The location URI MUST be an HTTPS URL.

The optional expires member identifies the point in time at which the caller MUST NOT redirect its SWD requests 
for that domain to the previously obtained location and MUST instead return to the .well-known/simple-web-discovery location. 
The value of the expires member MUST encode the number of seconds from 1970-01-01T0:0:0Z as measured in UTC 
until the desired date/time. 
See RFC 3339 [RFC3339] for details regarding date/times in general and UTC in particular. 
If the expires value is in the past or if the value is more than one hour in the future 
then the response MUST be treated as if it didn't contain an expires value.

If the expires value is omitted or if its value is incorrect 
then the expires value MUST be treated as having a value of exactly one hour into the future.

If a JSON response is received that contains both a member pair with the name SWD_service_redirect 
and a member pair with the name locations as children of the object root 
then the SWD_service_redirect member pair MUST be ignored.


.. _swd_3_3:

3.3.  401 Unauthorized Response
------------------------------------------------------------------------------------------------

A SWD server MAY respond to a request with a 401 Unauthorized Response, 
as described in RFC 2616 [RFC2616], Section 10. 
Per the RFC, the request MAY be repeated with a suitable Authorization header field. 
Authorization information may be communicated in this manner, including a JSON Web Token [:term:`JWT`].

.. _swd_3_4:

3.4.  Other HTTP 1.1 Responses
------------------------------------------------------------------------------------------------

A SWD server MAY return other HTTP 1.1 responses, including 404 Not Found, 400 Bad Request, 
and 403 Forbidden. 
SWD implementations MUST correctly handle these responses.


