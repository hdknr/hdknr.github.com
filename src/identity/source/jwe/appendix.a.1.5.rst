A.1.5.  Additional Authenticated Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let the Additional Authenticated Data encryption parameter 
be ASCII(BASE64URL(UTF8(JWE Protected Header))).  

This value is:

::

   [101, 121, 74, 104, 98, 71, 99, 105, 79, 105, 74, 83, 85, 48, 69,
   116, 84, 48, 70, 70, 85, 67, 73, 115, 73, 109, 86, 117, 89, 121, 73,
   54, 73, 107, 69, 121, 78, 84, 90, 72, 81, 48, 48, 105, 102, 81]
