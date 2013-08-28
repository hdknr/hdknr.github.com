A.2.6. Initialization Vector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
    - 初期化ベクタは 16 オクテットランダムで作ってみる

Generate a random 128 bit JWE Initialization Vector.  
In this example, the value is:

::

   [3, 22, 60, 12, 43, 67, 104, 105, 108, 108, 105, 99, 111, 116, 104, 101]

Base64url encoding this value yields this Encoded JWE Initialization
Vector value:


::

     AxY8DCtDaGlsbGljb3RoZQ

( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-13#appendix-A.2.6 )
