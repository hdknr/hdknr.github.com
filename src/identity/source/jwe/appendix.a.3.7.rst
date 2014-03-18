A.3.7.  Complete Representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assemble the final representation: The Compact Serialization of this
result is the string 
BASE64URL(UTF8(JWE Protected Header)) || '.' ||
BASE64URL(JWE Encrypted Key) || '.' || 
BASE64URL(JWE Initialization Vector) || '.' || 
BASE64URL(JWE Ciphertext) || '.' || 
BASE64URL(JWE Authentication Tag).

The final result in this example (with line breaks for display
purposes only) is:

::

     eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.
     6KB707dM9YTIgHtLvtgWQ8mKwboJW3of9locizkDTHzBC2IlrT1oOQ.
     AxY8DCtDaGlsbGljb3RoZQ.
     KDlTtXchhZTGufMYmOYGS4HffxPSUrfmqCHXaI9wOGY.
     U0m_YmjN04DJvceFICbCVQ

(draft23)
