A.2.5.  Additional Authenticated Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let the Additional Authenticated Data encryption parameter be
ASCII(BASE64URL(UTF8(JWE Protected Header))).  

This value is:

::

   [101, 121, 74, 104, 98, 71, 99, 105, 79, 105, 74, 83, 85, 48, 69,
   120, 88, 122, 85, 105, 76, 67, 74, 108, 98, 109, 77, 105, 79, 105,
   74, 66, 77, 84, 73, 52, 81, 48, 74, 68, 76, 85, 104, 84, 77, 106, 85,
   50, 73, 110, 48]


(draft23)
