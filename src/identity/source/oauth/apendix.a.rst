Appendix A. Augmented Backus-Naur Form (ABNF) Syntax
========================================================

This section provides Augmented Backus-Naur Form (ABNF) syntax
descriptions for the elements defined in this specification using the
notation of :term:`[RFC5234]`.  The ABNF below is defined in terms of Unicode
code points :term:`[W3C.REC-xml-20081126]`; these characters are typically
encoded in UTF-8.  Elements are presented in the order first defined.

Some of the definitions that follow use the "URI-reference"
definition from :term:`[RFC3986]`.

Some of the definitions that follow use these common definitions:

::

     VSCHAR     = %x20-7E
     NQCHAR     = %x21 / %x23-5B / %x5D-7E
     NQSCHAR    = %x20-21 / %x23-5B / %x5D-7E
     UNICODECHARNOCRLF = %x09 /%x20-7E / %x80-D7FF /
                         %xE000-FFFD / %x10000-10FFFF

(The UNICODECHARNOCRLF definition is based upon the Char definition
in Section 2.2 of :term:`[W3C.REC-xml-20081126]`, but omitting the Carriage
Return and Linefeed characters.)

( http://tools.ietf.org/html/rfc6749.html#appendix-A )
