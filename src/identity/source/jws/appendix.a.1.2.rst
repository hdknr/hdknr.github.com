A.1.2.  Decoding
^^^^^^^^^^^^^^^^^^^^^^^^

Decoding the JWS first requires 
removing the base64url encoding from the :term:`Encoded JWS Header`, 
the :term:`Encoded JWS Payload`, 
and the :term:`Encoded JWS Signature`. 

We base64url decode the inputs 
and turn them into the corresponding byte arrays. 

We translate the header input byte array containing UTF-8 encoded characters 
into the :term:`JWS Header string`.


(v.03)
