Appendix E.  Negative Test Case for "crit" Header Parameter
========================================================================

Conforming implementations must reject input containing critical
extensions that are not understood or cannot be processed.  

The following JWS must be rejected by all implementations, 
because it uses an extension Header Parameter name
"http://example.invalid/UNDEFINED" that they do not understand.  

Any other similar input, 
in which the use of the value "http://example.invalid/UNDEFINED" 
is substituted for any other Header Parameter name not understood 
by the implementation, 
must also be rejected.

The JWS Protected Header value for this JWS is:

.. code-block:: javascript

  {"alg":"none",
   "crit":["http://example.invalid/UNDEFINED"],
   "http://example.invalid/UNDEFINED":true
  }

The complete JWS that must be rejected is as follows (with line
breaks for display purposes only):

::

  eyJhbGciOiJub25lIiwNCiAiY3JpdCI6WyJodHRwOi8vZXhhbXBsZS5jb20vVU5ERU
  ZJTkVEIl0sDQogImh0dHA6Ly9leGFtcGxlLmNvbS9VTkRFRklORUQiOnRydWUNCn0.
  RkFJTA.

(draft27)
