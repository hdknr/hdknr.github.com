.. _jose_usecase.abstract:

Abstract
====================

.. note::
    ASN.1(バイナリ書式) -> JSON(テキスト書式)

Many Internet applications have a need 
for **object-based security mechanisms** 
in addition to security mechanisms 
at the **network layer** or **transport layer**.  

For many years,
the Cryptographic Message Syntax(CMS) has provided 
a **binary secure object format** based on :term:`ASN.1`.  

Over time, 
the use of binary object encodings such as ASN.1 has been 
less common than text-based encodidngs, 
for example :term:`JavaScript Object Notation`.

This document defines a set of use cases and requirements 
for a secure object format encoded 
using JavaScript Object Notation(JSON), 
drawn from a variety of application security mechanisms 
currently in development.

( http://tools.ietf.org/html/draft-ietf-jose-use-cases-06 )
