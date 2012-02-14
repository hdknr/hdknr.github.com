============================================================
Web Services Security SAML Token Profile Version 1.1.1
============================================================

http://docs.oasis-open.org/wss-m/wss/v1.1.1/wss-SAMLTokenProfile-v1.1.1.html


.. _saml_token_profile.abstarct:

Abstract
============

This document describes how to use Security Assertion Markup Language (SAML) V1.1 and 
V2.0 assertions with the Web Services Security SOAP Message Security Version 1.1.1 specification.

With respect to the description of the use of SAML V1.1, 
this document subsumes and is totally consistent 
with the Web Services Security: SAML Token Profile 1.0 
and includes all corrections identified in the 1.0 errata.

This document integrates specific error corrections 
or editorial changes to the preceding specification, 
within the scope of the Web Services Security and this TC.

This document introduces a third digit in the numbering convention 
where the third digit represents a consolidation of error corrections, 
bug fixes or editorial formatting changes (e.g., 1.1.1); 
it does not add any new features beyond those of the base specifications (e.g., 1.1).


.. contents:: Table of Contents

.. _saml_token_profile.2.3:

2.3 Terminology
---------------------------------

This specification employs the terminology defined in the WSS: SOAP Message Security specification. 
The definitions for additional terminology used in this specification appear below.

.. glossary::

    Attesting Entity 
        the entity that provides the :term:`confirmation evidence`
        that will be used to establish the correspondence 
        between the :term:`subjects` and claims of SAML statements (in SAML assertions) and SOAP message content.

    Confirmation Method Identifier 
        the value within a SAML SubjectConfirmation element 
        that identifies the subject confirmation process to be used with the corresponding statements.

    Subject Confirmation 
        the process of establishing the correspondence 
        between the subject and claims of SAML statements (in SAML assertions) and SOAP message content 
        by verifying the confirmation evidence provided by an attesting entity.

    SAML Assertion Authority 
        A system entity that issues assertions.

    Subject 
        A representation of the entity to which the claims in one or more SAML statements apply.

    Subjects
        :term:`Subject`

.. _saml_token_profile.3:

3 Usage
========================

This section defines the specific mechanisms and 
procedures for using SAML assertions as security tokens.

.. _saml_token_profile.3.1:

3.1 Processing Model
---------------------------

This specification extends 
the token-independent processing model defined 
by the WSS: SOAP Message Security specification.
When a receiver processes a <wsse:Security> header 
containing or referencing SAML assertions, 
it selects, based on its policy, 
the signatures and assertions that it will process. 

It is assumed that 
a receiver’s signature selection policy MAY rely on semantic labeling[1] 
of <wsse:SecurityTokenReference> elements occurring in the <ds:KeyInfo> elements 
within the signatures. 

It is also assumed that the assertions selected for validation and 
processing will include those referenced from the <ds:KeyInfo> and 
<ds:SignedInfo> elements of the selected signatures.

As part of its validation and processing of the selected assertions, 
the receiver MUST[2] establish the relationship 
between the subject and claims of the SAML statements 
(of the referenced SAML assertions) 
and the entity providing the evidence to satisfy the confirmation method 
defined for the statements (i.e., the attesting entity). 

Two methods for establishing this correspondence, 
holder-of-key and sender-vouches are described below. 
Systems implementing this specification MUST implement the processing necessary 
to support both of these subject confirmation methods.


.. _saml_token_profile.3.5:

3.5 Subject Confirmation of SAML Assertions
---------------------------------------------------


The SAML profile of WSS: SOAP Message Security requires that 
systems support the holder-of-key and sender-vouches methods of subject confirmation. 

It is strongly RECOMMENDED that 
an XML signature be used to establish 
the relationship between the message and the statements of the attached assertions. 

This is especially RECOMMENDED 
whenever the SOAP message exchange is conducted over an unprotected transport.

Any processor of SAML assertions MUST conform to the required validation 
and processing rules defined in the corresponding SAML specification 
including the validation of assertion signatures, 
the processing of <saml:Condition> elements within assertions, 
and the processing of <saml2:SubjectConfirmationData> attributes. 

[SAMLCoreV1] defines the validation and processing rules for V1.1 assertions, 
while [SAMLCoreV2] is authoritative for V2.0 assertions.
The following table enumerates 
the mandatory subject confirmation methods and 
summarizes their associated processing models:


Mechanism:

    holder-of-key

        urn
            - urn:oasis:names:tc:SAML:1.0:cm:holder-of-key
            - urn:oasis:names:tc:SAML:2.0:cm:holder-of-key


        RECOMMENDED Processing Rules

            The attesting entity demonstrates knowledge of a confirmation key identified 
            in a holder-of-key SubjectConfirmation element within the assertion.

    sender-vouches

        urn
            - urn:oasis:names:tc:SAML:1.0:cm:sender-vouches
            - urn:oasis:names:tc:SAML:2.0:cm:sender-vouches

        RECOMMENDED Processing Rules
            
            The attesting entity, (presumed to be) different from the subject, 
            vouches for the verification of the subject. 
            The receiver MUST have an existing trust relationship with the attesting entity. 
            The attesting entity MUST protect the assertion in combination 
            with the message content against modification by another party. See also section 4.




Note that 
the high level processing model described in the following sections 
does not differentiate between the attesting entity and the message sender 
as would be necessary to guard against replay attacks. 

The high-level processing model also does not take into account requirements 
for authentication of receiver by sender, 
or for message or assertion confidentiality. 

These concerns must be addressed by means other than those described 
in the high-level processing model (i.e., :ref:`section 3.1 <saml_token_profile.3.1>`).

.. _saml_token_profile.3.5.1:

3.5.1 Holder-of-key Subject Confirmation Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following sections describe the holder-of-key method of establishing the correspondence 
between a :term:`SOAP message` and the :term:`subject` and :term:`claims of SAML assertions` 
added to the SOAP message according to this specification.

3.5.1.1 Attesting Entity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An :term:`attesting entity` demonstrates that 
it is authorized to act as the subject of a holder-of-key confirmed SAML statement 
by demonstrating knowledge of any key identified in a holder-of-key SubjectConfirmation element 
associated with the statement by the assertion containing the statement. 

Statements attested for by the holder-of-key method MUST be associated, 
within their containing assertion, 
with one or more holder-of-key SubjectConfirmation elements.

The SubjectConfirmation elements MUST include a <ds:KeyInfo> element 
that identifies a public or secret key[5] that can be used to confirm the identity of the subject.

To satisfy the associated confirmation method processing to be performed by the message receiver, 
the attesting entity MUST demonstrate knowledge of the :term:`confirmation key`. 
The attesting entity MAY accomplish this by using the :term:`confirmation key`
to sign content within the message and by including the resulting <ds:Signature> element 
in the <wsse:Security> header. 
<ds:Signature> elements produced for this purpose MUST conform to the canonicalization and 
token pre-pending rules defined in the WSS: SOAP Message Security specification.
The attesting entity MAY protect against substitution of a different 
but equivalently confirmed[6] assertion by including, 
as described in section 3.4.3 "SAML Assertion Referenced from SignedInfo", 
the :term:`SAML assertion` (or an unambiguous reference to it) 
in the content signed to demonstrate knowledge of the confirmation key.

SAML assertions that contain a holder-of-key SubjectConfirmation element 
SHOULD contain a <ds:Signature> element 
that protects the integrity of the confirmation <ds:KeyInfo> 
established by the assertion authority.

The canonicalization method used to produce the <ds:Signature> elements 
used to protect the integrity of SAML assertions MUST support 
the validation of these <ds:Signature> elements in contexts 
(such as <wsse:Security> header elements) 
other than those in which the signatures were calculated.

3.5.1.2  Receiver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Of the SAML assertions 
it selects for processing, 
a message receiver MUST NOT accept statements of these assertions 
based on a holder-of-key SubjectConfirmation element defined for the statements 
(within the assertion) 
unless the receiver has validated the integrity of the assertion 
and the attesting entity has demonstrated knowledge of a key identified 
within the confirmation element.

If the receiver determines that 
the attesting entity has demonstrated knowledge of a subject confirmation key, 
then the subjects and claims of the SAML statements confirmed by the key 
MAY be attributed to the attesting entity 
and any content of the message 
(including any SAML statements) 
whose integrity is protected by the key 
MAY be considered to have been provided by the attesting entity.


3.5.1.4 Example V2.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example illustrates the use of the holder-of-key subject confirmation method to establish the correspondence between the SOAP message and the subject of the SAML V2.0 assertion in the <wsse:Security> header:


.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <S12:Envelope xmlns:S12="..." xmlns:wsu="...">
      <S12:Header>
     
        <wsse:Security xmlns:wsse="..." xmlns:wsse11="..." xmlns:ds="...">
          <saml2:Assertion xmlns:saml2="..." xmlns:xsi="..."
                ID=”_a75adf55-01d7-40cc-929f-dbd8372ebdfc”>
          <saml2:Subject>
                  <saml2:NameID>
                         …
                  </saml2:NameID>
                  <saml2:SubjectConfirmation
                Method=”urn:oasis:names:tc:SAML:2.0:cm:holder-of-key”>
                <saml2:SubjectConfirmationData
                                 xsi:type="saml2:KeyInfoConfirmationDataType">
                   <ds:KeyInfo>
                      <ds:KeyValue>…</ds:KeyValue>
                   </ds:KeyInfo>
                </saml2:SubjectConfirmationData>
             </saml2:SubjectConfirmation>
          </saml2:Subject>
          <saml2:Statement>
                  …
          </saml2:Statement>
            <ds:Signature>…</ds:Signature>
          </saml2:Assertion>
     
          <ds:Signature>
            <ds:SignedInfo>
              <ds:CanonicalizationMethod
                Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
              <ds:SignatureMethod
                Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
              <ds:Reference
                URI="#MsgBody">
                <ds:DigestMethod
                  Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
                <ds:DigestValue>GyGsF0Pi4xPU...</ds:DigestValue>
              </ds:Reference>
            </ds:SignedInfo>
            <ds:SignatureValue>HJJWbvqW9E84vJVQk…</ds:SignatureValue>
            <ds:KeyInfo>
              <wsse:SecurityTokenReference wsu:Id=”STR1”
                wsse11:TokenType=”http://docs.oasis-open.org/wss/oasis-wss-saml-token-profile-1.1#SAMLV2.0”>
                <wsse:KeyIdentifier wsu:Id=”…”
                  ValueType=”http://docs.oasis-open.org/wss/oasis-wss-saml-token-profile-1.1#SAMLID”>
                  _a75adf55-01d7-40cc-929f-dbd8372ebdfc
                </wsse:KeyIdentifier>
              </wsse:SecurityTokenReference>
            </ds:KeyInfo>
          </ds:Signature>
        </wsse:Security>
      </S12:Header>
     
      <S12:Body wsu:Id="MsgBody">
        <ReportRequest>
          <TickerSymbol>SUNW</TickerSymbol>
        </ReportRequest>
      </S12:Body>
    </S12:Envelope>
    


