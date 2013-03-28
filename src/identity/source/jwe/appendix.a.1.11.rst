A.1.11. Complete Representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Assemble the final representation: 
The :term:`Compact Serialization` of this result is the concatenation of 
the Encoded JWE Header, 
the Encoded JWE Encrypted Key, 
the Encoded JWE Initialization Vector, 
the Encoded JWE Ciphertext, and 
the Encoded JWE Integrity Value in that order,
with the five strings being separated by four period ('.') characters.

The final result in this example (with line breaks for display purposes only) is:

::

     eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00ifQ.
     M2XxpbORKezKSzzQL_95-GjiudRBTqn_omS8z9xgoRb7L0Jw5UsEbxmtyHn2T71m
     rZLkjg4Mp8gbhYoltPkEOHvAopz25-vZ8C2e1cOaAo5WPcbSIuFcB4DjBOM3t0UA
     O6JHkWLuAEYoe58lcxIQneyKdaYSLbV9cKqoUoFQpvKWYRHZbfszIyfsa18rmgTj
     zrtLDTPnc09DSJE24aQ8w3i8RXEDthW9T1J6LsTH_vwHdwUgkI-tC2PNeGrnM-dN
     SfzF3Y7-lwcGy0FsdXkPXytvDV7y4pZeeUiQ-0VdibIN2AjjfW60nfrPuOjepMFG
     6BBBbR37pHcyzext9epOAQ.
     48V1_ALb6US04U3b.
     _e21tGGhac_peEFkLXr2dMPUZiUkrw.
     7V5ZDko0v_mf2PAc4JMiUg

(draft 08, http://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-08#appendix-A.1.11 )
