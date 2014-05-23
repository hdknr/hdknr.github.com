Abstract
==============


This specification provides a framework 
for the use of **assertions** with OAuth 2.0 
in the form of a new **client authentication mechanism** 
and a new **authorization grant type**.  

Mechanisms are specified for transporting assertions 
during interactions with a :term:`token endpoint`, as
well as general processing rules.

The intent of this specification is 
to provide a common framework for OAuth 2.
0 to interwork with other identity systems using assertions,
and to provide alternative client authentication mechanisms.

Note that this specification only defines abstract message flows 
and processing rules.  

In order to be implementable, 
companion specifications are necessary to provide 
the corresponding concrete instantiations.

.. note::

    Abstract message flow and assertion content for 

        - クライアントクレデンシャル :term:`client credeintial`
        - グラントタイプ :term:`authorization grant`

    Token in OAuth can be in two type of generic format (":ref:`oauth_threat.3.1` "):

        - Handle - "artifact"
        - Assertion - "self-contained token"

(draft 16)
