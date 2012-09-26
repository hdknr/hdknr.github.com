Abstract
============

This specification describes a JavaScript API for performing basic cryptographic operations in web applications, 
such as hashing, signature generation and verification, and encryption and decryption. 
Additionally, it describes an API for applications to generate and/or manage the :term:`keying material`
necessary to perform these operations. 
Key storage is provided for both temporary and permanent keys. 
Access to :term:`keying material` is contingent on the :term:`same origin policy.` 
Uses for this API range from user or service authentication, 
document or code signing, 
and the confidentiality and integrity of communications.

The section on Use Cases [:ref:`REQ <webcrypto.2>`] covers the motivation behind this specification.

Editorial note
----------------------------

This is revision $Id: Overview.html,v 1.5 2012/09/12 21:54:55 wseltzer Exp $.

There are 14 further editorial notes in the document.

Status of this Document

This section describes the status of this document at the time of its publication. Other documents may supersede this document. A list of current W3C publications and the latest revision of this technical report can be found in the W3C technical reports index at http://www.w3.org/TR/.

This document is produced by the Web Cryptography WG of the W3C.

This is the first Public Working Draft of the Web Cryptography API. Publication as a Working Draft does not imply endorsement by the W3C Membership. This is a draft document and may be updated, replaced or obsoleted by other documents at any time. It is inappropriate to cite this document as other than work in progress.

The Web Cryptography Working Group invites discussion and feedback on this draft document by web developers, companies, standardization bodies or forums interested in deployment of secure services with web applications. Specifically, Web Cryptography Working Group is looking for feedback on:

developer convenience for managing keys and algorithms;
comments on open issues the WG is currently dealing with, highlighted in this working draft;
potential missing functionalities to deploy secure web applications.
Please send comments to public-webcrypto-comments@w3.org, the W3C's public email list for issues related to Web Cryptography. Archives of the public list and archives of the member's-only list are available.

Changes made to this document can be found in the W3C public CVS server.

This document was produced by a group operating under the 5 February 2004 W3C Patent Policy. W3C maintains a public list of any patent disclosures made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent which the individual believes contains Essential Claim(s) must disclose the information in accordance with section 6 of the W3C Patent Policy.

