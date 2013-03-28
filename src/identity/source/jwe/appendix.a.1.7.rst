A.1.7. "Additional Authenticated Data" Parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Concatenate 
the :term:`Encoded JWE Header` value, a period character ('.'),
the :term:`Encoded JWE Encrypted Key`, a second period character ('.'), and
the :term:`Encoded JWE Initialization Vector` 
to create the ":term:`additional authenticated data`" parameter 
for the :term:`AES GCM` algorithm.  

This result (with line breaks for display purposes only) is:

::

     eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00ifQ.
     M2XxpbORKezKSzzQL_95-GjiudRBTqn_omS8z9xgoRb7L0Jw5UsEbxmtyHn2T71m
     rZLkjg4Mp8gbhYoltPkEOHvAopz25-vZ8C2e1cOaAo5WPcbSIuFcB4DjBOM3t0UA
     O6JHkWLuAEYoe58lcxIQneyKdaYSLbV9cKqoUoFQpvKWYRHZbfszIyfsa18rmgTj
     zrtLDTPnc09DSJE24aQ8w3i8RXEDthW9T1J6LsTH_vwHdwUgkI-tC2PNeGrnM-dN
     SfzF3Y7-lwcGy0FsdXkPXytvDV7y4pZeeUiQ-0VdibIN2AjjfW60nfrPuOjepMFG
     6BBBbR37pHcyzext9epOAQ.
     48V1_ALb6US04U3b

The representation of this value is:

.. code-block:: javascript

   [101, 121, 74, 104, 98, 71, 99, 105, 79, 105, 74, 83, 85, 48, 69,
   116, 84, 48, 70, 70, 85, 67, 73, 115, 73, 109, 86, 117, 89, 121, 73,
   54, 73, 107, 69, 121, 78, 84, 90, 72, 81, 48, 48, 105, 102, 81, 46,
   77, 50, 88, 120, 112, 98, 79, 82, 75, 101, 122, 75, 83, 122, 122, 81,
   76, 95, 57, 53, 45, 71, 106, 105, 117, 100, 82, 66, 84, 113, 110, 95,
   111, 109, 83, 56, 122, 57, 120, 103, 111, 82, 98, 55, 76, 48, 74,
   119, 53, 85, 115, 69, 98, 120, 109, 116, 121, 72, 110, 50, 84, 55,
   49, 109, 114, 90, 76, 107, 106, 103, 52, 77, 112, 56, 103, 98, 104,
   89, 111, 108, 116, 80, 107, 69, 79, 72, 118, 65, 111, 112, 122, 50,
   53, 45, 118, 90, 56, 67, 50, 101, 49, 99, 79, 97, 65, 111, 53, 87,
   80, 99, 98, 83, 73, 117, 70, 99, 66, 52, 68, 106, 66, 79, 77, 51,
   116, 48, 85, 65, 79, 54, 74, 72, 107, 87, 76, 117, 65, 69, 89, 111,
   101, 53, 56, 108, 99, 120, 73, 81, 110, 101, 121, 75, 100, 97, 89,
   83, 76, 98, 86, 57, 99, 75, 113, 111, 85, 111, 70, 81, 112, 118, 75,
   87, 89, 82, 72, 90, 98, 102, 115, 122, 73, 121, 102, 115, 97, 49, 56,
   114, 109, 103, 84, 106, 122, 114, 116, 76, 68, 84, 80, 110, 99, 48,
   57, 68, 83, 74, 69, 50, 52, 97, 81, 56, 119, 51, 105, 56, 82, 88, 69,
   68, 116, 104, 87, 57, 84, 49, 74, 54, 76, 115, 84, 72, 95, 118, 119,
   72, 100, 119, 85, 103, 107, 73, 45, 116, 67, 50, 80, 78, 101, 71,
   114, 110, 77, 45, 100, 78, 83, 102, 122, 70, 51, 89, 55, 45, 108,
   119, 99, 71, 121, 48, 70, 115, 100, 88, 107, 80, 88, 121, 116, 118,
   68, 86, 55, 121, 52, 112, 90, 101, 101, 85, 105, 81, 45, 48, 86, 100,
   105, 98, 73, 78, 50, 65, 106, 106, 102, 87, 54, 48, 110, 102, 114,
   80, 117, 79, 106, 101, 112, 77, 70, 71, 54, 66, 66, 66, 98, 82, 51,
   55, 112, 72, 99, 121, 122, 101, 120, 116, 57, 101, 112, 79, 65, 81,
   46, 52, 56, 86, 49, 95, 65, 76, 98, 54, 85, 83, 48, 52, 85, 51, 98]

( draft 08, http://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-08#appendix-A.1.7 )
