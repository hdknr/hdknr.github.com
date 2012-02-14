============================================================
SAML V2.0 Holder-of-Key Assertion Profile Version 1.0
============================================================

Committee Specification 02 
23 January 2010

 - http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml2-holder-of-key.html
 - http://wiki.oasis-open.org/security/SAMLHoKSubjectConfirmation

Declared XML Namespace(s):
============================================================

    urn:oasis:names:tc:SAML:2.0:profiles:holder-of-key

Abstract
============

The :doc:`SAML V2.0 Holder-of-Key Assertion Profile <SamlHokProfile>` describes 
the **issuing** and **processing** of :term:`holder-of-key` SAML assertions. 
Specifically, 
we show how a :term:`SAML issuer` binds :term:`X.509 data` to a **<ds:KeyInfo>** element 
and how a :term:`relying party` confirms that a **<ds:KeyInfo>** element matches given :term:`X.509 data`. 
The binding material used by the SAML issuer 
and the matching data used by the relying party are obtained from an X.509 certificate.

.. contents:: Table of Contents


.. _SamlHokProfile.1:

1 Introduction
====================

The :doc:`SAML V2.0 Holder-of-Key Assertion Profile <SamlHokProfile>` describes 
the **issuing** and **processing** of a :term:`holder-of-key SAML assertion`, 
that is, an :term:`assertion` containing a **<saml:SubjectConfirmation>** element 
whose **Method** attribute is set to **urn:oasis:names:tc:SAML:2.0:cm:holder-of-key**. 

Specifically, 
we describe the structural characteristics of a **<ds:KeyInfo>** element with bound :term:`X.509 data` 
and show how a :term:`relying party` confirms that such a **<ds:KeyInfo>** element matches given :term:`X.509 data`. 
The binding material used by the :term:`SAML issuer` and 
the matching data used by the :term:`relying party` are obtained from an :term:`X.509 certificate`.

This profile involves 
a :term:`SAML issuer` and a :term:`SAML relying party`, 
each with an :term:`X.509 certificate` in its possession. 
The :term:`SAML issuer` uses its certificate to produce a :term:`holder-of-key SAML assertion`. 
The :term:`relying party` consumes the :term:`assertion`, 
confirming the attesting entity by comparing the :term:`X.509 data` 
in the assertion with the :term:`X.509 data` in its possession.

.. _SamlHokProfile.1.1:

1.1 Notation
-----------------------------------

This specification uses normative text. The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this specification are to be interpreted as described in [RFC2119]:

::

    …they MUST only be used where it is actually required for interoperation or to limit behavior which has potential for causing harm (e.g., limiting retransmissions)…

These keywords are thus capitalized 
when used to unambiguously specify requirements over protocol and application features and behavior 
that affect the interoperability and security of implementations. 
When these words are not capitalized, they are meant in their natural-language sense.

::

    Listings of XML schemas appear like this.

::

    Example code listings appear like this.

Conventional XML namespace prefixes are used throughout the listings in this specification to stand for their respective namespaces as follows, whether or not a namespace declaration is present in the example:

 +--------------+-------------------------------------------+---------------------------------------------------+
 | Prefix       | XML Namespace                             | Comments                                          |
 +==============+===========================================+===================================================+
 | saml:        | urn:oasis:names:tc:SAML:2.0:assertion     | This is the SAML V2.0 assertion namespace         |
 |              |                                           | defined in the SAML V2.0 core specification       |
 |              |                                           | [SAML2Core].                                      | 
 |              |                                           |                                                   |
 +--------------+-------------------------------------------+---------------------------------------------------+
 | ds:          | http://www.w3.org/2000/09/xmldsig#        | This is the XML Signature namespace [XMLSig].     |
 |              |                                           |                                                   |
 +--------------+-------------------------------------------+---------------------------------------------------+
 | xs:          | http://www.w3.org/2001/XMLSchema          | This is the XML Schema namespace [Schema1].       |
 |              |                                           |                                                   |
 +--------------+-------------------------------------------+---------------------------------------------------+
 | xsi:         | http://www.w3.org/2001/XMLSchema-instance | This is the XML Schema namespace for              |
 |              |                                           | schema-related markup                             |
 |              |                                           | that appears in XML instances [Schema1].          |
 |              |                                           |                                                   |
 +--------------+-------------------------------------------+---------------------------------------------------+

.. _SamlHokProfile.1.2:

1.2 Terminology
-----------------------------------

In this specification, a SAML issuer is a producer of holder-of-key assertions. Similarly, a relying party is a consumer of holder-of-key assertions.

A presenter transmits a holder-of-key assertion to the relying party. An attesting entity is a presenter who is able to satisfy the subject confirmation requirements of the holder-of-key assertion.

Usually the attesting entity is the subject of the assertion (hence the terms "subject confirmation" and "confirming the subject"). In general, however, the attesting entity may not be the subject, in which case the previous phrases are misnomers. Thus the terms "attestation" and "confirming the attesting entity" are more technically correct than "subject confirmation" and "confirming the subject," respectively. We will use the term "attesting entity" exclusively in this document.


.. glossary::
        
    SAML issuer 
        a producer of holder-of-key assertions. 

    relying party 
        a consumer of holder-of-key assertions.

    presenter 
        A presenter transmits a holder-of-key assertion to the relying party. 

    attesting entity 
        a :term:`presenter` who is able to satisfy 
        the subject confirmation requirements of the holder-of-key assertion.

        Usually the attesting entity is the subject of the assertion 
        (hence the terms "subject confirmation" and "confirming the subject"). 

        In general, however, 
        the attesting entity may not be the subject, 
        in which case the previous phrases are misnomers. 

        Thus the terms "attestation" 
        and "confirming the attesting entity" are more technically correct than 
        "subject confirmation" and "confirming the subject," respectively. 

.. _SamlHokProfile.1.3:

1.3 Normative References
--------------------------------

.. glossary::

    RFC2119
        S. Bradner. Key words for use in RFCs to Indicate Requirement Levels. IETF RFC 2119, March 1997. http://www.ietf.org/rfc/rfc2119.txt
    
    RFC4514
        K. Zeilenga. Lightweight Directory Access Protocol (LDAP): String Representation of Distinguished Names. IETF RFC 4514, June 2006. http://www.ietf.org/rfc/rfc4514.txt
    
    RFC5280
        D. Cooper, S. Santesson, S. Farrell, S. Boeyen, R. Housley, W. Polk. Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile. IETF RFC 5280, May 2008. http://www.ietf.org/rfc/rfc5280.txt
    
    SAML2Core
        OASIS Standard, Assertions and Protocols for the OASIS Security Assertion Markup Language (SAML) V2.0. March 2005. http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf
    
    SAML2Prof
        OASIS Standard, Profiles for the OASIS Security Assertion Markup Language (SAML) V2.0. March 2005. http://docs.oasis-open.org/security/saml/v2.0/saml-profiles-2.0-os.pdf
    
    Schema1
        H. S. Thompson et al. XML Schema Part 1: Structures. World Wide Web Consortium Recommendation, May 2001. See http://www.w3.org/TR/2001/REC-xmlschema-1-20010502/
    
    XMLSig
        D. Eastlake, J. Reagle, D. Solo, F. Hirsch, T. Roessler. XML Signature Syntax and Processing (Second Edition). World Wide Web Consortium Recommendation, 10 June 2008. http://www.w3.org/TR/xmldsig-core/


.. _SamlHokProfile.1.4:

1.4 Non-normative References
---------------------------------

.. glossary::

    RFC3820
        S. Tuecke, V. Welch, D. Engert, L. Pearlman, M. Thompson. Internet X.509 Public Key Infrastructure (PKI) Proxy Certificate Profile. IETF RFC 3820, June 2004. http://www.ietf.org/rfc/rfc3820.txt
    
    RFC4346
        T. Dierks, E. Rescorla. The Transport Layer Security (TLS) Protocol Version 1.1. IETF RFC 4346, April 2006. http://www.ietf.org/rfc/rfc4346.txt
    
    SAML2ConDel
        S. Cantor. SAML V2.0 Condition for Delegation Restriction. OASIS SSTC Committee Draft 01, 10 March 2009. http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-delegation-cd-01.pdf


.. _SamlHokProfile.2:

2 SAML V2.0 Holder-of-Key Assertion Profile
======================================================

.. _SamlHokProfile.2.1:

2.1 Required Information
--------------------------------

Identification: 
    urn:oasis:names:tc:SAML:2.0:profiles:holder-of-key

Contact information: 
    security-services-comment@lists.oasis-open.org

SAML Confirmation Method Identifiers: 
    The SAML V2.0 holder-of-key confirmation method identifier 
    (urn:oasis:names:tc:SAML:2.0:cm:holder-of-key) 
    is associated with every **<saml:SubjectConfirmation>** element issued under this profile.

Description: 
    Given below.

Updates: 
    Supplements the holder-of-key confirmation method described in section 3.1 of [:term:`SAML2Prof`].


.. _SamlHokProfile.2.2:

2.2 Profile Description
---------------------------------

.. glossary::

    holder-of-key assertion
        A SAML assertion which contains **<saml:SubjectConfirmation>** XML element,
        where 

        .. code-block :: xml
        
            <saml:SubjectConfirmation
                'Method'='urn:oasis:names:tc:SAML:2.0:cm:holder-of-key'
            > 

    holder-of-key SAML assertion
        :term:`holder-of-key assertion`

This specification profiles 
a type of :term:`assertion` called a :term:`holder-of-key assertion`. 
By definition, 
a :term:`holder-of-key SAML assertion` contains 
a **<saml:SubjectConfirmation>** element 
whose **Method** attribute is set to urn:oasis:names:tc:SAML:2.0:cm:holder-of-key. 

This specification describes how the :term:`SAML issuer` binds 
selected :term:`X.509 data` from an :term:`X.509 certificate` 
to the **<saml:SubjectConfirmation>** element of a holder-of-key assertion. 
The complementary process involves 
a :term:`relying party` who confirms that the :term:`X.509 data` 
bound to the :term:`assertion` matches the data in a given :term:`X.509 certificate`.

Suppose 
a :term:`SAML response` issued by a :term:`SAML issuer` contains 
one or more holder-of-key assertions 
(otherwise this specification is not applicable). 

At the time the assertion is issued, 
the issuer possesses an X.509 certificate known to be associated with the attesting entity 
(who may or may not be present when the assertion is issued). 
The SAML issuer binds some (or all) of the :term:`X.509 data`
in the certificate to the holder-of-key assertion.

Subsequently, 
the :term:`attesting entity` presents 
the :term:`holder-of-key assertion` and an :term:`X.509 certificate` to the :term:`relying party`. 
The :term:`attesting entity` proves possession of the :term:`private key` 
corresponding to the :term:`public key` bound to the certificate, 
the details of which are out of scope with respect to this profile. 
The :term:`relying party` compares the :term:`X.509 data` in the certificate 
to the :term:`X.509 data` bound to the :term:`assertion`, 
thereby confirming the :term:`attesting entity`.

Precisely how the :term:`issuer` comes to possess a certificate 
known to be associated with :term:`attesting entity` and 
how the :term:`assertion` and the certificate are presented to the :term:`relying party` are 
all out of scope with respect to this profile. 

On the other hand, 
the issuing of the :term:`holder-of-key assertion` itself and 
the ultimate confirmation of the :term:`attesting entity` are in scope.

We assume that the relying party trusts the SAML issuer to issue holder-of-key assertions. The SAML issuer, on the other hand, may not even know the intended relying party, so there is no underlying assumption that the SAML issuer trusts the relying party.

.. _SamlHokProfile.2.3:

2.3 X.509 Certificate Usage
------------------------------------------

There are no explicit requirements with respect to the :term:`X.509 certificate` (s) possessed by 
the SAML issuer and the relying party. 
If, however, a certificate contains a :term:`Subject Key Identifier` (:term:`SKI`) extension, 
then the certificate MUST be an X.509 v3 certificate [RFC5280]. 
Other than that, 
the specific characteristics of these certificates are wholly out of scope 
with respect to this specification. 

In particular, 
there is no expectation that either the SAML issuer or the relying party trusts 
the issuer of the certificate, 
and therefore all portions of the certificate, 
apart from the :term:`X.509 data` specified in the following sections, are unspecified.

The only exception to the above rule is the case 
where the <ds:X509Data> element specified in :ref:`section 2.4.1 <SamlHokProfile.2.4.1>` 
contains a <ds:X509SubjectName> element or a <ds:X509SerialIssuer> element. 

In these two cases, 
the :term:`relying party` MUST trust the :term:`X.509 issuer` 
in order to confirm the :term:`attesting entity`. 
This is discussed more fully in :ref:`section 2.5 <SamlHokProfile.2.5>` below.

.. _SamlHokProfile.2.4:

2.4 Issuing Holder-of-Key Assertions
---------------------------------------------

Every :term:`assertion` containing a :term:`holder-of-key` **<saml:SubjectConfirmation>** element 
MUST conform to [:term:`SAML2Core`] 
(see section 2.4.1 of Core, especially section 2.4.1.3) 
and section 3.1 of [:term:`SAML2Prof`]. 

Where this specification conflicts with the SAML V2.0 specification, 
the former takes precedence.
Suppose a :term:`SAML issuer` wishes to issue a response 
containing one or more :term:`holder-of-key assertions`. 
As a prerequisite, 
the :term:`SAML issuer` MUST possess an :term:`X.509 certificate` 
known to be associated with the :term:`attesting entity`. 

The SAML issuer binds some or all of the :term:`X.509 data` 
in the certificate to the **<saml:SubjectConfirmation>** 
element of a :term:`SAML assertion`.

Briefly, 
the :term:`SAML issuer` binds a **<ds:KeyInfo>** element 
to the **<saml:SubjectConfirmationData>** element of a :term:`holder-of-key assertion`. 
The **<ds:KeyInfo>** element contains 
one or more of the following elements: 
**<ds:X509Certificate>**, 
**<ds:X509SKI>**, 
**<ds:X509SubjectName>**, or 
**<ds:X509IssuerSerial>**. 

A **<ds:X509Certificate>** element contains a base64 encoding of the certificate 
possessed by the :term:`SAML issuer`

.. note::
    SAML issuer ? Atesting entity's certificate.....

A **<ds:X509SKI>** element contains the base64 encoding of the :term:`Subject Key Identifier` (SKI) extension 
(if there is one) bound to the certificate. 

A **<ds:X509SubjectName>** element contains the :term:`subject distinguished name` (DN) 
bound to the certificate. 

A **<ds:X509IssuerSerial>** element contains the issuer DN and the issuer serial number 
bound to the certificate. 

In each case, 
the content of the **<ds:KeyInfo>** element conforms to the XML Signature specification [:term:`XMLSig`]. 
These requirements are spelled out more clearly in the next section.

If the SAML issuer has reason to believe that the :term:`relying party` trusts the certificate issuer, 
the SAML issuer MAY include **NotBefore** or **NotOnOrAfter** XML attributes 
on the **<saml:SubjectConfirmationData>** element. 
If so, 
the values bound to the assertion MUST be consistent with the values in the certificate. 
In particular, 
the value of the **NotBefore** attribute 
(resp., the **NotOnOrAfter** attribute) 
MUST be greater than or equal to (resp., less than or equal to) the **NotBefore** field 
(resp., the **NotOnOrAfter** field) of the certificate.

The **<saml:SubjectConfirmation>** element MAY contain a **<saml:NameID>** element. 
If it does, 
the latter identifies an :term:`attesting entity` different from 
the subject of the :term:`assertion`. 
If the **<saml:SubjectConfirmation>** element does not contain a **<saml:NameID>** element, 
then the :term:`attesting entity` and the subject are one and the same.

If the **<saml:SubjectConfirmation>** element contains a **<saml:NameID>** element, 
the :term:`attesting entity` is presumably acting 
on behalf of the subject. 

To more strongly signal such a delegation scenario, 
a **<saml:Condition>** element MAY be used (cf. [:term:`SAML2ConDel`]).

.. _SamlHokProfile.2.4.1:

2.4.1 KeyInfo Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. glossary::

    X.509 data
        A <ds:X509Data> XML element which is contained in **<ds:KeyInfo>** XML element of XML Signature.

According to the SAML V2.0 specification, 
a :term:`holder-of-key assertion` MUST contain at least one **<ds:KeyInfo>** element 
within the <saml:SubjectConfirmationData> element 
and that the **<ds:KeyInfo>** element MUST conform to the :term:`XML Signature` specification. 

This :doc:`SAML V2.0 Holder-of-Key Assertion Profile <SamlHokProfile>` requires that 
the **<ds:KeyInfo>** element MUST conform to 
the Second Edition of the XML Signature specification [:term:`XMLSig`] and 
further constrains the content of each **<ds:KeyInfo>** element to contain exactly 
**one** <ds:X509Data> element. 
The <ds:X509Data> element **MUST NOT contain** a <ds:X509CRL> element. 
Instead, the following content options are specified, 
**at least one of which MUST be satisfied**:

    The <ds:X509Data> element MAY contain a <ds:X509Certificate> element. 
    If it does, 
    the <ds:X509Certificate> element MUST contain a base64 encoding of the X.509 certificate 
    possessed by the SAML issuer.

        .. code-block:: xml

            <ds:X509Data>
                <ds:X509Certificate>
                --------
                -- base 64 encoded X.509 certificate
                --------
                </ds:X509Certificate>
            </ds:X509Data>

    The <ds:X509Data> element MAY contain a <ds:X509SKI> element. 
    If it does, 
    the <ds:X509SKI> element MUST contain the base64 encoding of the plain 
    (i.e., not DER-encoded) value of the :term:`Subject Key Identifier` (:term:`SKI`) extension 
    (as specified in [:term:`XMLSig`]) of the :term:`X.509 certificate` possessed by the SAML issuer. 
    If the certificate does not contain an :term:`SKI extension`, 
    the <ds:X509Data> element MUST NOT contain a <ds:X509SKI> element.

        .. code-block:: xml

            <ds:X509Data>
                <ds:X509SKI>
                plan value fo SKI extension
                </ds:X509SKI>
            </ds:X509Data>

    The <ds:X509Data> element MAY contain a <ds:X509SubjectName> element. 
    If it does, 
    the <ds:X509SubjectName> element MUST contain the :term:`subject distinguished name` (DN) 
    bound to the :term:`X.509 certificate` possessed by the SAML issuer.

        .. code-block:: xml

            <ds:X509Data>
                <ds:X509SubjectName>
                subject distingushied name(DN)
                </ds:X509SubjectName>
            </ds:X509Data>

    The <ds:X509Data> element MAY contain a <ds:X509IssuerSerial> element. 
    If it does, 
    the <ds:X509IssuerSerial> element MUST contain the issuer DN and the :term:`issuer serial number`
    (as specified in [:term:`XMLSig`]) 
    bound to the X.509 certificate possessed by the SAML issuer. (**This is the most ristrictive way**)

        .. code-block:: xml

            <ds:X509Data>
                <ds:X509IssuerSerial>
                issuer serial number
                </ds:X509IssuerSerial>
            </ds:X509Data>

Use of the <ds:X509Certificate> element or the <ds:X509IssuerSerial> element is most restrictive 
since each implies that 
the **exact same certificate** is used by both the :term:`SAML issuer` and the :term:`relying party`. 
Use of the <ds:X509SKI> element or the <ds:X509SubjectName> element is less restrictive 
since each permits a different certificate to be used by the :term:`relying party` 
provided the certificate contains the same key or DN (resp.) as in the certificate used by the SAML issuer.

Use of the <ds:X509SubjectName> element or the <ds:X509IssuerSerial> element is warranted 
in those situations where the :term:`relying party` trusts theissuer of the :term:`X.509 certificate`. 
The SAML issuer SHOULD NOT bind either of these elements to the <ds:X509Data> element 
unless it knows that such a **trust relationship** exists.

Note that 
the format of the DN contained in the <ds:X509SubjectName> element or 
the <ds:X509IssuerSerial> element is specified in [:term:`XMLSig`]. 
In accordance with that specification, 
it is RECOMMENDED that the DN conform to [:term:`RFC4514`] in all cases.

Since the **<ds:KeyInfo>** element is extensible [:term:`XMLSig`], 
other fields or extensions from the X.509 certificate may be bound to the :term:`holder-of-key assertion`. 
These are provided as a convenience to the relying party, 
so that the :term:`relying party` need not have to decode and parse the certificate. 
All such extensions are out of scope with respect to this profile, however.

.. _SamlHokProfile.2.4.2:

2.4.2 Example
^^^^^^^^^^^^^^^^^^

Here is an example of a holder-of-key **<saml:SubjectConfirmation>** element 
illustrating three of the content options specified in :ref:`section 2.4 <SamlHokProfile.2.4>`:

.. code-block:: xml

    <saml:SubjectConfirmation
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    Method="urn:oasis:names:tc:SAML:2.0:cm:holder-of-key">
    <saml:SubjectConfirmationData
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:type="saml:KeyInfoConfirmationDataType">
    <ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <ds:X509Data>
    
    <!-- a base64 encoding of an X.509 certificate -->
    <ds:X509Certificate>
    MIIDuDCCAqACCQCJZK8wF0xVXjANBgkqhkiG9w0BAQQFADCBnTELMAkGA1UEBhMCQlIxEzARBgNV
    BAgTClNvbWUtU3RhdGUxEjAQBgNVBAcTCVNvbWUtQ2l0eTESMBAGA1UEChMJR1NvQyAyMDA4MRIw
    EAYDVQQLEwlHU29DIDIwMDgxFzAVBgNVBAMTDkpvYW5hIFRyaW5kYWRlMSQwIgYJKoZIhvcNAQkB
    FhVzb21lLWFkZHJlc3NAaG9zdC5vcmcwHhcNMDgwNjE2MTcyMTQzWhcNMDkwNjE2MTcyMTQzWjCB
    nTELMAkGA1UEBhMCQlIxEzARBgNVBAgTClNvbWUtU3RhdGUxEjAQBgNVBAcTCVNvbWUtQ2l0eTES
    MBAGA1UEChMJR1NvQyAyMDA4MRIwEAYDVQQLEwlHU29DIDIwMDgxFzAVBgNVBAMTDkpvYW5hIFRy
    aW5kYWRlMSQwIgYJKoZIhvcNAQkBFhVzb21lLWFkZHJlc3NAaG9zdC5vcmcwggEiMA0GCSqGSIb3
    DQEBAQUAA4IBDwAwggEKAoIBAQDIDVKdO2CCVYA0TspOPmcSNnivjQq7jCacrgRPawKi3/pTuvnW
    3c2XCpyT2s6Sks3Eg5T4HIXta5E+lOpN8VbTunVdSrac54r2uK8x+8AqX7M0wQw+98iGw9E2an5q
    xRZfqqE1T5jWL/a/G1/e2TGlmp521W3k1nNtf8rYH39JpwBSZMeW7uHOSZOkT/pVvqPTgG7vUQT6
    BiRh7PfwsLrLOMubbeQ6Z2m3Vnsv20E1FbPzwswzh4X1gXj9bnyI2UsuoisW9Y4p4byjL3GJ/hxp
    mjRjXs+aIpzi0V3MH+jVJ98eomhlUFLaE83xycC8lns+FcCSQZ8RsbnaLZrtC8r7AgMBAAEwDQYJ
    KoZIhvcNAQEEBQADggEBACwnWSEpwq5aE7QBdDNNXyok34RIonYi9690yw7i+JU7R/QdE42GERJS
    DVKBN959ELLJf5d0vybGv08QWbZVQ7eBGn9xaZ7MhSnblYNDXs9vuv1V2Dy32q1J5nCSzqpJDyln
    lVFWe9UQMCJOO6ibUtWLhiDQ49kmMabgyYfX28qB6oRdVL+mDI/XTt+mkCgk4Rs78n4kbX6qnRlj
    dE/YnibP1A7iMh8pQkv49J6sP9SeUmQ2zxKCt3tSRzzypWc8JjOZGuBYGQHl9Xm7WEs4CXS7iZJW
    E32frMAtavMcTM/gnDtCc8tZAxl2PSLOF1954vapfMjBhg3VTI6QRW//wPE=
    </ds:X509Certificate>
    
    <!-- the above X.509 certificate does not contain a
    Subject Key Identifier extension so the SAML issuer
    must not include a <ds:X509SKI> element -->
    <!-- the subject DN (in RFC 5414 format) bound to the
    above X.509 certificate -->
    <ds:X509SubjectName>emailAddress=some-address@host.org,CN=Joana Trindade,OU=GSoC 2008,O=GSoC 2008,L=Some-City,ST=Some-State,C=BR</ds:X509SubjectName>
    <!-- the issuer DN (in RFC 5414 format) and the issuer serial
    number (in decimal) bound to the above X.509 certificate -->
    <ds:X509IssuerSerial>
    <ds:X509IssuerName>emailAddress=some-address@host.org,CN=Joana Trindade,OU=GSoC 2008,O=GSoC 2008,L=Some-City,ST=Some-State,C=BR</ds:X509IssuerName>
    <ds:X509SerialNumber>9900230501951362398</ds:X509SerialNumber>
    </ds:X509IssuerSerial>
    
    </ds:X509Data>
    </ds:KeyInfo>
    </saml:SubjectConfirmationData>
    </saml:SubjectConfirmation>

A :term:`relying party` can confirm 
the :term:`attesting entity` by the matching the available :term:`X.509 data` 
to any of the above child elements of the **<ds:X509Data>** element.

.. _SamlHokProfile.2.5:

2.5 Processing Holder-of-Key Assertions
------------------------------------------------------------

The :term:`attesting entity` presents a :term:`holder-of-key assertion` 
and an :term:`X.509 certificate` to the :term:`relying party`. 
The :term:`attesting entity` MUST **prove possession** of the :term:`private key` 
corresponding to the :term:`public key` bound to the certificate, 
the details of which are out of scope with respect to this profile. 

The :term:`relying party` confirms the :term:`attesting entity` 
by comparing the :term:`X.509 data` in the certificate to 
the :term:`X.509 data` bound to the :term:`assertion`. 
If the :term:`X.509 data` in the certificate matches the :term:`X.509 data` bound to the :term:`assertion`, 
the :term:`attesting entity` is said to be confirmed.

Regardless of the protocol used, 
any assertions relied upon MUST be valid according to the processing rules specified in [:term:`SAML2Core`]. 
In particular, 
the :term:`relying party` MUST verify the signature (if any) 
on each :term:`assertion` containing a :term:`holder-of-key` **<saml:SubjectConfirmation>** element. 
Any :term:`assertion` that is not valid, 
or whose subject confirmation requirements cannot be met, 
SHOULD be discarded and SHOULD NOT be used to establish a security context for the subject.

If the <ds:X509Data> element contains multiple child elements, 
the :term:`relying party` may choose to confirm the :term:`attesting entity` 
based on any one of them. 
Specifically, 
the :term:`relying party` MUST confirm that 
the certificate matches the content of the <ds:X509Data> element as follows:

    If the <ds:X509Data> element contains a <ds:X509Certificate> element, 
    and the :term:`relying party` chooses to confirm the :term:`attesting entity` based on this element, 
    the :term:`relying party` MUST ensure that 
    the certificate bound to the :term:`assertion` matches the :term:`X.509 certificate` in its possession. 
    Matching is done by 
    comparing the base64-decoded certificates, 
    or the hash values of the base64-decoded certificates, byte-for-byte.

    If the <ds:X509Data> element contains a <ds:X509SKI> element, 
    and the :term:`relying party` chooses to confirm the :term:`attesting entity` based on this element, 
    the :term:`relying party` MUST ensure that 
    the value bound to the :term:`assertion` matches the :term:`Subject Key Identifier` (:term:`SKI`) extension 
    bound to the :term:`X.509 certificate`. 
    Matching is done by 
    comparing the base64-decoded SKI values byte-for-byte. 
    If the :term:`X.509 certificate` does not contain an SKI extension, 
    the :term:`attesting entity` is not confirmed and the :term:`relying party` SHOULD disregard the assertion.

    If the <ds:X509Data> element contains a <ds:X509SubjectName> element, 
    and the :term:`relying party` chooses to confirm the :term:`attesting entity` based on this element, 
    the :term:`relying party` MUST ensure that 
    the subject distinguished name (DN) bound to the assertion matches the DN bound to the X.509 certificate. 
    If, however, the relying party does not trust the certificate issuer to issue such a DN, 
    the attesting entity is not confirmed and the relying party SHOULD disregard the assertion.

    If the <ds:X509Data> element contains a <ds:X509IssuerSerial> element, 
    and the :term:`relying party` chooses to confirm the :term:`attesting entity` based on this element, 
    the :term:`relying party` MUST ensure that the :term:`issuer DN` and :term:`issuer serial number` 
    bound to the :term:`assertion` match the :term:`issuer DN` and the :term:`issuer serial number` (resp.) 
    bound to the :term:`X.509 certificate`. 
    If the :term:`relying party` does not trust the certificate issuer to issue X.509 certificates, 
    however, 
    the :term:`attesting entity` is not confirmed and the :term:`relying party` SHOULD disregard the assertion.

In the case of a <ds:X509Certificate> element or a <ds:X509SKI> element, 
the matching process is relatively straightforward. 
If the <ds:X509Data> element contains a <ds:X509SubjectName> element or 
a <ds:X509IssuerSerial> element, however, 
and the :term:`relying party` chooses to confirm the :term:`attesting entity` 
based on one of these elements, 
the :term:`relying party` MUST trust the issuer of the :term:`X.509 certificate` 
before the :term:`attesting entity` can be considered confirmed. 
If such a :term:`trust relationship` between the :term:`relying party` 
and the :term:`certificate issuer` does not exist, 
the :term:`relying party` SHOULD disregard the assertion.

If the <saml:SubjectConfirmationData> element includes **NotBefore** or **NotOnOrAfter** attributes, 
and the :term:`relying party` trusts the issuer of the :term:`X.509 certificate`, 
the :term:`relying party` MUST confirm that 
the current time is greater than or equal to (resp., less than or equal to) the value of the **NotBefore** 
(resp., the **NotOnOrAfter**) attribute. 
If this requirement is not met, 
the :term:`attesting entity` is not confirmed and 
the :term:`relying party` SHOULD disregard the :term:`assertion`.

.. _SamlHokProfile.2.6:

2.6 Security and Privacy Considerations
------------------------------------------------

This profile assumes that 
both the :term:`SAML issuer` and the :term:`relying party` have access to an :term:`X.509 certificate`. 
For those deployments that wish to avoid or do not require an X.509-based public key infrastructure (PKI), 
this may seem unnecessarily restrictive. 

In fact, the use of X.509 certificates is typical and provides a number of advantages. 
First, 
observe that the SSL/TLS protocol [:term:`RFC4346`] requires the use of X.509 certificates. 
Second, and most importantly, 
since there is no presumption of an underlying trust model for X.509 certificates, 
the full range of possible content for the **<ds:KeyInfo>** element is avoided. 
Those deployments that are in fact based on such a trust model, 
or wish to avoid X.509 certificates altogether, 
may choose to profile additional child elements such as **<ds:KeyName>** or **<ds:KeyValue>**.

Deployments that rely on :term:`holder-of-key SAML assertions` will no doubt impose 
their own requirements on the X.509 certificates 
used to obtain those assertions. 

For example, some deployments will require the certificate to be an X.509 end-entity certificate [:term:`RFC5280`] 
issued by a trusted X.509 certification authority (CA) 
or a certificate based on a trusted X.509 end-entity certificate 
(such as an X.509 proxy certificate [RFC3820]). 
This specification imposes no such restrictions, however.

.. _SamlHokProfile.2.6.1:

2.6.1 ASN.1 Encoding
^^^^^^^^^^^^^^^^^^^^^^^^

For compatibility with the XML Signature specification [:term:`XMLSig`], 
this profile intentionally avoids any discussion of the :term:`ASN.1 encoding` 
of the :term:`X.509 certificate` possessed by the :term:`SAML issuer` and the :term:`relying party`. 

Indeed, 
in the case of the **<ds:X509Certificate>** element, 
the :term:`ASN.1 encoding` of the certificate doesn't matter. 
In this case, 
the :term:`SAML issuer` simply base64-encodes the ASN.1-encoded certificate in its possession 
and binds it to the **<ds:X509Certificate>** element. 
Later the :term:`relying party` base64-decodes the content of the **<ds:X509Certificate>** element 
and compares the resulting certificate (byte-for-byte) with the ASN.1-encoded certificate in its possession.

In the case of the **<ds:X509SKI>**, **<ds:X509SubjectName>**, or **<ds:X509IssuerSerial>** elements, 
however, 
the :term:`ASN.1 encoding` of the certificates does matter. 

To produce these elements, 
the :term:`SAML issuer` must ASN.1-decode the certificate in its possession 
and parse the ASN.1 to obtain the :term:`X.509 data` to be bound to the :term:`assertion`. 
Likewise the :term:`relying party` must ASN.1-decode the certificate in its possession, 
parsing the ASN.1 to obtain the required :term:`X.509 data`, 
which it compares to the :term:`X.509 data` bound to the assertion.

The basic problem is that the :term:`ASN.1 encoding` of an :term:`X.509 certificate` is not guaranteed. 
While it is true that an :term:`X.509 certificate` is often DER-encoded, 
a robust implementation must be prepared to handle other :term:`ASN.1 encodings` besides :term:`DER`, 
mainly :term:`BER` and :term:`CER`. 

Consequently 
it is anticipated that 
deployments will prefer the **<ds:X509Certificate>** element for maximum interoperability. 
In fact, 
this preference is reflected in the conformance requirements of this profile (:ref:`section 3 <SamlHokProfile.3>` ).

.. _SamlHokProfile.2.6.2:

2.6.2 X.509 Serial Number
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note that 
some CAs use large random numbers as serial numbers to prevent sequence guessing. 

However, 
not all XML libraries are capable of dealing with large integers in the **<ds:X509IssuerSerial>** element. 
The problem is that 
the **<ds:X509SerialNumber>** child element of the **<ds:X509IssuerSerial>** element is typed 
as an arbitrary integer in [:term:`XMLSig`] 
yet conforming implementations are required to support only 18 decimal digits. 
Thus the **<ds:X509IssuerSerial>** element should be used with care.

.. _SamlHokProfile.3:

3 Conformance
===========================

.. _SamlHokProfile.3.0.1:

3.0.1 SAML V2.0 Holder-of-Key Assertion Profile
----------------------------------------------------

Both the :term:`SAML issuer` and the :term:`relying party` MUST conform to :ref:`section 2.3 <SamlHokProfile.2.3>`.

A :term:`SAML issuer` MUST follow the issuing rules in :ref:`section 2.4 <SamlHokProfile.2.4>`. 
In particular, 
a :term:`SAML issuer` MUST produce **<ds:KeyInfo>** elements that conform to :ref:`section 2.4.1 <SamlHokProfile.2.4.1>`. 

Likewise, 
a :term:`relying party` MUST follow the processing rules in :ref:`section 2.5 <SamlHokProfile.2.5>`.

To claim conformance to this specification, 
a :term:`SAML issuer` implementation MUST support the **<ds:X509Certificate>** element 
specified in :ref:`section 2.4.1 <SamlHokProfile.2.4.1>`. 

Support for the remaining child elements specified 
in :ref:`section 2.4.1 <SamlHokProfile.2.4.1>` is **OPTIONAL** for :term:`SAML issuers`.

Likewise a conforming :term:`relying party` implementation MUST support 
the **<ds:X509Certificate>** element specified in :ref:`section 2.5 <SamlHokProfile.2.5>`. 
Support for the remaining child elements specified in :ref:`section 2.5 <SamlHokProfile.2.5>` is OPTIONAL for relying parties.

