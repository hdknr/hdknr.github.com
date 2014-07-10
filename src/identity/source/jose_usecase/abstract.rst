.. _jose_usecase.abstract:

Abstract
====================

.. note::
    :term:`ASN.1` (バイナリ書式) -> JSON(テキスト書式)

Many Internet applications have a need 
for object-based security mechanisms 
in addition to security mechanisms at the network layer or
transport layer.  

For many years, 
the Cryptographic Message Syntax (CMS) has provided 
a binary secure object format based on ASN.1.  

Over time, 
binary object encodings such as ASN.1 have become 
less common than text-based encodings, 
such as the JavaScript Object Notation (JSON).  

This document defines a set of use cases and requirements 
for a secure object format encoded using JSON, 
drawn from a variety of application security mechanisms currently 
in development.

(:rfc:`7165`)
