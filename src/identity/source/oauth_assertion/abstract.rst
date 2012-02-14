Abstract
==============

This specification provides **a general framework for the use of assertions** 
as **client credentials** and/or **authorization grants** with :doc:`OAuth 2.0 <oauth>`.  

It includes a generic mechanism 
for transporting assertions during interactions with a :term:`token endpoint`, 
as wells as rules for the content and processing of those assertions.  
The intent is to provide an enhanced security profile 
by using derived values such as signatures or HMACs, 
as well as facilitate the use of OAuth 2.0 
in client-server integration scenarios where the end-user may not be present.

This specification only defines **abstract message flow** and **assertion content**.  
Actual use requires implementation of a companion protocol binding specification.  
Additional profile documents provide standard representations in formats such as :term:`SAML` and :term:`JWT`.

.. note::

    Abstract message flow and assertion content for 

        - :term:`client credeintial`
        - :term:`authorization grant`

    Token in OAuth can be in two type of generic format (":ref:`oauth_threat.3.1` "):

        - Handle - "artifact"
        - Assertion - "self-contained token"

